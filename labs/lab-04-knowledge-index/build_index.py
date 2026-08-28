"""Lab 4 (Python script) — chunk a handbook, embed it, store it in ChromaDB.

The complete RAG indexing pipeline: load -> chunk -> embed -> store.
ChromaDB's default embedder (all-MiniLM-L6-v2) runs locally, so this
script needs no API key. Run:  uv run python lab-04-knowledge-index/build_index.py
"""
from pathlib import Path
import re
import chromadb

DATA = Path(__file__).parent.parent / "data"
DB_DIR = str(DATA / "chroma_db")

# 1. LOAD — read the synthetic company handbook
text = (DATA / "opsdesk_handbook.md").read_text()

# 2. CHUNK — split on '## ' section headers so each chunk is one coherent policy
sections = re.split(r"\n(?=## )", text)
chunks, ids, metas = [], [], []
for sec in sections:
    m = re.match(r"## (\w+-\d+) — (.+)", sec.strip())
    if not m:
        continue  # skip the intro header block
    doc_id, title = m.group(1), m.group(2)
    chunks.append(sec.strip())
    ids.append(doc_id)
    metas.append({"source": doc_id, "title": title})
print(f"Chunked handbook into {len(chunks)} policy chunks: {ids}")

# 3+4. EMBED + STORE — Chroma embeds each chunk locally and persists the index
client = chromadb.PersistentClient(path=DB_DIR)
try:
    client.delete_collection("opsdesk")   # rebuild cleanly on every run
except Exception:
    pass
col = client.create_collection("opsdesk", metadata={"hnsw:space": "cosine"})
col.add(documents=chunks, ids=ids, metadatas=metas)
print(f"Stored {col.count()} embedded chunks in {DB_DIR}")
