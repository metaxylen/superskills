---
name: executing-plans
description: >-
  Implements an approved plan task-by-task in the current session using
  TDD and verification. Use when a plan file exists and the user chose
  inline execution here rather than subagents per task. Use after
  writing-plans or when the user says execute the plan, follow the
  checklist, or implement from docs/superskills/plans. Do not use when
  there is no plan, when only brainstorming or planning is requested, or
  when the user asked for subagent-per-task execution—use writing-plans,
  brainstorming, or subagent-driven-development instead.
---

# Executing plans

## Done

- Every plan task checkbox completed or explicitly ruled out in the ledger.
- Each behavior change used `test-driven-development` (red shown once).
- Suite command from `AGENTS.md` run after each task (summary logged).
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
2. Execute steps in order; use `test-driven-development` for code changes.
3. If reality disagrees with the plan: ledger `Ruling: <decision> — <why> — <risk>`, then continue or escalate.
4. If code is wrong: `systematic-debugging` (not random edits).
5. Mark task complete in the plan and ledger; commit when the plan says so.

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
Status: complete | blocked — <reason>
```
