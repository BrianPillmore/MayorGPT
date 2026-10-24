# Coding assistants and IDE tools

Editor and terminal assistants read instruction files from a project folder. MayorGPT is Markdown, so no conversion is needed. These tools suit staff who keep agendas, ordinances, templates and data in a Git repository or synced folder.

This repository already ships the discovery files, so opening it in one of these tools works immediately:

| Tool | File read automatically |
|---|---|
| Many agentic tools (generic standard) | `AGENTS.md` |
| Cursor | `.cursor/rules/mayorgpt.mdc` (also reads `AGENTS.md`) |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Aider | `CONVENTIONS.md` (load with `aider --read CONVENTIONS.md`) |
| Windsurf | `.windsurfrules` |
| Gemini CLI and Gemini Code Assist | `GEMINI.md` |
| Cline, Continue, Zed, JetBrains assistants, others | `AGENTS.md`, or the tool's rules directory |

All of them point to `AGENTS.md`, which explains the repo layout and how an assistant should behave.

## Use MayorGPT in your own city repository

1. Copy the role you need into a rules file your tool reads. The export script strips front matter and gives you plain text:
   ```bash
   python scripts/export_bundle.py --agent city-manager --context-pack <your-city-pack> --format markdown > city-role.md
   ```
2. Paste the result into the tool's rule file (`.cursor/rules/<name>.mdc`, `.github/copilot-instructions.md`, `CONVENTIONS.md`, `.windsurfrules`, or `AGENTS.md`). Keep it short; long instruction files dilute attention.
3. Reference prompts on demand by file mention (for example `prompts/daily/executive-brief.md`) instead of loading all of them as rules.
4. For skills, see below.

## Running a prompt

Open the chat or agent panel, attach or mention the source document, and paste a "Copy/paste prompt" block from `prompts/`. Ask for the draft, a missing-information list, a risk/process list and next steps.

## Size and limit tips

- Check each tool's current limits for rule file length and context window. Rule files are sent with every request, so brevity saves cost and improves focus.
- One role per rule file. Keep separate files or folders for finance, clerk and HR work.
- Prefer on-demand file mentions over always-on rules for long material.

## Data handling for government use

- Instruction files are plain text and usually committed to Git. Never put personnel, payroll, sealed-record or resident data in them.
- These tools send file contents to a model provider. Check the provider, retention and training terms for your plan, and exclude sensitive folders (most tools support an ignore file).
- Agentic tools can edit and run commands. Review every change, and do not give them access to production systems or credentials.
- Outputs are drafts for human review; they may be public records.

## Skills

Many of these tools can read a skills or rules folder. Install skills where your tool looks:

```bash
integrations/skills-installer/install_mayorgpt_skills.sh --category finance --target <folder your tool reads>
```

For tools without such a folder, reference the `SKILL.md` file by path in your request, or bundle skills with `export_bundle.py --skills`. See `integrations/skills-installer/README.md`.
