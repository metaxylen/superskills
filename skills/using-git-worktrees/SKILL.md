---
name: using-git-worktrees
description: >-
  Creates or reuses an isolated git worktree before feature work or plan
  execution. Use when implementation should not touch the current checkout,
  when executing-plans or subagent-driven-development needs isolation, or the
  user asks for a worktree or separate branch workspace. Do not use when already
  in an isolated worktree, for read-only review, or when the user declined
  isolation—work in place or use git-workflow-and-versioning only. Turkish cues:
  worktree, izole çalışma, ayrı klasör, ana branch temiz kalsın.
---

# Using git worktrees

## Done

- Work happens on a named feature branch, not unapproved `main` edits.
- Worktree path is ignored by git (`.worktrees/` or project convention).
- Baseline tests run once after setup (command from `AGENTS.md`).
- Path and branch reported to the user.

## Step 0 — Detect existing isolation

```bash
git rev-parse --git-dir
git rev-parse --git-common-dir
git branch --show-current
```

If linked worktree (dirs differ, not a submodule): **do not** nest another worktree; continue in place.

If normal checkout: ask once unless user already prefers worktrees:

> Set up an isolated worktree so your current branch stays clean?

Honor decline — skip creation, still use a feature branch if possible.

## Step 1 — Create workspace

1. Prefer the editor's native worktree command if available.
2. Else git fallback:
   - Directory: `.worktrees/` (default) — must be `git check-ignore` clean; add to `.gitignore` and commit if needed.
   - `git worktree add .worktrees/<branch> -b <branch>`
   - `cd` into the worktree.

Branch name: short, kebab-case, tied to task (`feat/short-name`).

## Step 2 — Setup

Install deps per project (`package.json`, `pyproject.toml`, etc.). Run a quick smoke test or full suite per plan risk.

## Finish

Hand off to `git-workflow-and-versioning` for merge/PR/cleanup. Remove worktree only after successful integration.

## Boundaries

- **Always:** verify ignore before `.worktrees/`; never commit worktree contents into main tree accidentally.
- **Ask first:** worktree on external drive; deleting user's existing worktrees.
- **Never:** force operations on `main`; create worktree without consent when user declined.

## Output

```
Worktree: <path>
Branch: <name>
Baseline: <command> — <summary>
```
