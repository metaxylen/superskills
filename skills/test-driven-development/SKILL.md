---
name: test-driven-development
description: >-
  Implements behavior through red-green-refactor. Use for test-first work, a
  regression test, or implementing against an existing failing test. Do not
  use for root-cause investigation, review, or planning only; use
  systematic-debugging, code-review-and-quality, or writing-plans. Turkish
  cues: TDD, test önce, kırmızı yeşil, önce test yaz, regresyon testi.
---

# Test-driven development

## Done

- One failing test was run and shown (red) for the target behavior or bug.
- Minimal production code makes that test pass (green).
- Full project test command from `AGENTS.md` passes (summary pasted).
- No test was deleted or weakened to force green.
- Refactor (if any) happened only on green.

## Iron law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

If implementation already exists, preserve it. Establish that the test detects the missing behavior or defect before treating it as regression evidence; do not discard user work to recreate RED.

## The loop

1. **RED** — One minimal test at an agreed **seam** (public interface, user-visible behavior).
2. **Verify RED** — Run it; paste failure; confirm it fails for the right reason.
3. **GREEN** — Smallest change in the owning module to pass.
4. **Verify GREEN** — Run the test and affected checks; run required project gates before completion or when the project requires them.
5. **REFACTOR** — Optional cleanup only while green; no new behavior.

Work in **vertical slices** (one test → one implementation). Do not batch-write all tests then all code.

## Good tests

- Assert behavior through public interfaces, not private helpers.
- Expected values from spec or literals — not copy-paste of production logic (tautology).
- Prefer real collaborators at the seam; mock only when necessary (I/O, time, network).
- Names read like specifications ("user can …", "rejects invalid …").

Use the existing public boundary and test conventions. Ask only if choosing a different boundary changes the intended behavior.

## Discover commands

Read nearest `AGENTS.md`. If absent, infer from `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`.

## Boundaries

- **Always:** show red once; keep the new test in the final diff.
- **Ask first:** changes to public behavior or interfaces not covered by the request. Generated or configuration-only changes use their relevant validation rather than a forced TDD cycle.
- **Never:** implementation-coupled tests that break on harmless refactors; horizontal "all tests then all code" dumps.

## Gotchas

- A test that never failed does not prove behavior.
- Skipping RED "just this once" usually means the test does not catch the bug.
- Large refactors belong after green, often under `code-review-and-quality`, not mid-loop.

## Output

```
Seam: <interface>
RED: <test path> — <failure snippet>
GREEN: <files changed>
Suite: <command> — <summary>
```
