# superskills

A library of **agent skills** for software development with Cursor (and Claude Code / Codex when needed). Instead of re-describing the same discipline in every chat, your message switches the agent into the right mode: **sixteen focused workflows** for planning, debugging, TDD, PRs, git, worktrees, subagents and skill authoring. All skills follow the [Agent Skills](https://agentskills.io/specification) format; Turkish trigger phrases live in each `description`, bodies are English.

This repo is **not application code**. The product is `skills/*/SKILL.md`. Skills do not memorize what `npm test` means in your project; they read the **`AGENTS.md`** at the project root.

---

## Is it worth it?

Yes, if you write code with an agent. What you get:

- **Vague message** ("take a look", pasted logs) → `dev-router` first, then one specialist.
- **Clear job** ("write a plan", "root cause", "review this PR") → the matching skill directly; plan mode does not drift into debugging.
- **"Done"** → `verification-before-completion`: run the command, then speak.

Skills are not magic; they are **checklists plus routing** that remind the agent of good engineering habits in every session.

---

## Setup in five minutes

**1.** Clone the repo.

**2.** Link the skills on your machine. **Pick one method for the v1 names** (do not mix both for the same names):

| What are you doing? | Command |
|----------------|--------|
| Editing skills here (symlinks) | `./scripts/link-cursor-skills.sh` |
| A "real" Cursor plugin directory | `./scripts/install-cursor-plugin.sh` |
| Everything: Cursor + Claude + Codex + optional | `./scripts/link-all-skills.sh` |

With symlinks, after changing the repo use **Reload Window** in Cursor or start a **new Agent chat**.

Details: [docs/plugins.md](docs/plugins.md), [docs/claude-code.md](docs/claude-code.md), [docs/codex.md](docs/codex.md).

**3.** In the **application** repo you work on, put an `AGENTS.md` at the root. Template: [docs/templates/AGENTS.example.md](docs/templates/AGENTS.example.md). Test, lint and build commands live there.

After that, open the chat in the application folder; skills are loaded globally (`~/.cursor/skills`), commands come from the project.

---

## Daily flow

```
Idea unclear         → brainstorming → writing-plans
Plan ready           → executing-plans / incremental-implementation / spec-driven-development
Test broke           → systematic-debugging → (if needed) test-driven-development
PR / diff            → code-review-and-quality
Ship                 → git-workflow-and-versioning + verification-before-completion
Parallel / isolation → using-git-worktrees, subagent-driven-development
```

Unsure which skill to use → `using-agent-skills`. Session went badly → `diagnosing-workflow`.

---

## v1: sixteen skills

Full list and summary: [skills/CONSOLIDATION.md](skills/CONSOLIDATION.md).

| Stage | Skills |
|--------|-----------|
| Routing | `dev-router` |
| Discovery and planning | `brainstorming`, `writing-plans` |
| Code | `executing-plans`, `incremental-implementation`, `spec-driven-development`, `test-driven-development` |
| Quality | `systematic-debugging`, `verification-before-completion`, `code-review-and-quality` |
| Git and environment | `git-workflow-and-versioning`, `using-git-worktrees`, `subagent-driven-development` |
| Meta | `using-agent-skills`, `writing-skills`, `diagnosing-workflow` |

Example Turkish triggers: `plan yaz`, `kök neden`, `PR incele`, `worktree`, `hangi skill`, `oturum kötü`. All of them are in each skill's YAML `description` field (`Turkish cues:`).

---

## Optional

`optional/` is a separate catalog: Codex fleet, usage-limit screen (`limit`), plan interrogation (`grilling`), two-axis review, domain modeling, UI resources with a 3D asset source list (`ui-resources`), and more. It is **not** part of the plugin package; `./scripts/link-optional-skills.sh` links it into the same symlink locations.

Summary table: [optional/README.md](optional/README.md).

---

## Repo map

| Folder | What |
|--------|------|
| `skills/` | v1; the Cursor plugin is built from here |
| `optional/` | Extra skills (MIT parts in `optional/LICENSE-MIT-*.txt`) |
| `scripts/` | Installation |
| `tests/` | Frontmatter, routing and scenario smoke tests: `./tests/run-all.sh` |
| `docs/` | Plan/spec templates, install notes, research notes |
| `.cursor-plugin/` | Plugin manifest |
| `AGENTS.md` | Operating guide for agents **in this repo** (when authoring skills) |

`documentations/` holds **local** notes only (gitignored; not on GitHub).

---

## Changing a feature or skill in this repo

- Plan: `docs/superskills/plans/YYYY-MM-DD-<feature>.md`
- Spec: `docs/superskills/specs/<feature>.md`
- After a change: `./tests/run-all.sh` (or `npm test`)
- Try routing in Cursor: [tests/routing-manual-test.md](tests/routing-manual-test.md)

Agent commands and limits: [AGENTS.md](AGENTS.md).

---

## License

The main skill set and repo text are personal and there is no root `LICENSE` file yet; settle your own terms if you fork it. Vendored parts under `optional/` are covered by [LICENSE-MIT-vendor.txt](optional/LICENSE-MIT-vendor.txt) and [LICENSE-MIT-mattpocock.txt](optional/LICENSE-MIT-mattpocock.txt). `optional/codex-fleet` is third-party work; see [optional/README.md](optional/README.md).
