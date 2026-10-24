"""Shared helpers for MayorGPT repo tooling (stdlib only)."""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse a minimal YAML frontmatter block. Returns (meta, body).

    Supports `key: value` scalars and `key:` followed by `- item` lists.
    Returns ({}, text) when there is no frontmatter.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    current_list = None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and current_list is not None:
            meta[current_list].append(_unquote(item.group(1).strip()))
            continue
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            if val == "":
                meta[key] = []
                current_list = key
            else:
                meta[key] = _unquote(val)
                current_list = None
    return meta, m.group(2)


def _unquote(val: str) -> str:
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        return val[1:-1]
    return val


def sections(body: str) -> dict[str, str]:
    """Map '## Heading' -> section text (until the next '## ' heading)."""
    out: dict[str, str] = {}
    current = None
    buf: list[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if current is not None:
                out[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf).strip()
    return out


def bullets(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^\s*[-*]\s+(.*)$", text, re.M)]


def flatten(text: str) -> str:
    return " ".join(line.strip() for line in text.splitlines() if line.strip())


def readme_folder_order(readme: Path) -> list[str]:
    """Category order from a 'Browse by folder:' bullet list in a README."""
    if not readme.is_file():
        return []
    order, seen = [], False
    for line in readme.read_text(encoding="utf-8").splitlines():
        if "Browse by folder" in line:
            seen = True
            continue
        if seen:
            m = re.match(r"^\s*-\s+`?([a-z0-9-]+)`?\s*$", line)
            if m:
                order.append(m.group(1))
            elif order:
                break
    return order


def title_from_name(name: str) -> str:
    return " ".join(w.capitalize() for w in name.split("-"))
