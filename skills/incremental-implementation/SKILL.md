---
name: incremental-implementation
description: >-
  Delivers multi-file changes in thin vertical slices with test and verify
  between slices. Use when implementing a bounded feature or plan task,
  when more than one file changes, or when tempted to write a large batch
  before running tests. Use for rollout slices or contract-first API work.
  Do not use for a single-line fix, when a full spec does not exist yet and
  scope is still fuzzy, or when only planning or debugging—use
  brainstorming, writing-plans, systematic-debugging, or
  test-driven-development for single-behavior TDD cycles instead.
---

# Incremental implementation

## Done

- Each slice leaves the repo buildable and tests green per `AGENTS.md`.
- Slices are vertical (end-to-end path) unless contract-first explicitly chosen.
- No slice larger than ~100 lines without a test run (guideline, not law).
- Commits follow `git-workflow-and-versioning` (atomic, one logical change).

## The cycle

```
Implement smallest slice → Test → Verify → Commit → Next slice
```

Use `test-driven-development` within a slice when behavior changes.

## Slicing strategies

| Strategy | When |
|----------|------|
| **Vertical** | Default — one user-visible path through stack per slice |
| **Contract-first** | Parallel FE/BE — types/OpenAPI first, then sides, then integrate |
| **Risk-first** | Highest uncertainty first; fail cheap before polish |

Before coding: "What is the simplest thing that could work?" After: fewer lines, no speculative abstractions.

## Rules

- One slice at a time; do not start slice N+1 while slice N is red.
- Prefer feature flags over long-lived branches for incomplete work (see git skill).
- Match existing repo patterns; split files only when the plan or review calls for it.

## Boundaries

- **Always:** run verification command after each slice; commit at known-good points.
- **Ask first:** schema migrations; public API changes; deleting code paths users rely on.
- **Never:** giant uncommitted batches; mixing refactor + feature in one slice without plan.

## Output

```
Slice: <n> — <name>
Files: <list>
Tests: <command> — <summary>
Commit: <hash or message>
Remaining: <next slice or done>
```
