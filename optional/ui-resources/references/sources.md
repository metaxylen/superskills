# UI sources

Verified against the GitHub API and vendor docs on 2026-10-13; stars change, re-check before relying on a number. Rationale and evidence: `docs/superskills/research/2026-10-13-ui-resources.md`. Add your own rows at the bottom. Entries marked `unverified` come from your bookmarks and have not been checked.

## Design direction (fetch, read, apply)

| Source | What it gives | How the agent gets it |
|---|---|---|
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | `DESIGN.md` per brand: colors, type, layout, depth, shapes, components, do's and don'ts | `gh api repos/VoltAgent/awesome-design-md/contents/design-md/<brand>/DESIGN.md --jq .content \| base64 -d` |
| [anthropics/skills `frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Direction, typography, anti-default process | Install as a companion skill; do not copy its text |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT) | Brief inference, variance/motion/density dials, redesign, image-to-code skills | Install as a companion skill |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX skill (large, 135k stars) | Mine for ideas; not evaluated |

### DESIGN.md brands (`design-md/<brand>`)

1win, airbnb, airtable, aljazeera, apple, binance, bmw-m, bmw, bugatti, cal, claude, clay, clickhouse, cohere, coinbase, composio, cursor, dell-1996, dji, elevenlabs, expo, ferrari, figma, framer, hashicorp, hp, ibm, intercom, jobright, kraken, lamborghini, linear.app, lovable, mastercard, mercury, meta, minimax, mintlify, miro, mistral.ai, mongodb, mydealz, nerdwallet, nike, nintendo-2001, notion, nvidia, ollama, opencode.ai, oracle, oura, pinterest, playstation, posthog, raycast, renault, replicate, resend, revolut, runwayml, sanity, sap, sentry, shopify, slack, spacex, spotify, starbucks, stripe, supabase, superhuman, tesla, theverge, together.ai, uber, vercel, vodafone, voltagent, warp, webflow, wired, wise, x.ai, zapier. The repo README has a one-line vibe per brand; list the directory first (`gh api repos/VoltAgent/awesome-design-md/contents/design-md --jq '.[].name'`) because the set changes.

## Components

| Source | Use for | Access |
|---|---|---|
| [shadcn/ui](https://ui.shadcn.com) | Accessible base components, blocks, registry | CLI; MCP: `pnpm dlx shadcn@latest mcp init --client claude` ([docs](https://ui.shadcn.com/docs/mcp)). Supports third-party and `@namespace` registries in `components.json` |
| [21st.dev](https://21st.dev) | Community React/Tailwind components | 21st MCP: `npx @21st-dev/cli@latest init --client claude`; needs an API key; `search` and `get_component` work without hosted AI. Check each component's license |
| [React Bits](https://github.com/DavidHDev/react-bits) | Animated, interactive React components | Copy-in; site reactbits.dev |
| [Magic UI](https://github.com/magicuidesign/magicui) | Animated components and effects | Copy-in; site magicui.design |
| [motion-primitives](https://github.com/ibelick/motion-primitives) | Animated UI kit | Copy-in |
| Material UI, Fluent UI | Full suites for Material or Microsoft-style products | Own theming; avoid in Tailwind-first projects without a reason |

## Motion, 3D, shaders

| Source | Use for |
|---|---|
| [motion](https://github.com/motiondivision/motion) | Component and layout animation in React/JS |
| [GSAP](https://github.com/greensock/GSAP) | Timelines, ScrollTrigger; verify current license terms |
| [Lenis](https://github.com/darkroomengineering/lenis) | Smooth scroll; sync with ScrollTrigger |
| [three.js](https://github.com/mrdoob/three.js), [react-three-fiber](https://github.com/pmndrs/react-three-fiber), [drei](https://github.com/pmndrs/drei), [postprocessing](https://github.com/pmndrs/postprocessing) | 3D scenes, helpers, effects |
| [paper-design/shaders](https://github.com/paper-design/shaders) | Zero-dependency canvas shader backgrounds |
| [lottie-web](https://github.com/airbnb/lottie-web), [rive-react](https://github.com/rive-app/rive-react) | Playing authored animations (assets come from design tools) |
| [shuding/cobe](https://github.com/shuding/cobe) | Small WebGL globe |
| [chenglou/pretext](https://github.com/chenglou/pretext) | Text measurement and layout; not evaluated in depth |

## Fonts, generators, verification

| Source | Use for |
|---|---|
| [Google Fonts](https://fonts.google.com) | Typeface choice; use the framework's font loader or self-host |
| [vercel/geist-font](https://github.com/vercel/geist-font) | Geist family |
| [v0](https://v0.dev) | UI drafts from prompts; adapt to project components; ask before sending project content |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Screenshots and browser checks for the build-look-critique loop |

## From your bookmarks, not yet verified

MotionSites (premium hero prompts), a "build 3D websites without writing code" tool, Framer (as visual reference), Fluent UI. No URLs recorded for the first two; add them before the agent can use them.

## Add your own

Append a row under the closest category: name, URL, what it is for, how the agent fetches it, one caveat.
