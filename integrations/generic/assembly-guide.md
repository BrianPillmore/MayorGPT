# Generic Assembly Guide

## Recipe
1. Pick a city context pack.
2. Pick one role from `agents/`.
3. Pick one task from `prompts/`.
4. If your platform supports instruction bundles, or you want reusable procedures, add one or more `skills/`.
5. Attach the source material.
6. Ask for:
   - the draft,
   - a missing-information list,
   - a risk/process list,
   - and recommended next steps.

## Automate the assembly

`scripts/export_bundle.py` performs steps 1 to 4 and prints the result in the format your platform needs:

```bash
python scripts/export_bundle.py --list
python scripts/export_bundle.py --agent city-manager --prompt executive-brief \
  --context-pack sample-springfield-example --format text
```

Formats: `text`, `markdown`, `openai-messages`, `gemini`, `custom-gpt` and `all`. See `integrations/README.md` for the platform guides.

## Works well for
- custom GPTs and saved assistants,
- Gemini Gems,
- local and open-weight models,
- coding assistants and IDE rule files,
- prompt libraries inside knowledge bases,
- document-grounded municipal copilots.
