# AGENTS.md (application project)

Copy to your app repo root. Skills read this for commands; superskills do not hardcode your stack.

## Commands

```bash
# install
npm install

# test (full suite)
npm test

# test (single file)
npm test -- path/to/file.test.ts

# lint
npm run lint

# build
npm run build
```

## Conventions

- TypeScript strict; prefer existing folder layout.
- No force-push to `main`.
- Commits: small, one logical change each.

## Plans (optional)

If you use superskills plan paths in this project:

- Specs: `docs/superskills/specs/<feature>.md`
- Plans: `docs/superskills/plans/YYYY-MM-DD-<feature>.md`

Override paths in chat if your layout differs.

## Delegation (optional project policy)

Adopt this section only if you want the agent to decide when to delegate.

Autonomous subagents are requested only for bounded work where independent
progress, context isolation or consequential fresh review outweighs handoff
and integration cost. Keep tiny, tightly dependent and same-file tasks inline.
Use the installed `subagent-driven-development` skill's
`references/delegation-policy.md` for the decision and budget rules; if it is
unavailable, stay inline. Default: two child work runs shared across the whole
requested objective, including plan tasks, research, reviews, follow-ups,
retries and resumed sessions; no nested delegation. Respect explicit
inline-only requests, host limits and model preferences. Keep the owning
specialist; an investigation does not require a development plan.
