# Manual routing check (Cursor)

Run after install (`link-cursor-skills.sh` or `install-cursor-plugin.sh`) and **Reload Window**. New agent chat. Send one message per row; expect the agent to follow the skill (or name it).

## Turkish

| Message | Expected skill |
|---------|----------------|
| şuna bir bak projede | `dev-router` → specialist |
| plan yaz bu feature için | `writing-plans` |
| planı uygula | `executing-plans` |
| TDD ile yap | `test-driven-development` |
| kök neden ne | `systematic-debugging` |
| bitti mi testler | `verification-before-completion` |
| PR incele | `code-review-and-quality` |
| worktree aç | `using-git-worktrees` |
| hangi skill kullanmalıyım | `using-agent-skills` |
| oturum kötü gitti | `diagnosing-workflow` |

## English

| Message | Expected skill |
|---------|----------------|
| fix this (paste logs) | `dev-router` |
| write a plan for auth | `writing-plans` |
| execute the plan inline | `executing-plans` |
| review my PR | `code-review-and-quality` |
| merge when tests pass | `git-workflow-and-versioning` |

## Optional (after `link-optional-skills.sh`)

| Message | Expected skill |
|---------|----------------|
| kota ne kadar kaldı | `limit` |
| codex exec ile şunu yap | `codex-fleet` |
| grill the plan | `grilling` |

Automated: `./tests/routing_scenarios.py` (synthetic paths). Full suite: `./tests/run-all.sh`.

## Focused triggers and near misses (2026-10-12)

Run each prompt in a fresh chat with the updated skills available. These cases are a manual evaluation set; the automated substring checks do not run a model or establish routing accuracy. Record the selected skill and whether the expected action happened. For a performance comparison, repeat with the previous skill revision under the same model and settings.

| Message | Expected action | Should not activate |
|---------|-----------------|---------------------|
| Write a PRD with acceptance criteria for a new billing subsystem | `spec-driven-development` writes the spec | `executing-plans` |
| This approved spec needs an implementation plan | `writing-plans` writes tasks from the spec | `spec-driven-development` |
| Execute the approved plan inline | `executing-plans` continues the tasks | `brainstorming`, `subagent-driven-development` |
| Rename this documented CLI flag; validate the docs | Make the bounded edit and run relevant checks | `spec-driven-development`, `test-driven-development` |
| How skills work and which skill should I choose? | `using-agent-skills` explains selection | `writing-skills` |
| Simplify this SKILL.md description and fix skill triggers | `writing-skills` edits and validates it | `using-agent-skills` |
| Checkout crashes with this stack trace; find root cause | `systematic-debugging` investigates the failure | `dev-router` when the debugging task is already clear |
| Review this pull request; do not apply fixes | `code-review-and-quality` reports findings | Implementation skills |
| Implement this approved plan here, without delegation | `executing-plans` works inline | `subagent-driven-development` |
| Run Codex CLI to review this file read-only | `codex-fleet` runs the CLI task, loading runtime and task references | Image references |
| Explain what codex exec does; do not run it | Explain the CLI | `codex-fleet` execution |
| Generate a raster illustration using the native image tool | Use the host's native image workflow when available | `codex-fleet` without a CLI request |
| Complete this local change; leave it uncommitted | Implement and verify; leave the working changes for review | Automatic commits or an integration-options pause |

If routing is wrong, edit **description** only (keep body English), add a row to `routing-triggers.tsv`, `routing-triggers-en.tsv`, or `optional-routing-triggers.tsv`, then run `./tests/run-all.sh`.

## Bounded execution behavior (2026-10-12)

These define the behavior screen. The opt-in CLI runner selects the skill explicitly; it does not prove automatic routing. See [the evaluation report](../docs/superskills/research/2026-10-12-loop-engineering-evaluation.md) for actual trials, protocol corrections and limits. Use an approved fixture plan in a disposable workspace; record tool actions, ledger entries, and the final status.

| Case | Expected behavior |
|------|-------------------|
| Execute one ordinary approved documentation task inline | Use normal `executing-plans`; no separate loop contract or scheduler. |
| Repeat an approved task until its acceptance check passes, at most four iterations; it passes on the second | Load loop control; record two attempts and acceptance evidence; complete after required final gates. |
| A check fails every time; the supplied two-iteration budget is used | Preserve partial work and the counter; report `budget-exhausted`; do not start a third attempt. |
| Resume with one of four iterations remaining and one verified task | Reconcile the current tree and ledger; continue the unfinished task with one iteration; do not reset the budget or reimplement the unchanged completed task. |
| Retry produces the identical failure on unchanged inputs and there is no informative experiment | Report `blocked` with evidence and the missing prerequisite; do not repeat the same edit/check indefinitely. |
| The targeted test passes but a required acceptance behavior is unverified | Keep the task unverified; do not mark it complete or weaken the criteria. |
| The ledger says complete, but the implementation changed afterward | Reconcile the current tree, reopen affected work and verify it; preserve unaffected completed tasks. |

Additional scenarios remain **unexecuted**: interrupted in-flight side effects,
unavailable model graders, recurring trigger deduplication, and a rubric judged
by a separate model. The source-backed instructions cover their contract;
the seven-case CLI screen does not establish runtime support for them.

## Delegation decisions (2026-10-12)

These are unexecuted behavior scenarios, not substring-test or cost results.
The delegation report records the single actual native reviewer invocation.

| Case | Expected decision |
|------|-------------------|
| Rename one documented label under a project policy allowing autonomous delegation | Inline; permission to delegate does not make the task worthwhile. |
| Analyze a bounded noisy log while the parent implements an independent reproduced fix | One read-only child if gates pass; parent does different useful work; verify returned evidence. |
| Make dependent edits in the same file | Inline; do not create competing write lanes. |
| Approved plan, user says choose delegation if worthwhile | Use the existing plan executor's benefit gate, not an automatic child per task. |
| Start plan task 3 after two child runs across implementation and review | Same allocation is used; finish inline, no task-level counter reset. |
| Resume after compaction with one child run reserved/consumed | Reconcile the note; at most one further child work run under the default allocation. |
| Usage telemetry unavailable but a bounded read-only investigation has clear value | At most a conservative first run under the recorded allowance; report usage unknown, stop dispatch on limit errors. |
| User explicitly says no delegation | Zero children, even under project autonomous-delegation policy. |
