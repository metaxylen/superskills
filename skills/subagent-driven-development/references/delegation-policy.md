# Decide whether to delegate

This policy guides a primary agent using native subagent tools. It is not a scheduler or a hard spending limiter. Use only within user authorization and host permissions; explicit inline-only instructions win. A task can stay inline even when delegation is allowed.

## Benefit gate

Delegate only when all hold:

1. **Useful separation:** the task is a substantial independent investigation, a noisy read-heavy job, an isolated implementation slice, or a consequential review that benefits from fresh judgment. File count alone is not a trigger.
2. **Bounded handoff:** the objective, input paths, permitted changes, output and acceptance check fit a concise brief. Do not dispatch vague exploration or a task requiring repeated parent-child coordination.
3. **Net benefit:** saved critical-path time, avoided context noise, or review value plausibly outweigh startup, repeated reads, reporting and integration. A fast search, deterministic script or inline edit is cheaper for routine work. Do not duplicate the delegated work while waiting.
4. **Safe ownership:** no shared-file writers; parallel implementation requires separate worktrees and an integration owner. Resolve shared contracts first. Read-only investigations may share a checkout.
5. **Available budget:** reserve allowance for the child, integration and required verification; follow tighter user/host limits and any exposed usage information. If benefit is unclear or an exposed limit is insufficient, work inline. Missing usage telemetry is not proof of capacity or a blanket ban: prefer one bounded read-only run within the recorded allocation, watch for limit errors, and report usage as unknown.

Examples: delegate a bounded log investigation while the parent fixes a separate reproduced issue; request a focused read-only review of a risky change. Keep a one-line edit, one documentation lookup, or dependent changes in the same file inline.

## Conservative defaults

Unless the user supplies a different allocation, allow **two child work runs shared across the entire user-requested objective**, including all plan tasks, research, reviews and resumed sessions, with at most **two children active**. A new plan task or specialist does not open a new allocation. Start with one; add another only for a distinct useful task. A spawn, substantive follow-up or retry consumes a run. Coordination/status messages do not renew work. These numbers are a local cost preference, not a provider recommendation or measured optimum.

Before dispatch, record the decision, assigned task, consumed/reserved runs, remaining allowance and acceptance check in the existing ledger, or a short task note if none exists. Reserve the run before calling. Do not reset the counter after compaction or disguise new work as a status message. At the cap, finish remaining work inline or report what cannot be completed within a supplied hard limit; do not silently expand the allocation.

No nested delegation, speculative fleets, automatic reviewer agents for every task, or paid API fallback. Respect model preferences; use an available lighter model only when already permitted and adequate for the work. Do not raise reasoning effort or change account/model pools merely to obtain more capacity.

Set a finite child runtime/turn allowance where the host supports it; otherwise give a bounded input scope and stop condition and state that the limit is instructional. The host must enforce hard limits where supported. A concurrency limit does not cap total session spend. If usage is not exposed, report it as unknown; do not claim token or money savings from agent count alone.

## Dispatch and collect

Give the child only what it needs:

```text
Objective and scope:
Inputs / current revision:
Allowed files and tools (read-only unless implementation requires writes):
Constraints, including no further delegation:
Stop condition / supplied runtime budget:
Return: concise findings or artifact paths, evidence, checks and uncertainties.
```

For independent work or fresh review, prefer a fresh child with this brief. In Codex tools supporting `fork_turns`, use `none` for that purpose. A full-history fork can be reasonable when essential shared context and cache reuse outweigh rebuilding context; do not claim fresh independent judgment from it. Follow the installed host's API rather than copying flags across products.

The parent continues a different useful task, or waits when a consequential review is the remaining gate. Reuse a suitable child for clarification instead of starting another context, but count new work against the same allowance. Cancel unnecessary work and stop new dispatches on quota/tool failures; do not retry blindly.

Read the returned evidence and relevant changed code. Integrate once, verify the actual result, and retain required project gates. Do not reread whole investigations by default, but inspect consequential claims or stale evidence before trusting them. Report the delegation reason, runs used, useful outputs and actual limits; a child's success message is not proof.
