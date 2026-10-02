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

## One source, two hosts

| Tool | Script | Target |
|------|--------|--------|
| Cursor | `link-cursor-skills.sh` | `~/.cursor/skills/` |
| Codex | `link-codex-skills.sh` | `~/.agents/skills/` |

Both symlink to this repo’s `skills/` folder.
