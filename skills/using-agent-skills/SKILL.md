---
name: using-agent-skills
description: >-
  Explains how the superskills library is loaded, chosen, and combined with the
  project's AGENTS.md. Use when the user asks how skills work, which skill to
  use, what order to follow, or mentions skills, workflows, or slash commands
  for skills. Use when two or more skills could apply and the choice is unclear
  after reading their descriptions. Do not use when the user already named a
  concrete task (bug, failing test, PR or diff review, write tests, plan or
  spec, ship or merge, worktree, subagent)—invoke that specialist or
  dev-router instead. Do not use as a required first step on every message; do
  not replace dev-router for vague coding requests.
---

# Using agent skills

## Done

- The user knows which skill applies (or that `dev-router` handles ambiguity).
- The agent reads the project's nearest `AGENTS.md` for commands and boundaries.
- At most one process skill and one specialist skill are active for the current step.
- No skill text was copied from external repos; this library's `SKILL.md` files are authoritative.

## How this library works

Skills live under `skills/<name>/SKILL.md`. Cursor loads **name** and **description** for every skill at session start. The body loads only after a skill is selected.

Progressive disclosure:

1. **Description** — routing signal only (what + when + when not).
2. **Body** — steps after the skill is active.
3. **references/** — optional; only when the body points to them.

Project commands (`test`, `build`, `lint`) belong in the **project** `AGENTS.md`, not inside skills.

## The sixteen skills (v1)

| Skill | Use for |
|-------|---------|
| `dev-router` | Vague coding request; pick one specialist |
| `brainstorming` | Clarify what to build; no implementation |
| `writing-plans` | Turn spec into ordered steps |
| `executing-plans` | Run an approved plan |
| `incremental-implementation` | Small, incremental code changes |
| `spec-driven-development` | Implement from an explicit spec |
| `test-driven-development` | Red-green tests before or with behavior |
| `systematic-debugging` | Root cause before fixes |
| `verification-before-completion` | Prove done before claiming done |
| `code-review-and-quality` | Review diff or PR; do not rewrite by default |
| `git-workflow-and-versioning` | Branch, merge, finish work |
| `using-git-worktrees` | Isolated worktree for a task |
| `subagent-driven-development` | Subagents or parallel lanes |
| `using-agent-skills` | This file — meta usage |
| `writing-skills` | Author or edit skills in this repo |
| `diagnosing-workflow` | Session went wrong; find process failure |

Full list is also in `skills/CONSOLIDATION.md`.

## Choosing a skill

```
User message
    │
    ├── Vague coding ask, no task name? ──→ dev-router
    ├── Concrete task named? ────────────→ matching specialist (table above)
    ├── How do skills work / which one? ─→ using-agent-skills (this skill)
    └── Session quality / wrong skill? ──→ diagnosing-workflow
```

When multiple skills match:

1. **Process before implementation** (e.g. `systematic-debugging` before editing code for a failure).
2. **One primary skill** per step; hand off explicitly in one line, then follow that skill's body.
3. If still tied, ask **one** clarifying question with two concrete options; then stop.

Do **not** stack "mandatory on every message" behavior (that causes token bloat and wrong activations).

## Core behaviors (all skills)

### Surface assumptions

Before non-trivial work, state assumptions once and invite correction:

```
ASSUMPTIONS:
1. ...
2. ...
→ Correct me or I proceed.
```

### Stop on confusion

If spec, code, and user message disagree: stop, name the conflict, ask once, wait.

### Push back when needed

If the requested approach has a clear downside, say so with a concrete reason; propose a smaller alternative.

### Read skills fresh

When a skill activates, read its current `SKILL.md` in this repo; do not rely on memory from an older version.

## Boundaries

- **Always:** Prefer project `AGENTS.md` for tool commands; prefer one skill per step.
- **Ask first:** Adding a new skill to the v1 set; changing another skill's description for routing.
- **Never:** Install whole third-party skill catalogs into this repo; paste system prompts as skills; run destructive git commands unless the user asked.

## Output

When this skill is invoked to answer "which skill?":

```
Skill: <name>
Why: <one sentence>
Next: <read SKILL.md path or hand off to dev-router>
AGENTS.md: <path or "none — read package manifest">
```
