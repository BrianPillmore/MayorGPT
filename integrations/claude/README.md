# Claude (chat, Projects, API)

## Chat and Projects

A Project is a saved workspace with standing instructions and attached files.

1. Generate a single pasteable prompt:
   ```bash
   python scripts/export_bundle.py --agent city-manager --context-pack <your-city-pack> --format text > project-instructions.txt
   ```
2. Create a Project and paste the contents as its custom instructions.
3. Upload your context pack and reference documents (charter, code sections, budget, staff reports) as project files, or attach them in the conversation.
4. Run a task by pasting a "Copy/paste prompt" block from `prompts/` and attaching the source documents.

The XML-style tagged blocks in `prompts/` work well here. Put long source material before the task block and the request near the end.

## Skills

Skills are plain `SKILL.md` folders. Where your Claude product supports skill folders, install them with the [skills installer](../skills-installer/README.md) using `--target` pointed at the directory your product reads. Everywhere else, include them in a bundle:

```bash
python scripts/export_bundle.py --agent city-clerk --skills --skill-category governance --format text
```

## API

```bash
export MAYORGPT_PROVIDER=claude MAYORGPT_MODEL=<model id from the provider's docs> ANTHROPIC_API_KEY=...
python integrations/api/mayorgpt_llm.py --agent city-manager --prompt <prompt-name> --user "Draft the brief." --attach notes.txt
```

Add `--dry-run` to see the request with the key redacted and nothing sent. For scripted use of the Messages format, `export_bundle.py --format text` gives you the system text to pass as the `system` field.

## Size and limit tips

- Check current limits for project file size, number of files and context window.
- Attach only the documents the task needs, and quote section or page references when asking for facts from long documents.

## Data handling for government use

- Consumer, team, enterprise and API offerings have different retention and training terms. Confirm which applies and what your agreement says before using city material.
- Do not paste personnel, criminal-justice or other restricted records unless your agreement and policy allow it. See [../../docs/deployment-and-data-options.md](../../docs/deployment-and-data-options.md).
- Keep prompts and outputs that become public records under your retention schedule.
