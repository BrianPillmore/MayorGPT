#!/usr/bin/env python3
"""Export a MayorGPT agent (+ prompt, context pack, skills) as a portable bundle.

Works with any chat model or platform: the output is plain text or a small JSON
document you can paste, upload, or send to any provider. Stdlib only. No network.

Formats
  text           one pasteable system prompt (default)
  markdown       the same content as a readable Markdown document
  openai-messages  JSON {"messages": [...]} for any OpenAI-compatible chat API
  gemini         JSON {"system_instruction": ..., "contents": [...]} for generateContent
  custom-gpt     instructions trimmed to fit a character limit, plus knowledge files
  all            every format, written to dist/<agent>/

Examples
  python scripts/export_bundle.py --list
  python scripts/export_bundle.py --agent city-manager > system-prompt.txt
  python scripts/export_bundle.py --agent city-manager --prompt executive-brief \\
      --context-pack sample-springfield-example --format markdown
  python scripts/export_bundle.py --agent finance-director-budget-officer \\
      --skills budget-variance-analysis --format openai-messages --user "Explain Q2 variances."
  python scripts/export_bundle.py --agent mayor --format custom-gpt --out dist/mayor-gpt
  python scripts/export_bundle.py --agent city-clerk --format all
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mayorgpt_common import REPO_ROOT, parse_frontmatter, sections as md_sections  # noqa: E402

FORMATS = ("text", "markdown", "openai-messages", "gemini", "custom-gpt", "all")
SKIP_NAMES = {"README.md", "SOURCE_NOTES.md"}
CUSTOM_GPT_LIMIT = 8000          # characters; check your platform's current limit
LARGE_PROMPT_CHARS = 48000       # warn above this (roughly 12k tokens)
USER_PLACEHOLDER = "[YOUR REQUEST HERE]"

OPERATING_RULES = (
    "Produce a working draft for human review. List missing information, "
    "legal/process/fiscal flags, and recommended next steps. Do not invent facts, "
    "citations, or dollar amounts; mark anything unverified. Do not request or "
    "retain protected personal data beyond what the task needs."
)

# Tags of the agent's portable XML block, dropped first-to-last when trimming.
TRIM_ORDER = ["handoffs", "inputs-to-request", "core-work", "escalation-triggers",
              "working-style", "quality-check"]


class BundleError(Exception):
    """A user-facing problem (unknown name, bad option)."""


@dataclass
class Section:
    title: str
    body: str


# --------------------------------------------------------------------------- lookup

def strip_frontmatter(text: str) -> str:
    return parse_frontmatter(text)[1].strip()


def _entity_paths(root: Path, kind: str) -> list[Path]:
    base = root / kind
    if not base.is_dir():
        return []
    return [p for p in sorted(base.rglob("*.md")) if p.name not in SKIP_NAMES and p.parent != base]


def skill_paths(root: Path) -> list[Path]:
    base = root / "skills"
    return sorted(base.rglob("SKILL.md")) if base.is_dir() else []


def pack_names(root: Path) -> list[str]:
    base = root / "context-packs"
    if not base.is_dir():
        return []
    return [d.name for d in sorted(base.iterdir()) if (d / "README.md").is_file()]


def find_entity(root: Path, kind: str, name: str) -> Path:
    matches = [p for p in _entity_paths(root, kind) if p.stem == name]
    if not matches:
        raise BundleError(f"no {kind[:-1]} named '{name}' (try --list)")
    if len(matches) > 1:
        raise BundleError(f"'{name}' is ambiguous: " + ", ".join(str(m) for m in matches))
    return matches[0]


def find_skill(root: Path, name: str) -> Path:
    matches = [p for p in skill_paths(root) if p.parent.name == name]
    if not matches:
        raise BundleError(f"no skill named '{name}' (try --list)")
    return matches[0]


def split_names(values: list[str] | None) -> list[str]:
    out: list[str] = []
    for v in values or []:
        out.extend(x.strip() for x in v.split(",") if x.strip())
    return out


# --------------------------------------------------------------------------- assembly

def portable_block(body: str) -> str | None:
    """The fenced block under '## Portable system prompt', if any."""
    sec = md_sections(body).get("Portable system prompt", "")
    m = re.search(r"```[a-zA-Z]*\n(.*?)\n```", sec, re.S)
    return m.group(1).strip() if m else None


def agent_text(path: Path, mode: str) -> str:
    body = strip_frontmatter(path.read_text(encoding="utf-8"))
    if mode == "portable":
        return portable_block(body) or body
    return body


def skill_section(path: Path) -> Section:
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    name = meta.get("name", path.parent.name)
    desc = meta.get("description", "")
    text = f"{desc}\n\n{body.strip()}" if desc else body.strip()
    return Section(f"SKILL: {name}", text)


def resolve_skills(root: Path, names: list[str], categories: list[str]) -> list[Path]:
    found: list[Path] = []
    for n in names:
        found.append(find_skill(root, n))
    for c in categories:
        d = root / "skills" / c
        if not d.is_dir():
            raise BundleError(f"no skill category '{c}' (try --list)")
        found.extend(sorted(d.glob("*/SKILL.md")))
    seen, uniq = set(), []
    for p in found:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def build_sections(root: Path, agent: str, prompt: str | None = None,
                   context_pack: str | None = None, skills: list[str] | None = None,
                   skill_categories: list[str] | None = None,
                   agent_mode: str = "full") -> list[Section]:
    out = [Section("ROLE", agent_text(find_entity(root, "agents", agent), agent_mode))]
    if context_pack:
        pack = root / "context-packs" / context_pack / "README.md"
        if not pack.is_file():
            raise BundleError(f"context pack not found: {context_pack} (try --list)")
        out.append(Section("CITY CONTEXT PACK", strip_frontmatter(pack.read_text(encoding="utf-8"))))
    if prompt:
        p = find_entity(root, "prompts", prompt)
        out.append(Section("TASK PLAYBOOK", strip_frontmatter(p.read_text(encoding="utf-8"))))
    for sp in resolve_skills(root, skills or [], skill_categories or []):
        out.append(skill_section(sp))
    out.append(Section("OPERATING RULES", OPERATING_RULES))
    return out


# --------------------------------------------------------------------------- renderers

def estimate_tokens(text: str) -> int:
    """Very rough estimate (about 4 characters per token for English prose)."""
    return (len(text) + 3) // 4


def render_text(secs: list[Section]) -> str:
    return "\n\n---\n\n".join(f"# {s.title}\n\n{s.body}" for s in secs) + "\n"


def render_markdown(secs: list[Section], agent: str) -> str:
    parts = [f"# MayorGPT bundle: {agent}\n"]
    for s in secs:
        # demote headings inside the body so the bundle keeps a single outline
        body = re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", s.body)
        parts.append(f"## {s.title}\n\n{body}\n")
    return "\n".join(parts)


def render_openai(system: str, user: str | None) -> str:
    return json.dumps({"messages": [
        {"role": "system", "content": system.rstrip("\n")},
        {"role": "user", "content": user or USER_PLACEHOLDER},
    ]}, indent=2, ensure_ascii=False) + "\n"


def render_gemini(system: str, user: str | None) -> str:
    return json.dumps({
        "system_instruction": {"parts": [{"text": system.rstrip("\n")}]},
        "contents": [{"role": "user", "parts": [{"text": user or USER_PLACEHOLDER}]}],
    }, indent=2, ensure_ascii=False) + "\n"


def _split_tags(block: str) -> tuple[list[tuple[str, str]], str]:
    """Split an XML-ish block into [(tag, full_text)] top-level elements."""
    items = [(m.group(1), m.group(0)) for m in
             re.finditer(r"<([a-z][a-z0-9-]*)>.*?</\1>", block, re.S)]
    return items, block


def _fit_xml(block: str, limit: int) -> str:
    items, _ = _split_tags(block)
    if not items:
        return block
    keep = list(items)
    for tag in TRIM_ORDER:
        if len("\n\n".join(t for _, t in keep)) <= limit:
            break
        keep = [(n, t) for n, t in keep if n != tag]
    return "\n\n".join(t for _, t in keep)


def _fit_markdown(body: str, limit: int) -> str:
    secs = md_sections(body)
    priority = ["Mission", "Authority and limits", "Guardrails", "Escalation triggers",
                "Operating workflow", "Red flags to watch for", "Best used for",
                "Typical deliverables", "Inputs to request", "Handoffs"]
    chosen: list[str] = []
    for name in priority:
        if name in secs:
            candidate = chosen + [name]
            text = "\n\n".join(f"## {n}\n\n{secs[n]}" for n in candidate)
            if len(text) <= limit:
                chosen = candidate
    return "\n\n".join(f"## {n}\n\n{secs[n]}" for n in chosen)


def render_custom_gpt(root: Path, agent: str, prompt: str | None, context_pack: str | None,
                      skills: list[Path], limit: int = CUSTOM_GPT_LIMIT
                      ) -> tuple[str, dict[str, str], list[str]]:
    """Return (instructions, {knowledge filename: content}, warnings)."""
    warnings: list[str] = []
    apath = find_entity(root, "agents", agent)
    body = strip_frontmatter(apath.read_text(encoding="utf-8"))
    core = portable_block(body)
    knowledge: dict[str, str] = {}
    knowledge[f"role-{agent}-full.md"] = body + "\n"
    refs = [f"role-{agent}-full.md (complete role definition)"]
    if context_pack:
        pack = root / "context-packs" / context_pack / "README.md"
        if not pack.is_file():
            raise BundleError(f"context pack not found: {context_pack} (try --list)")
        knowledge[f"context-pack-{context_pack}.md"] = strip_frontmatter(pack.read_text(encoding="utf-8")) + "\n"
        refs.append(f"context-pack-{context_pack}.md (city facts: use as the source of local context)")
    if prompt:
        p = find_entity(root, "prompts", prompt)
        knowledge[f"playbook-{prompt}.md"] = strip_frontmatter(p.read_text(encoding="utf-8")) + "\n"
        refs.append(f"playbook-{prompt}.md (task playbook: follow it when the user asks for this task)")
    for sp in skills:
        s = skill_section(sp)
        fname = f"skill-{sp.parent.name}.md"
        knowledge[fname] = f"# {s.title}\n\n{s.body}\n"
        refs.append(f"{fname} (skill instructions)")

    head = "# ROLE\n\n"
    ref_text = ("\n\n# KNOWLEDGE FILES\n\nThe uploaded knowledge files hold fuller detail. Consult them "
                "before answering and say when an answer relies on them:\n"
                + "\n".join(f"- {r}" for r in refs))
    rules = "\n\n# OPERATING RULES\n\n" + OPERATING_RULES
    overhead = len(head) + len(ref_text) + len(rules)
    budget = max(limit - overhead, 0)
    if core:
        fitted = core if len(core) <= budget else _fit_xml(core, budget)
    else:
        fitted = _fit_markdown(body, budget)
    if len(fitted) > budget:
        cut = fitted[:budget].rsplit("\n", 1)[0]
        fitted = cut + "\n[trimmed: see role file in knowledge]"
        warnings.append("role text was hard-truncated to fit; rely on the knowledge file")
    elif core and fitted != core:
        warnings.append("lower-priority role sections were moved to the knowledge file to fit the limit")
    instructions = head + fitted + ref_text + rules
    if len(instructions) > limit:  # reference list itself too long
        instructions = instructions[:limit].rsplit("\n", 1)[0]
        warnings.append("knowledge listing was truncated in the instructions; see KNOWLEDGE.md")
    return instructions + "\n", knowledge, warnings


def knowledge_listing(agent: str, knowledge: dict[str, str]) -> str:
    lines = [f"# Knowledge files for {agent}", "",
             "Upload these files to the platform's knowledge / file area, then paste "
             "`instructions.txt` into the instructions field.", ""]
    for name, text in knowledge.items():
        lines.append(f"- `{name}` ({len(text):,} characters, about {estimate_tokens(text):,} tokens)")
    lines += ["", "Check the platform's current file-count and size limits before uploading.", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------- warnings

def size_warnings(text: str, label: str = "output") -> list[str]:
    w = [f"{label}: {len(text):,} characters, about {estimate_tokens(text):,} tokens (rough estimate)"]
    if len(text) > LARGE_PROMPT_CHARS:
        w.append("warning: this is a large prompt; consider dropping skills or the playbook, "
                 "or use a model with a longer context window")
    return w


# --------------------------------------------------------------------------- listing

def listing(root: Path, kind: str = "all") -> str:
    lines: list[str] = []
    if kind in ("all", "agents"):
        lines.append("agents:")
        lines += [f"  {p.stem}  ({p.parent.name})" for p in _entity_paths(root, "agents")]
    if kind in ("all", "prompts"):
        lines.append("prompts:")
        lines += [f"  {p.stem}  ({p.parent.name})" for p in _entity_paths(root, "prompts")]
    if kind in ("all", "skills"):
        lines.append("skills:")
        lines += [f"  {p.parent.name}  ({p.parent.parent.name})" for p in skill_paths(root)]
    if kind in ("all", "context-packs"):
        lines.append("context-packs:")
        lines += [f"  {n}" for n in pack_names(root)]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- main

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_user(args) -> str | None:
    user = args.user
    for f in args.attach:
        p = Path(f)
        if not p.is_file():
            raise BundleError(f"attachment not found: {f}")
        user = (user or "") + f"\n\n--- ATTACHMENT: {p.name} ---\n" + p.read_text(encoding="utf-8")
    return user


def export(args) -> int:
    root = args.root
    skills = split_names(args.skills)
    cats = split_names(args.skill_category)
    user = read_user(args)
    fmt = args.format
    mode = args.agent_mode
    if mode == "auto":
        mode = "portable"

    def sections_for(m: str) -> list[Section]:
        return build_sections(root, args.agent, args.prompt, args.context_pack, skills, cats, m)

    if fmt == "all":
        out = args.out or (root / "dist" / args.agent)
        full = sections_for(mode)
        system = render_text(full)
        write(out / "system-prompt.txt", system)
        write(out / "bundle.md", render_markdown(full, args.agent))
        write(out / "openai-messages.json", render_openai(system, user))
        write(out / "gemini.json", render_gemini(system, user))
        ins, know, cw = render_custom_gpt(root, args.agent, args.prompt, args.context_pack,
                                          resolve_skills(root, skills, cats))
        write(out / "custom-gpt" / "instructions.txt", ins)
        for n, t in know.items():
            write(out / "custom-gpt" / "knowledge" / n, t)
        write(out / "custom-gpt" / "KNOWLEDGE.md", knowledge_listing(args.agent, know))
        for line in size_warnings(system, "system prompt") + cw:
            print(line, file=sys.stderr)
        print(f"custom-gpt instructions: {len(ins):,} characters", file=sys.stderr)
        print(f"wrote bundle to {out}", file=sys.stderr)
        return 0

    if fmt == "custom-gpt":
        ins, know, cw = render_custom_gpt(root, args.agent, args.prompt, args.context_pack,
                                          resolve_skills(root, skills, cats), args.limit)
        listing_md = knowledge_listing(args.agent, know)
        if args.out:
            out = args.out
            write(out / "instructions.txt", ins)
            for n, t in know.items():
                write(out / "knowledge" / n, t)
            write(out / "KNOWLEDGE.md", listing_md)
            print(f"wrote {out}", file=sys.stderr)
        else:
            sys.stdout.write(ins)
            print("\n" + listing_md, file=sys.stderr)
        print(f"instructions: {len(ins):,} characters (limit {args.limit:,})", file=sys.stderr)
        for line in cw:
            print("warning: " + line, file=sys.stderr)
        return 0

    secs = sections_for(mode)
    system = render_text(secs)
    if fmt == "text":
        text = system
    elif fmt == "markdown":
        text = render_markdown(secs, args.agent)
    elif fmt == "openai-messages":
        text = render_openai(system, user)
    else:
        text = render_gemini(system, user)
    if args.out:
        write(args.out, text)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    for line in size_warnings(system, "system prompt"):
        print(line, file=sys.stderr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("--root", type=Path, default=REPO_ROOT, help="repo root (default: this repo)")
    ap.add_argument("--list", nargs="?", const="all",
                    choices=["all", "agents", "prompts", "skills", "context-packs"],
                    help="list available names and exit")
    ap.add_argument("--agent", help="agent name, e.g. city-manager")
    ap.add_argument("--prompt", help="prompt (task playbook) name, e.g. executive-brief")
    ap.add_argument("--context-pack", help="folder name under context-packs/")
    ap.add_argument("--skills", action="append", help="skill names, comma-separated (repeatable)")
    ap.add_argument("--skill-category", action="append", help="include every skill in a category")
    ap.add_argument("--format", choices=FORMATS, default="text")
    ap.add_argument("--agent-mode", choices=["auto", "full", "portable"], default="auto",
                    help="auto/portable: the agent's portable system prompt block (default); full: the whole agent file")
    ap.add_argument("--user", help="user message for JSON formats")
    ap.add_argument("--attach", action="append", default=[], help="text file appended to the user message")
    ap.add_argument("--out", type=Path, help="output file (or directory for custom-gpt / all)")
    ap.add_argument("--limit", type=int, default=CUSTOM_GPT_LIMIT,
                    help="character limit for custom-gpt instructions (default %(default)s)")
    args = ap.parse_args(argv)
    try:
        if args.list:
            sys.stdout.write(listing(args.root, args.list))
            return 0
        if not args.agent:
            ap.error("--agent is required (or use --list)")
        return export(args)
    except BundleError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
