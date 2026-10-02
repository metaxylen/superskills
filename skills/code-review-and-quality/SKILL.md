---
name: code-review-and-quality
description: >-
  Reviews a diff, branch, or pull request without rewriting code by default.
  Use when the user asks for a review, PR feedback, "look at my changes", or
  before merge. Use when evaluating code from another agent or model. Do not use
  when the user wants implementation, root-cause debugging of a failure, or
  only a test written—use incremental-implementation, systematic-debugging, or
  test-driven-development instead. Do not use when there is no diff or change
  set to review.
---

# Code review and quality

## Done

- Review scope is pinned (base ref, commit range, or pasted diff).
- Findings are tied to **file:line** (or hunk) with a short quote.
- Each finding has severity: **blocker**, **suggestion**, or **nit**.
- Tests and verification for the change were checked (commands from `AGENTS.md`).
- No unsolicited rewrite unless the user asked to apply fixes.

## Pin the change

1. Resolve the base: branch, SHA, tag, or `main` (ask once if missing).
2. Use `git diff <base>...HEAD` (three-dot) and `git log <base>..HEAD --oneline`.
3. Confirm non-empty diff and valid refs before deep review.

If only a paste is provided, review that paste; say what you cannot see (full repo context).

## Read order

1. **Intent** — issue, spec, commit messages, or user summary.
2. **Tests** — do new/changed tests match the claimed behavior? Would they fail if the bug returned?
3. **Implementation** — five axes below.
4. **Verification** — were project checks run? Request evidence if the author claims green.

Verify findings against the **current** tree when possible; do not trust a review artifact over live code.

## Five axes

| Axis | Question |
|------|----------|
| Correctness | Matches spec? Edge and error paths? Race or state bugs? |
| Readability | Names, flow, proportion; no gratuitous cleverness |
| Architecture | Fits existing patterns; boundaries; no feature logic in shared cores |
| Security | Input validation, secrets, authz, injection, untrusted external data |
| Performance | N+1, unbounded work, hot-path cost (flag only; deep tuning is out of scope) |

**Approval bar:** Approve when the change clearly improves code health and meets intent — not when it matches your personal style exactly.

## Findings format

```
[blocker] path:line — <claim>
  Evidence: <quote or test name>
  Fix: <one concrete direction>

[suggestion] ...

[nit] ...
```

Blockers: wrong behavior, missing tests for fixed bugs, security issues, broken verification.

## Process rules

- Do not drive-by refactor unrelated files in the same review pass.
- Prefer structural fixes by name (extract helper, explicit type boundary, move feature logic home).
- If standards docs exist (`CONTRIBUTING.md`, `AGENTS.md`, lint config), cite them; repo docs override generic smell lists.

## Boundaries

- **Always:** cite locations; separate blocker vs suggestion; check tests first.
- **Ask first:** applying fixes in the repo; scope beyond the given diff.
- **Never:** rubber-stamp without reading tests; approve with failing verification.

## Output

```
Scope: <base>...HEAD (<N> commits)
Intent: <one sentence>
Verification: <command outputs or "not provided">
Blockers: <count> — <list or none>
Suggestions: <count>
Nits: <count>
Verdict: approve | request changes
```
