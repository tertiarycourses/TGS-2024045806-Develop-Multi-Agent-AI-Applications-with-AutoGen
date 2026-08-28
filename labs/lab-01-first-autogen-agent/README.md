# Lab 1 — Set Up AutoGen and Run Your First Agent

**Topic 1 · LO1** — Evaluate LLM AI models by identifying their strengths and limitations.

You verify the lab environment from the Pre-Lab, call an LLM directly with the
OpenAI SDK, then wrap the same model in an AutoGen `AssistantAgent` and stream
its reply with the `Console` UI.

| File | What it is |
|---|---|
| `llm_app.py` | **Python script** — a plain OpenAI chat-completion call (no framework). |
| `first_agent.py` | **AutoGen script** — the same model as an AutoGen `AssistantAgent`. |

## Run it

```bash
cd labs
uv run python lab-01-first-autogen-agent/llm_app.py
uv run python lab-01-first-autogen-agent/first_agent.py
```

## What to look for

- `llm_app.py` prints the raw model reply plus the token count — one stateless call.
- `first_agent.py` streams a `TextMessage` from `ops_assistant` — AutoGen manages
  the event loop, message types and model client for you.
- Change `temperature` in `llm_app.py` to `0` and re-run twice: the answer becomes
  repeatable — your first evidence of an LLM strength/limitation trade-off.

## Done when

Both scripts print a model reply with no traceback, and you can explain the
difference between calling a model and running an agent.
