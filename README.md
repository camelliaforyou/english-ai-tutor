# English AI Tutor

Local-first English speaking tutor built with Next.js 16, FastAPI and Ollama. This repository is a learning project and a portfolio-quality application, not a generic AI chat platform.

## MVP

1. Push-to-talk English recording in the browser.
2. Local speech-to-text (Whisper family).
3. Short conversational replies from Ollama `qwen3.5:9b` (thinking disabled where supported).
4. Local text-to-speech (Kokoro).
5. Transcript and post-conversation language feedback.

## Non-goals (MVP)

Cloud APIs, authentication, payments, multi-user hosting, always-on listening, full-duplex streaming, and pronunciation scoring from transcripts alone.

## Structure

- `apps/web/`: Next.js UI
- `apps/api/`: FastAPI orchestration and model adapters
- `docs/`: source of truth for architecture, product scope, decisions and tasks
- `AGENTS.md`: agent operating contract; nested files add app-specific constraints
- `scripts/dev-setup.sh`: clone 후 의존성·Git 훅 원샷 설치
- `scripts/check-harness.sh`: verifies mandatory documentation

## Setup

Prerequisites: Node >=20.9 (22 LTS recommended), Python 3.11, uv, Git. Ollama + `qwen3.5:9b` for `/chat`.

```bash
git clone <repo-url> english-ai-tutor
cd english-ai-tutor
./scripts/dev-setup.sh
```

There is **no remote CI yet**. Local `pre-commit` / `pre-push` hooks are the quality gate — run `dev-setup.sh` once per clone. Full notes: `docs/SETUP.md`.

## Working agreement

Read `AGENTS.md`, `docs/PRODUCT.md`, and `docs/ARCHITECTURE.md` before changing code. Work in small verifiable steps; update relevant docs when changing contracts. Never claim tests ran unless actually executed.
