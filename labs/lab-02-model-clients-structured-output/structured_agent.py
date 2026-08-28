"""Lab 2 (AutoGen script) — structured output with a Pydantic schema.

Free text is hard to automate. Giving the agent an output_content_type forces
the model to return validated JSON your code can rely on — the foundation of
dependable multi-agent workflows.
Run:  uv run python lab-02-model-clients-structured-output/structured_agent.py
"""
import asyncio
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


class TicketTriage(BaseModel):
    """The schema every reply must follow."""
    summary: str
    priority: str        # P1 / P2 / P3 / P4
    category: str        # access / hardware / software / network / other
    needs_human: bool


model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")
)

triage_agent = AssistantAgent(
    name="triage_agent",
    model_client=model_client,
    system_message=(
        "You triage IT support tickets for TechTrend Solutions. "
        "Classify priority using: P1 outage/security, P2 major degradation, "
        "P3 normal request, P4 low impact."
    ),
    output_content_type=TicketTriage,   # <- structured output
)


async def main() -> None:
    result = await triage_agent.run(
        task="Ticket: 'The whole checkout page is down, every customer gets an error 500.'"
    )
    triage = result.messages[-1].content   # a TicketTriage object, not a string
    print("Validated structured output:")
    print("  summary     :", triage.summary)
    print("  priority    :", triage.priority)
    print("  category    :", triage.category)
    print("  needs_human :", triage.needs_human)
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
