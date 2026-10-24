# Contributing

Thanks for contributing to MayorGPT.

## What good contributions look like
- grounded in real municipal workflow,
- written in clear, inspectable Markdown,
- explicit about assumptions and review gates,
- reusable across cities,
- respectful of clerk/legal/finance/HR/public-process boundaries.

## Keep contributions model-agnostic
MayorGPT works with any capable model. Agents, prompts, and skills must not contain vendor-specific syntax,
product names as requirements, or frontmatter that assumes a particular model. Use plain Markdown, XML-style
tagged blocks, and bracketed placeholders. Put platform-specific setup in `integrations/`, never in the core files.

## Contribution ideas
- new city context packs,
- new role agents,
- new prompts for recurring municipal tasks,
- new skills for real city workflows,
- stronger evaluation rubrics,
- local adaptations for state-specific process.

## Before opening a PR
1. Check whether the issue already exists.
2. Keep role boundaries intact.
3. Include at least one example workflow.
4. If adding a legal/process-sensitive artifact, note the review points it should trigger.

## Style guide

General rules for everything in this repository:
- Write in plain, direct language. Prefer short sentences and active voice.
- Mark what is fact, assumption, and unknown. Do not invent statistics, quotes, or case law.
- Never fabricate legal citations. Name the type of authority to check (state statute, charter, local code) and tell the reader to confirm with the City Attorney.
- Flag state-law variance explicitly where open meetings, public records, procurement, labor, land use, elections, or utility rate rules are involved. Do not present one state's rule as national.
- Use fictional names, places, and numbers in examples. No real residents, employees, or officials.
- Link only to files that exist. Use repository-relative paths.
- Avoid partisan framing. Outputs should serve whoever holds the office.

### Skills (`skills/<category>/<skill-name>/SKILL.md`)
- Folder name is lowercase-hyphenated and matches the skill's `name`.
- Start with front matter: `name`, `description` (one sentence: what it produces and for whom), and `argument-hint` where useful.
- Follow the workflow convention: clarify the question, list the minimum source material, give numbered steps, state outputs, and name review gates.
- List required attachments explicitly and say what to do if they are missing (ask, do not assume).
- State the limits: what the skill cannot determine and who must review.
- Put templates or checklists in separate files in the skill folder and reference them.

### Agents (`agents/<group>/<role>.md`)
- Describe the role's authority and its limits. State what the role must refer upward or outward.
- Keep role boundaries intact: a Finance Director agent does not set policy; a City Attorney agent does not issue formal opinions.
- Include tone, typical inputs, typical outputs, and what the role should always ask for.
- Do not embed a specific city's facts; use context packs for that.

### Prompts (`prompts/<cadence-or-topic>/<name>.md`)
- Name by the task, not the tool.
- Include placeholders in square brackets, a statement of audience, required attachments, desired output format, and review points.
- Keep one task per prompt. Chain prompts through stacks instead of making a mega-prompt.

### Stacks, examples, evals, and docs
- Stacks follow the format in `stacks/README.md` and the handoff, gate, and trace rules in `stacks/ORCHESTRATION_PROTOCOL.md`.
- Examples contain `README.md`, `input.md`, `output.md`, and `notes.md`, and are clearly labeled fictional.
- Rubrics score 1-5 per criterion, list automatic fail conditions where relevant, and define a pass threshold. See `evals/eval-runbook.md` for testing changes.
- Docs state who they are for and note that they are not legal advice.

## Pull request checklist

Copy this into your PR description.

- [ ] Searched existing issues and files; this is not a duplicate
- [ ] Follows the style guide for its type (skill, agent, prompt, stack, example, eval, doc)
- [ ] Role boundaries preserved; required referrals (attorney, finance, HR, clerk) are named
- [ ] Review gates and required human sign-offs are stated
- [ ] No fabricated citations, statistics, or quotes; state-law variance flagged
- [ ] No real personal data; examples use fictional names and figures
- [ ] All internal links resolve to files that exist
- [ ] At least one example workflow or a pointer to an existing example is included
- [ ] Tested with at least one fictional scenario, ideally scored with the relevant rubric in `evals/`
- [ ] Indexes updated (README tables, catalog files, `CHANGELOG.md`) where applicable
- [ ] Privacy check: nothing in the PR requires entering sensitive data into an AI tool (see `docs/data-privacy-and-pii-handling.md`)
