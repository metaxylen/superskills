#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OPTIONAL_SRC="$REPO_ROOT/optional"
DRY_RUN=0
UNLINK=0

DESTS=(
  "${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills}"
  "${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
  "${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
)

usage() {
  cat <<EOF
Usage: $(basename "$0") [--dry-run] [--unlink]

Symlink optional/* skills (codex-fleet, limit) into Cursor, Claude, and Codex
skill directories. Skips destinations that are not creatable.

See optional/README.md.
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

link_one() {
  local name="$1"
  local src="$OPTIONAL_SRC/$name"
  local dest_root="$2"
  local dest="$dest_root/$name"

  [[ -d "$src" && -f "$src/SKILL.md" ]] || return 0

  mkdir -p "$dest_root"

  if [[ $UNLINK -eq 1 ]]; then
    if [[ -L "$dest" ]] && [[ "$(readlink "$dest")" == "$src" ]]; then
      [[ $DRY_RUN -eq 1 ]] && echo "would unlink: $dest" || rm "$dest"
      echo "unlinked: $name from $dest_root"
    fi
    return 0
  fi

  if [[ -e "$dest" ]]; then
    if [[ -L "$dest" ]] && [[ "$(readlink "$dest")" == "$src" ]]; then
      echo "ok: $name -> $dest_root"
      return 0
    fi
    echo "skip (exists): $dest" >&2
    return 1
  fi

  if [[ $DRY_RUN -eq 1 ]]; then
    echo "would link: $dest -> $src"
  else
    ln -s "$src" "$dest"
    echo "linked: $name -> $dest_root"
  fi
}

fail=0
for skill_dir in "$OPTIONAL_SRC"/*/; do
  [[ -d "$skill_dir" ]] || continue
  name="$(basename "$skill_dir")"
  [[ "$name" == "README.md" ]] && continue
  [[ -f "$skill_dir/SKILL.md" ]] || continue
  for dest_root in "${DESTS[@]}"; do
    link_one "$name" "$dest_root" || fail=1
  done
done

exit "$fail"
