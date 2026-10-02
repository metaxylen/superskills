#!/usr/bin/env python3
"""Validate skills/*/SKILL.md frontmatter for superskills v1."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
ROUTING_TSV = Path(__file__).resolve().parent / "routing-triggers.tsv"
MAX_DESC = 1024
EXPECTED_COUNT = 16


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        raise ValueError("missing opening ---")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("missing closing ---")
    block = text[3:end].strip("\n")
    fields: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal key, buf
        if key is not None:
            folded = "\n".join(buf).strip()
            fields[key] = re.sub(r"\s+", " ", folded)
        key = None
        buf = []

    for line in block.splitlines():
        if line.startswith("  ") and key is not None:
            buf.append(line[2:].strip())
            continue
        flush()
        m = re.match(r"^([a-z0-9_-]+):\s*(.*)$", line)
        if not m:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key = m.group(1)
        rest = m.group(2)
        if rest in (">-", "|-", ">", "|"):
            buf = []
        elif rest:
            buf = [rest]
        else:
            buf = []
    flush()
    return fields


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())

    if len(skill_dirs) != EXPECTED_COUNT:
        errors.append(f"expected {EXPECTED_COUNT} skill dirs, found {len(skill_dirs)}")

    names: list[str] = []
    descriptions: dict[str, str] = {}

    for d in skill_dirs:
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{d.name}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        try:
            fm = parse_frontmatter(text)
        except ValueError as e:
            errors.append(f"{d.name}: {e}")
            continue

        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not name:
            errors.append(f"{d.name}: missing name")
            continue
        if name != d.name:
            errors.append(f"{d.name}: name '{name}' != folder name")
        if not desc:
            errors.append(f"{d.name}: missing description")
            continue
        if len(desc) > MAX_DESC:
            errors.append(f"{d.name}: description length {len(desc)} > {MAX_DESC}")
        lower = desc.lower()
        if "do not use" not in lower:
            errors.append(f"{d.name}: description must include 'Do not use'")
        if "turkish cues:" not in lower:
            errors.append(f"{d.name}: description must include 'Turkish cues:'")
        if not text.strip().split("---", 2)[2].strip():
            errors.append(f"{d.name}: empty body after frontmatter")

        names.append(name)
        descriptions[name] = desc

    if ROUTING_TSV.is_file():
        for line in ROUTING_TSV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                errors.append(f"routing-triggers.tsv: bad line: {line!r}")
                continue
            skill, trigger = parts[0].strip(), parts[1].strip()
            if skill not in descriptions:
                errors.append(f"routing: unknown skill {skill!r}")
                continue
            if trigger.lower() not in descriptions[skill].lower():
                errors.append(
                    f"routing: trigger '{trigger}' not in {skill} description"
                )

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(names)} skills validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
