# Develop Multi-Agent AI Applications with AutoGen — Hands-On Labs

**WSQ Course Code:** TGS-2024045806 · Tertiary Infotech Academy Pte Ltd

8 labs across 3 topics · 2 days. Every lab folder contains a **plain Python
script** (the concept without a framework) and an **AutoGen script** (the same
concept with AutoGen AgentChat), plus a README with run instructions.

**Start with the Pre-Lab** — it installs `uv`, the lab environment and your API key.

| # | Lab | Folder |
|---|-----|--------|
| 0 | Pre-Lab: Install uv and Prepare the Environment | [lab-00-prelab-uv-setup](lab-00-prelab-uv-setup/) |

## Topic 1 — Introduction to LLM AI Orchestration

| # | Lab | Folder |
|---|-----|--------|
| 1 | Set Up AutoGen and Run Your First Agent | [lab-01-first-autogen-agent](lab-01-first-autogen-agent/) |
| 2 | Configure Model Clients and Structured Output | [lab-02-model-clients-structured-output](lab-02-model-clients-structured-output/) |
| 3 | Equip an Agent with Tools | [lab-03-agent-tools](lab-03-agent-tools/) |

## Topic 2 — Retrieval-Augmented Generation (RAG)

| # | Lab | Folder |
|---|-----|--------|
| 4 | Build a Knowledge Index with Embeddings and a Vector Database | [lab-04-knowledge-index](lab-04-knowledge-index/) |
| 5 | Build and Evaluate a Grounded RAG Agent | [lab-05-rag-agent](lab-05-rag-agent/) |

## Topic 3 — Implementing a Multi-Agent AI Workflow

| # | Lab | Folder |
|---|-----|--------|
| 6 | Implement a ReAct Agent with Human-in-the-Loop | [lab-06-react-human-in-loop](lab-06-react-human-in-loop/) |
| 7 | Orchestrate a Round-Robin Multi-Agent Team | [lab-07-round-robin-team](lab-07-round-robin-team/) |
| 8 | Route Specialists with SelectorGroupChat (Capstone) | [lab-08-selector-workflow-capstone](lab-08-selector-workflow-capstone/) |

## Mock data

`data/opsdesk_handbook.md` (synthetic IT policy handbook with POL-/PROC-/SLA-/SEC- ids)
and `data/tickets.json` (synthetic support tickets) power the tool and RAG labs.
All data is fictional. Keep your `.env` out of Git.

## Quick start

```bash
cd labs
uv sync
cp .env.example .env   # paste your OPENAI_API_KEY
uv run python lab-01-first-autogen-agent/first_agent.py
```
