---
name: brainstorming
description: >-
  Clarifies feature intent and design before coding. Use when exploring an
  idea, asking how should we build it, or scope is fuzzy. Do not use for an
  approved design or plan, a reproducible bug, or PR review; use
  incremental-implementation, executing-plans, systematic-debugging, or
  code-review-and-quality. Turkish cues: fikir, nasıl yap, kapsam, netleştir,
  ne yapacağız, tasarım önce.
---

# Brainstorming

## Done

- Path is chosen: **spike**, **bounded**, or **architectural** (stated in one line).
- User saw a short design or spec summary and **approved** before any implementation.
- Open assumptions are listed; user could correct them.
- Handoff is explicit: spike report, bounded chat design, or `writing-plans` for architectural work.

## Classify first (announce out loud)

| Path | When | Artifact |
|------|------|----------|
| **Spike** | Feasibility question; throwaway code OK | Answer + recommendation; code labeled disposable |
| **Bounded** | Small change to **existing** flow in this repo | Short design in chat; approval gate |
| **Architectural** | New subsystem, new project, cross-cutting interfaces | Written spec section, then `writing-plans` |

Choose the lightest path that resolves the design uncertainty. Re-classify when new evidence changes scope or risk; ask only about decisions the existing request does not settle.

For relentless Q&A stress-testing (design tree, numbered rounds), optional `grilling` in `optional/` after scope is roughly known.

## Process

1. **Intent** — Outcome, user, success criteria. One focused question if purpose is missing.
2. **Write back** — Separate facts from assumptions; invite correction.
3. **Design** — Scale to path (spike plan / bounded paragraphs / architectural sections).
4. **Approve** — Obtain agreement on unresolved design choices before implementation. Honor approval already given; revisit it only when scope or risk materially changes.
5. **Hand off** — Implementation skills only after approval.

Read-only exploration is allowed before approval; no feature commits on `main` without consent.

## Boundaries

- **Always:** no implementation before approval on the chosen path; one classification line up front.
- **Ask first:** spikes that touch production data; architectural work without a place for the spec.
- **Never:** "too simple to need approval"; keep spike code as production without a new classification.

## Output

```
Path: spike | bounded | architectural
Understanding: <3 bullets>
Design: <short text or spec path>
Approval: pending | received
Next: writing-plans | executing-plans | test-driven-development | stop
```
