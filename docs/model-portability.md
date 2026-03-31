# Model Portability

MayorGPT is designed so the same content can be used in multiple ways:

## Generic use
- Open any agent file and paste the **Portable system prompt** into your model's system field.
- Open any prompt file and paste the XML block into a user prompt, replacing bracketed placeholders.
- Read any skill directory as a structured instruction set even if your platform does not support SKILL.md natively.

## Claude use
- The `skills/` directories are written in Claude-compatible `SKILL.md` format.
- The prompt files use XML blocks that are especially effective with Claude.
- The agents use direct role framing and explicit workflow language suited to Claude's instruction following.

## Other models
- ChatGPT / GPTs: use agent files as system instructions and prompt files as reusable actions.
- Gemini: use the same role/system prompt structure and attach context files as needed.
- Open-weight models: use shortened versions of the prompts if context windows are smaller.

## Best practice
Keep model-specific behavior at the edge. The core municipal logic should live in these Markdown files,
not in hidden app settings that no one can inspect or version.
