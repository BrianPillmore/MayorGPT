# MayorGPT

MayorGPT is an open-source collection of AI agents, prompts, and skills designed specifically for mayors,
city council members, city managers, clerks, attorneys, department directors, and municipal consultants.

It is built to help city leaders move faster on real work: agenda packets, ordinances, budget analysis,
capital planning, constituent response, zoning cases, procurement, grants, emergency communication, and
the month-to-month rhythm of local government.

## What is in this repo?

- **40 role agents** that mirror typical city hall roles and outside advisors.
- **85 reusable prompts** covering the full lifecycle of mayor/council/staff work.
- **95 portable skills**, each a `SKILL.md` instruction folder that is also readable as plain Markdown.
- A **context-pack system** for layering in city-specific charter, code, and local norms as a configuration overlay.
- **15 curated stacks**, **evaluation rubrics**, **worked examples**, and **integration notes** so the repo is GitHub-ready and actually usable.

## Design goals

MayorGPT is built around five goals:

1. **Municipal realism** – it mirrors real city roles, approvals, meeting cycles, and review gates.
2. **Model portability** – everything is plain Markdown that any major LLM can read.
3. **Works with any capable model** – prompts use XML-style tagged blocks that work well across models, and no vendor-specific syntax is required.
4. **Process integrity** – drafts should surface legal, fiscal, HR, procurement, and public-process review needs.
5. **Public trust** – outputs should be calm, clear, practical, and fit for government use.

## Repository map

```text
MayorGPT/
├── agents/                 # 40 role-based municipal agents
├── prompts/                # 85 reusable prompts by cadence and function
├── skills/                 # 95 portable SKILL.md skill directories
├── context-packs/          # city-specific overlays (add your city folder here)
├── stacks/                 # recommended combinations for common workflows
├── docs/                   # architecture, safety, research, portability, model choice, deployment
├── evals/                  # review rubrics
├── integrations/           # per-platform guides, API CLI, skills installer
├── scripts/                # validation and export_bundle.py
└── catalog/                # JSON/CSV manifests
```

## Use it with any model

MayorGPT is plain Markdown. Any capable model can use it: paste an agent file as the system or
instructions text, paste a prompt file as the task, and attach your source material. Each platform
differs in how it accepts instructions and files, so check that platform's current documentation.

| Platform | Guide |
|---|---|
| All platforms (index and matrix) | [integrations/README.md](integrations/README.md) |
| Provider-agnostic API command line | [integrations/api/README.md](integrations/api/README.md) |
| ChatGPT / OpenAI | [integrations/chatgpt/README.md](integrations/chatgpt/README.md) |
| Google Gemini | [integrations/gemini/README.md](integrations/gemini/README.md) |
| Grok | [integrations/grok/README.md](integrations/grok/README.md) |
| Microsoft Copilot | [integrations/microsoft-copilot/README.md](integrations/microsoft-copilot/README.md) |
| Mistral | [integrations/mistral/README.md](integrations/mistral/README.md) |
| Local / open-weight models (Llama, Qwen, DeepSeek, others) | [integrations/local-models/README.md](integrations/local-models/README.md) |
| Coding assistants and agentic tools | [integrations/coding-assistants/README.md](integrations/coding-assistants/README.md) |
| Other assistants (Perplexity and more) | [integrations/other-assistants/README.md](integrations/other-assistants/README.md) |
| Skills installer | [integrations/skills-installer/README.md](integrations/skills-installer/README.md) |
| Assemble a bundle by hand | [integrations/generic/assembly-guide.md](integrations/generic/assembly-guide.md) |
| Tyler Munis pairing | [integrations/tyler-munis/README.md](integrations/tyler-munis/README.md) |

### The basic workflow
1. Pick a local context pack or create your own.
2. Pick one file from `agents/` (system or instructions text).
3. Pick one file from `prompts/` (the task).
4. Attach your source material: charter, code, budget pages, staff report examples.
5. Ask the model for:
   - the draft,
   - a missing-information list,
   - a risk/process list,
   - and recommended next steps.

To build a ready-to-paste bundle, use `python scripts/export_bundle.py` (formats: text, markdown,
openai-messages, gemini, custom-gpt, all; use `--skills` to include skills and `--list` to see what is
available). Agent tools also read the root `AGENTS.md`.

### Choosing and deploying
- [docs/model-portability.md](docs/model-portability.md) – what is portable and what to adapt per model.
- [docs/choosing-a-model.md](docs/choosing-a-model.md) – capability checklist for city use.
- [docs/deployment-and-data-options.md](docs/deployment-and-data-options.md) – consumer, enterprise, government cloud, or self-hosted; records and data implications.
- [docs/cross-model-evaluation.md](docs/cross-model-evaluation.md) – compare models on your own tasks.

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
These are action-oriented instruction bundles written as portable `SKILL.md` instruction folders.
Tools that load skill folders can use them directly; with any other model, paste the file contents
into the conversation.

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
