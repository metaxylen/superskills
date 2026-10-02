---
name: dev-router
description: >-
  Routes vague or underspecified software development requests to exactly one
  superskills specialist. Use when the user wants help on a project but does not
  name the task type—fixing, planning, reviewing, testing, shipping, or
  implementing. Use for messages like "take a look", "fix this", "continue",
  "something broke", or a paste of logs or errors without a clear ask. Do not
  use when the user already named the task (PR review, write a plan, add tests,
  debug with root cause, merge branch, worktree, run subagents, or how skills
  work)—invoke that skill directly. Do not implement code in this skill; only
  route and hand off. Turkish cues: belirsiz istek, şuna bak, bir bak, düzelt,
  devam et, ne yapayım, log yapıştırdım. Optional installs: codex exec → codex-fleet;
  kota → limit (see optional/).
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
| Has direction, needs a written step plan | `writing-plans` |
| Approved plan exists; execute it | `executing-plans` |
| Small concrete change or "add X" with enough detail | `incremental-implementation` |
| Explicit spec or acceptance criteria to implement | `spec-driven-development` |
| Wrong behavior, crash, regression, "broken", intermittent bug | `systematic-debugging` |
| Failing test or build, stack trace, no suspected line yet | `systematic-debugging` |
| Add or lock in tests, TDD, red-green | `test-driven-development` |
| Review PR, diff, "look at my changes", pre-merge review | `code-review-and-quality` |
| Branch, merge, release, finish this work | `git-workflow-and-versioning` |
| Parallel worktree or isolate this task | `using-git-worktrees` |
| Subagents, parallel lanes, delegate chunks | `subagent-driven-development` |
| Run Codex CLI, codex exec, parallel codex lanes | `codex-fleet` (optional — `optional/`) |
| Usage limit, quota left, how much capacity | `limit` (optional — `optional/`) |
| Claiming done; need proof before closing | `verification-before-completion` |
| Skills meta, which workflow, slash skill help | `using-agent-skills` |
| Session went wrong, wrong skill, wasted loop | `diagnosing-workflow` |
| Author or edit a skill in superskills | `writing-skills` |

## Tie-breakers

- Failing test **and** named wrong behavior: `systematic-debugging` first (root cause), then `test-driven-development` if the next step is to add or fix tests.
- New feature **and** no spec: `brainstorming` before `writing-plans` before implementation skills.
- "Fix" with no error detail: `systematic-debugging` unless the user only wants a review of existing changes (`code-review-and-quality`).

## If still ambiguous

Ask one question with two options taken from the table. Do not start editing files.

## Hand off

Say exactly:

```
Routing to: <skill-name>
Reason: <one sentence>
```

Then open `skills/<skill-name>/SKILL.md` and follow it. Do not merge steps from multiple skills in one turn.

## Boundaries

- **Always:** route to a single skill; read project `AGENTS.md` for commands after handoff.
- **Ask first:** routing that changes project code or git state.
- **Never:** implement, refactor, or "quickly fix" while routing; never invoke `dev-router` recursively.

## Output

```
Route: <skill-name>
Reason: <one sentence>
AGENTS.md: <path or manifest fallback>
Next: follow skills/<skill-name>/SKILL.md
```
