---
name: test-driven-development
description: >-
  Implements behavior with red-green-refactor: failing test first, minimal code,
  then refactor only while green. Use when adding or changing behavior, fixing a
  bug with a regression test, or the user asks for TDD or test-first work. Use
  when a failing test already exists and the next step is minimal implementation.
  Do not use for root-cause investigation without a test idea yet, for PR review
  only, for planning or brainstorming only, or for claiming work complete—use
  systematic-debugging, code-review-and-quality, writing-plans, or
  verification-before-completion instead. Turkish cues: TDD, test önce, kırmızı
  yeşil, önce test yaz, regresyon testi.
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

Code written before the test? Remove it and start from the test.

## The loop

1. **RED** — One minimal test at an agreed **seam** (public interface, user-visible behavior).
2. **Verify RED** — Run it; paste failure; confirm it fails for the right reason.
3. **GREEN** — Smallest change in the owning module to pass.
4. **Verify GREEN** — Run the test, then the suite command from `AGENTS.md`.
5. **REFACTOR** — Optional cleanup only while green; no new behavior.

Work in **vertical slices** (one test → one implementation). Do not batch-write all tests then all code.

## Good tests

- Assert behavior through public interfaces, not private helpers.
- Expected values from spec or literals — not copy-paste of production logic (tautology).
- Prefer real collaborators at the seam; mock only when necessary (I/O, time, network).
- Names read like specifications ("user can …", "rejects invalid …").

Confirm seams with the user when unclear: "Which public boundary should this test use?"

## Discover commands

Read nearest `AGENTS.md`. If absent, infer from `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`.

## Boundaries

- **Always:** show red once; keep the new test in the final diff.
- **Ask first:** new seam across modules; changing public API; skipping tests for generated or config-only files.
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
