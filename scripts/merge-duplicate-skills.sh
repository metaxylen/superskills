#!/usr/bin/env bash
# One-off consolidation: merge overlapping skill folders into canonical paths.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)/skills"

merge_into() {
  local dest="$1" src="$2" tag="$3"
  [[ -d "$ROOT/$src" ]] || return 0
  local out="$ROOT/$dest/references/merged-$tag"
  mkdir -p "$out"
  rsync -a "$ROOT/$src/" "$out/"
  if [[ -f "$out/SKILL.md" ]]; then
    mv "$out/SKILL.md" "$out/SKILL.md.from-$tag"
  fi
  rm -rf "$ROOT/$src"
}

merge_tree_into() {
  local dest="$1" src="$2"
  [[ -d "$ROOT/$src" ]] || return 0
  local tag
  tag=$(basename "$src")
  for sub in prompts references templates agents scripts; do
    [[ -d "$ROOT/$src/$sub" ]] || continue
    mkdir -p "$ROOT/$dest/$sub"
    rsync -a "$ROOT/$src/$sub/" "$ROOT/$dest/$sub/"
  done
  mkdir -p "$ROOT/$dest/references/merged-$tag"
  [[ -f "$ROOT/$src/SKILL.md" ]] && cp "$ROOT/$src/SKILL.md" "$ROOT/$dest/references/merged-$tag/SKILL.md.from-$tag"
  rm -rf "$ROOT/$src"
}

merge_into dev-router engineering/ask-matt ask-matt
merge_into dev-router engineering/wayfinder wayfinder
merge_into dev-router engineering/triage triage

merge_into test-driven-development engineering/tdd tdd

merge_into systematic-debugging debugging-and-error-recovery osmani-debugging
merge_into systematic-debugging engineering/diagnosing-bugs pocock-diagnosing-bugs

merge_into code-review-and-quality requesting-code-review requesting
merge_into code-review-and-quality receiving-code-review receiving
merge_into code-review-and-quality engineering/code-review pocock-code-review
merge_into code-review-and-quality engineering/pr pr

merge_into writing-plans planning-and-task-breakdown osmani-planning
merge_into writing-plans engineering/to-tickets to-tickets

merge_into spec-driven-development engineering/implement-spec implement-spec
merge_into spec-driven-development engineering/to-spec to-spec
merge_into incremental-implementation engineering/implement implement

merge_into using-agent-skills using-superpowers using-superpowers
merge_tree_into diagnosing-workflow diagnosing-superpowers

merge_into subagent-driven-development dispatching-parallel-agents dispatching-parallel
merge_into git-workflow-and-versioning finishing-a-development-branch finishing-branch

merge_into engineering/grill-with-docs productivity/grill-me grill-me
merge_into engineering/grill-with-docs productivity/grilling grilling
merge_into productivity/handoff in-progress/claude-handoff claude-handoff

echo "SKILL.md count: $(find "$ROOT" -name SKILL.md | wc -l | tr -d ' ')"
