# Effect to tech tiers

Pick the lowest tier that delivers the idea. Facts and star counts are in `sources.md` (verified 2026-10-13); verify package names and licenses before installing.

| Tier | Motion level | Use | Tech |
|---|---|---|---|
| 0 | Static, trust-first | Product UI, docs, regulated or accessibility-critical | Project's own components, CSS transitions, shadcn/ui |
| 1 | Subtle | Marketing pages, polish on interactions | CSS scroll-driven animation, `motion` (React), React Bits / Magic UI / motion-primitives pieces |
| 2 | Choreographed | Agency, portfolio, storytelling landing | GSAP + ScrollTrigger for timelines and pinned sections, Lenis for smooth scroll (wire Lenis to ScrollTrigger so scroll-linked animation stays in sync) |
| 3 | Immersive | Hero with depth, product showcase, experiments | three.js or react-three-fiber (+ drei, postprocessing), or `paper-design/shaders` for shader backgrounds without a 3D scene |

Notes:

- Authored assets (Lottie, Rive, Spline scenes, models from Blender) come from design tools. If none are provided, use code-generated visuals (shaders, CSS, SVG) instead of inventing assets.
- 3D on mobile: cap pixel ratio, pause off-screen canvases, provide a static fallback, and skip the 3D tier when the content does not need it.
- Motion is spent in one place: one orchestrated page-load or reveal beats effects on every section. Motion that answers a user action is always fine.

## Generic defaults to avoid (agent tells)

- Cream background with a high-contrast serif and terracotta accent; near-black with one acid-green accent.
- Identical rounded cards, one radius everywhere, the same soft shadow, gradient washes as decoration.
- Tracked all-caps eyebrow above every heading; numbered 01/02/03 markers on content that is not a sequence; a single accented word in every headline.
- Fade-and-slide-up entrance on every section; hover lift on every card.
- Inter or system fonts chosen because they are the default, not because they fit.

These are legitimate when the brief calls for them; they are defaults, not choices, when they appear regardless of subject. (Pattern list paraphrased from Anthropic's `frontend-design` skill.)

## Dial shorthand

When the brief gives only a vibe, map it: minimalist or editorial, tiers 0–1 with low density; premium consumer, tier 1–2; Awwwards, experimental or agency, tier 2–3 with high variance; trust-first or public-sector, tier 0. This mirrors the dial table in taste-skill; use that skill's table when it is installed.
