# xAI Grok

## In the Grok app or web chat

1. Generate a pasteable prompt:
   ```bash
   python scripts/export_bundle.py --agent mayor --context-pack <your-city-pack> --format text > role.txt
   ```
2. If your plan offers custom instructions, a project, or a saved assistant, paste the text there. Otherwise paste it at the start of a new chat and say "Follow this for the whole conversation."
3. Run a task by pasting a "Copy/paste prompt" block from `prompts/` with source text or attachments.

## API

Grok models are served through an OpenAI-compatible API:

```bash
export MAYORGPT_PROVIDER=xai MAYORGPT_MODEL=<model id from xAI's docs> XAI_API_KEY=...
python integrations/api/mayorgpt_llm.py --agent mayor --prompt executive-brief --user "Draft a brief on ..." --dry-run
```

Remove `--dry-run` to send. You can also produce raw messages with `python scripts/export_bundle.py --agent mayor --format openai-messages`.

## Size and limit tips

- Check current limits for custom instructions, attachments and context window.
- If the full prompt is too long, use `--agent-mode portable` (the default) and attach the context pack as a file instead of pasting it.
- Live web or social search features can add unverified material. Ask the assistant to separate sourced facts from assumptions, and verify any citation, statute, or figure yourself.

## Data handling for government use

- Confirm account type, data retention and training terms before using city material. Consumer terms often differ from business or API terms.
- Do not enter SSNs, payroll or HR detail, sealed records, privileged legal advice, or resident personal data unless your policy and agreement allow it.
- Outputs are drafts for human review; they may be public records.

## Skills

No skills folder. Export with `--skills name1,name2` to include them in the prompt, or paste a `SKILL.md` body into the chat. See `integrations/skills-installer/README.md`.
