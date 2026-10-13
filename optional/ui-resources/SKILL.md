---
name: ui-resources
description: >-
  Guides UI design decisions and pulls components, brand design-system
  references, fonts, and animation or 3D tooling from a curated source list
  while building or restyling a frontend. Use when working on UI, a landing
  page, layout, styling, motion, or components and a direction or source is
  needed. Do not use for backend work, UI bugs with a clear root cause, or PR
  review; use systematic-debugging or code-review-and-quality. Turkish cues:
  arayüz, ui, tasarım, bileşen, landing page, animasyon, 3d, font seç, ilham.
---

# UI resources

The agent decides the design direction and fetches what it needs. Sources are in [references/sources.md](references/sources.md), effect-to-tech mapping in [references/stack-tiers.md](references/stack-tiers.md). Read them when the step below calls for them, not up front.

## Process

1. **Read the project.** `package.json`, `components.json`, CSS/Tailwind setup, existing components and any `DESIGN.md`. An established design system beats everything here; skip to step 5.
2. **Design read, one line.** "Reading this as: <page kind> for <audience>, <vibe>, leaning <aesthetic family>." Infer it from the brief, named references and audience. Ask one question only when two readings genuinely diverge. Quiet constraints (accessibility, regulated, trust-first) override taste.
3. **Pull one reference.** If the brief names a brand or vibe, fetch the closest `DESIGN.md` from the index in `sources.md` and take its structure (spacing, hierarchy, depth, component rules). Do not clone a brand's identity.
4. **Plan before code.** 4–6 named colors, type roles (one or two families, clearly distinct), a layout idea, and **one memorable element**. Check the plan against the generic defaults listed in `stack-tiers.md`; revise any part you would produce for every brief.
5. **Choose the tech tier** from the motion level the read implies (`stack-tiers.md`). Use the lowest tier that delivers the idea. Prefer components already in the project, then copy-in components (shadcn registry, React Bits, Magic UI) over new dependencies.
6. **Build, then look.** Screenshot at mobile and desktop widths when a browser tool exists, critique against the plan, remove one decoration. Quality floor: responsive, visible keyboard focus, `prefers-reduced-motion` respected, readable contrast, no layout shift from effects.

## Autonomy

- **Do without asking:** read-only fetches (`gh api` for repo files, docs pages, `shadcn` view/search commands), reading the catalog, screenshots of a local dev server.
- **Ask first:** adding a dependency, installing an MCP server, any paid tool or API key, sending project content to an external generator, replacing an existing design system.

## Boundaries

- Name the source used and why; one library per concern.
- Check a source's license before copying code or assets; confirm package names with `npm view` before installing.
- Never invent a URL, package or API; the catalog entries are the only ones verified.
- Companions that already cover design taste (install separately if wanted): `anthropics/skills` `frontend-design` and `Leonxlnx/taste-skill`. This skill supplies the resources and tech mapping, not a second copy of them.
