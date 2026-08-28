"""Lab 6 (AutoGen script) — human-in-the-loop approval with UserProxyAgent.

An assistant drafts, a HUMAN (you) reviews. The team keeps looping until you
type a message containing APPROVE — the termination condition.
Run:  uv run python lab-06-react-human-in-loop/human_in_loop.py
"""
import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

drafter = AssistantAgent(
    name="drafter",
    model_client=model_client,
    system_message=(
        "You draft short, professional customer-facing incident notices for "
        "TechTrend Solutions. Revise according to the reviewer's feedback."
    ),
)

# The human: input() is called whenever it is this agent's turn.
reviewer = UserProxyAgent(
    name="human_reviewer",
    description="A human reviewer who approves or requests changes.",
    input_func=input,
)

# Stop when the human types APPROVE, or after 12 messages as a safety net.
termination = TextMentionTermination("APPROVE") | MaxMessageTermination(12)

team = RoundRobinGroupChat([drafter, reviewer], termination_condition=termination)


async def main() -> None:
    print("Type feedback to request changes, or a message containing APPROVE to accept.\n")
    await Console(team.run_stream(
        task="Draft a 3-sentence customer notice about the checkout outage in ticket TT-1001."
    ))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
