# OpenAI Codex

The same `skills/<name>/SKILL.md` files work in Codex. Cursor install scripts do **not** apply; Codex reads user skills from `~/.agents/skills/` (legacy path: `~/.codex/skills/`).

## Install

```bash
./scripts/link-codex-skills.sh
```

Restart Codex or open the skills picker (`/skills` in CLI, product UI may vary).

## Usage

- Implicit: Codex matches your message to each skill `description` (including Turkish cues).
- Explicit: `$skill-name` or the in-app skills menu (per Codex version).

## Application projects

Copy or adapt [templates/AGENTS.example.md](./templates/AGENTS.example.md) into each app repo. Skills still expect test/build commands there.

## One source, multiple hosts

See [claude-code.md](./claude-code.md) and [plugins.md](./plugins.md). Codex uses `link-codex-skills.sh` → `~/.agents/skills/`.
