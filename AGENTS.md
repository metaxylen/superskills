# AGENTS.md — superskills repository

You are in the **skill library** repo: Agent Skills for Cursor, Claude Code, and Codex. This is not an application codebase. There is no `npm run build` for a product here; the deliverable is **`skills/*/SKILL.md`** (and optionally **`optional/*/SKILL.md`**) plus install scripts and tests.

When the user’s task is in **another** project, read **that** repo’s `AGENTS.md` for test/lint/build commands. This file is authoritative only while the workspace is superskills.

---

## Commands

Run from the repository root.

| Intent | Command |
|--------|---------|
| **Validate everything** (required before claiming skill work is done) | `./tests/run-all.sh` or `npm test` |
| Frontmatter + plugin JSON only | `./tests/skill-frontmatter.sh` |
| Routing triggers + Turkish token uniqueness | `python3 ./tests/routing_eval.py` |
| dev-router table ↔ files on disk | `python3 ./tests/router_integrity.py` |
| Synthetic routing walkthrough | `python3 ./tests/routing_scenarios.py` |

**Install (pick one method for v1 names — do not combine plugin copy + symlink for the same skill names):**

| Intent | Command |
|--------|---------|
| Dev: symlink v1 into Cursor | `./scripts/link-cursor-skills.sh` |
| Dev: symlink v1 + optional into Cursor, Claude, Codex | `./scripts/link-all-skills.sh` |
| Optional skills only | `./scripts/link-optional-skills.sh` |
| Plugin layout under `~/.cursor/plugins/local/superskills/` | `./scripts/install-cursor-plugin.sh` |
| Dry-run / uninstall | add `--dry-run` or `--unlink` / `--remove` per script |

After install or skill edits that affect Cursor: **reload the window** or start a **new agent chat** so descriptions reload.

Details: [docs/plugins.md](docs/plugins.md), [docs/claude-code.md](docs/claude-code.md), [docs/codex.md](docs/codex.md), [scripts/README.md](scripts/README.md).

---

## How to choose a skill in this repo

Use **one** specialist per step. Do not implement product features in `dev-router`.

| User intent in superskills | Skill |
|----------------------------|-------|
| Vague “fix this / look at the repo” without naming the job | `dev-router` |
| Change routing, descriptions, or add/edit a v1 skill | `writing-skills` (read `skills/CONSOLIDATION.md` first) |
| Meta: how skills load, symlink vs plugin, which workflow | `using-agent-skills` |
| Last chat went wrong (wrong skill, wasted loop) | `diagnosing-workflow` |
| Ship: commit, branch, PR for this repo | `git-workflow-and-versioning` |
| Prove tests pass before closing | `verification-before-completion` |

Optional workflows (`grilling`, `codex-fleet`, `limit`, two-axis `code-review`, etc.) live under **`optional/`** and are listed in `dev-router`’s table. Paths on handoff: `optional/<name>/SKILL.md`, not `skills/`.

Full v1 catalog: [skills/CONSOLIDATION.md](skills/CONSOLIDATION.md). Optional catalog: [optional/README.md](optional/README.md).

---

## Repository map

| Path | Role for agents |
|------|------------------|
| `skills/` | **v1 — sixteen skills.** Shipped by `.cursor-plugin/plugin.json`. One `SKILL.md` per folder; folder name = `name` in frontmatter. |
| `optional/` | **Extras** (vendored MIT). Not in the plugin bundle; linked via `link-optional-skills.sh`. |
| `tests/` | Automated gates: frontmatter, EN/TR triggers, router integrity, scenario smoke. |
| `scripts/` | Install and symlink only. |
| `docs/` | Human docs; plan/spec **templates** under `docs/superskills/`. |
| `.cursor-plugin/` | Plugin manifest; bump `version` when publishing or tagging releases. |
| `documentations/` | **Local-only** personal notes (`documentations/` in `.gitignore`). Not in the public repo; `.cursorignore` if present locally. Do not use for workflow. |
| `.upstream/` | Optional private notes (gitignored). |

Application repos should copy [docs/templates/AGENTS.example.md](docs/templates/AGENTS.example.md), not this file.

---

## Playbooks (common changes)

### Edit an existing v1 skill

1. Read `skills/CONSOLIDATION.md` and every skill that might overlap (especially `dev-router` and cousins).
2. Follow `skills/writing-skills/SKILL.md`.
3. Body: **English**. Turkish routing: **`Turkish cues:`** in YAML `description` only.
4. If `description` changed: add or adjust rows in `tests/routing-triggers.tsv` and/or `tests/routing-triggers-en.tsv`.
5. Run `./tests/run-all.sh` and paste a one-line result if claiming done.

### Add or change optional skill

1. Put `optional/<name>/SKILL.md`; keep MIT attribution in `optional/LICENSE-MIT-*.txt` when vendored.
2. Update `optional/README.md` and, if routed, `skills/dev-router/SKILL.md`.
3. Add triggers to `tests/optional-routing-triggers.tsv` when description cues matter.
4. Run `./tests/run-all.sh`.

### Bump Cursor plugin version

1. Edit `.cursor-plugin/plugin.json` `version`.
2. Note in `CHANGELOG.md`.
3. `./tests/run-all.sh`.

### Plan or spec work on superskills itself

| Artifact | Path |
|----------|------|
| Feature spec | `docs/superskills/specs/<feature>.md` |
| Implementation plan | `docs/superskills/plans/YYYY-MM-DD-<feature>.md` |
| Runtime ledger (optional) | `<plan-stem>-ledger.md` next to the plan (gitignored pattern `*-ledger.md` unless user wants it committed) |

Use `writing-plans` / `executing-plans` / `subagent-driven-development` when the user is driving a multi-step change; use `writing-skills` when the change is skill authoring.

---

## Conventions (this repo)

- **v1 count stays sixteen** unless the user explicitly expands the set; then update `CONSOLIDATION.md`, `skill_frontmatter.py` `EXPECTED_COUNT`, plugin copy, and routing tests together.
- **No duplicate routing:** each Turkish cue token must map to one v1 skill (`routing_eval.py` enforces uniqueness).
- **Do not** paste entire third-party skill trees into `~/.cursor/skills` or commit them as v1.
- **Do not** name external skill catalogs in committed skill bodies or docs (distill patterns; keep licenses in `optional/`).
- **Commits:** only when the user asks. Never `git config --global`. If identity is unset:

```bash
export GIT_AUTHOR_NAME='your-name'
export GIT_AUTHOR_EMAIL='you@users.noreply.github.com'
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"
export GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
```

Isolated feature work: `.worktrees/<branch>` (gitignored). See `using-git-worktrees`.

---

## Done means (skill-library work)

- `./tests/run-all.sh` exits 0 (not assumed — run it).
- Routing changes reflected in TSV files and `dev-router` if applicable.
- README / `optional/README.md` updated when install surface or layout changes.
- User approved wording for new or heavily rewritten skill text before commit.

Manual Cursor check after routing edits: [tests/routing-manual-test.md](tests/routing-manual-test.md).

Marketplace publish checklist (optional): [docs/marketplace.md](docs/marketplace.md).

---

## Boundaries

| | |
|--|--|
| **Always** | One skill per step; validate with `./tests/run-all.sh` before “done”; English skill bodies; Turkish only in descriptions. |
| **Ask first** | Adding a seventeenth v1 skill; destructive git; pushing without user request. |
| **Never** | Treat `documentations/` as product docs; combine plugin install + symlink for the same skill names; implement app features here unless the user is changing superskills itself. |
