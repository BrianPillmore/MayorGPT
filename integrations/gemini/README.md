# Google Gemini (Gems and AI Studio)

## Gems

A Gem is a saved assistant with its own instructions.

1. Generate a single pasteable prompt:
   ```bash
   python scripts/export_bundle.py --agent city-clerk --context-pack <your-city-pack> --format text > gem-instructions.txt
   ```
2. Create a new Gem and paste the contents as its instructions. If the text is too long, export with `--format custom-gpt`: it produces trimmed instructions plus knowledge files you can attach to the Gem (the format name refers to the size-fitting layout, and works for any platform).
3. Attach the context pack and reference documents as files, or paste them into the chat.
4. Run a task by pasting a "Copy/paste prompt" block from `prompts/` and attaching source documents.

## Google AI Studio and the API

For experiments, paste the system text into the "system instructions" box. For scripted use:

```bash
python scripts/export_bundle.py --agent city-clerk --format gemini --user "Draft minutes from the attached notes." > request.json
```

`request.json` has `system_instruction` and `contents` in the shape the `generateContent` method expects. Or call the API directly with the provider-neutral client:

```bash
export MAYORGPT_PROVIDER=gemini MAYORGPT_MODEL=<model id from Google's docs> GEMINI_API_KEY=...
python integrations/api/mayorgpt_llm.py --agent city-clerk --user "Draft minutes." --attach notes.txt
```

Add `--dry-run` to see the request with the key redacted and nothing sent.

## Size and limit tips

- Check current limits for instructions length, files per Gem, file size and context window.
- Long context lets you include a whole context pack plus several documents, but accuracy still improves when you attach only what the task needs.
- Quote page or section references when asking for facts from long documents.

## Data handling for government use

- Consumer, workspace and cloud (API) offerings have different retention and training terms. Confirm which applies and what your agreement says before using city material.
- Do not enter SSNs, payroll or HR detail, sealed records, privileged legal advice, or resident personal data unless policy allows it.
- Check who can see a shared Gem and its attached files.
- Treat all output as a draft for human review; drafts may be public records.

## Skills

Gems have no skills folder. Include skills at export time with `--skills name1,name2`, or paste the relevant `SKILL.md` body into the chat. See `integrations/skills-installer/README.md`.
