#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLONE=0
UPSTREAM_DIR="$REPO_ROOT/.upstream"

repos=(
  "obra/superpowers"
  "mattpocock/skills"
  "anthropics/skills"
  "addyosmani/agent-skills"
  "avenoxai/avenoxskills"
)

usage() {
  echo "Usage: $(basename "$0") [--clone]"
  echo "List upstream repos and optional plugin.json version fields (GitHub raw)."
  echo "  --clone  Shallow clone missing repos into .upstream/ (gitignored)"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --clone) CLONE=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
  shift
done

manifest_paths=(
  ".cursor-plugin/plugin.json"
  ".claude-plugin/plugin.json"
  "plugin.json"
)

fetch_version() {
  local repo="$1"
  local path
  for path in "${manifest_paths[@]}"; do
    local url="https://raw.githubusercontent.com/${repo}/main/${path}"
    local body
    body="$(curl -fsSL "$url" 2>/dev/null)" || continue
    local ver name
    ver="$(printf '%s' "$body" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('version','?'))" 2>/dev/null || echo "?")"
    name="$(printf '%s' "$body" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('name','?'))" 2>/dev/null || echo "?")"
    echo "  manifest: $path → name=$name version=$ver"
    return 0
  done
  echo "  manifest: (none found on main)"
}

echo "Upstream sources (see docs/SOURCES.md, docs/UPSTREAM-WORKFLOW.md)"
echo

for repo in "${repos[@]}"; do
  echo "■ $repo"
  echo "  https://github.com/$repo"
  fetch_version "$repo"

  if [[ $CLONE -eq 1 ]]; then
    local_name="${repo##*/}"
    dest="$UPSTREAM_DIR/$local_name"
    if [[ -d "$dest/.git" ]]; then
      echo "  clone: $dest (exists)"
    else
      mkdir -p "$UPSTREAM_DIR"
      git clone --depth 1 "https://github.com/$repo.git" "$dest"
      echo "  clone: $dest"
    fi
  fi
  echo
done

echo "superskills (this repo):"
if [[ -f "$REPO_ROOT/.cursor-plugin/plugin.json" ]]; then
  python3 -c "import json, pathlib; d=json.loads(pathlib.Path('$REPO_ROOT/.cursor-plugin/plugin.json').read_text()); print('  .cursor-plugin/plugin.json → name=%s version=%s' % (d.get('name'), d.get('version')))"
fi
