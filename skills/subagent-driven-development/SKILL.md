---
name: subagent-driven-development
description: >-
  Executes an approved plan with subagents and per-task review. Use when the
  user requests delegation or project instructions authorize agent-chosen
  delegation; decide whether the work warrants it. Do not use without a
  plan, for a tiny change, inline execution, or without a subagent tool; use
  executing-plans or incremental-implementation. Turkish cues: alt ajan,
  subagent, paralel görev, her task review.
---

# Subagent-driven development

## Done

- Each plan task: choose inline or delegated work → implement → task review → ledger entry.
- Implementers receive a **brief** (task text, files, spec excerpt); use fresh context unless essential shared context justifies a history fork under the policy.
- Final `code-review-and-quality` on the branch diff.
- `verification-before-completion` before claiming all tasks done.

## vs `executing-plans`

| | SDD | Inline executing-plans |
|--|-----|-------------------------|
| Context | Fresh per task | One session |
| Review | After every task | End (plus optional final) |
| Cost | Higher token use | Lower |

Use this workflow when delegation is requested or applicable project instructions authorize the agent to choose it. Before spawning, read [the delegation policy](references/delegation-policy.md); inline execution remains valid when delegation does not justify its cost. Do not use this plan executor for standalone research or review.

## Setup

1. `using-git-worktrees` if isolation needed.
2. Read plan + spec; ledger at `<plan-stem>-ledger.md` (first line = plan path). Record the delegation allocation and reserve each child work run before dispatch.
3. Resume: skip tasks marked complete in ledger.

## Per task

1. **Brief** — goal, files, acceptance, test command, constraints from spec.
2. **Implement** — delegate only if the policy gates pass; otherwise execute inline. Use `test-driven-development` for behavior changes and appropriate checks for documentation/configuration.
3. **Task review** — the primary agent checks spec match, relevant diff and actual evidence. An additional reviewer subagent needs its own benefit decision and reserved run.
4. **Fix loop** — bounded by the same allocation, including follow-ups and retries; ledger `Ruling:` on plan/spec conflicts. Finish inline when the delegation allocation is used.
5. Mark task complete in plan checkboxes and ledger.

Do not pause for "continue?" between tasks unless a stop condition fires.

## Parallel lanes

When several tasks are **independent** and the host can run background jobs:

- One **worktree per write lane** (`using-git-worktrees`); never two writers on the same checkout.
- Run only the useful independent lanes within the recorded allocation; concurrency alone does not establish net value.
- Each lane gets a **complete brief** (spec slice, files, acceptance, test command). Instruction-following runners do not improvise missing scope.
- Check exposed subscription headroom before dispatch; optional `limit` skill if installed. Do not invent headroom or auto-launch a large fleet.

External Codex CLI delegation: optional `codex-fleet` skill if installed — action skill, not commentary.

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
