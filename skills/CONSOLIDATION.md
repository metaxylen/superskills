# Skill consolidation (canonical folders)

Overlapping skills were merged into one folder each. Removed paths are preserved under `references/merged-*` (and subfolders for `diagnosing-workflow`) until content is rewritten into the canonical `SKILL.md`.

| Canonical skill | Merged into it (no longer separate skills) |
|-----------------|---------------------------------------------|
| `dev-router` | `engineering/ask-matt`, `engineering/wayfinder`, `engineering/triage` |
| `test-driven-development` | `engineering/tdd` |
| `systematic-debugging` | `debugging-and-error-recovery`, `engineering/diagnosing-bugs` |
| `code-review-and-quality` | `requesting-code-review`, `receiving-code-review`, `engineering/code-review`, `engineering/pr` |
| `writing-plans` | `planning-and-task-breakdown`, `engineering/to-tickets` |
| `spec-driven-development` | `engineering/implement-spec`, `engineering/to-spec` |
| `incremental-implementation` | `engineering/implement` |
| `using-agent-skills` | `using-superpowers` |
| `diagnosing-workflow` | `diagnosing-superpowers` |
| `subagent-driven-development` | `dispatching-parallel-agents` |
| `git-workflow-and-versioning` | `finishing-a-development-branch` |
| `engineering/grill-with-docs` | `productivity/grill-me`, `productivity/grilling` |
| `productivity/handoff` | `in-progress/claude-handoff` |

Re-run consolidation: `bash scripts/merge-duplicate-skills.sh` (only after restoring `skills/` from git if needed).
