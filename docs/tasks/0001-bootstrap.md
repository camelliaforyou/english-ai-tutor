# Task 0001 — Bootstrap applications

Status: TODO

## Goal

Create working Next.js 16 and FastAPI applications while retaining the harness docs.

## Scope

- Scaffold `apps/web` and `apps/api`
- Implement `GET /health`
- Add a text-only `POST /chat` with Ollama `qwen3.5:9b`
- Verify local execution and record actual results

## Out of scope

Whisper, Kokoro, auth, databases, streaming, deployments.

## Acceptance criteria

- `npm run dev` starts web
- `uv run uvicorn main:app --reload` starts API
- `/health` returns 200
- `/chat` returns a short English reply
- Docs updated to match implemented contracts

## Agent handoff

Before: identify files and checks. After: summarize diff, commands executed, observed results, limitations and next task.
