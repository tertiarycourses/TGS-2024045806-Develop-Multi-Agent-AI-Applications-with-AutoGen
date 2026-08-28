"""Lab 4 (AutoGen script) — give an agent eyes on the vector index.

A first look at retrieval + agent: the ChromaDB query becomes a FunctionTool,
so the agent can search the handbook before answering (fully grounded RAG
comes in Lab 5). Run:  uv run python lab-04-knowledge-index/index_agent.py
"""
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
import chromadb
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
DB_DIR = str(Path(__file__).parent.parent / "data" / "chroma_db")
col = chromadb.PersistentClient(path=DB_DIR).get_collection("opsdesk")


def search_handbook(query: str) -> str:
    """Semantic search over the TechTrend IT operations handbook. Returns the 3 most similar policy chunks with their source ids."""
    res = col.query(query_texts=[query], n_results=3)
    out = []
    for doc_id, doc in zip(res["ids"][0], res["documents"][0]):
        out.append(f"[{doc_id}]\n{doc}")
    return "\n\n".join(out)


search_tool = FunctionTool(search_handbook, description="Search the IT operations handbook.")
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

agent = AssistantAgent(
    name="handbook_agent",
    model_client=model_client,
    tools=[search_tool],
    reflect_on_tool_use=True,
    system_message=(
        "Answer ONLY from the handbook chunks returned by search_handbook. "
        "Cite the source id (e.g. POL-001) after every fact."
    ),
)


async def main() -> None:
    await Console(agent.run_stream(task="What are the rules for contractor VPN access?"))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
