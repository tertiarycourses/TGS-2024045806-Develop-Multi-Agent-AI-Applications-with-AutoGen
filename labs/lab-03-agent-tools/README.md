# Lab 3 — Equip an Agent with Tools

**Topic 1 · LO1** — Evaluate LLM AI models by identifying their strengths and limitations.

An LLM cannot see your data — tools fix that. You first do raw OpenAI function
calling by hand, then let AutoGen's `FunctionTool` do the schema, execution and
reflection for you, against the synthetic ticket dataset in `../data/tickets.json`.

| File | What it is |
|---|---|
| `function_calling.py` | **Python script** — hand-rolled OpenAI function calling (schema → tool_call → result → answer). |
| `tool_agent.py` | **AutoGen script** — `AssistantAgent` with two `FunctionTool`s and `reflect_on_tool_use=True`. |

## Run it

```bash
cd labs
uv run python lab-03-agent-tools/function_calling.py
uv run python lab-03-agent-tools/tool_agent.py
```

## What to look for

- In `function_calling.py` the model *asks* for `lookup_ticket("TT-1003")` —
  your code executes it. The model never runs anything itself.
- In `tool_agent.py` watch the streamed events: `ToolCallRequestEvent` →
  `ToolCallExecutionEvent` → the final grounded answer that uses BOTH tools.
- The system message makes the tools read-only — a deliberate guardrail.

## Done when

The AutoGen agent answers with the real subject of TT-1005 (account locked)
and the correct open P2 count from the dataset — no invented facts.
