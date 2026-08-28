"""Lab 7 (AutoGen script) — a writer/reviewer team with RoundRobinGroupChat.

Two specialists take turns in a fixed order and share one conversation.
The reviewer says the exact word FINALISED when satisfied — that text mention
terminates the team. Run:  uv run python lab-07-round-robin-team/team_round_robin.py
"""
import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

writer = AssistantAgent(
    name="writer",
    model_client=model_client,
    description="Writes and revises the announcement draft.",
    system_message=(
        "You write concise internal IT announcements for TechTrend Solutions. "
        "Produce or revise ONE draft per turn, applying every reviewer comment."
    ),
)

reviewer = AssistantAgent(
    name="reviewer",
    model_client=model_client,
    description="Reviews drafts against the policy checklist.",
    system_message=(
        "You review announcements against the handbook: correct SLA times "
        "(P1=15 min ack), correct VPN approval chain (manager + IT Security), "
        "professional tone, under 120 words. Give numbered fix requests. "
        "Only when the draft needs NO further changes, reply exactly: FINALISED"
    ),
)

termination = TextMentionTermination("FINALISED") | MaxMessageTermination(10)
team = RoundRobinGroupChat([writer, reviewer], termination_condition=termination)


async def main() -> None:
    result = await Console(team.run_stream(
        task="Announce the new contractor VPN process: manager + IT Security approval, "
             "90-day validity, requests via the IT portal."
    ))
    print("\nStop reason:", result.stop_reason)
    print("Total messages:", len(result.messages))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
