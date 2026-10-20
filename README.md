# Develop Multi-Agent AI Applications with AutoGen

Build, ground and orchestrate teams of AI agents with Microsoft AutoGen — from your first LLM call to a routed multi-agent workflow with RAG, tools and human-in-the-loop approval.

| Course detail | Information |
|---|---|
| Course code | `TGS-2024045806` |
| Programme | WSQ (Singapore Workforce Skills Qualifications) |
| Duration | 2 days · 16 hours (including 2 hours of assessment) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-develop-multi-agent-ai-applications-with-autogen.html) |
| Funding | Up to 50% SkillsFuture course fee funding, or up to 70% for eligible SME employees and Singapore Citizens aged 40 and above. Eligibility and terms apply — see the course page for current details. |

## About the course

Large Language Models answer; agents act. This hands-on WSQ course teaches you to develop multi-agent AI applications with **Microsoft AutoGen (AgentChat)**: evaluating LLMs by their measured strengths and limitations, grounding agents in your own data with **Retrieval-Augmented Generation (RAG)**, equipping agents with function-calling tools, and orchestrating specialist agents into bounded, human-supervised workflows. Every concept is practised twice — once as a plain Python script so the mechanism is visible, and once with AutoGen so you see what the framework automates.

Aligned to the Skills Framework TSC **Artificial Intelligence Application (AER-TEM-4026-1.1)**.

## Learning outcomes

- **LO1** — Evaluate Large Language Model (LLM) AI models by identifying their strengths and limitations.
- **LO2** — Analyze Retrieval-Augmented Generation (RAG) algorithms to improve efficiency.
- **LO3** — Assess the feasibility of implementing multi-agent AI applications.

## Topics covered

1. **Introduction to LLM AI Orchestration** — LLM strengths & limitations · AI agents and the agentic loop · the AutoGen stack · model clients (cloud and local) · structured output · function-calling tools
2. **Retrieval-Augmented Generation (RAG)** — embeddings · chunking · vector databases (ChromaDB) · similarity search · grounded RAG agents with citations · retrieval evaluation (hit@k, latency)
3. **Implementing a Multi-Agent AI Workflow** — ReAct · human-in-the-loop · RoundRobinGroupChat · termination conditions · SelectorGroupChat routing · feasibility assessment · AutoGen Studio

## Labs

Start with the Pre-Lab, then work in order — each lab builds on the one before. Each lab folder contains a plain **Python script**, an **AutoGen script** and a README with run instructions. The tool and RAG labs use the synthetic TechTrend dataset in [labs/data/](labs/data/).

| # | Lab |
|---|-----|
| 0 | [Pre-Lab — Install uv and Prepare the Environment](labs/lab-00-prelab-uv-setup/) |
| 1 | [Set Up AutoGen and Run Your First Agent](labs/lab-01-first-autogen-agent/) |
| 2 | [Configure Model Clients and Structured Output](labs/lab-02-model-clients-structured-output/) |
| 3 | [Equip an Agent with Tools](labs/lab-03-agent-tools/) |
| 4 | [Build a Knowledge Index with Embeddings and a Vector Database](labs/lab-04-knowledge-index/) |
| 5 | [Build and Evaluate a Grounded RAG Agent](labs/lab-05-rag-agent/) |
| 6 | [Implement a ReAct Agent with Human-in-the-Loop](labs/lab-06-react-human-in-loop/) |
| 7 | [Orchestrate a Round-Robin Multi-Agent Team](labs/lab-07-round-robin-team/) |
| 8 | [Route Specialists with SelectorGroupChat (Capstone)](labs/lab-08-selector-workflow-capstone/) |

## What's in this repository

- [labs/](labs/) — the 8 hands-on labs + Pre-Lab, one `uv`-managed Python project (`uv sync` and go)
- [LG-Develop Multi-Agent AI Applications with AutoGen.md](LG-Develop%20Multi-Agent%20AI%20Applications%20with%20AutoGen.md) — the Learner Guide (Markdown mirror) with detailed step-by-step instructions
- `courseware/` — the current slide deck (`Develop Multi-Agent AI Applications with AutoGen-v9.pptx` + PDF), Lesson Plan and Learner Guide (DOCX + PDF)

**Distribution boundary:** this public repository carries learner-facing material only. Assessments, answer keys and trainer-only records are distributed privately through the LMS/Google Drive and are never published here. Keep your `labs/.env` (API key) out of Git.

## Getting started

```bash
git clone https://github.com/tertiarycourses/TGS-2024045806-Develop-Multi-Agent-AI-Applications-with-AutoGen.git
cd TGS-2024045806-Develop-Multi-Agent-AI-Applications-with-AutoGen/labs
uv sync
cp .env.example .env   # paste your OPENAI_API_KEY
uv run python lab-01-first-autogen-agent/first_agent.py
```

---

Conducted by **Tertiary Infotech Academy Pte Ltd** (UEN 201200696W) · [tertiarycourses.com.sg](https://www.tertiarycourses.com.sg) · enquiry@tertiaryinfotech.com · +65 6100 0613
