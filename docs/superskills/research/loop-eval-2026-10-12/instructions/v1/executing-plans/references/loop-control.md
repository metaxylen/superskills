# Loop control for plan execution

Use for an approved plan with requested repeated execution or work spanning sessions. These instructions guide an agent; a runner must enforce hard time, token, and iteration limits. A skill alone does not create a scheduler or guarantee unattended operation.

## Establish the contract

Reuse the plan and its ledger; do not create a second task list. Record only missing fields:

- **Goal:** current plan task and its acceptance criteria.
- **Check:** command or observable check, expected result, and evidence location. A passing command must cover the requested behavior; required project gates still apply at completion.
- **Budget:** user or runner limits and consumed/remaining allowance. For requested unattended retries without a supplied limit, choose and state a finite iteration cap appropriate to the task before starting. Do not invent token usage when the host does not expose it.
- **Next:** next action or hypothesis within the approved scope.

Existing user authorization and host permissions apply. Repeated execution does not authorize additional scope, new scheduled jobs, delegation, paid model changes, or publishing.

## Each iteration

1. Read the current task and latest ledger checkpoint.
2. Check the remaining budget, then take one scoped action or diagnostic experiment.
3. Run the affected acceptance check; read its actual result.
4. Record the attempt count, changed files, check result/evidence, and next decision in the ledger. Count unsuccessful and verification-only attempts too. Link logs rather than copying full outputs.
5. If the task's acceptance criteria hold, mark it complete and move to the next planned task within the remaining budget. Otherwise, use the failure evidence to choose the next experiment.

Do not weaken acceptance criteria or tests to make the loop finish. Unavailable checks mean unverified work, not success.

## Continue or stop

| Observation | Decision |
|---|---|
| All planned outcomes and required final gates are verified | Stop: `complete`; cite the evidence. |
| A check fails and there is a specific new hypothesis or informative experiment | Continue within scope and budget; use `systematic-debugging` for the failure. |
| The same action/check produces the same failure on unchanged inputs | Do not repeat blindly; diagnose using new evidence. If no informative next step is available, stop: `blocked`; record attempts and the missing input or access. |
| A user or runner limit is reached | Save a checkpoint and stop: `budget-exhausted`; report unfinished work. Do not silently raise the limit. |
| The next action crosses an existing authorization boundary | Save a checkpoint and follow the executor's stop-and-ask rules; reuse authorization already given. |

Repeated samples in a defined flakiness experiment can provide new evidence; keep the sample count bounded and recorded.

## Resume from evidence

Before a planned session handoff, save the current task, completed outcomes, failed hypotheses, evidence paths, remaining budget, and next action. Update after each iteration so an interruption loses as little state as possible.

On resume:

1. Read the plan and latest ledger entry; inspect the current diff and relevant environment changes.
2. Reconcile recorded progress with the current tree. Rerun affected checks when their inputs changed or evidence is missing; keep unaffected verified tasks complete.
3. Continue the next unfinished task with the recorded remaining budget. A new session is not a budget reset; only an explicit user or runner renewal changes the allowance.

Leave partial changes visible and describe their state. Do not reset user work or commit merely to create a checkpoint.
