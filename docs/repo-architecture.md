# Repository Architecture

MayorGPT currently includes:

- **40 agents** in role-based folders,
- **85 reusable prompts** organized by cadence and function,
- **95 portable SKILL.md skills** grouped by municipal workstream,
- example city context notes,
- integration guides,
- evaluation rubrics, and
- recommended stacks for common use cases.

## Why this structure works

### `agents/`
Reusable role definitions. These are the closest thing to a reusable municipal “team.”

### `prompts/`
Task-specific prompts. These cover the day-to-day, month-to-month, and annual rhythm of city work.

### `skills/`
Action-oriented instruction bundles. Each skill is a portable folder with a `SKILL.md` file that any model can read as plain Markdown.

### `context-packs/`
City-specific overlays. Add a folder here for each city you configure the system for.

### `stacks/`
Curated combinations of agents, prompts, skills, and context for common workflows.

### `evals/`
Rubrics that help a human reviewer judge whether an output is actually fit for municipal use.
