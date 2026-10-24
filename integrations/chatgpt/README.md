# ChatGPT (Custom GPTs and Projects)

MayorGPT is plain Markdown, so it fits ChatGPT without conversion. Two approaches work well: a Custom GPT (a reusable assistant for one role) and a Project (a workspace with instructions and files).

## Generate the files

```bash
python scripts/export_bundle.py --agent city-manager \
  --prompt executive-brief --context-pack <your-city-pack> \
  --format custom-gpt --out dist/city-manager-gpt
```

This writes `instructions.txt` (trimmed to fit an instructions field of roughly 8,000 characters), a `knowledge/` folder with the full role file, context pack, playbook and any skills, and `KNOWLEDGE.md` listing what to upload. Check the platform's current limits, since they change.

## Custom GPT

1. Create a new GPT and open its configuration.
2. Paste `instructions.txt` into the instructions field.
3. Upload the files from `knowledge/` as knowledge.
4. Turn off any capability you do not need. Review the sharing setting before saving; keep GPTs that contain city material private to your organization.
5. Test with a prompt from `prompts/` (use its "Copy/paste prompt" block) and an attachment.

## Project

1. Create a Project and paste the contents of `python scripts/export_bundle.py --agent <name> --format text` into the project instructions.
2. Add the context pack and reference documents as project files.
3. Keep one Project per role or confidentiality level (for example, separate HR work from general work).

## Running a prompt

Open `prompts/<category>/<name>.md`, copy the "Copy/paste prompt" block, replace the bracketed placeholders, and attach source documents. Ask for the draft, a missing-information list, a risk/process list and next steps.

## Size and limit tips

- Check current limits for instructions length, number of files, file size and context window before building. Do not assume last year's numbers.
- If instructions are too long, keep the role core in the instructions and move detail to knowledge files; the export script does this for you.
- Long uploads can be summarized rather than read in full. For exact figures, attach the specific table or page.

## Data handling for government use

- Confirm your city's AI policy and the account type (consumer, team, enterprise) before use. Check whether conversations or uploads may be retained or used to improve models, and what the contract says.
- Do not upload SSNs, payroll detail, sealed records, criminal justice information, privileged legal advice, or resident personal data unless policy and agreement allow it.
- AI-assisted drafts may be public records. Keep them under your records retention schedule.
- Outputs are drafts. Keep the human review gates in each agent's Guardrails section.

## Skills

ChatGPT has no skills folder. Add the skills you need with `--skills name1,name2` (or `--skill-category`) when exporting; they become knowledge files. In a conversation, say "Use the budget-variance-analysis skill" and attach the data. See `integrations/skills-installer/README.md`.
