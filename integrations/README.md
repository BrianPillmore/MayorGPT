# Integrations

MayorGPT's logic lives in plain Markdown, so it runs on any model or platform that accepts a system prompt or file attachments. Nothing here depends on a single vendor.

The fastest path on any platform:

```bash
python scripts/export_bundle.py --list
python scripts/export_bundle.py --agent city-manager --prompt executive-brief \
  --context-pack sample-springfield-example --format text
```

`scripts/export_bundle.py` assembles an agent, optional prompt, optional context pack and optional skills into `text`, `markdown`, `openai-messages`, `gemini`, `custom-gpt` (size-fitted instructions plus knowledge files) or `all` (writes `dist/<agent>/`). It prints size estimates and warns when a prompt is large.

## Platform support matrix

| Platform | Guide | Paste prompt | Upload files | Skills | API client |
|---|---|---|---|---|---|
| ChatGPT (Custom GPTs, Projects) | [chatgpt](chatgpt/README.md) | yes | yes | via export | `openai` |
| Claude (chat, Projects, API) | [claude](claude/README.md) | yes | yes | folder or export | `claude` |
| Google Gemini (Gems, AI Studio) | [gemini](gemini/README.md) | yes | yes | via export | `gemini` |
| xAI Grok | [grok](grok/README.md) | yes | varies | via export | `xai` |
| Microsoft Copilot, Azure | [microsoft-copilot](microsoft-copilot/README.md) | yes | yes | via export | `azure` |
| Mistral | [mistral](mistral/README.md) | yes | varies | via export | `mistral` |
| Local models (Ollama, LM Studio, llama.cpp, vLLM) | [local-models](local-models/README.md) | yes | n/a | via export | `ollama`, `lmstudio`, `llamacpp`, `vllm` |
| Coding assistants (Cursor, GitHub Copilot, Aider, Windsurf, Cline, ...) | [coding-assistants](coding-assistants/README.md) | rule files | yes | folder or export | n/a |
| Perplexity, DeepSeek, Meta AI, Cohere, Qwen, others | [other-assistants](other-assistants/README.md) | yes | varies | via export | `perplexity`, `deepseek`, `cohere`, `qwen`, `openrouter` |
| Any OpenAI-compatible gateway | [api](api/README.md) | n/a | n/a | via export | `openai-compatible` |

"Varies" means it depends on plan and current product features; check the platform's documentation. Skills are plain `SKILL.md` folders; see the skills installer below.

## Guides

- [API](api/README.md): provider-agnostic command line client (`mayorgpt_llm.py`) for OpenAI-compatible APIs, native Gemini and native Claude, with `--print-prompt` and `--dry-run`. Standard library only.
- [Skills installer](skills-installer/README.md): copy `SKILL.md` folders into any tool's skills or instructions directory, or bundle them with the export script.
- [Generic assembly guide](generic/assembly-guide.md): the platform-independent recipe.
- [Tyler Munis ERP pairing](tyler-munis/README.md): which Munis exports to pull for each financial workflow, how to clean them, which skills pair with them, and which data must never be pasted into an AI session. MayorGPT has no direct Munis connection.

## Auto-discovered instruction files

Open this repository in a coding or chat tool and it will find `AGENTS.md`, `GEMINI.md`, `CONVENTIONS.md`, `.github/copilot-instructions.md`, `.cursor/rules/mayorgpt.mdc` or `.windsurfrules`. All point to `AGENTS.md`.

## Before you use any of them

Choose a tool your city has approved for the data involved. Protected data (SSNs, payroll detail, sealed records, privileged legal advice, resident personal data) belongs only in approved, appropriately configured or local deployments. Outputs are working drafts that need human review. See `docs/safety-and-governance.md`.
