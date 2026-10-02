# superskills — agent commands

This file applies to **this repository** (the skill library). Application projects should have their own `AGENTS.md` with stack-specific commands.

## Upstream sources (required before edits)

Do **not** change skills, plugin JSON, or consolidation docs until you have checked counterparts in all five repos listed in [docs/SOURCES.md](docs/SOURCES.md). Record merge/skip decisions in the commit message.

```bash
./scripts/check-upstream.sh        # versions on GitHub main
./scripts/check-upstream.sh --clone  # optional local mirrors in .upstream/
```

Full checklist: [docs/UPSTREAM-WORKFLOW.md](docs/UPSTREAM-WORKFLOW.md).

## Install in Cursor

**Plugin copy** (see [docs/plugins.md](docs/plugins.md)):

```bash
./scripts/install-cursor-plugin.sh
./scripts/install-cursor-plugin.sh --dry-run
./scripts/install-cursor-plugin.sh --remove
```

**Symlink** (dev on this repo; do not combine with plugin install for same skill names):

```bash
./scripts/link-cursor-skills.sh
./scripts/link-cursor-skills.sh --dry-run
./scripts/link-cursor-skills.sh --unlink
```

Validate manifest: `.cursor-plugin/plugin.json`. Skills directory: `skills/`.

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

## Validation

```bash
./tests/skill-frontmatter.sh
```

Checks: 16 folders, `name` matches directory, `description` ≤1024 chars, includes `Do not use` and `Turkish cues:`, non-empty body; `tests/routing-triggers.tsv` keywords appear in the matching skill description.

Manual: overlap review against `skills/CONSOLIDATION.md`. Body language: English.

## Boundaries

- Do not symlink or copy entire third-party skill trees into `~/.cursor/skills`.
- `documentations/` is archive only — do not route agents through it for workflow.
