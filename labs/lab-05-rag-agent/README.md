# Lab 5 — Build and Evaluate a Grounded RAG Agent

**Topic 2 · LO2** — Analyze RAG algorithms to improve efficiency.

You turn Lab 4's index into a production-shaped RAG agent — retrieval tool,
mandatory citations, refusal on missing evidence, prompt-injection defence —
then measure retrieval quality with a gold question set.

| File | What it is |
|---|---|
| `rag_agent.py` | **AutoGen script** — grounded RAG `AssistantAgent` with a `retrieve()` tool. |
| `evaluate_rag.py` | **Python script** — hit@1 / hit@3 / latency over 6 gold questions. |

Requires the index from Lab 4 (`uv run python lab-04-knowledge-index/build_index.py`).

## Run it

```bash
cd labs
uv run python lab-05-rag-agent/rag_agent.py
uv run python lab-05-rag-agent/evaluate_rag.py
```

## What to look for

- Question 1 is answered with citations like `(POL-001)`.
- Question 2 (annual leave) is NOT in the handbook — the agent must refuse,
  not hallucinate. That refusal is a feature you engineered.
- `evaluate_rag.py` prints a scoreboard. hit@1 should be ≥ 5/6. Retrieval
  quality and latency are the efficiency levers of every RAG system.

## Done when

The RAG agent cites sources on the VPN question, refuses the annual-leave
question, and your evaluation prints hit@1 ≥ 83% with single/double-digit-ms
latency.
