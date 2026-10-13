---
name: writing-plans
description: >-
  Writes an implementation plan from approved requirements. Use when
  multi-step work needs ordered tasks, files, and verification. Do not use for
  a bounded fix, executing an existing plan, or debugging; use
  incremental-implementation, executing-plans, or systematic-debugging.
  Turkish cues: plan yaz, uygulama planı, adım adım, görev listesi.
---

# Writing plans

## Done

- Plan saved at the project's plan path; in superskills use `docs/superskills/plans/YYYY-MM-DD-<feature>.md` unless the user overrides it.
- Header includes goal, architecture summary, spec link, and global constraints copied verbatim.
- Tasks are right-sized: each ends with an independently testable deliverable.
- Behavior changes include a failing test and verification; documentation or configuration tasks use their relevant checks.
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
- [ ] Run affected checks and required AGENTS.md gates — expect: …
- [ ] Commit (only if the user requested commits)

**Completion:** …
```

One step = one checkable action. Fold scaffolding into the task that needs it.

## Boundaries

- **Always:** exact paths; spec travels with the plan; checkbox tasks.
- **Ask first:** plans that change public API or multiple services without spec approval.
- **Never:** vague "implement feature" tasks without tests; oversized process trees in the plan body.

## Hand off

Tell the user which executor skill to invoke and the plan path. Do not start implementation in this skill.

## Output

```
Plan: <project plan path>
Tasks: <N>
Executor: executing-plans | subagent-driven-development
Ready: yes — invoke <executor> after user confirms
```
