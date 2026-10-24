#!/usr/bin/env python3
"""Validate MayorGPT repo structure. Stdlib only.

Checks:
  * SKILL.md frontmatter (name matches directory, description present)
  * agent / prompt frontmatter and required sections
  * duplicate names within agents, prompts and skills
  * internal Markdown links resolve
  * README / catalog counts match the filesystem

Usage: python scripts/validate_repo.py [--root PATH] [--skip links,counts,...]
Exit code 0 when clean, 1 when any problem is found.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mayorgpt_common import REPO_ROOT, parse_frontmatter, sections  # noqa: E402

AGENT_SECTIONS = ["Mission", "Best used for", "Typical deliverables", "Operating workflow",
                  "Guardrails", "Portable system prompt"]
PROMPT_SECTIONS = ["Use when", "Inputs to gather", "Expected output", "Copy/paste prompt"]
SKIP_FILES = {"README.md", "SOURCE_NOTES.md"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)>?")


def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()


def md_files(root: Path):
    for p in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(p.relative_to(root).parts):
            continue
        yield p


def entity_files(root: Path, kind: str) -> list[Path]:
    base = root / kind
    if not base.is_dir():
        return []
    return [p for p in sorted(base.rglob("*.md"))
            if p.name not in SKIP_FILES and p.parent != base]


def skill_files(root: Path) -> list[Path]:
    base = root / "skills"
    return sorted(base.rglob("SKILL.md")) if base.is_dir() else []


def check_skills(root: Path, errors: list[str]):
    for p in skill_files(root):
        r = rel(root, p)
        meta, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not meta:
            errors.append(f"{r}: missing or malformed YAML frontmatter")
            continue
        if meta.get("name") != p.parent.name:
            errors.append(f"{r}: frontmatter name {meta.get('name')!r} does not match directory {p.parent.name!r}")
        if not str(meta.get("description", "")).strip():
            errors.append(f"{r}: missing description in frontmatter")


def check_entities(root: Path, kind: str, etype: str, required: list[str], errors: list[str]):
    for p in entity_files(root, kind):
        r = rel(root, p)
        meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not meta:
            errors.append(f"{r}: missing or malformed YAML frontmatter")
            continue
        if meta.get("name") != p.stem:
            errors.append(f"{r}: frontmatter name {meta.get('name')!r} does not match filename {p.stem!r}")
        if meta.get("type") != etype:
            errors.append(f"{r}: frontmatter type should be {etype!r}, got {meta.get('type')!r}")
        if not str(meta.get("title", "")).strip():
            errors.append(f"{r}: missing title in frontmatter")
        if meta.get("category") != p.parent.name:
            errors.append(f"{r}: category {meta.get('category')!r} does not match folder {p.parent.name!r}")
        secs = sections(body)
        for s in required:
            if s not in secs:
                errors.append(f"{r}: missing required section '## {s}'")
            elif not secs[s].strip():
                errors.append(f"{r}: section '## {s}' is empty")


def check_duplicates(root: Path, errors: list[str]):
    seen: dict[str, dict[str, list[str]]] = {}
    for kind, files in (("agent", entity_files(root, "agents")),
                        ("prompt", entity_files(root, "prompts")),
                        ("skill", skill_files(root))):
        names = defaultdict(list)
        for p in files:
            meta, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
            names[meta.get("name", p.stem if kind != "skill" else p.parent.name)].append(rel(root, p))
        seen[kind] = names
        for n, paths in names.items():
            if len(paths) > 1:
                errors.append(f"duplicate {kind} name {n!r}: " + ", ".join(paths))


def strip_code(text: str) -> str:
    text = re.sub(r"(?ms)^(```|~~~).*?^\1[^\n]*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def check_links(root: Path, errors: list[str]):
    for p in md_files(root):
        text = strip_code(p.read_text(encoding="utf-8"))
        for m in list(LINK_RE.finditer(text)) + list(IMG_RE.finditer(text)):
            target = m.group(1)
            if re.match(r"^([a-zA-Z][a-zA-Z0-9+.-]*:|#|//)", target):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            dest = (root / path_part.lstrip("/")) if path_part.startswith("/") else (p.parent / path_part)
            if not dest.exists():
                errors.append(f"{rel(root, p)}: broken link -> {target}")


COUNT_RE = re.compile(r"\*\*(\d+)\s+(?:[A-Za-z-]+\s+){0,3}?(agents?|prompts?|skills?|stacks?)\*\*", re.I)


def actual_counts(root: Path) -> dict[str, int]:
    stacks = root / "stacks"
    return {
        "agent": len(entity_files(root, "agents")),
        "prompt": len(entity_files(root, "prompts")),
        "skill": len(skill_files(root)),
        "stack": len(list(stacks.glob("*-stack.md"))) if stacks.is_dir() else 0,
    }


def check_counts(root: Path, errors: list[str]):
    actual = actual_counts(root)
    for name in ("README.md", "agents/README.md", "prompts/README.md", "skills/README.md",
                 "stacks/README.md"):
        p = root / name
        if not p.is_file():
            continue
        for m in COUNT_RE.finditer(p.read_text(encoding="utf-8")):
            kind = m.group(2).lower().rstrip("s")
            if int(m.group(1)) != actual[kind]:
                errors.append(f"{name}: states {m.group(1)} {kind}s but filesystem has {actual[kind]}")
    cat = root / "catalog"
    if not cat.is_dir():
        return
    for kind, key in (("agent", "agents"), ("prompt", "prompts"), ("skill", "skills")):
        jp = cat / f"{key}.json"
        if jp.is_file():
            n = len(json.loads(jp.read_text(encoding="utf-8")))
            if n != actual[kind]:
                errors.append(f"catalog/{key}.json: has {n} entries but filesystem has {actual[kind]} (run scripts/build_catalog.py)")
    sp = cat / "summary.json"
    if sp.is_file():
        s = json.loads(sp.read_text(encoding="utf-8"))
        for kind, key in (("agent", "agents"), ("prompt", "prompts"), ("skill", "skills"), ("stack", "stacks")):
            if s.get(key) != actual[kind]:
                errors.append(f"catalog/summary.json: {key}={s.get(key)} but filesystem has {actual[kind]}")
    cr = cat / "README.md"
    if cr.is_file():
        for key, kind in (("Agents", "agent"), ("Prompts", "prompt"), ("Skills", "skill")):
            m = re.search(rf"(?m)^- {key}: (\d+)", cr.read_text(encoding="utf-8"))
            if m and int(m.group(1)) != actual[kind]:
                errors.append(f"catalog/README.md: {key} count {m.group(1)} but filesystem has {actual[kind]}")


CHECKS = {
    "skills": lambda r, e: check_skills(r, e),
    "agents": lambda r, e: check_entities(r, "agents", "agent", AGENT_SECTIONS, e),
    "prompts": lambda r, e: check_entities(r, "prompts", "prompt", PROMPT_SECTIONS, e),
    "duplicates": check_duplicates,
    "links": check_links,
    "counts": check_counts,
}


def validate(root: Path, skip: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    for name, fn in CHECKS.items():
        if skip and name in skip:
            continue
        fn(root, errors)
    return errors


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=REPO_ROOT)
    ap.add_argument("--skip", default="", help="comma-separated checks to skip: " + ",".join(CHECKS))
    args = ap.parse_args(argv)
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}
    errors = validate(args.root, skip)
    if errors:
        print(f"Validation FAILED with {len(errors)} problem(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    c = actual_counts(args.root)
    print(f"OK: {c['agent']} agents, {c['prompt']} prompts, {c['skill']} skills, {c['stack']} stacks validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
