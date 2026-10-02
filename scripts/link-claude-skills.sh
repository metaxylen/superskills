#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
CLAUDE_SKILLS="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
DRY_RUN=0
UNLINK=0

usage() {
  cat <<EOF
Usage: $(basename "$0") [--dry-run] [--unlink]

Symlink each v1 skill from $SKILLS_SRC into $CLAUDE_SKILLS for Claude Code.
Same SKILL.md files as Cursor; different path than ~/.cursor/skills.

If ~/.claude/skills did not exist when Claude Code started, run /reload-skills
or restart the app.

Environment:
  CLAUDE_SKILLS_DIR  Override destination (default: ~/.claude/skills)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --unlink) UNLINK=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
  shift
done

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "Missing skills directory: $SKILLS_SRC" >&2
  exit 1
fi

mkdir -p "$CLAUDE_SKILLS"

link_one() {
  local name="$1"
  local src="$SKILLS_SRC/$name"
  local dest="$CLAUDE_SKILLS/$name"

  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "skip (no SKILL.md): $name"
    return 0
  fi

  if [[ $UNLINK -eq 1 ]]; then
    if [[ -L "$dest" ]] && [[ "$(readlink "$dest")" == "$src" ]]; then
      [[ $DRY_RUN -eq 1 ]] && echo "would unlink: $dest" || rm "$dest"
      echo "unlinked: $name"
    fi
    return 0
  fi

  if [[ -e "$dest" ]]; then
    if [[ -L "$dest" ]] && [[ "$(readlink "$dest")" == "$src" ]]; then
      echo "ok (already linked): $name"
      return 0
    fi
    echo "skip (exists, not our symlink): $dest" >&2
    return 1
  fi

  if [[ $DRY_RUN -eq 1 ]]; then
    echo "would link: $dest -> $src"
  else
    ln -s "$src" "$dest"
    echo "linked: $name"
  fi
}

fail=0
while IFS= read -r -d '' dir; do
  name="$(basename "$dir")"
  link_one "$name" || fail=1
done < <(find "$SKILLS_SRC" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

exit "$fail"
