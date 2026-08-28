"""Lab 8 (AutoGen script) — route requests to specialists with SelectorGroupChat.

Unlike round-robin, a selector model reads each agent's description and picks
WHO speaks next — dynamic routing. A planner coordinates two specialists and
closes with TERMINATE. Run:  uv run python lab-08-selector-workflow-capstone/selector_team.py
"""
import asyncio
import json
import os
from pathlib import Path
from dotenv import load_dotenv
import chromadb
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
DATA = Path(__file__).parent.parent / "data"
TICKETS = json.loads((DATA / "tickets.json").read_text())["tickets"]
col = chromadb.PersistentClient(path=str(DATA / "chroma_db")).get_collection("opsdesk")


def lookup_ticket(ticket_id: str) -> str:
    """Look up one TechTrend support ticket by id (e.g. TT-1002)."""
    for t in TICKETS:
        if t["id"] == ticket_id:
            return json.dumps(t)
    return json.dumps({"error": "not found"})


def search_policy(query: str) -> str:
    """Search the IT handbook; returns top-3 chunks with source ids."""
    res = col.query(query_texts=[query], n_results=3)
    return "\n\n".join(f"[{i}]\n{d}" for i, d in zip(res["ids"][0], res["documents"][0]))


model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

planner = AssistantAgent(
    name="planner",
    model_client=model_client,
    description="Coordinates the work: breaks the request into steps, delegates, and writes the final reply.",
    system_message=(
        "You coordinate TechTrend's OpsDesk. Break the user's request into steps, "
        "say which specialist should act next, and when both specialists have "
        "reported, write the final customer reply ending with the word TERMINATE."
    ),
)

ticket_specialist = AssistantAgent(
    name="ticket_specialist",
    model_client=model_client,
    description="Looks up ticket facts (status, priority, requester) using the ticket tool.",
    tools=[FunctionTool(lookup_ticket, description="Ticket lookup")],
    reflect_on_tool_use=True,
    system_message="You answer ONLY with facts from lookup_ticket. Read-only.",
)

policy_specialist = AssistantAgent(
    name="policy_specialist",
    model_client=model_client,
    description="Finds and cites the applicable handbook policy using semantic search.",
    tools=[FunctionTool(search_policy, description="Policy search")],
    reflect_on_tool_use=True,
    system_message="You quote the applicable policy with its source id, e.g. (POL-001).",
)

team = SelectorGroupChat(
    [planner, ticket_specialist, policy_specialist],
    model_client=model_client,                 # the selector LLM
    termination_condition=TextMentionTermination("TERMINATE") | MaxMessageTermination(15),
    allow_repeated_speaker=False,
)


async def main() -> None:
    result = await Console(team.run_stream(
        task="For ticket TT-1002: what is being requested, and what does policy say "
             "about approval and validity? Draft the reply to the requester."
    ))
    print("\nStop reason:", result.stop_reason)
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
