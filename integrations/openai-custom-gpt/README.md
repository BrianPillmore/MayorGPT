# OpenAI / Custom GPT Integration

Use the contents of an `agents/` file as the role or instruction layer, then copy a `prompts/` XML block
into the user prompt/action area. If you want skill-like behavior, convert the corresponding `SKILL.md`
instructions into actions or reusable prompt snippets.

MayorGPT keeps the logic in Markdown so it is easy to port even when the hosting platform does not support
Claude-style skills directly.
