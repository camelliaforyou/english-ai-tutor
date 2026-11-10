#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
files=(README.md AGENTS.md apps/api/README.md apps/api/AGENTS.md apps/web/README.md apps/web/AGENTS.md docs/PRODUCT.md docs/ARCHITECTURE.md docs/API.md docs/DECISIONS.md docs/SETUP.md)
for file in "${files[@]}"; do
  if [[ ! -s "$file" ]]; then echo "MISSING or EMPTY: $file" >&2; exit 1; fi
done
echo "Harness documentation OK (${#files[@]} required files)."
