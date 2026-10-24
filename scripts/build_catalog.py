#!/usr/bin/env python3
"""Regenerate catalog/{agents,prompts,skills}.{json,csv} and catalog/summary.json.

Usage:
    python scripts/build_catalog.py            # write files
    python scripts/build_catalog.py --check    # exit 1 if catalog is out of date

Stdlib only. Output is deterministic, so running it twice changes nothing.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mayorgpt_common import (  # noqa: E402
    REPO_ROOT, bullets, flatten, parse_frontmatter, readme_folder_order,
    sections, title_from_name,
)

SKIP_NAMES = {"README.md", "SOURCE_NOTES.md"}


def _order_key(order: list[str]):
    def key(rec: dict):
        cat = rec["category"]
        idx = order.index(cat) if cat in order else len(order)
        return (idx, cat, rec["name"])
    return key


def _md_files(root: Path):
    for p in sorted(root.rglob("*.md")):
        if p.name in SKIP_NAMES or p.parent == root:
            continue
        yield p


def collect_agents(root: Path) -> list[dict]:
    base = root / "agents"
    recs = []
    for p in _md_files(base):
        meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not meta:
            continue
        sec = sections(body)
        name = meta.get("name", p.stem)
        recs.append({
            "name": name,
            "title": meta.get("title", title_from_name(name)),
            "category": meta.get("category", p.parent.name),
            "best_for": bullets(sec.get("Best used for", "")),
            "deliverables": bullets(sec.get("Typical deliverables", "")),
        })
    recs.sort(key=_order_key(readme_folder_order(base / "README.md")))
    return recs


def collect_prompts(root: Path) -> list[dict]:
    base = root / "prompts"
    recs = []
    for p in _md_files(base):
        meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not meta:
            continue
        sec = sections(body)
        name = meta.get("name", p.stem)
        recs.append({
            "name": name,
            "title": meta.get("title", title_from_name(name)),
            "category": meta.get("category", p.parent.name),
            "use_when": flatten(sec.get("Use when", "")),
            "output": flatten(sec.get("Expected output", "")),
        })
    recs.sort(key=_order_key(readme_folder_order(base / "README.md")))
    return recs


def collect_skills(root: Path) -> list[dict]:
    base = root / "skills"
    recs = []
    for p in sorted(base.rglob("SKILL.md")):
        meta, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        name = meta.get("name", p.parent.name)
        hint = meta.get("argument-hint", "")
        if hint.startswith("[") and hint.endswith("]"):
            hint = hint[1:-1]
        recs.append({
            "name": name,
            "title": title_from_name(name),
            "category": p.parent.parent.name,
            "description": meta.get("description", ""),
            "argument_hint": hint,
        })
    recs.sort(key=_order_key(readme_folder_order(base / "README.md")))
    return recs


def count_stacks(root: Path) -> int:
    d = root / "stacks"
    return len(list(d.glob("*-stack.md"))) if d.is_dir() else 0


def render_json(records) -> str:
    return json.dumps(records, indent=2, ensure_ascii=True) + "\n"


def render_csv(records: list[dict]) -> str:
    if not records:
        return ""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    fields = list(records[0].keys())
    w.writerow(fields)
    for r in records:
        w.writerow([", ".join(v) if isinstance(v, list) else v for v in (r[f] for f in fields)])
    return buf.getvalue()


def build(root: Path) -> dict[str, str]:
    """Return {relative catalog filename: content}."""
    data = {
        "agents": collect_agents(root),
        "prompts": collect_prompts(root),
        "skills": collect_skills(root),
    }
    out: dict[str, str] = {}
    for kind, recs in data.items():
        out[f"{kind}.json"] = render_json(recs)
        out[f"{kind}.csv"] = render_csv(recs)
    summary = {k: len(v) for k, v in data.items()}
    summary["stacks"] = count_stacks(root)
    out["summary.json"] = render_json(summary)
    readme = root / "catalog" / "README.md"
    if readme.is_file():
        out["README.md"] = update_readme_counts(readme.read_text(encoding="utf-8"), summary)
    return out


def update_readme_counts(text: str, summary: dict) -> str:
    """Rewrite the '- Agents: N' style count lines in catalog/README.md."""
    for key in ("agents", "prompts", "skills"):
        text = re.sub(rf"(?m)^(- {key.capitalize()}: )\d+\s*$", rf"\g<1>{summary[key]}", text)
    return text


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=REPO_ROOT, help="repo root")
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if catalog files differ")
    args = ap.parse_args(argv)

    cat_dir = args.root / "catalog"
    files = build(args.root)
    stale = []
    for name, content in files.items():
        path = cat_dir / name
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current != content:
            stale.append(name)
            if not args.check:
                cat_dir.mkdir(exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    if args.check:
        if stale:
            print("Catalog is out of date: " + ", ".join(stale), file=sys.stderr)
            print("Run: python scripts/build_catalog.py", file=sys.stderr)
            return 1
        print("Catalog is up to date.")
        return 0
    print("Updated: " + ", ".join(stale) if stale else "Catalog already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
