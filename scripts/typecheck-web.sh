#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root/apps/web"

if [[ ! -d node_modules ]]; then
  echo "apps/web/node_modules 가 없습니다. 먼저: ./scripts/dev-setup.sh" >&2
  exit 1
fi

npm run typecheck
