# AGENTS.md

Instructions for any AI tool or agent working with this repository. They are vendor-neutral and apply to every model and platform.

## What this repository is

MayorGPT is an open-source library of Markdown content for city and local government work: role agents, task prompts, reusable skills, workflow stacks and city context packs. It contains no application server. A small set of standard-library Python scripts validates and exports the content.

## Layout

| Path | Contents |
|---|---|
| `agents/<category>/<name>.md` | Role definitions. Front matter, then Mission, Best used for, Typical deliverables, Operating workflow, Guardrails and a `Portable system prompt` block. |
| `prompts/<category>/<name>.md` | Task playbooks with a `Copy/paste prompt` block (XML-style tags, bracketed placeholders). |
| `skills/<category>/<name>/SKILL.md` | Reusable procedures. Front matter `name` must equal the folder name; `description` is required. |
| `stacks/` | Multi-step workflows that combine agents, prompts and skills. |
| `context-packs/` | City-specific facts. `TEMPLATE/` is the starting point; `sample-springfield-example/` is fictional. |
| `catalog/` | Generated indexes. Never edit by hand; run `python scripts/build_catalog.py`. |
| `scripts/` | `validate_repo.py`, `build_catalog.py`, `export_bundle.py`. |
| `integrations/` | Platform guides, the provider-agnostic API client, the skills installer. |
| `tests/` | pytest suite (no network needed). |

## How to behave when using the content

- Treat every output as a working draft for human review. Do not present anything as a legal, fiscal, HR or procedural determination.
- Do not invent facts, citations, statutes, case names, code sections, or dollar amounts. Mark anything unverified. State law and local charters vary: flag the variance.
- Ask for missing information. End substantive work with a missing-information list, legal/process/fiscal flags and recommended next steps.
- Stay within the role's authority and escalation triggers. Hand off to the roles named in the agent's Handoffs section.
- Keep protected data out of prompts and files: SSNs, payroll and benefits detail, sealed records, privileged legal advice, resident personal data. Use fictional or redacted examples.
- Remain politically neutral in administration roles; give options when policy direction is unsettled.

## How to behave when editing the repository

1. Edit Markdown directly; keep the existing section names and front matter keys, since the validator checks them.
2. After changes run:
   ```bash
   python scripts/build_catalog.py
   python scripts/validate_repo.py
   pytest tests
   ```
3. Do not hard-code model identifiers, vendor-specific assumptions or secrets anywhere. Models and keys come from environment variables or flags.
4. Keep content vendor-neutral. Platform-specific notes belong under `integrations/`.
5. Use plain language, short paragraphs and relative links. Keep README count lines accurate.
6. The scripts use only the Python standard library; do not add runtime dependencies.

## Using the content

```bash
python scripts/export_bundle.py --list
python scripts/export_bundle.py --agent city-manager --prompt executive-brief \
  --context-pack sample-springfield-example --format text
```

See `integrations/README.md` for per-platform guides.
