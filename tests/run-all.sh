#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
./tests/skill-frontmatter.sh
python3 ./tests/routing_eval.py
