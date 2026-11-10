# API — FastAPI

Python 3.11 + uv. Responsible for voice processing orchestration, conversation sessions and learner feedback.

## Planned endpoints

- `GET /health`: service health
- `POST /chat`: text-only local LLM smoke test
- `POST /voice/conversation`: audio upload -> transcript -> reply -> synthesized audio (later milestone)

These are **planned contracts**, not implemented by this harness overlay. Define exact request/response shapes before implementation.

## Development (after app scaffolding)

```bash
cd apps/api
uv sync --group dev
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Lint / format (Ruff):

```bash
uv run ruff check --fix .
uv run ruff format .
```

Repo-root `pre-commit` runs the same checks on commit. See `docs/SETUP.md`.

## Rules

See `AGENTS.md`. Do not load heavyweight models per request. Separate routers, orchestration, and provider adapters. Keep LLM at `http://127.0.0.1:11434` by default. Handle empty STT and upstream failures explicitly.
