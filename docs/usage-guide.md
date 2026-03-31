# Usage Guide

## The four-component system

Every MayorGPT workflow uses the same four pieces:

| Component | What it does | Where it lives |
|---|---|---|
| **Context pack** | Supplies your city's governance facts, fiscal rules, and meeting norms so drafts match how your city actually works | `context-packs/[your-city]/` |
| **Agent** | Defines the role, voice, authority boundary, and review posture of the AI for this task | `agents/` |
| **Prompt** | Defines the specific task — what to produce, in what format, with what inputs | `prompts/` |
| **Skill** | Defines the step-by-step execution pattern for a complex or recurring task type | `skills/` |

You do not need all four every time. A simple constituent response might only need an agent and a prompt. A budget variance analysis benefits from all four.

---

## Recommended reading order (new to the repo)

1. `README.md` — what MayorGPT is and what it covers
2. This guide — how to run a workflow
3. `docs/field-guide.md` — quick-reference prompts and situational guidance for common scenarios
4. Pick a stack — go to `stacks/` and find the one that matches your current situation

---

## Workflow A: Claude Code / CLI

This is the highest-capability path. Claude Code reads `SKILL.md` files natively.

1. Copy selected skill directories into `.claude/skills/` in your project.
2. Paste the relevant agent file into your `CLAUDE.md` or system prompt.
3. Store your city context pack in the project and reference it in prompts.
4. Attach the source documents that the stack calls for.
5. Run the prompt. Ask for a draft, a missing-information list, and a risk/process list.

See `integrations/claude-code/README.md` for full setup instructions, including the Claude Projects (browser) variation for staff who do not use the CLI.

---

## Workflow B: Claude Projects, ChatGPT, or any other model

Works on any platform that accepts a system prompt and file attachments.

1. Set the system prompt using the relevant agent file from `agents/`.
2. Upload slow-changing files as persistent knowledge: the stack file, key charter/code sections, recurring templates.
3. Attach live operational documents (current budget export, draft staff report, incident log) per conversation — do not add them as permanent knowledge files; they go stale.
4. In the user prompt, reference the relevant prompt from `prompts/` and any skill instructions you want the model to follow.
5. Ask for a draft, a missing-information list, and a risk/process list.

See `integrations/` for platform-specific guidance, including OpenAI Custom GPT and Tyler Munis ERP pairing.

---

## Building your city's context pack in one session

Open `context-packs/context-pack-builder.md`. Gather your city charter, key code sections, current adopted budget, and org chart. Paste the builder prompt into any AI session, attach your documents, and the model will produce a completed `README.md` and `SOURCE_NOTES.md` for your city. Review every fact before saving. Do not commit raw charter or budget PDFs to the public repo — keep those local and attach them at prompt time.

---

## Three common mistakes to avoid

**1. Using AI without attaching source material.**
AI drafts grounded only in general knowledge will use generic procurement thresholds, default governance assumptions, and placeholder fiscal figures. Attach the actual charter section, staff report, budget page, or policy document the task depends on. Ask the model to cite or quote from it in the draft.

**2. Treating AI output as final without review.**
Every output from this toolkit is a working draft. Staff reports, legal analysis, disciplinary documents, financial memos, and public communications all require qualified human review before use — by the relevant department head, city attorney, or finance officer, depending on the content. The evals in `evals/` help you score whether a draft is ready for that review step.

**3. Skipping the context pack entirely.**
Without a context pack, the AI does not know your fiscal year, your procurement authority thresholds, your form of government, or your meeting schedule. Drafts built without that context require more human correction and carry a higher risk of governance errors. Building the pack once pays off on every subsequent task.
