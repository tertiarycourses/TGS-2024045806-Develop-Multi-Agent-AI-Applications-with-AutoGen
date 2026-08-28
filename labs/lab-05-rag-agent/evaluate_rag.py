"""Lab 5 (Python script) — measure retrieval quality and latency.

RAG efficiency is measurable: a small gold set of question -> expected-source
pairs gives you hit@1, hit@3 and average latency. Change top_k or chunking and
re-run to see the numbers move. Run:
  uv run python lab-05-rag-agent/evaluate_rag.py
"""
import time
from pathlib import Path
import chromadb

DB_DIR = str(Path(__file__).parent.parent / "data" / "chroma_db")
col = chromadb.PersistentClient(path=DB_DIR).get_collection("opsdesk")

# Gold set: stable questions with the source that SHOULD come back first
GOLD = [
    ("Who approves VPN access for contractors?",              "POL-001"),
    ("How long must passwords be?",                           "POL-002"),
    ("How fast must a P1 incident be acknowledged?",          "PROC-101"),
    ("How often are production databases backed up?",         "PROC-102"),
    ("When can standard changes be deployed?",                "SLA-202"),
    ("Can I paste payroll data into an external AI tool?",    "POL-004"),
]

hit1 = hit3 = 0
lat = []
print(f"{'expected':9s} {'top-1':9s} {'hit@1':6s} {'hit@3':6s} {'ms':>6s}")
for q, expected in GOLD:
    t0 = time.perf_counter()
    res = col.query(query_texts=[q], n_results=3)
    ms = (time.perf_counter() - t0) * 1000
    lat.append(ms)
    got = res["ids"][0]
    h1, h3 = got[0] == expected, expected in got
    hit1 += h1
    hit3 += h3
    print(f"{expected:9s} {got[0]:9s} {str(h1):6s} {str(h3):6s} {ms:6.0f}")

n = len(GOLD)
print(f"\nhit@1 = {hit1}/{n} ({hit1/n:.0%})   hit@3 = {hit3}/{n} ({hit3/n:.0%})   "
      f"avg latency = {sum(lat)/n:.0f} ms")
print("Try: change n_results, re-chunk by paragraph in Lab 4, and re-run — "
      "these numbers are how you ANALYSE a RAG algorithm.")
