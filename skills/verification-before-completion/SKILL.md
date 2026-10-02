---
name: verification-before-completion
description: >-
  Requires fresh command evidence before claiming tests pass, build succeeds, a
  bug is fixed, or work is done. Use when finishing a task, before commit or
  push, before opening a PR, or when the user asks if something is ready. Use
  when an agent or prior message asserted success without pasted output. Do not
  use as the first step on a new vague task, for routing, or for writing a
  review of someone else's diff—use dev-router or code-review-and-quality
  instead. Turkish cues: bitti mi, doğrula, kanıt göster, test geçti mi, hazır mı.
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
2. **Run** — Full command from project `AGENTS.md` (or manifest fallback).
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

Partial runs, earlier runs, or "should pass" are not evidence.

## Red flags — stop

- "Should", "probably", "seems fine"
- Celebrating before running commands
- Commit/PR without verification
- Trusting another agent's success without re-run
- Linter green but build not run (when build exists)

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
