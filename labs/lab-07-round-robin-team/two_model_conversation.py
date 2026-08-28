"""Lab 7 (Python script) — two models conversing, without a framework.

A hand-rolled writer/critic exchange: two chat histories, alternating turns,
a manual stop check. Compare its length and fragility with team_round_robin.py
— this is the orchestration cost AutoGen removes.
Run:  uv run python lab-07-round-robin-team/two_model_conversation.py
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

WRITER_SYS = "You write a short IT announcement. Revise per the critic's feedback. One draft per turn."
CRITIC_SYS = ("You are a strict critic. Give at most 2 short improvement points. "
              "If the draft is good enough, reply exactly DONE.")

task = "Announce that MFA becomes mandatory for e-mail and VPN next Monday."
writer_hist = [{"role": "system", "content": WRITER_SYS}, {"role": "user", "content": task}]
critic_hist = [{"role": "system", "content": CRITIC_SYS}]

for turn in range(1, 5):
    draft = client.chat.completions.create(model="gpt-4o-mini", messages=writer_hist)\
        .choices[0].message.content
    print(f"\n=== WRITER (turn {turn}) ===\n{draft}")

    critic_hist.append({"role": "user", "content": draft})
    feedback = client.chat.completions.create(model="gpt-4o-mini", messages=critic_hist)\
        .choices[0].message.content
    print(f"\n=== CRITIC (turn {turn}) ===\n{feedback}")

    if "DONE" in feedback:            # manual termination condition
        print("\nCritic accepted the draft — stopping.")
        break
    writer_hist += [{"role": "assistant", "content": draft},
                    {"role": "user", "content": f"Feedback: {feedback}"}]
    critic_hist.append({"role": "assistant", "content": feedback})
