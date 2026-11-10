#!/usr/bin/env bash
# Clone 후 한 번 실행: 의존성 + pre-commit/pre-push 훅 설치
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

log() { printf '==> %s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail "'$1' 이(가) 필요합니다. 설치 후 다시 실행하세요. ($2)"
}

log "필수 도구 확인"
need_cmd node "https://nodejs.org/ (Node >= 20.9, 22 LTS 권장)"
need_cmd npm "Node.js와 함께 설치됩니다"
need_cmd uv "https://docs.astral.sh/uv/ (Python 3.11 도구)"

node_major="$(node -p "process.versions.node.split('.')[0]")"
if [[ "$node_major" -lt 20 ]]; then
  fail "Node >= 20.9 필요 (현재: $(node -v))"
fi

log "pre-commit 설치 (없으면 uv tool 로 설치)"
if ! command -v pre-commit >/dev/null 2>&1; then
  uv tool install pre-commit
fi
pre-commit --version

log "apps/web 의존성 (npm install)"
(
  cd "$root/apps/web"
  npm install
)

log "apps/api 의존성 (uv sync --group dev)"
(
  cd "$root/apps/api"
  uv sync --group dev
)

log "Git 훅 설치 (pre-commit + pre-push)"
if [[ ! -d "$root/.git" ]]; then
  fail ".git 이 없습니다. git clone 한 저장소 루트에서 실행하세요."
fi
pre-commit install --hook-type pre-commit
pre-commit install --hook-type pre-push

log "문서 하네스 확인"
bash "$root/scripts/check-harness.sh"

cat <<EOF

설정 완료.

다음 단계:
  # API (http://127.0.0.1:8000)
  cd apps/api && uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000

  # Web (http://localhost:3000)
  cd apps/web && npm run dev

  # 훅 전체 검증 (선택)
  pre-commit run --all-files

참고:
  - CI는 아직 없습니다. 커밋/푸시 전 로컬 훅이 품질 게이트입니다.
  - Ollama + qwen3.5:9b 가 있어야 /chat 이 동작합니다. (ollama list)
  - 자세한 내용: docs/SETUP.md
EOF
