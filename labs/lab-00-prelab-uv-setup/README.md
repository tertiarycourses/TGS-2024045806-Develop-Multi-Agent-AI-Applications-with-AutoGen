# Pre-Lab — Install uv and Prepare the Lab Environment

**Do this BEFORE Lab 1.** Every lab in this course runs inside one `uv`-managed
Python environment in the `labs/` folder. `uv` is a fast, modern Python package
and project manager that replaces `pip` + `venv` with a single tool.

## 1. Install uv

**macOS / Linux (Terminal):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal, then verify:

```bash
uv --version
```

You should see something like `uv 0.8.x`.

## 2. Get the lab files

Clone the course repository (the link is on your LMS course page), then move
into the `labs/` folder:

```bash
git clone https://github.com/tertiarycourses/TGS-2024045806-Develop-Multi-Agent-AI-Applications-with-AutoGen.git
cd TGS-2024045806-Develop-Multi-Agent-AI-Applications-with-AutoGen/labs
```

## 3. Install Python and the AutoGen packages

`uv sync` reads `pyproject.toml`, installs a private Python 3.10+ interpreter
if needed, creates `.venv/` and installs AutoGen AgentChat, the OpenAI
extension, ChromaDB and everything else the labs use:

```bash
uv sync
```

> If you were starting from an empty folder you would instead run
> `uv init` and then
> `uv add autogen-agentchat "autogen-ext[openai]" python-dotenv chromadb`.

## 4. Set your OpenAI API key

Copy the template and paste your key (the trainer provides a course key if you
do not have one):

```bash
cp .env.example .env
# then edit .env so it contains:  OPENAI_API_KEY=sk-...
```

The `.env` file stays on your machine — never commit it to Git and never paste
a key into a prompt, a slide or a screenshot.

## 5. Verify everything works

```bash
uv run python -c "import autogen_agentchat, autogen_ext, chromadb; print('AutoGen labs environment OK')"
```

Expected output:

```
AutoGen labs environment OK
```

## Troubleshooting

| Symptom | Fix |
|---|---|
| `uv: command not found` | Reopen the terminal, or add `~/.local/bin` (macOS/Linux) to PATH. |
| Corporate proxy/SSL errors | Ask the trainer for the offline wheel bundle, or set `UV_NATIVE_TLS=1`. |
| `ModuleNotFoundError` later in a lab | Run commands with the `uv run` prefix so the `.venv` is used. |
