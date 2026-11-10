# Setup runbook

## Clone 후 (권장)

저장소 루트에서 한 번만 실행합니다.

```bash
./scripts/dev-setup.sh
```

이 스크립트가 하는 일:

1. Node / npm / uv 존재 여부 확인
2. `pre-commit` 설치 (`uv tool install`, 없을 때만)
3. `apps/web` → `npm install`
4. `apps/api` → `uv sync --group dev`
5. Git 훅 설치: `pre-commit` + `pre-push`
6. `scripts/check-harness.sh`로 필수 문서 확인

완료 후 앱 실행:

```bash
# Terminal 1 — API
cd apps/api
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2 — Web
cd apps/web
npm run dev
```

Ollama에 `qwen3.5:9b`가 있어야 `/chat`이 동작합니다.

```bash
ollama list   # qwen3.5:9b 확인
# 없으면: ollama pull qwen3.5:9b
```

## Prerequisites

| Tool | Notes |
| --- | --- |
| Node.js | >= 20.9 (22 LTS recommended) |
| npm | comes with Node |
| Python | 3.11 (via uv) |
| uv | https://docs.astral.sh/uv/ |
| Git | clone + hooks |
| Ollama | local LLM; model `qwen3.5:9b` for `/chat` |

Optional later: Whisper-family STT, Kokoro TTS (voice pipeline).

## Local quality gates (CI 없음)

이 레포에는 아직 GitHub Actions 등 **원격 CI가 없습니다.**
대신 각 개발자 로컬에서 pre-commit 훅이 품질 게이트 역할을 합니다.

| When | What runs |
| --- | --- |
| `git commit` | trailing whitespace, YAML/JSON, Ruff (api), Prettier/ESLint check (web), harness docs |
| `git push` | TypeScript `tsc --noEmit` (web) |

설정 파일:

- 루트: `.pre-commit-config.yaml` (오케스트레이션만)
- web 포맷: `apps/web/.prettierrc`
- api 포맷/린트: `apps/api/pyproject.toml` (`[tool.ruff]`)

훅은 `.git/hooks`에만 설치되므로 **clone한 사람마다** `./scripts/dev-setup.sh`가 필요합니다. (훅 자체는 git에 커밋되지 않음)

수동 재설치:

```bash
pre-commit install --hook-type pre-commit
pre-commit install --hook-type pre-push
```

전체 검증:

```bash
pre-commit run --all-files
```

앱별 수동 명령:

```bash
cd apps/web && npm run lint && npm run format:check && npm run typecheck
cd apps/api && uv run ruff check . && uv run ruff format --check .
```

커밋 훅은 **자동 수정이 아니라 검사**입니다. 포맷이 깨져 있으면 로컬에서 고친 뒤 다시 커밋하세요.

```bash
cd apps/web && npm run format
cd apps/api && uv run ruff check --fix . && uv run ruff format .
```

## Initial scaffolding (legacy / empty apps)

앱 디렉터리가 아직 스캐폴딩되지 않은 경우에만:

```bash
# From repository root
npx create-next-app@16 apps/web --typescript --tailwind --eslint --app --src-dir --use-npm
# If create-next-app refuses a non-empty directory, scaffold into a temporary directory,
# then merge generated app files into apps/web without overwriting README.md or AGENTS.md.
uv init --app apps/api --python 3.11
cd apps/api && uv add fastapi 'uvicorn[standard]' httpx python-multipart && cd ../..
```

The same non-empty-directory concern applies to `uv init`; if it refuses, initialize a temporary app directory and merge while preserving the harness docs.

After scaffolding, implement `/health`, then `/chat`, then audio modules. Verify `ollama list` includes `qwen3.5:9b`. Use `scripts/check-harness.sh` to verify documentation coverage.
