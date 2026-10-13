---
name: dev-router
description: >-
  Routes an unclear coding request to one specialist. Use for take a look, fix
  this, or logs without a clear ask. Do not use when the job is identifiable,
  including something broke with a failure to investigate; invoke the matching
  specialist. Routes only; does not implement. Turkish cues: belirsiz istek,
  şuna bak, bir bak, düzelt, devam et, ne yapayım, log yapıştırdım.
---

# Dev router

## Done

- One specialist skill is chosen and named in one line.
- The nearest project `AGENTS.md` was located (or the package manifest if missing).
- No code was written in this routing step.
- If still ambiguous after the table, one clarifying question was asked, then stop.

## Read first

1. Nearest `AGENTS.md` from the project root (commands only; not routing).
2. This table. Do not scan the whole repository before routing.

## Route

| Signal in the user message | Skill |
|----------------------------|-------|
| What to build is unclear; ideas, options, scope fuzzy | `brainstorming` |
| Stress-test a plan, "grill" the design | `grilling` (optional — `optional/`) |
| Has direction, needs a written step plan | `writing-plans` |
| Approved plan exists; execute it | `executing-plans` |
| Small concrete change or "add X" with enough detail | `incremental-implementation` |
| Needs a written PRD, requirements doc, or acceptance criteria | `spec-driven-development` |
| Approved spec exists; needs ordered implementation tasks | `writing-plans` |
| Wrong behavior, crash, regression, "broken", intermittent bug | `systematic-debugging` |
| Failing test or build, stack trace, no suspected line yet | `systematic-debugging` |
| Add or lock in tests, TDD, red-green | `test-driven-development` |
| Review PR, diff, "look at my changes", pre-merge review | `code-review-and-quality` |
| "Review since" a branch/commit; Standards + Spec in parallel | `code-review` (optional — `optional/`) |
| Glossary, ADR, domain terminology | `domain-modeling` (optional — `optional/`) |
| Deep module, seam, module interface design | `codebase-design` (optional — `optional/`) |
| Research topic; official docs legwork to a file | `research` (optional — `optional/`) |
| Hard bug or perf; diagnosis loop already stuck | `diagnosing-bugs` (optional — `optional/`) |
| Handoff doc for next session | `handoff` (optional — `optional/`) |
| Agent environment retro (not a bad-chat post-mortem) | `retro` (optional — `optional/`) |
| Branch, merge, release, finish this work | `git-workflow-and-versioning` |
| Parallel worktree or isolate this task | `using-git-worktrees` |
| Approved plan with requested or project-authorized delegation | `subagent-driven-development` |
| Run Codex CLI, codex exec, parallel codex lanes | `codex-fleet` (optional — `optional/`) |
| Usage limit, quota left, how much capacity | `limit` (optional — `optional/`) |
| Claiming done; need proof before closing | `verification-before-completion` |
| Skills meta, which workflow, slash skill help | `using-agent-skills` |
| Session went wrong, wrong skill, wasted loop | `diagnosing-workflow` |
| Author or edit a skill in superskills | `writing-skills` |
| Long-form agent doc mechanics in an app repo | `writing-for-agents` (optional — `optional/`) |

## Tie-breakers

- Failing test **and** named wrong behavior: `systematic-debugging` first (root cause), then `test-driven-development` if the next step is to add or fix tests.
- New feature with unresolved design: `brainstorming`; explicit written-spec request: `spec-driven-development`. A bounded, concrete request can go directly to `incremental-implementation`.
- "Fix" with no error detail: `systematic-debugging` unless the user only wants a review of existing changes (`code-review-and-quality`).
- PR/diff review vs two-axis since fixed point: `code-review-and-quality` for commentary; `code-review` (optional) when Standards and Spec must run in parallel sub-agents.
- Fresh failure vs stuck diagnosis: `systematic-debugging` first; `diagnosing-bugs` (optional) only when the loop is stuck or user asks to diagnose deeper.

## If still ambiguous

Ask one question with two options taken from the table. Do not start editing files.

## Hand off

Say exactly:

```
Routing to: <skill-name>
Reason: <one sentence>
```

Then open the skill file and follow it. Do not merge steps from multiple skills in one turn.

- v1 skills: `skills/<skill-name>/SKILL.md` in this repo (or `~/.cursor/skills/<skill-name>/` when symlinked).
- Optional skills: `optional/<skill-name>/SKILL.md` (or the same name under `~/.cursor/skills/` after `link-optional-skills.sh`).

## Boundaries

- **Always:** route to a single skill; read project `AGENTS.md` for commands after handoff.
- **Ask first:** missing information that prevents choosing a specialist; the handoff itself needs no new approval.
- **Never:** implement, refactor, or "quickly fix" while routing; never invoke `dev-router` recursively.

## Output

```
Route: <skill-name>
Reason: <one sentence>
AGENTS.md: <path or manifest fallback>
Next: follow skills/<skill-name>/SKILL.md or optional/<skill-name>/SKILL.md
```
