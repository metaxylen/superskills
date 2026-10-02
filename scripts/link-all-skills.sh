#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
./scripts/link-cursor-skills.sh
./scripts/link-claude-skills.sh
./scripts/link-codex-skills.sh
./scripts/link-optional-skills.sh
echo "Done: v1 skills + optional skills linked for Cursor, Claude, and Codex."
