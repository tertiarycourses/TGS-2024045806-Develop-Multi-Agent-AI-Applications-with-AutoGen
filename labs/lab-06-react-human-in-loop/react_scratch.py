"""Lab 6 (Python script) — a minimal ReAct loop from scratch.

Thought -> Action -> Observation, hand-rolled in ~50 lines, so you can see
exactly what agent frameworks automate. The 'tools' are plain functions;
the loop feeds each observation back to the model until it emits ANSWER.
Run:  uv run python lab-06-react-human-in-loop/react_scratch.py
"""
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TICKETS = json.loads((Path(__file__).parent.parent / "data" / "tickets.json").read_text())["tickets"]


def lookup_ticket(ticket_id: str) -> str:
    for t in TICKETS:
        if t["id"] == ticket_id:
            return json.dumps(t)
    return "not found"


def sla_for(priority: str) -> str:
    sla = {"P1": "15 minutes", "P2": "1 hour", "P3": "4 business hours", "P4": "1 business day"}
    return sla.get(priority, "unknown")


TOOLS = {"lookup_ticket": lookup_ticket, "sla_for": sla_for}

SYSTEM = """Answer by looping through Thought/Action/Observation.
Available actions: lookup_ticket[ticket_id], sla_for[priority].
Format EXACTLY:
Thought: <your reasoning>
Action: <tool>[<arg>]
... (I will reply with Observation: <result>) ...
When you know the answer, reply:
ANSWER: <final answer>"""

question = "Is ticket TT-1001 inside its SLA response target? What is the target?"
messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}]

for step in range(6):
    reply = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, stop=["Observation:"]
    ).choices[0].message.content.strip()
    print(f"\n--- model turn {step+1} ---\n{reply}")
    messages.append({"role": "assistant", "content": reply})
    if "ANSWER:" in reply:
        break
    # parse "Action: tool[arg]" and execute it
    action = [l for l in reply.splitlines() if l.startswith("Action:")][-1]
    name, arg = action.replace("Action:", "").strip().rstrip("]").split("[", 1)
    obs = TOOLS[name.strip()](arg.strip())
    print(f"Observation: {obs}")
    messages.append({"role": "user", "content": f"Observation: {obs}"})
