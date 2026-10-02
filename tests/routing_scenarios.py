#!/usr/bin/env python3
"""
Synthetic end-to-end routing walkthrough (no LLM).

Simulates: install → user message → expected specialist per dev-router table + descriptions.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
OPTIONAL_DIR = REPO_ROOT / "optional"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_frontmatter import parse_frontmatter  # noqa: E402

# Fake product context (not a real repo)
FAKE_APP = "Fixit Corp checkout service"


@dataclass(frozen=True)
class Scenario:
    id: str
    user_message: str
    expect_skill: str
    reason: str
    entry: str  # "direct" | "via-dev-router"


# Keyword → skill (first match wins; order = dev-router table priority approx.)
ROUTE_RULES: list[tuple[str, str]] = [
    ("hangi skill", "using-agent-skills"),
    ("how skills work", "using-agent-skills"),
    ("skill yaz", "writing-skills"),
    ("grill", "grilling"),
    ("planı uygula", "executing-plans"),
    ("execute the plan", "executing-plans"),
    ("plan yaz", "writing-plans"),
    ("implementation plan", "writing-plans"),
    ("tdd", "test-driven-development"),
    ("review since", "code-review"),
    ("pr incele", "code-review-and-quality"),
    ("look at my changes", "code-review-and-quality"),
    ("glossary", "domain-modeling"),
    ("adr", "domain-modeling"),
    ("deep module", "codebase-design"),
    ("primary source", "research"),
    ("codex exec", "codex-fleet"),
    ("kota", "limit"),
    ("quota", "limit"),
    ("worktree", "using-git-worktrees"),
    ("subagent", "subagent-driven-development"),
    ("oturum kötü", "diagnosing-workflow"),
    ("bitti mi", "verification-before-completion"),
    ("merge", "git-workflow-and-versioning"),
    ("kök neden", "systematic-debugging"),
    ("stack trace", "systematic-debugging"),
    ("bozuldu", "systematic-debugging"),
    ("something broke", "systematic-debugging"),
    ("500", "systematic-debugging"),
    ("netleştir", "brainstorming"),
    ("scope is fuzzy", "brainstorming"),
]

DEV_ROUTER_CUES = [
    "belirsiz istek",
    "şuna bak",
    "bir bak",
    "log yapıştırdım",
    "fix this",
    "take a look",
    "ne yapayım",
]


def skill_path(name: str) -> Path:
    v1 = SKILLS_DIR / name / "SKILL.md"
    if v1.is_file():
        return v1
    opt = OPTIONAL_DIR / name / "SKILL.md"
    if opt.is_file():
        return opt
    raise FileNotFoundError(name)


def load_description(name: str) -> str:
    fm = parse_frontmatter(skill_path(name).read_text(encoding="utf-8"))
    return fm.get("description", "")


def route_message(message: str) -> tuple[str, str]:
    lower = message.lower()
    for cue in DEV_ROUTER_CUES:
        if cue in lower:
            entry = "via-dev-router"
            break
    else:
        entry = "direct"

    for needle, skill in ROUTE_RULES:
        if needle in lower:
            return skill, entry
    if entry == "via-dev-router":
        return "systematic-debugging", entry  # default tie-breaker for vague + error-ish
    return "dev-router", "direct"


SCENARIOS = [
    Scenario(
        "S1-vague-log",
        "log yapıştırdım checkout 500 veriyor ne yapayım",
        "systematic-debugging",
        "vague + failure symptom → dev-router then debugging",
        "via-dev-router",
    ),
    Scenario(
        "S2-plan",
        "plan yaz: Fixit Corp için retry policy",
        "writing-plans",
        "explicit plan request",
        "direct",
    ),
    Scenario(
        "S3-pr",
        "PR incele lütfen",
        "code-review-and-quality",
        "Turkish PR review cue",
        "direct",
    ),
    Scenario(
        "S4-quota",
        "kota ne kadar kaldı codex için",
        "limit",
        "optional limit skill",
        "direct",
    ),
    Scenario(
        "S5-grill",
        "grill this design before we code",
        "grilling",
        "optional grilling",
        "direct",
    ),
    Scenario(
        "S6-meta",
        "hangi skill kullanmalıyım merge için",
        "using-agent-skills",
        "meta question (merge also present; skill question wins by rule order)",
        "direct",
    ),
]


def main() -> int:
    errors: list[str] = []
    print(f"Scenario app: {FAKE_APP}")
    print("Install path (simulated): ./scripts/link-all-skills.sh → ~/.cursor/skills/<name>")
    print()

    for sc in SCENARIOS:
        predicted, entry = route_message(sc.user_message)
        path = skill_path(sc.expect_skill)
        rel = path.relative_to(REPO_ROOT)
        steps = [
            f"1. User message: {sc.user_message!r}",
            f"2. Entry: {entry} (dev-router cues checked)",
            f"3. Table/rules → skill: {predicted!r} (expected {sc.expect_skill!r})",
            f"4. Open: {rel}",
            f"5. Why: {sc.reason}",
        ]
        if predicted != sc.expect_skill:
            errors.append(f"{sc.id}: predicted {predicted}, expected {sc.expect_skill}")
        if not path.is_file():
            errors.append(f"{sc.id}: missing {path}")
        try:
            load_description(sc.expect_skill)
        except Exception as e:
            errors.append(f"{sc.id}: bad frontmatter: {e}")
        print(f"--- {sc.id} ---")
        for line in steps:
            print(line)
        print()

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print(f"OK: routing scenarios ({len(SCENARIOS)} synthetic paths)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
