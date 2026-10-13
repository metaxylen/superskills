---
name: git-workflow-and-versioning
description: >-
  Handles commits, branches, rebasing, pull request creation, merge, and
  releases after verification. Use when the user asks to commit, push, open a
  PR, merge, or cut a release. Do not use for review commentary or root-cause
  debugging; use code-review-and-quality or systematic-debugging. Turkish
  cues: commit, merge, branch, push, PR aç, bitir, sürüm, tag.
---

# Git workflow and versioning

## Done

- History is atomic, descriptive, and reversible.
- Integration choice (merge local, PR, keep branch) is explicit user consent.
- Full test suite passed on the integration target before merge or PR claim.
- Worktree cleanup only after successful merge when applicable.

## Principles

- **Trunk-based default** — short-lived branches; `main` stays deployable.
- **When commits are requested** — one logical change per commit; split by purpose, not line count.
- **Separate concerns** — feat vs refactor vs chore in separate commits when practical.
- **Messages** — `type: summary` + why in body when helpful (`feat`, `fix`, `refactor`, `test`, `docs`, `chore`).

Commands come from project `AGENTS.md`, not hardcoded package managers.

## During implementation

Pattern: slice → test → verify (`incremental-implementation`); commit only when the user requested commits.

Do not mix drive-by format refactors with behavior in one commit without user OK.

## Finishing a branch

**1. Verify** — Run full suite; if red, stop and use `systematic-debugging`.

**2. Confirm base** — Branch forked from which base? Ask once if unknown.

**3. Use the user's integration choice** if already explicit. Otherwise present options:

```
1. Merge into <base> locally
2. Push and open a pull request
3. Keep branch as-is (I will handle later)
```

Detached HEAD: options 2–3 only (no local merge). Discard work only if user explicitly asks.

**4. Execute** — Checkout base, merge or push, re-run tests on result, then cleanup worktree if used (`using-git-worktrees`).

**5. Hand off** — `code-review-and-quality` before merge when not already done; `verification-before-completion` before claiming integrated.

## PR hygiene

- PR describes intent and test evidence; link issue/spec when present.
- Do not force-push shared branches without user request.

## Versioning (when releasing)

- Semantic versioning when the project tags releases; changelog entry for user-visible changes.
- Tag only after green verification on the release commit.

## Boundaries

- **Always:** verify before merge/PR; atomic commits; confirm base branch.
- **Ask first:** force push; rewriting published history; merging to `main` without review policy met.
- **Never:** commit secrets; `--no-verify` unless user requests.

## Output

```
Branch: <name>
Base: <branch>
Verification: <command> — <summary>
Choice: merge | pr | hold
Result: <sha / PR url / pending>
```
