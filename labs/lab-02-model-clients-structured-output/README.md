# Lab 2 — Configure Model Clients and Structured Output

**Topic 1 · LO1** — Evaluate LLM AI models by identifying their strengths and limitations.

You compare a cloud model against a local LLM (Ollama, optional), then force an
AutoGen agent to answer in a validated Pydantic schema instead of free text.

| File | What it is |
|---|---|
| `model_clients.py` | **Python script** — the same prompt against OpenAI cloud and a local Ollama model, with timing. |
| `structured_agent.py` | **AutoGen script** — `AssistantAgent` with `output_content_type=TicketTriage` returning validated JSON. |

## Run it

```bash
cd labs
uv run python lab-02-model-clients-structured-output/model_clients.py
uv run python lab-02-model-clients-structured-output/structured_agent.py
```

Optional local LLM: install Ollama from https://ollama.com, then
`ollama pull llama3.2` before running `model_clients.py`.

## What to look for

- Latency and answer quality differ between the cloud and local model — that
  difference (plus cost and privacy) is how you *evaluate* which model fits an app.
- `structured_agent.py` prints fields, not prose: `priority: P1`,
  `needs_human: True`. Downstream code can branch on these safely.

## Done when

The triage agent returns a valid `TicketTriage` object for the outage ticket
with `priority` = `P1`.
