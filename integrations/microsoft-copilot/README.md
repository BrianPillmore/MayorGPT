# Microsoft Copilot (and Azure OpenAI)

Many cities already license Microsoft 365, which makes Copilot and Azure-hosted models a practical, governed option.

## Copilot Chat and Microsoft 365 Copilot

1. Generate a pasteable prompt:
   ```bash
   python scripts/export_bundle.py --agent city-manager --format text > role.txt
   ```
2. If your tenant lets you build agents or saved prompts (for example in Copilot Studio or a prompt library), paste the text as the agent instructions and add the context pack and reference documents as knowledge sources. Availability depends on your licence and administrator settings; check current documentation.
3. Without agent building, paste the text at the start of a chat, or save it as a reusable prompt, then attach or reference documents from your tenant.
4. Run a task by pasting a "Copy/paste prompt" block from `prompts/` and pointing at the source documents.

## Azure OpenAI and other Azure-hosted models

Use the provider-neutral client with the `azure` preset and your own endpoint:

```bash
export MAYORGPT_PROVIDER=azure
export MAYORGPT_BASE_URL=<your resource's OpenAI-compatible endpoint>
export MAYORGPT_MODEL=<your deployment or model name>
export AZURE_OPENAI_API_KEY=...
python integrations/api/mayorgpt_llm.py --agent city-manager --user "Draft a brief on ..." --dry-run
```

Azure URL shapes and API versions change; follow your resource's current documentation and override the base URL as needed.

## Size and limit tips

- Check current limits for instructions length, knowledge sources and file sizes in your tenant.
- Keep instructions short and move detail to knowledge sources; `--format custom-gpt` produces size-fitted instructions plus knowledge files for any platform.
- Tenant search can pull in documents you did not intend. Review what the assistant cites.

## Data handling for government use

- Commercial data protection, tenant boundaries, sensitivity labels, and retention differ by licence. Have IT and counsel confirm what applies, including whether your tenant meets required government compliance programs.
- Respect existing permissions: the assistant can surface anything the user can open. Clean up over-shared folders first.
- Do not use it for SSNs, sealed records, or privileged material outside approved workflows.
- AI-assisted drafts may be public records and subject to retention.

## Skills

Copilot has no skills folder. Include skills at export time (`--skills name1,name2`) or add the relevant `SKILL.md` as a knowledge file. See `integrations/skills-installer/README.md`.
