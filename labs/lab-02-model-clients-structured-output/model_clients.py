"""Lab 2 (Python script) — comparing model clients: OpenAI cloud vs local LLM.

AutoGen talks to any OpenAI-compatible endpoint. This script calls
(1) OpenAI's cloud API and, if you have Ollama running locally,
(2) the same request against a local model — so you can compare quality,
speed and cost. Run:  uv run python lab-02-model-clients-structured-output/model_clients.py
"""
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
PROMPT = "List two strengths and two limitations of large language models."


def ask(client: OpenAI, model: str, label: str) -> None:
    t0 = time.perf_counter()
    r = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": PROMPT}]
    )
    dt = time.perf_counter() - t0
    print(f"\n=== {label} ({model}) — {dt:.1f}s ===")
    print(r.choices[0].message.content[:600])


# 1. Cloud model (OpenAI)
ask(OpenAI(api_key=os.getenv("OPENAI_API_KEY")), "gpt-4o-mini", "OpenAI cloud")

# 2. Local model via Ollama (optional — run `ollama pull llama3.2` first)
try:
    local = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    ask(local, "llama3.2", "Local Ollama")
except Exception as e:
    print(f"\n[Ollama not running — skipped local model: {type(e).__name__}]")
