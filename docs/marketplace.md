# Cursor Marketplace (when you are ready)

v1 is installed locally; publishing is optional.

## Prerequisites

- Cursor team or marketplace access per your plan.
- Plugin validates: `./tests/run-all.sh`
- Version bumped in `.cursor-plugin/plugin.json`

## Local smoke test

```bash
./scripts/install-cursor-plugin.sh
```

Reload Cursor → **Customize → Skills** → confirm `superskills` and sixteen skills.

## Publish checklist

1. Repository public or team-visible per marketplace policy.
2. Manifest complete: `name`, `displayName`, `description`, `version`, `author`, `repository`, `skills`.
3. No secrets in `skills/` or scripts.
4. README install section matches plugin path.
5. Changelog entry in `CHANGELOG.md`.

## Team marketplace

Admins upload or connect the Git repo in Cursor dashboard (Marketplace / Plugins). Exact UI varies by Cursor version; follow in-app **Publish plugin** or team docs.

## After publish

Users install from marketplace instead of `install-cursor-plugin.sh`. Keep local script for development.
