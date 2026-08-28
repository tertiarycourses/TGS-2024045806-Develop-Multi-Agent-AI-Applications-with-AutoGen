"""Lab 4 (Python script) — similarity search against the vector index.

Ask questions in natural language and inspect WHICH chunks come back and HOW
similar they are (cosine distance). This is the retrieval half of RAG,
isolated so you can evaluate it. Run:
  uv run python lab-04-knowledge-index/similarity_search.py
"""
from pathlib import Path
import chromadb

DB_DIR = str(Path(__file__).parent.parent / "data" / "chroma_db")
col = chromadb.PersistentClient(path=DB_DIR).get_collection("opsdesk")

QUESTIONS = [
    "Who has to approve VPN access for a contractor?",
    "How fast must a critical P1 incident be acknowledged?",
    "How long are database backups kept?",
]

for q in QUESTIONS:
    res = col.query(query_texts=[q], n_results=3)
    print(f"\nQ: {q}")
    for doc_id, dist, meta in zip(res["ids"][0], res["distances"][0], res["metadatas"][0]):
        print(f"   {doc_id:9s}  distance={dist:.3f}  {meta['title']}")
    print(f"   top-1 evidence: {res['documents'][0][0][:120]}...")
