---
name: writing-plans
description: >-
  Turns an approved spec or requirements into a bite-sized implementation
  plan with files, steps, and tests. Use when brainstorming or the user
  provided a spec and multi-step work is next, before writing production
  code. Use when tasks need ordering, checkpoints, or TDD steps spelled
  out. Do not use when the user only wants a quick bounded fix already
  approved in chat, when executing an existing plan, or for debugging—use
  incremental-implementation, executing-plans, or systematic-debugging
  instead.
---

# Writing plans

## Done

- Plan saved under `docs/superskills/plans/YYYY-MM-DD-<feature>.md` (user may override path).
- Header includes goal, architecture summary, spec link, and global constraints copied verbatim.
- Tasks are right-sized: each ends with an independently testable deliverable.
- Steps include explicit TDD beats where behavior changes (fail → pass → suite).
- Executor named: `executing-plans` (inline) or `subagent-driven-development` (per-task gates).

## Before tasks

1. **Scope** — Multiple subsystems → separate plans or clearly sequenced phases.
2. **File map** — Create/modify/test paths; one responsibility per file where possible.
3. **Follow repo patterns** — Match existing layout; do not restructure unrelated areas.

## Plan header (required)

```markdown
# [Feature] implementation plan

**Goal:** …
**Architecture:** …
**Spec:** <path or chat summary>
**Executor:** executing-plans | subagent-driven-development

## Global constraints
- …

## Review focus
- <behaviors the spec implies but tests might miss>
```

## Task template

```markdown
### Task N: [name]

**Files:** create / modify / test paths (exact)

**Steps:**
- [ ] Write failing test — expected: …
- [ ] Run test — expect failure: …
- [ ] Implement minimal change
- [ ] Run test — expect pass
- [ ] Run suite per AGENTS.md — expect: …
- [ ] Commit (if plan says so)

**Completion:** …
```

One step = one checkable action. Fold scaffolding into the task that needs it.

## Boundaries

- **Always:** exact paths; spec travels with the plan; checkbox tasks.
- **Ask first:** plans that change public API or multiple services without spec approval.
- **Never:** vague "implement feature" tasks without tests; duplicate Osmani-scale process trees in the plan body.

## Hand off

Tell the user which executor skill to invoke and the plan path. Do not start implementation in this skill.

## Output

```
Plan: docs/superskills/plans/<file>.md
Tasks: <N>
Executor: executing-plans | subagent-driven-development
Ready: yes — invoke <executor> after user confirms
```
