# Integrations

MayorGPT's logic lives in plain Markdown, so it runs on any model or platform that accepts a system prompt and file attachments. These guides cover the four main integration approaches.

---

## Claude Code / CLI — `claude-code/`

The highest-capability integration. MayorGPT skills use Claude-compatible `SKILL.md` files that Claude Code picks up natively. Install selected skill directories into `.claude/skills/` in your project, paste an agent file into `CLAUDE.md` or a system prompt, and keep your city context pack in the project for reference. Claude Code users should also read the Claude Projects section in `claude-code/README.md`, which covers setting up a persistent browser-based workspace for city staff who do not use the CLI.

## Claude Projects (browser) — covered in `claude-code/README.md`

Claude Projects (available on Claude.ai) let staff configure a persistent AI workspace with a system prompt, uploaded knowledge files, and per-conversation attachments — no CLI required. Set the project instructions using `claude-code/sample-project-instructions.md`, upload the relevant agent and stack files as persistent knowledge, and attach live operational documents (current budget exports, draft staff reports) per conversation rather than as permanent files. Create separate projects for workflows with different role boundaries or confidentiality levels.

## Generic (any model) — `generic/`

Works with ChatGPT, Gemini Gems, open-source system prompts, and any platform that accepts a role instruction and file attachment. The pattern: pick a context pack, pick an agent from `agents/`, pick a prompt from `prompts/`, optionally add skills as reusable prompt snippets, attach source material, and ask for a draft plus a missing-information list, a risk/process list, and recommended next steps. Because MayorGPT keeps all logic in Markdown, porting to any platform is straightforward even when the platform does not support Claude-style skills.

## OpenAI Custom GPT — `openai-custom-gpt/`

Use an `agents/` file as the GPT's role or instruction layer. Copy a `prompts/` XML block into the user prompt or action area. For skill-like behavior, convert the corresponding `SKILL.md` instructions into actions or reusable prompt snippets. The Markdown-based structure makes this translation direct.

## Tyler Munis ERP pairing — `tyler-munis/`

MayorGPT has no direct API connection to Munis. Instead, this guide specifies exactly which Munis report exports to pull for each financial workflow (budget variance, CIP status, fund balance, grant accounting, debt service), how to clean those exports before attaching them (remove auto-inserted subtotals, fix column headers, add fund labels, separate multi-fund exports by tab), which MayorGPT skills pair with each export, and what Munis data categories must never be pasted into any AI session (employee payroll detail, SSNs, benefits enrollment, vendor TINs, utility billing account data). Munis data is authoritative; AI analysis of it is a working draft requiring Finance Director review before use.
