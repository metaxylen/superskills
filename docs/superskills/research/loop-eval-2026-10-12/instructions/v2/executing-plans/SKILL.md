---
name: executing-plans
description: >-
  Executes an approved plan task by task with inline execution. Use when the
  user says execute the plan or continue its checklist. Do not use without a
  plan, for planning only, or for subagent execution; use writing-plans or
  subagent-driven-development. Turkish cues: planı uygula, plandan devam,
  checklist, planı çalıştır.
---

# Executing plans

## Done

- Every plan task checkbox completed or explicitly ruled out in the ledger.
- Each behavior change used `test-driven-development` (red shown once).
- Affected checks run after each task; required `AGENTS.md` gates run at completion or at checkpoints the project requires (summary logged).
- Final pass uses `verification-before-completion` before claiming done.
- Optional: `code-review-and-quality` on the branch diff before merge handoff.

## Principles

- The plan already decided **what**; you execute and **prove** steps.
- Do not pause between tasks for "continue?" unless a stop condition below fires.
- Narrate briefly between tools; the plan checkboxes and commits are the record.

## Setup

1. Read the plan and linked spec.
2. Confirm worktree/branch policy (`using-git-worktrees` if isolation needed).
3. Open or create a **ledger** beside the plan: `<plan-stem>-ledger.md` — task status, rulings, test commands run.

## Per task

1. Read task files and steps.
2. Execute steps in order; use `test-driven-development` for behavior changes and relevant checks for documentation or configuration.
3. If reality disagrees with the plan: ledger `Ruling: <decision> — <why> — <risk>`, then continue or escalate.
4. If code is wrong: `systematic-debugging` (not random edits).
5. Mark task complete in the plan and ledger; commit only when the user requested commits.

## Bounded loops and resume

For a requested repeat-until-verified loop or execution spanning sessions, read [loop control](references/loop-control.md). Reuse the ledger for acceptance evidence, remaining budget, and the next action. Ordinary task execution uses the steps above; no separate loop setup is needed.

## Stop and ask (only these)

- Irreversible or destructive operation without user OK.
- Security-sensitive action (secrets, auth, production).
- Push/merge/publish to shared branches without user OK.
- Plan is broken every way forward is guesswork.

## End of plan

1. `verification-before-completion` on full suite/build.
2. `code-review-and-quality` if merging or user asked.
3. `git-workflow-and-versioning` for finish/merge if applicable.

## Boundaries

- **Always:** follow plan order unless ledgered ruling; fresh verification before "done".
- **Ask first:** scope creep beyond the plan; skipping tests "to save time".
- **Never:** re-plan the whole feature silently; delete failing tests to finish.

## Output

```
Plan: <path>
Tasks: <completed>/<total>
Ledger: <path>
Verification: <commands + summary>
Status: complete | blocked | budget-exhausted — <reason>
```
