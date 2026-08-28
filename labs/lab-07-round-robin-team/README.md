# Lab 7 — Orchestrate a Round-Robin Multi-Agent Team

**Topic 3 · LO3** — Assess the feasibility of implementing multi-agent AI applications.

The first true multi-agent workflow: you hand-roll a two-model conversation to
feel the orchestration cost, then let `RoundRobinGroupChat` run a
writer/reviewer team with proper termination conditions.

| File | What it is |
|---|---|
| `two_model_conversation.py` | **Python script** — manual two-model writer/critic loop. |
| `team_round_robin.py` | **AutoGen script** — `RoundRobinGroupChat` + `TextMentionTermination("FINALISED") | MaxMessageTermination(10)`. |

## Run it

```bash
cd labs
uv run python lab-07-round-robin-team/two_model_conversation.py
uv run python lab-07-round-robin-team/team_round_robin.py
```

## What to look for

- The manual version needs two histories, copy-paste plumbing and a hand-made
  stop check — for just TWO agents.
- In the AutoGen version the agents share ONE conversation; the round-robin
  order is writer → reviewer → writer → …; the run ends with
  `stop_reason` naming the termination condition that fired.
- Bounded runs matter: without `MaxMessageTermination` a fussy reviewer could
  loop (and bill) forever.

## Done when

The team stops on FINALISED (not the message cap), and you can read the
speaker sequence and stop reason from the `TaskResult`.
