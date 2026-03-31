# MayorGPT

MayorGPT is an open-source collection of AI agents, prompts, and skills designed specifically for mayors,
city council members, city managers, clerks, attorneys, department directors, and municipal consultants.

It is built to help city leaders move faster on real work: agenda packets, ordinances, budget analysis,
capital planning, constituent response, zoning cases, procurement, grants, emergency communication, and
the month-to-month rhythm of local government.

## What is in this repo?

- **34 role agents** that mirror typical city hall roles and outside advisors.
- **73 reusable prompts** covering the full lifecycle of mayor/council/staff work.
- **82 Claude-compatible skills** using `SKILL.md` files that are also readable as plain Markdown.
- A **context-pack system** for layering in city-specific charter, code, and local norms as a configuration overlay.
- **11 curated stacks**, **evaluation rubrics**, **worked examples**, and **integration notes** so the repo is GitHub-ready and actually usable.

## Design goals

MayorGPT is built around five goals:

1. **Municipal realism** – it mirrors real city roles, approvals, meeting cycles, and review gates.
2. **Model portability** – everything is readable as plain Markdown for any major LLM.
3. **Claude-first ergonomics** – the prompt structure, XML blocks, and skills are especially strong for Claude.
4. **Process integrity** – drafts should surface legal, fiscal, HR, procurement, and public-process review needs.
5. **Public trust** – outputs should be calm, clear, practical, and fit for government use.

## Repository map

```text
MayorGPT/
├── agents/                 # 34 role-based municipal agents
├── prompts/                # 73 reusable prompts by cadence and function
├── skills/                 # 82 Claude-compatible SKILL.md skill directories
├── context-packs/          # city-specific overlays (add your city folder here)
├── stacks/                 # recommended combinations for common workflows
├── docs/                   # architecture, safety, research, and portability
├── evals/                  # review rubrics
├── integrations/           # Claude, generic, and Custom GPT integration notes
└── catalog/                # JSON/CSV manifests
```

## Quick start

### Generic model workflow
1. Pick a local context pack or create your own.
2. Pick one file from `agents/`.
3. Pick one file from `prompts/`.
4. Attach your source material.
5. Ask the model for:
   - the draft,
   - a missing-information list,
   - a risk/process list,
   - and recommended next steps.

### Claude workflow
1. Use an `agents/` file as your system prompt or project instruction layer.
2. Use a `prompts/` file as the task prompt.
3. Copy selected directories from `skills/` into `.claude/skills/` in your target project,
   or use the helper script in `integrations/claude-code/`.
4. Keep your city charter, code, agenda templates, budget pages, and staff report examples nearby.

## How to think about the content

### `agents/`
These are reusable role definitions. Each one includes:
- the mission of the role,
- best use cases,
- typical deliverables,
- guardrails,
- a portable system prompt block.

### `prompts/`
These are task prompts. They cover:
- daily executive and constituent work,
- weekly operating rhythm,
- monthly agenda/finance/reporting cycles,
- quarterly strategy and capital review,
- annual budget/audit/goal-setting work,
- elections and transitions,
- emergencies,
- legislation and procurement,
- HR and public engagement.

### `skills/`
These are action-oriented instruction bundles written in a Claude-compatible `SKILL.md` format.
They are the most Claude-native part of the repo, but they still work as plain instruction files on
other platforms.

## Recommended stacks

Start with one of the curated stacks in `stacks/`:

- `mayor-office-stack.md`
- `council-stack.md`
- `city-manager-stack.md`
- `budget-season-stack.md`
- `land-use-hearing-stack.md`
- `emergency-operations-stack.md`
- `public-safety-review-stack.md`
- `labor-and-personnel-stack.md`
- `grant-pursuit-stack.md`
- `intergovernmental-relations-stack.md`
- `fiscal-productivity-stack.md`

See `stacks/ORCHESTRATION_PROTOCOL.md` for how to coordinate multiple agents on the same decision.

## Review before official use

Always require human review for:
- ordinances and resolutions,
- contracts,
- legal analysis,
- personnel matters,
- budget adoption materials,
- public records responses,
- election materials,
- emergency proclamations,
- public-facing crisis statements.

## Start here

If you only open three places first, make them:
- `docs/usage-guide.md`
- `agents/`
- `skills/`

## About

MayorGPT was created by **Brian Pillmore**, Mayor of Yukon, Oklahoma. It grew out of real day-to-day
work in city hall — building AI workflows that respected municipal process, kept humans in the decision
seat, and held up to the scrutiny that comes with public office.

The goal was a toolkit grounded in how local government actually works, not how it looks from the outside.
If it is useful to other cities, mayors, managers, clerks, or staff, that is the point.

**Contact:** [brian@pillmoreforyukon.com](mailto:brian@pillmoreforyukon.com)

Contributions, feedback, and context packs from other cities are welcome. See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
