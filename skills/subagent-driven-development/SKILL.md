---
name: subagent-driven-development
description: >-
  Executes an implementation plan by dispatching a fresh implementer context per
  task plus review after each task and a final branch review. Use when a plan
  has mostly independent tasks and the user wants per-task quality gates or
  subagents instead of inline executing-plans. Use when parallel lanes are
  needed for separate tasks. Do not use without a plan file, for a single tiny
  change, when the user chose inline execution, or when no subagent or Task tool
  exists—use executing-plans or incremental-implementation instead. Turkish cues:
  alt ajan, subagent, paralel görev, her task review.
---

# Subagent-driven development

## Done

- Each plan task: implement → task review → ledger entry → next task.
- Implementers receive a **brief** (task text, files, spec excerpt) — not full chat history.
- Final `code-review-and-quality` on the branch diff.
- `verification-before-completion` before claiming all tasks done.

## vs `executing-plans`

| | SDD | Inline executing-plans |
|--|-----|-------------------------|
| Context | Fresh per task | One session |
| Review | After every task | End (plus optional final) |
| Cost | Higher token use | Lower |

User chose SDD explicitly or tasks are independent and review gates matter.

## Setup

1. `using-git-worktrees` if isolation needed.
2. Read plan + spec; ledger at `<plan-stem>-ledger.md` (first line = plan path).
3. Resume: skip tasks marked complete in ledger.

## Per task

1. **Brief** — goal, files, acceptance, test command, constraints from spec.
2. **Implement** — subagent/Task with brief only; `test-driven-development` inside task.
3. **Task review** — spec match + quality; use `code-review-and-quality` scoped to task diff.
4. **Fix loop** — bounded rounds; ledger `Ruling:` on plan/spec conflicts.
5. Mark task complete in plan checkboxes and ledger.

Do not pause for "continue?" between tasks unless a stop condition fires.

## Stop and ask (only)

- Irreversible/destructive ops; security-sensitive; push/merge/publish; plan unsalvageable.

## End

1. Final branch review (`code-review-and-quality`).
2. `git-workflow-and-versioning` for integration.
3. `verification-before-completion`.

## Boundaries

- **Always:** ledger rulings; no re-dispatch of completed tasks; minimal briefs.
- **Ask first:** exceeding planned task scope; shared-branch push.
- **Never:** fabricate subagent results; skip review to save time.

## Output

```
Plan: <path>
Tasks: <completed>/<total>
Ledger: <path>
Final review: <verdict>
```
