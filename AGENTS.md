# superskills — agent commands

This file applies to **this repository** (the skill library). Application projects should have their own `AGENTS.md` with stack-specific commands.

## Install skills in Cursor

```bash
./scripts/link-cursor-skills.sh
./scripts/link-cursor-skills.sh --dry-run   # print actions only
./scripts/link-cursor-skills.sh --unlink    # remove symlinks created by this script
```

Target: `~/.cursor/skills/<skill-name>` → `<repo-root>/skills/<skill-name>`.

## Git

Commit and push after skill or doc changes when the user expects it. Use repo-local author via environment if global git identity is unset:

```bash
export GIT_AUTHOR_NAME='your-name'
export GIT_AUTHOR_EMAIL='you@users.noreply.github.com'
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"
export GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
```

Do not run `git config --global` on the user's machine.

## Worktrees

Isolated feature work: `.worktrees/<branch>` (git-ignored). See skill `using-git-worktrees`.

## Plans and specs

| Artifact | Path |
|----------|------|
| Implementation plan | `docs/superskills/plans/YYYY-MM-DD-<feature>.md` |
| Feature spec | `docs/superskills/specs/<feature>.md` |
| Plan ledger (runtime) | `<plan-stem>-ledger.md` next to the plan file |

## Validation (manual until automated)

- Every skill folder: `name` in frontmatter matches directory name.
- `description` includes use-when and do-not-use-when; no overlap with other v1 skills (`skills/CONSOLIDATION.md`).
- Body language: English.

Future: `tests/skill-frontmatter` (not required for v1).

## Boundaries

- Do not symlink or copy entire third-party skill trees into `~/.cursor/skills`.
- `documentations/` is archive only — do not route agents through it for workflow.
