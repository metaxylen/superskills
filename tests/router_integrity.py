#!/usr/bin/env python3
"""Ensure dev-router table targets exist and optional routing triggers match."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
OPTIONAL_DIR = REPO_ROOT / "optional"
DEV_ROUTER = SKILLS_DIR / "dev-router" / "SKILL.md"
OPTIONAL_TRIGGERS = Path(__file__).resolve().parent / "optional-routing-triggers.tsv"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_frontmatter import parse_frontmatter  # noqa: E402

V1_SKILL_NAMES = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}


def skills_in_router_table(text: str) -> set[str]:
    found: set[str] = set()
    for m in re.finditer(r"\|\s*`([a-z0-9-]+)`", text):
        found.add(m.group(1))
    return found


def load_optional_descriptions() -> dict[str, str]:
    out: dict[str, str] = {}
    if not OPTIONAL_DIR.is_dir():
        return out
    for d in sorted(OPTIONAL_DIR.iterdir()):
        if not d.is_dir():
            continue
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        fm = parse_frontmatter(md.read_text(encoding="utf-8"))
        out[d.name] = fm.get("description", "")
    return out


def main() -> int:
    errors: list[str] = []
    router_text = DEV_ROUTER.read_text(encoding="utf-8")
    routed = skills_in_router_table(router_text)
    optional_desc = load_optional_descriptions()

    for name in sorted(routed):
        if name in V1_SKILL_NAMES:
            continue
        opt_md = OPTIONAL_DIR / name / "SKILL.md"
        if not opt_md.is_file():
            errors.append(f"dev-router targets missing skill: {name!r} (not in skills/ or optional/)")

    # v1 skills referenced in table should exist
    for name in routed:
        if name not in V1_SKILL_NAMES and name not in optional_desc:
            continue

    if OPTIONAL_TRIGGERS.is_file():
        for line in OPTIONAL_TRIGGERS.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                errors.append(f"optional-routing-triggers.tsv: bad line: {line!r}")
                continue
            skill, trigger = parts[0].strip(), parts[1].strip()
            desc = optional_desc.get(skill, "")
            if not desc:
                errors.append(f"optional-routing: unknown skill {skill!r}")
            elif trigger.lower() not in desc.lower():
                errors.append(
                    f"optional-routing: trigger '{trigger}' not in {skill} description"
                )

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    opt_count = len(optional_desc)
    print(
        f"OK: router integrity ({len(routed)} routed skills, "
        f"{opt_count} optional SKILL.md, optional triggers checked)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
