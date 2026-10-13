---
name: incremental-implementation
description: >-
  Implements a bounded feature or plan task in vertical slices with
  verification between slices. Do not use for unresolved requirements,
  planning only, or root-cause investigation; use brainstorming,
  writing-plans, or systematic-debugging. Turkish cues: artımlı, küçük adım,
  ince dilim, çok dosya değişecek.
---

# Incremental implementation

## Done

- Each slice leaves the repo buildable and tests green per `AGENTS.md`.
- Slices are vertical (end-to-end path) unless contract-first explicitly chosen.
- Each slice has one verifiable outcome; its boundary follows behavior and risk, not a line count.
- If the user requested commits, follow `git-workflow-and-versioning` (one logical change).

## The cycle

```
Implement smallest slice → Run affected checks → Verify → Next slice
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

- **Always:** verify each slice; run required project gates before completion; commit only when requested.
- **Ask first:** schema migrations; public API changes; deleting code paths users rely on.
- **Never:** mix unrelated refactors and features in one slice.

## Output

```
Slice: <n> — <name>
Files: <list>
Tests: <command> — <summary>
Commit: <hash if requested, otherwise not requested>
Remaining: <next slice or done>
```
