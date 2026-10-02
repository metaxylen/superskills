# Manual routing check (Cursor)

Run after install (`link-cursor-skills.sh` or `install-cursor-plugin.sh`) and **Reload Window**. New agent chat. Send one message per row; expect the agent to follow the skill (or name it).

## Turkish

| Message | Expected skill |
|---------|----------------|
| şuna bir bak projede | `dev-router` → specialist |
| plan yaz bu feature için | `writing-plans` |
| planı uygula | `executing-plans` |
| TDD ile yap | `test-driven-development` |
| kök neden ne | `systematic-debugging` |
| bitti mi testler | `verification-before-completion` |
| PR incele | `code-review-and-quality` |
| worktree aç | `using-git-worktrees` |
| hangi skill kullanmalıyım | `using-agent-skills` |
| oturum kötü gitti | `diagnosing-workflow` |

## English

| Message | Expected skill |
|---------|----------------|
| fix this (paste logs) | `dev-router` |
| write a plan for auth | `writing-plans` |
| execute the plan inline | `executing-plans` |
| review my PR | `code-review-and-quality` |
| merge when tests pass | `git-workflow-and-versioning` |

If routing is wrong, edit **description** only (keep body English), add a row to `routing-triggers.tsv` or `routing-triggers-en.tsv`, run `./tests/run-all.sh`.
