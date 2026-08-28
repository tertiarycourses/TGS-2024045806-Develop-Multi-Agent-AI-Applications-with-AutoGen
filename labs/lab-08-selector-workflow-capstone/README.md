# Lab 8 — Route Specialists with SelectorGroupChat (Capstone)

**Topic 3 · LO3** — Assess the feasibility of implementing multi-agent AI applications.

The capstone OpsDesk workflow: a planner and two tool-equipped specialists
(tickets + policy RAG) coordinated by `SelectorGroupChat`, where an LLM
selector reads each agent's `description` and routes dynamically. Then you run
the no-LLM readiness checks that decide whether this workflow is fit to ship.

| File | What it is |
|---|---|
| `selector_team.py` | **AutoGen script** — planner + ticket specialist + policy specialist under `SelectorGroupChat`. |
| `run_checks.py` | **Python script** — feasibility/readiness checks (data, index, retrieval accuracy, secrets hygiene). |

Requires the Lab 4 index (`uv run python lab-04-knowledge-index/build_index.py`).

## Run it

```bash
cd labs
uv run python lab-08-selector-workflow-capstone/selector_team.py
uv run python lab-08-selector-workflow-capstone/run_checks.py
```

## What to look for

- The selector routes: planner → ticket_specialist (tool call) →
  policy_specialist (RAG with `(POL-001)` citation) → planner's final reply →
  TERMINATE. Routing is driven by the agents' `description` fields — write
  them like job adverts.
- `run_checks.py` proves feasibility with evidence: index health, retrieval
  accuracy, `.env` kept out of Git. Every check must PASS before you would
  put a workflow like this in front of users.
- Optional: launch AutoGen Studio (`uv run --with autogenstudio autogenstudio ui`)
  and rebuild this team visually.

## Done when

The team run ends with stop reason `TextMentionTermination` on TERMINATE and a
customer-ready reply citing POL-001, and `run_checks.py` prints `0 failed`.
