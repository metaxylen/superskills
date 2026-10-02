---
name: git-workflow-and-versioning
description: >-
  Guides commits, branches, merge, and finishing work with verification first.
  Use when committing, splitting messy changes into atomic commits, opening or
  updating a pull request, merging or rebasing, choosing version tags, or when
  implementation is done and integration is next. Use after plans or features
  complete. Do not use for code review commentary only or root-cause debugging—use
  code-review-and-quality or systematic-debugging instead.
---

# Git workflow and versioning

## Done

- History is atomic, descriptive, and reversible.
- Integration choice (merge local, PR, keep branch) is explicit user consent.
- Full test suite passed on the integration target before merge or PR claim.
- Worktree cleanup only after successful merge when applicable.

## Principles

- **Trunk-based default** — short-lived branches; `main` stays deployable.
- **Commit early** — one logical change per commit; ~100 lines target, split if larger.
- **Separate concerns** — feat vs refactor vs chore in separate commits when practical.
- **Messages** — `type: summary` + why in body when helpful (`feat`, `fix`, `refactor`, `test`, `docs`, `chore`).

Commands come from project `AGENTS.md`, not hardcoded package managers.

## During implementation

Pattern: slice → test → verify → commit (`incremental-implementation`).

Do not mix drive-by format refactors with behavior in one commit without user OK.

## Finishing a branch

**1. Verify** — Run full suite; if red, stop and use `systematic-debugging`.

**2. Confirm base** — Branch forked from which base? Ask once if unknown.

**3. Present options** (user chooses):

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
