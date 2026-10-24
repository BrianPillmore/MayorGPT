# Getting Started in 30 Minutes

A fast path from "I just found this repository" to a safe, useful first result. If you are in a small city with no IT staff, read `small-city-guide.md` after this.

## Minute 0-5: Safety check
1. Use only an AI tool your city has approved, on a city-managed account if possible.
2. Do not enter personal information, personnel or legal matters, or police-system data. See `data-privacy-and-pii-handling.md` for the short list.
3. Remember: a human reviews everything before it becomes official. AI output is a draft.

## Minute 5-10: Understand the four pieces
- **Agent**: a role (for example, City Manager, Finance Director). Folder: `../agents/`
- **Prompt**: a reusable request for a recurring task. Folder: `../prompts/`
- **Skill**: a step-by-step procedure for a task. Folder: `../skills/`
- **Stack**: a bundle of agents, prompts, and skills for a workflow. Folder: `../stacks/`

Find your situation quickly in `field-guide.md`.

## Minute 10-15: Pick one task
Choose something low-risk and common. Good first tasks:
- Rewrite a staff memo in plain language (public information only)
- Draft a community FAQ from a published policy
- Prepare questions for a meeting from a posted agenda
- Summarize a public report

Avoid for now: disciplinary matters, legal conclusions, public safety data, and anything with resident names.

## Minute 15-25: Run it
1. Open the matching agent file, for example `../agents/executive-office/city-manager.md`, and paste its contents (or attach it) as the role instruction. Tools differ; see `model-portability.md` and `../integrations/README.md`.
2. Open the matching skill or prompt, for example `../skills/public-engagement/faq-builder/SKILL.md` or a file from `../prompts/daily/`, and paste it or follow its steps.
3. Attach your source material (published documents only for this first run).
4. Ask for the output and tell the tool what you want to see: audience, length, and what to label as unknown.
5. Check the output against the source. Look for invented numbers, citations, and commitments.

## Minute 25-30: Review and decide
- Score the draft quickly with `../evals/municipal-output-rubric.md` (or the public-facing writing rubric for resident-facing text).
- Edit the draft as a human. Add your own judgment and local facts.
- Decide where the final version will be saved (your records system, not only the chat window). See `ai-procurement-and-records-retention.md`.
- Write down one thing you will do differently next time.

## What to do next
| If you want to... | Read |
|---|---|
| Learn the full method | `usage-guide.md` |
| Coordinate several roles on one decision | `multi-agent-guide.md` and `../stacks/ORCHESTRATION_PROTOCOL.md` |
| See complete worked cases | `../examples/README.md` |
| Set rules for your staff | `safety-and-governance.md`, `data-privacy-and-pii-handling.md` |
| Buy or approve a tool | `ai-procurement-and-records-retention.md` |
| Understand unfamiliar terms | `glossary.md` |
| Compare tools or model versions | `../evals/eval-runbook.md` |

## Common first-day mistakes
- Pasting real resident data into a free consumer tool
- Skipping the source attachment and getting generic answers
- Treating a legal-sounding paragraph as legal advice
- Posting output without checking numbers and dates
- Forgetting to save the final version
