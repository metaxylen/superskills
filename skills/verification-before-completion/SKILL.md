---
name: verification-before-completion
description: >-
  Checks fresh evidence before claiming work is ready, tests pass, or a bug is
  fixed; use at completion or before commit, push, or PR. Do not use for
  initial routing or review commentary; use dev-router or
  code-review-and-quality. Turkish cues: bitti mi, doğrula, kanıt göster, test
  geçti mi, hazır mı.
---

# Verification before completion

## Done

- Every completion claim in the message is backed by **fresh** command output from this session.
- Exit codes and failure counts were read, not assumed.
- If verification failed, the message states actual status — no false "done".

## Iron law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

## Gate (run before "done", "fixed", "passes", "ready")

1. **Identify** — What command proves the claim?
2. **Run** — Required project gates from `AGENTS.md` (or manifest fallback), plus the check that proves the specific claim.
3. **Read** — Exit code, failure count, first error if any.
4. **Match** — Does output support the exact claim?
5. **Claim** — State result **with** evidence snippet or say what failed.

Skip a step → the claim is invalid.

## Claim map

| Claim | Requires |
|-------|----------|
| Tests pass | Full test command, 0 failures |
| Build OK | Build command exit 0 |
| Lint clean | Linter command, 0 errors (if project uses lint) |
| Bug fixed | Reproduction or regression test green **and** suite per `AGENTS.md` |
| Task complete | User-visible checklist or acceptance criteria met **and** verification above |

A targeted run supports only its stated scope. Output from before the last relevant change, or "should pass", cannot prove the current result. Reuse a completed check when its inputs have not changed; follow stricter project requirements.

## Red flags — stop

- "Should", "probably", "seems fine"
- Celebrating before running commands
- Commit/PR without verification
- Trusting another agent's success without inspecting its evidence against the current tree
- Using lint output as evidence that a build succeeds

## Boundaries

- **Always:** run commands in the project root; paste summary or key failure lines.
- **Ask first:** skipping verification for "trivial" changes; destructive git operations.
- **Never:** imply green from code inspection alone when a command exists.

## Output

When closing work:

```
Verification:
- <command>: exit <code>, <summary>
- <command>: exit <code>, <summary>

Status: <ready | not ready — what failed>
```
