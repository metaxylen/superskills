---
name: brainstorming
description: >-
  Clarifies intent, constraints, and design before implementation code.
  Use when the user has a new feature, subsystem, or product idea, asks
  "can we", "how should we build", or scope is fuzzy. Use when changing
  behavior that needs agreement on what "done" means. Do not use when an
  approved spec or plan already exists and the user wants execution only,
  when the task is a clear bug with reproduction, or for PR review—use
  writing-plans, executing-plans, systematic-debugging, or
  code-review-and-quality instead. Turkish cues: fikir, nasıl yap, kapsam,
  netleştir, ne yapacağız, tasarım önce.
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

When unsure, take the **heavier** path. Mid-task discovery of hidden complexity **upgrades** the path — stop, say so, re-classify.

For relentless Q&A stress-testing (design tree, numbered rounds), optional `grilling` in `optional/` after scope is roughly known.

## Process

1. **Intent** — Outcome, user, success criteria. One focused question if purpose is missing.
2. **Write back** — Separate facts from assumptions; invite correction.
3. **Design** — Scale to path (spike plan / bounded paragraphs / architectural sections).
4. **Approve** — Stop until the user agrees. Approval of idea ≠ approval to skip later gates.
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
