# Mistral (Le Chat and API)

## Le Chat

1. Generate a pasteable prompt:
   ```bash
   python scripts/export_bundle.py --agent planning-and-development-director --format text > role.txt
   ```
   (Use `--list` to see agent names.)
2. If your plan supports custom agents or saved instructions, create one and paste the text. Otherwise paste it at the start of a conversation.
3. Upload the context pack and source documents as attachments or library files if available.
4. Run a task with a "Copy/paste prompt" block from `prompts/`.

## API

```bash
export MAYORGPT_PROVIDER=mistral MAYORGPT_MODEL=<model id from Mistral's docs> MISTRAL_API_KEY=...
python integrations/api/mayorgpt_llm.py --agent planning-and-development-director --user "Summarize the attached staff report." --attach report.txt
```

Add `--dry-run` to inspect the request without sending it.

## Open-weight and self-hosted use

Mistral publishes open-weight models that you can run locally. See `integrations/local-models/README.md`; this is the preferred route for sensitive material.

## Size and limit tips

- Check current limits for agent instructions, library size, and context window.
- Keep the role in the instructions and put the context pack and playbooks in files.
- Ask for a missing-information list; smaller models benefit from explicit structure.

## Data handling for government use

- Confirm the hosting region, retention, and training terms for your plan, and what your agreement provides.
- Do not enter SSNs, payroll or HR detail, sealed records, privileged legal advice, or resident personal data unless policy allows it.
- Outputs are drafts for human review and may be public records.

## Skills

No skills folder. Add skills with `--skills name1,name2` when exporting, or paste a `SKILL.md` body into the chat. See `integrations/skills-installer/README.md`.
