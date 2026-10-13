# Loop control for plan execution

Use for an approved plan with requested repeated execution or work spanning sessions. These instructions guide an agent; a runner must enforce hard time, token, and iteration limits. A skill alone does not create a scheduler or guarantee unattended operation.

## Establish the contract

Reuse the plan and its ledger; do not create a second task list. Record only missing fields:

- **Goal:** current plan task and its acceptance criteria. Keep the criteria fixed during execution; record newly discovered requirements separately rather than quietly dropping or replacing a criterion.
- **Check:** command or observable check, expected result, and evidence location for each criterion. Prefer deterministic checks where available. For judgment-based work, use a stated rubric and record uncertainty. A partial or incomplete grade cannot prove the whole task; required project gates still apply at completion.
- **Budget:** user or runner limits, their counting unit, and consumed/remaining allowance. Preserve supplied units. Otherwise, define an iteration as one scoped action or diagnostic experiment plus its check, including a verification-only experiment. Count started failed attempts; a rejected command that never ran does not consume an action iteration, but elapsed time and any reported resource use still count. For requested unattended retries without a supplied limit, choose and state a finite cap appropriate to the task before starting. Do not invent token usage when the host does not expose it.
- **Next:** next action or hypothesis within the approved scope.

Existing user authorization and host permissions apply. Repeated execution does not authorize additional scope, new scheduled jobs, delegation, paid model changes, or publishing.

## Each iteration

1. Read the current task and latest ledger checkpoint.
2. Check the remaining budget and record the pending action before starting it; then take one scoped action or diagnostic experiment.
3. Run the affected acceptance check; read its actual result.
4. Resolve the pending entry with the attempt count, changed files, criterion results/evidence, and next decision. Link logs rather than copying full outputs.
5. If the task's acceptance criteria hold, mark it complete and move to the next planned task within the remaining budget. Otherwise, use the failure evidence to choose the next experiment.

Do not weaken acceptance criteria or tests to make the loop finish. Distinguish a demonstrated behavior failure from a check that could not run or a grader error. For the latter, preserve the work as unverified and diagnose the check infrastructure before changing the implementation. Any retries still use the existing budget.

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
2. Reconcile recorded progress and any pending action with the current tree and observable side effects. Do not blindly replay an action whose completion is unknown; verify its outcome or use an idempotent recovery. Rerun affected checks when their inputs changed or evidence is missing; keep unaffected verified tasks complete.
3. Continue the next unfinished task with the recorded remaining budget. A new session is not a budget reset; only an explicit user or runner renewal changes the allowance.

Leave partial changes visible and describe their state. Do not reset user work or commit merely to create a checkpoint.

## Recurring runs

Use this section only when a recurring or event-triggered workflow was requested. The host owns the trigger, durable run identifier, hard limits, and overlap/deduplication policy. Record that contract in the ledger before enabling the workflow. Each invocation reconciles previous work and uses the configured per-run and overall allowances; a trigger is not permission to replay side effects or renew a shared budget. If the host lacks these controls, report the missing runtime support rather than claiming a Markdown skill provides it.

## Improve the workflow from traces

When workflow improvement is requested, close execution before changing its instructions:

1. Capture the input, expected outcome, observed outcome, trace, and relevant skill/model settings. Use `diagnosing-workflow` to identify a process failure from evidence.
2. Turn the failure into a reproducible evaluation case with an outside acceptance check. Validate the grader on a known good and a known bad outcome; do not let the evaluated agent rewrite it.
3. Use `writing-skills` for a scoped candidate. Compare the previous and candidate instructions in fresh workspaces with the same inputs, model/settings, and budgets; include ordinary tasks and regression cases. Inspect traces, not just final scores.
4. Keep a change only with a stated reason and its observed trade-offs. Report repeats, outcomes, time and exposed usage separately by environment. If results tie, say so; a small synthetic screen does not establish a percentage productivity gain. Apply existing user review and commit rules.

These are separate workflow steps, not instructions for a running agent to rewrite its own success criteria or launch new evaluation jobs without the requested scope.
