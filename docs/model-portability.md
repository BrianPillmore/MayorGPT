# Model Portability

MayorGPT works with any capable model. The core content is plain Markdown with XML-style tagged blocks,
so nothing depends on one vendor's product. This guide explains what carries over unchanged, what you
should adapt for each model or platform, and how to confirm a model is good enough for your city's work.
Platform details change often; always check current documentation for the product you use, and see
`../integrations/README.md` for the per-platform guides.

## What is portable

- **Agents** (`agents/`): role definitions with a portable system prompt block. Plain text, usable anywhere.
- **Prompts** (`prompts/`): task prompts written with XML-style tagged blocks that work well across models, plus bracketed placeholders.
- **Skills** (`skills/`): portable `SKILL.md` instruction folders. Each is readable as ordinary Markdown.
- **Context packs** (`context-packs/`): city facts as Markdown, attachable or pasteable anywhere.
- **Stacks, evals, and examples**: process documents and rubrics that do not depend on any model.

Keep model-specific behavior at the edge. The core municipal logic should live in these Markdown files,
not in hidden app settings that no one can inspect or version.

## What to adapt

| Area | What varies between models and platforms |
|---|---|
| Where instructions go | Some products have a system or instructions field, some only a chat box, some a saved assistant or project. |
| File handling | Upload limits, supported file types, and whether files are read in full or searched in pieces differ. |
| Context length | How much text fits in one conversation varies widely, especially for smaller or local models. |
| Structured output | Reliability of following a requested format (tables, JSON, fixed headings) varies. |
| Tool and skill loading | Some tools load skill folders on their own; most chat products do not. |
| Retention and data handling | Defaults differ by plan and by vendor. See `deployment-and-data-options.md`. |

## System prompt versus paste

Preferred: put the agent file's **Portable system prompt** block in the system or instructions field, and
send the prompt file as the user message.

If your product has no system field, paste the system block at the top of the first message, followed by a
line such as "Follow the role instructions above for this whole conversation", then the task prompt below it.
Start a new conversation for each unrelated task so earlier instructions and documents do not bleed over.

Saved assistants, projects, or custom bots are convenient for the agent text and slow-changing reference
files (charter excerpts, templates). Attach live documents per conversation so they do not go stale.

## Long-context versus short-context strategy

**Long-context models** can take the agent, the prompt, a context pack, and several source documents at once.
Still put the task and the most important instructions in clear tagged blocks, and ask for a list of what
the model could not find rather than letting it guess.

**Short-context or local models** need a lighter load:
- Use the shortest agent system block and one prompt at a time.
- Trim the context pack to the sections relevant to the task.
- Summarize long source documents in a first pass, then work from the summaries (keeping quotes you must cite).
- Split a stack into steps and carry forward only each step's output, per `../stacks/ORCHESTRATION_PROTOCOL.md`.
- Re-check anything citing a specific section or number against the source.

## Structured-output differences

Models differ in how strictly they follow output formats. To reduce surprises:
- State the exact headings or table columns you want, and ask for nothing else.
- Keep one task per prompt.
- For machine-readable output, ask for a specific format, validate it yourself, and re-ask on failure.
- If a model drifts, restate the format at the end of the prompt, where it is most likely to be followed.
- Always keep the required sections "missing information", "risks and review gates", and "next steps".

## Skills fallback

If your platform does not load skill folders, skills still work:
1. Open the skill's `SKILL.md` and paste it into the conversation, or attach it as a file.
2. Paste or attach any checklists or templates the skill references.
3. Tell the model: "Follow this skill. List which required attachments are missing before you begin."

For tools that do load skills, see `../integrations/skills-installer/README.md`.

## Testing across models

Do not assume a model is adequate because it is popular. Run the same fictional scenarios on each candidate
and score the results against the rubrics in `../evals/`. Follow `../evals/eval-runbook.md` for side-by-side
runs and `cross-model-evaluation.md` for a blind-comparison protocol. Re-test when you change models,
plans, or model versions, since behavior can change without notice.

## Related

- `choosing-a-model.md`: capability checklist for city use
- `deployment-and-data-options.md`: where the data goes and what that means for records
- `../integrations/README.md`: per-platform guides and the platform matrix
