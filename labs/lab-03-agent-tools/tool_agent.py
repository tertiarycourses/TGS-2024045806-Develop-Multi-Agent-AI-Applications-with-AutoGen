"""Lab 3 (AutoGen script) — the same tools, one line each with FunctionTool.

AutoGen turns a typed Python function into a tool schema automatically,
executes the call, and (with reflect_on_tool_use) reasons over the result.
Run:  uv run python lab-03-agent-tools/tool_agent.py
"""
import asyncio
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
DATA = Path(__file__).parent.parent / "data"
TICKETS = json.loads((DATA / "tickets.json").read_text())["tickets"]


def lookup_ticket(ticket_id: str) -> str:
    """Look up a TechTrend support ticket by its id (e.g. TT-1001) and return it as JSON."""
    for t in TICKETS:
        if t["id"] == ticket_id:
            return json.dumps(t)
    return json.dumps({"error": f"ticket {ticket_id} not found"})


def count_open_tickets(priority: str) -> str:
    """Count open (not resolved) tickets of a given priority: P1, P2, P3 or P4."""
    n = sum(1 for t in TICKETS if t["priority"] == priority and t["status"] != "resolved")
    return json.dumps({"priority": priority, "open_tickets": n})


ticket_tool = FunctionTool(lookup_ticket, description="Look up one support ticket by id.")
count_tool = FunctionTool(count_open_tickets, description="Count open tickets by priority.")

model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

agent = AssistantAgent(
    name="helpdesk_agent",
    model_client=model_client,
    tools=[ticket_tool, count_tool],
    reflect_on_tool_use=True,      # reason over the tool result before answering
    max_tool_iterations=3,
    system_message=(
        "You are TechTrend's help-desk agent. Use the tools for any ticket facts — "
        "never invent ticket data. Read-only: you cannot modify tickets."
    ),
)


async def main() -> None:
    await Console(agent.run_stream(
        task="Summarise ticket TT-1005, then tell me how many P2 tickets are still open."
    ))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
