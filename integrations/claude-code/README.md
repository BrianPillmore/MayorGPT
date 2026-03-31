# Claude Code Integration

MayorGPT is especially friendly to Claude Code because the `skills/` directories use Claude-compatible
`SKILL.md` files.

## Simple installation
1. Pick the skills you want.
2. Copy the selected skill directories into `.claude/skills/` in your target project.
3. Optionally paste one of the `agents/` files into your project `CLAUDE.md` or system prompt.
4. Keep your city context pack in the repo or copy it into a local docs folder and reference it in prompts.

## Suggested pattern
- Store local charter, code, staff templates, and recurring packet examples in your project.
- Use MayorGPT's agent + prompt + skill combination as the repeatable AI layer.

---

## Using Claude Projects with MayorGPT

Claude Projects (available in Claude.ai) let you configure a persistent AI workspace with a system prompt, uploaded knowledge files, and tool settings that persist across conversations. This is a good fit for city staff who want to work in a browser without setting up Claude Code CLI.

### Setting up a Claude Project for MayorGPT

**Step 1 — Create the project.**
In Claude.ai, create a new Project. Name it for the workflow or role it will serve (e.g., "City Manager Weekly Ops" or "Budget Season 2026").

**Step 2 — Set the system prompt (project instructions).**
Paste the contents of `integrations/claude-code/sample-project-instructions.md` into the project instructions field. Edit the bracketed placeholder fields for your city. This becomes the persistent role and behavior framing for every conversation in the project.

**Step 3 — Upload knowledge files.**
Use the project knowledge feature to upload the files your workflows depend on:
- The relevant agent file from `agents/` (e.g., `finance-director-budget-officer.md`)
- Your city's charter and/or key code sections (PDF or plain text)
- Recurring templates (budget memo format, staff report template)
- The applicable stack file from `stacks/` so the AI knows the recommended workflow

Keep knowledge files focused. A project loaded with 50 documents degrades in the same way an unfocused CLAUDE.md does.

**Step 4 — Bring source documents per conversation.**
Do not upload live operational documents (current budgets, draft staff reports, incident logs) as permanent knowledge files — they go stale and may contain information that should not persist. Instead, attach them at the start of each conversation as needed.

**Step 5 — Configure tool access.**
Enable web search only if the workflow genuinely requires real-time external information (e.g., checking current grant NOFA deadlines). Disable it for workflows where you want the AI grounded only in attached documents.

### Recommended project structure for a city-specific deployment

```
Claude Project: [City Name] — [Workflow Name]
│
├── Project instructions (system prompt)
│   └── sample-project-instructions.md (customized)
│
├── Knowledge files (persistent, slow-changing)
│   ├── agents/[relevant-role].md
│   ├── stacks/[relevant-stack].md
│   ├── docs/charter-summary.md
│   ├── docs/key-code-sections.md
│   └── docs/staff-report-template.md
│
└── Per-conversation attachments (operational, current)
    ├── [current budget export or variance report]
    ├── [draft staff report or agenda item]
    └── [relevant source documents for this session]
```

Create separate projects for workflows that have different role boundaries or confidentiality levels. A project used for budget analysis should not also be used for HR investigations. Keep personnel and legal matters in their own projects with access limited to the staff who need them.
