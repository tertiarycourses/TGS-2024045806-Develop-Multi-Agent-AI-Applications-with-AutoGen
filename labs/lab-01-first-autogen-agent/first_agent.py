"""Lab 1 (AutoGen script) — your first AutoGen AgentChat agent.

The same LLM, now wrapped in an AssistantAgent: it has a name, a system
message, and an async run() loop managed by AutoGen.
Run:  uv run python lab-01-first-autogen-agent/first_agent.py
"""
import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)

agent = AssistantAgent(
    name="ops_assistant",
    model_client=model_client,
    system_message=(
        "You are TechTrend's IT operations assistant. "
        "Answer clearly and concisely for a non-technical employee."
    ),
)


async def main() -> None:
    # Stream the agent's turn to the terminal with the Console UI.
    await Console(
        agent.run_stream(task="Explain in 3 sentences what a multi-agent AI application is.")
    )
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
