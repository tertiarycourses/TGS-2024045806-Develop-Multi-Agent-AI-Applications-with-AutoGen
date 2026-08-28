# Lab 4 — Build a Knowledge Index with Embeddings and a Vector Database

**Topic 2 · LO2** — Analyze RAG algorithms to improve efficiency.

You build the retrieval half of RAG from mock data: chunk the synthetic
TechTrend handbook (`../data/opsdesk_handbook.md`), embed each chunk locally,
store the vectors in ChromaDB, then run similarity searches and inspect the
cosine distances.

| File | What it is |
|---|---|
| `build_index.py` | **Python script** — load → chunk → embed → store (no API key needed). |
| `similarity_search.py` | **Python script** — query the index, print top-3 sources + distances. |
| `index_agent.py` | **AutoGen script** — the index wrapped as a `FunctionTool` for an agent. |

## Run it

```bash
cd labs
uv run python lab-04-knowledge-index/build_index.py
uv run python lab-04-knowledge-index/similarity_search.py
uv run python lab-04-knowledge-index/index_agent.py
```

## What to look for

- Chunking on `## ` headers keeps one policy per chunk — chunk boundaries are a
  design decision that directly changes retrieval quality.
- The VPN question retrieves `POL-001` at the smallest distance; the backup
  question retrieves `PROC-102`. Distances quantify similarity — this is the
  measurable part of RAG efficiency.
- `index_agent.py` answers with source ids like `[POL-001]` — grounding.

## Done when

`build_index.py` stores 10 chunks, and the top-1 result for the P1 question is
`PROC-101` (incident response) in `similarity_search.py`.
