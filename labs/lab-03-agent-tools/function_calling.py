"""Lab 3 (Python script) — raw OpenAI function calling, no framework.

This shows what AutoGen automates: you declare a JSON tool schema, the model
returns a tool_call, YOUR code executes it, and you send the result back for
the final answer. Run:  uv run python lab-03-agent-tools/function_calling.py
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
    return json.dumps({"error": f"ticket {ticket_id} not found"})


TOOLS = [{
    "type": "function",
    "function": {
        "name": "lookup_ticket",
        "description": "Look up a TechTrend support ticket by its id, e.g. TT-1001.",
        "parameters": {
            "type": "object",
            "properties": {"ticket_id": {"type": "string"}},
            "required": ["ticket_id"],
        },
    },
}]

messages = [{"role": "user", "content": "What is ticket TT-1003 about and how urgent is it?"}]

# Round 1 — the model decides to call the tool
r1 = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
call = r1.choices[0].message.tool_calls[0]
print("Model requested tool:", call.function.name, call.function.arguments)

# Round 2 — we run the function and return the result to the model
result = lookup_ticket(**json.loads(call.function.arguments))
messages += [r1.choices[0].message, {"role": "tool", "tool_call_id": call.id, "content": result}]
r2 = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)

print("\nFinal answer:\n", r2.choices[0].message.content)
