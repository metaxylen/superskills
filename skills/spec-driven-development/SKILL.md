---
name: spec-driven-development
description: >-
  Produces a structured specification before implementation when requirements
  are ambiguous, multi-module, or architectural. Use when starting a feature or
  project without a written spec, when the user wants a PRD or requirements
  doc, or when one request bundles several independently testable capabilities.
  Do not use for typo fixes, approved bounded chat designs ready to code, or
  when a spec file already exists and only execution is needed—use
  incremental-implementation, writing-plans, or executing-plans instead. Turkish
  cues: spec, spesifikasyon, gereksinim, PRD, kabul kriteri.
---

# Spec-driven development

## Done

- Spec exists at an agreed path (e.g. `docs/superskills/specs/<feature>.md` or project convention).
- Human reviewed assumptions and spec content before implementation skills run.
- Capability map written first when multiple independent modules are in scope.
- Handoff to `writing-plans` (or bounded → `incremental-implementation`) is explicit.

## Phase 0 — Scope check (multi-capability only)

If one request bundles several independently testable capabilities, propose a **capability map** first:

| Module id | Responsibility | Depends on |
|-----------|----------------|------------|
| … | … | … |

Stable kebab-case ids; acyclic dependencies; human approves map before module specs.

Single-capability work skips Phase 0.

## Phase 1 — Specify

List assumptions explicitly (user, stack, auth, scope). Then write:

1. **Objective** — what, why, who, success criteria  
2. **Commands** — build, test, lint from project or proposed `AGENTS.md` entries  
3. **Scope** — in / out  
4. **Behavior** — flows, edge cases, errors  
5. **Data & interfaces** — models, APIs, boundaries  
6. **Done** — acceptance checks a reviewer can verify  

Stop for human review. Do not code in this skill.

## Phase 2 — Plan (handoff)

After spec approval, invoke `writing-plans` with the spec path. Do not duplicate full task lists here.

## Per-module recursion

For multi-module maps: one spec file per module (`SPEC-<module-id>.md`), dependency order, each gated like Phase 1.

## Boundaries

- **Always:** assumptions block before spec body; spec before multi-file code.
- **Ask first:** architectural decisions that lock other teams; security/compliance claims without source.
- **Never:** silent defaults on ambiguous requirements; skipping review on "obvious" features.

## Output

```
Spec: <path>
Capabilities: single | <module ids>
Assumptions: <listed>
Review: pending | approved
Next: writing-plans | incremental-implementation
```
