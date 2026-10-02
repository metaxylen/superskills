#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_NAME="superskills"
DEST="${CURSOR_LOCAL_PLUGINS_DIR:-$HOME/.cursor/plugins/local}/$PLUGIN_NAME"
DRY_RUN=0
REMOVE=0

usage() {
  cat <<EOF
Usage: $(basename "$0") [--dry-run] [--remove]

Copy this repo's Cursor plugin (.cursor-plugin + skills/) into:
  $DEST

Cursor loads skills from the plugin tree. External symlinks under
~/.cursor/plugins/local are not supported — this script uses rsync copy.

After install: Developer: Reload Window, then Customize → Skills.

Do not use together with ./scripts/link-cursor-skills.sh for the same
skill names (duplicate routing). Pick one install method.

Environment:
  CURSOR_LOCAL_PLUGINS_DIR  Base dir (default: ~/.cursor/plugins/local)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --remove) REMOVE=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
  shift
done

if [[ ! -f "$REPO_ROOT/.cursor-plugin/plugin.json" ]]; then
  echo "Missing .cursor-plugin/plugin.json" >&2
  exit 1
fi

if [[ $REMOVE -eq 1 ]]; then
  if [[ -d "$DEST" ]]; then
    if [[ $DRY_RUN -eq 1 ]]; then
      echo "would remove: $DEST"
    else
      rm -rf "$DEST"
      echo "removed: $DEST"
    fi
  else
    echo "not installed: $DEST"
  fi
  exit 0
fi

run() {
  if [[ $DRY_RUN -eq 1 ]]; then
    echo "would: $*"
  else
    "$@"
  fi
}

mkdir -p "$DEST"
run rsync -a --delete "$REPO_ROOT/.cursor-plugin/" "$DEST/.cursor-plugin/"
run rsync -a --delete \
  --exclude 'CONSOLIDATION.md' \
  --exclude 'README.md' \
  "$REPO_ROOT/skills/" "$DEST/skills/"

echo "installed: $DEST"
echo "next: reload Cursor window; check Customize → Skills for plugin '$PLUGIN_NAME'"
