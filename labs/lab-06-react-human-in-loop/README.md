# Lab 6 — Implement a ReAct Agent with Human-in-the-Loop

**Topic 3 · LO3** — Assess the feasibility of implementing multi-agent AI applications.

Two sides of agent control: first you hand-roll the ReAct
(Reason + Act) loop so the pattern is visible, then you put a human inside an
AutoGen team as the approval gate.

| File | What it is |
|---|---|
| `react_scratch.py` | **Python script** — Thought → Action → Observation loop from scratch. |
| `human_in_loop.py` | **AutoGen script** — `UserProxyAgent` + `TextMentionTermination("APPROVE")`. |

## Run it

```bash
cd labs
uv run python lab-06-react-human-in-loop/react_scratch.py
uv run python lab-06-react-human-in-loop/human_in_loop.py
```

## What to look for

- In `react_scratch.py` the model *plans* (`Thought:`), *acts*
  (`Action: lookup_ticket[TT-1001]`), reads your `Observation:` and loops —
  ReAct is just this conversation shape.
- In `human_in_loop.py` it is YOUR turn after every draft. Ask for a change
  ("make it more apologetic"), watch the revision, then type `APPROVE`.
- The `|` (OR) combination of termination conditions is the safety net every
  interactive team needs.

## Done when

The scratch ReAct agent answers with the P1 SLA target (15 minutes), and the
human-in-the-loop team stops only when you type APPROVE.
