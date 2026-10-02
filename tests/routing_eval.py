#!/usr/bin/env python3
"""Routing checks: trigger files, English cues, unique Turkish cue tokens."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
TESTS_DIR = Path(__file__).resolve().parent

# Import frontmatter parser from sibling module
sys.path.insert(0, str(TESTS_DIR))
from skill_frontmatter import parse_frontmatter  # noqa: E402


def load_descriptions() -> dict[str, str]:
    out: dict[str, str] = {}
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir():
            continue
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        fm = parse_frontmatter(md.read_text(encoding="utf-8"))
        out[d.name] = fm.get("description", "")
    return out


def load_triggers(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            raise ValueError(f"bad line in {path.name}: {line!r}")
        rows.append((parts[0].strip(), parts[1].strip()))
    return rows


def turkish_cue_tokens(desc: str) -> list[str]:
    m = re.search(r"turkish cues:\s*(.+?)(?:\.\s*do not use|\.$|$)", desc, re.I)
    if not m:
        return []
    chunk = m.group(1)
    return [t.strip().lower() for t in re.split(r",\s*", chunk) if t.strip()]


def main() -> int:
    errors: list[str] = []
    descriptions = load_descriptions()

    for fname in ("routing-triggers.tsv", "routing-triggers-en.tsv"):
        for skill, trigger in load_triggers(TESTS_DIR / fname):
            if skill not in descriptions:
                errors.append(f"{fname}: unknown skill {skill!r}")
                continue
            if trigger.lower() not in descriptions[skill].lower():
                errors.append(f"{fname}: '{trigger}' not in {skill} description")

    owner: dict[str, str] = {}
    for skill, desc in descriptions.items():
        for token in turkish_cue_tokens(desc):
            if token in owner and owner[token] != skill:
                errors.append(
                    f"duplicate Turkish cue '{token}': {owner[token]} and {skill}"
                )
            else:
                owner[token] = skill

    # dev-router should not share primary Turkish tokens with specialists
    router_tokens = set(turkish_cue_tokens(descriptions.get("dev-router", "")))
    for skill, desc in descriptions.items():
        if skill == "dev-router":
            continue
        overlap = router_tokens & set(turkish_cue_tokens(desc))
        # allow generic words if identical token lists are small; flag exact dupes only
        for t in overlap:
            if len(t) > 12:
                errors.append(f"long Turkish cue shared by dev-router and {skill}: {t!r}")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    tr_count = len(load_triggers(TESTS_DIR / "routing-triggers.tsv"))
    en_count = len(load_triggers(TESTS_DIR / "routing-triggers-en.tsv"))
    print(f"OK: routing ({tr_count} TR + {en_count} EN triggers, {len(owner)} unique TR tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
