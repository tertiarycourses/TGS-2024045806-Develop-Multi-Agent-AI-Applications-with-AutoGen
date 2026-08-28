"""Lab 8 (Python script) — feasibility & readiness checks for the capstone.

Before you would ship the OpsDesk workflow, verify the parts that don't need
an LLM at all: data present, index healthy, retrieval accurate, secrets out of
Git. This is the assessment habit of LO3 — feasibility is checked, not felt.
Run:  uv run python lab-08-selector-workflow-capstone/run_checks.py
"""
import json
import sys
from pathlib import Path

LABS = Path(__file__).parent.parent
DATA = LABS / "data"
passed = failed = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global passed, failed
    passed, failed = passed + ok, failed + (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


print("1. Mock data present")
check("handbook exists", (DATA / "opsdesk_handbook.md").exists())
tickets = json.loads((DATA / "tickets.json").read_text())["tickets"]
check("tickets well-formed", all({"id", "priority", "status"} <= set(t) for t in tickets),
      f"{len(tickets)} tickets")

print("2. Vector index healthy")
try:
    import chromadb
    col = chromadb.PersistentClient(path=str(DATA / "chroma_db")).get_collection("opsdesk")
    check("index exists with 10 chunks", col.count() == 10, f"count={col.count()}")
    top1 = col.query(query_texts=["contractor VPN approval"], n_results=1)["ids"][0][0]
    check("VPN query retrieves POL-001", top1 == "POL-001", f"got {top1}")
except Exception as e:
    check("chroma index", False, f"{type(e).__name__}: {e} (run Lab 4 build_index.py)")

print("3. Secrets hygiene")
env = LABS / ".env"
gitignore = ""
for p in (LABS / ".gitignore", LABS.parent / ".gitignore"):
    if p.exists():
        gitignore += p.read_text()
check(".env exists locally", env.exists())
check(".env is git-ignored", ".env" in gitignore, "add '.env' to .gitignore!")
key = ""
if env.exists():
    for line in env.read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            key = line.split("=", 1)[1].strip()
check("API key set (not the placeholder)", bool(key) and "your-key" not in key)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
