# UI design resources for agents — research (2026-10-13)

Question: why do agent-built UIs look generic next to the work people post online, which stacks produce the impressive results, and what should a skill give an agent so it makes design decisions and fetches resources on its own?

Evidence quality: repo facts (stars, pushed date, file layout) come from the GitHub API on 2026-10-13. Two claims rest on secondary sources and are marked. There is no official Awwwards data on winning stacks.

## Findings

### 1. Impressive UI starts with a decision, not a library

- Anthropic's `frontend-design` skill ([anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)) tells the agent to ground the design in the subject and audience, commit to a specific direction, write a small token plan (4–6 named colors, type roles, layout concept) and review it against the brief before coding. It names the generic defaults to avoid: cream-and-terracotta, near-black with one acid accent, identical rounded cards with one shadow, eyebrow labels above every heading, fade-and-slide on every section. It limits boldness to one memorable element.
- `Leonxlnx/taste-skill` ([95k stars](https://github.com/Leonxlnx/taste-skill), MIT, pushed 2026-10-12) adds a "design read" step (page kind, audience, vibe, references, constraints), then three numeric dials: `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`, with a table mapping vibe words ("Awwwards", "Linear-style", "trust-first") to dial values. It asks at most one clarifying question and only when the read genuinely diverges.
- Takeaway: the missing piece in a link list is a decision procedure. A catalog tells the agent what exists; the procedure tells it what to choose and why.

### 2. Real brand design systems are fetchable as text

- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (120k stars, pushed 2026-10-12) holds `design-md/<brand>/DESIGN.md` for about 84 brands (Linear, Stripe, Vercel, Apple, Spotify, Ferrari, Raycast, Framer and more). A sample file (`linear.app`) has Overview, Colors, Typography, Layout, Elevation, Shapes, Components, and Do's and Don'ts sections. The README describes the intent: drop one in a project and tell the agent to build in that language.
- Agents can read these directly with `gh api repos/VoltAgent/awesome-design-md/contents/design-md/<brand>/DESIGN.md --jq .content | base64 -d`. This is the most direct answer to "pull what you need without me selecting it".
- Caveat: these describe other companies' visual identities. Use them for structure and principles (spacing, hierarchy, depth), not to clone a brand.

### 3. Reference image first, then code

- taste-skill ships `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit` and `image-to-code-skill`. Its README describes generating reference boards with an image generator, then handing the frames to a coding agent. This is a plausible part of why posted work looks richer: the visual was designed first (or by a design tool), and code reproduced it. An agent that designs while it codes tends toward the defaults in finding 1. This is an inference from the repo's stated workflow, not a measured result.

### 4. The "wow" stack is a small set of libraries with separate jobs

| Job | Tool | Evidence |
|---|---|---|
| 3D rendering | [three.js](https://github.com/mrdoob/three.js) (116k stars) | active 2026-10-13 |
| React 3D | [react-three-fiber](https://github.com/pmndrs/react-three-fiber) (33k), [drei](https://github.com/pmndrs/drei) (10k), [postprocessing](https://github.com/pmndrs/postprocessing) (2.9k) | active |
| Shader backgrounds, no 3D scene | [paper-design/shaders](https://github.com/paper-design/shaders) (3.6k) | active 2026-10-12 |
| Timeline and scroll animation | [GSAP](https://github.com/greensock/GSAP) (29k) | last push 2026-04 |
| Smooth scroll | [Lenis](https://github.com/darkroomengineering/lenis) (16.5k) | active 2026-10 |
| Component animation in React | [motion](https://github.com/motiondivision/motion) (34k) | active 2026-10-13 |
| Copy-in animated components | [React Bits](https://github.com/DavidHDev/react-bits) (49k), [Magic UI](https://github.com/magicuidesign/magicui) (22.6k), [motion-primitives](https://github.com/ibelick/motion-primitives) (6.5k) | active |
| Base components and registry | [shadcn/ui](https://github.com/shadcn-ui/ui) (125k) | active 2026-10-12 |
| Authored animation assets | [lottie-web](https://github.com/airbnb/lottie-web) (32k), [rive-react](https://github.com/rive-app/rive-react) | Lottie last push 2025-09 |
| Text measurement for layout effects | [pretext](https://github.com/chenglou/pretext) (50k) | active 2026-10-13; not evaluated in depth |

- Secondary source (search summary of a [Codrops case study](https://tympanus.net/codrops/?p=117096), page returned 403 to my fetch so I did not read it): award-style sites combine GSAP + ScrollTrigger, Lenis and Three.js, each with one responsibility, and Lenis must be synchronised with ScrollTrigger. Treat as common practice, not verified against current winners.
- GSAP licensing and which plugins are free changed in recent years; I did not verify the current terms. Check before use.

### 5. Agents can reach these sources without manual steps

- shadcn MCP ([docs](https://ui.shadcn.com/docs/mcp)): `pnpm dlx shadcn@latest mcp init --client claude`, or `.mcp.json` with `npx shadcn@latest mcp`. Lets the agent search and install from the default registry, third-party registries, and `@namespace` registries defined in `components.json`.
- 21st MCP ([21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)): replaces the old Magic MCP. Install with `npx @21st-dev/cli@latest init --client claude`; needs an API key. `search` and `get_component` work without hosted AI access.
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) (14k): screenshots for the build, look, critique loop.
- GitHub contents through `gh api` (read-only) for DESIGN.md files and registries.

## What I could not establish

- What specific viral Instagram pieces use. They are not reproducible from public repos; the toolchain above is the likely overlap, and some of that work uses design and 3D tools (Spline, Blender, Figma, After Effects) whose output an agent cannot recreate from a link list.
- Current Awwwards winner stacks.
- Whether the new skill improves output. A before/after comparison on the same briefs is the test; none has been run.

## Before/after check (2026-10-13)

Setup: three vague briefs (ceramics studio, open-source Docker CLI, motion designer portfolio), each generated once without and once with the skill by `claude -p --model sonnet` as a single `index.html`. Screenshots at 1440x900 (hero only), shuffled into blind A/B pairs, then judged by me before the key was opened.

Result: the skill version was preferred in 3 of 3 pairs. The baseline pages showed the generic defaults named above (cream and terracotta; centered purple-gradient hero; decorative gradient blob, plus a clipped "g" in the headline). The skill versions had subject-specific interaction (glaze picker, layer-race simulation, timecode and playhead).

Limits: three briefs, one run each, one judge from the same model family, hero view only. The run logs hold only final summaries, so I cannot show that the skill runs fetched a `DESIGN.md`; the effect may come from the skill's process text alone. Treat this as a first signal, not a measurement of the gain.

## Decisions for the skill

1. Put the decision procedure first: design read, one reference, token plan, one memorable moment, tech tier from motion intensity.
2. Keep the catalog in `references/`, with verified entries only and fetch commands next to each.
3. Let the agent do read-only fetches (GitHub API, docs, `shadcn view`) without asking; ask before installing dependencies, adding MCP servers, using paid tools or sending project content out.
4. Do not duplicate `anthropics/skills` frontend-design or taste-skill. Point to them as installable companions.

## 3D asset sources (2026-10-14)

Discovery by web search (one extended, two standard) and GitHub search (no useful awesome list found), then verification by fetching vendor pages and calling APIs. Findings that changed the first list:

- Sketchfab was bought by KitBash from Epic (announced 2026-08-10). Search still works today; the download API and free policy after the sale are unannounced.
- Smithsonian 3D models are CC0 and reachable through the Sketchfab search API under user `Smithsonian`; the Open Access API also responds.
- BlenderKit's search API works without login; its free assets are royalty-free, not CC0.
- Gobkit exposes a CC0 JSON API with rigged models, but only about 99 models.
- KayKit (CC0, itch.io) and OpenGameArt (mixed licenses) were missing from the first pass.
- Quaternius has its own license, not CC0.
- Objaverse is a research dataset with per-object licenses; not for production.
- Smithsonian 3D site, Mixamo, Poly Pizza's license page, CGTrader, TurboSquid and Free3D could not be fully verified.

The skill requires user approval before any asset is used. Full tables: `optional/ui-resources/references/3d-assets.md`.
