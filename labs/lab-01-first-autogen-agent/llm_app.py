"""Lab 1 (Python script) — a minimal LLM app with the plain OpenAI SDK.

Before any agent framework, this is what every LLM call looks like:
messages in, one completion out. Run:  uv run python lab-01-first-autogen-agent/llm_app.py
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.7,
    messages=[
        {"role": "system", "content": "You are a concise IT operations assistant."},
        {"role": "user", "content": "In 3 bullet points, what is an AI agent?"},
    ],
)

print("Model reply:\n")
print(response.choices[0].message.content)
print("\nTokens used:", response.usage.total_tokens)
