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
