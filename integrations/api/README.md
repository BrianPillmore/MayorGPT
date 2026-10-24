# API integration (any provider)

`mayorgpt_llm.py` assembles an agent, an optional task prompt, an optional city context pack and optional skills into one system prompt, then sends your request to the model API you choose. It uses only the Python standard library (`urllib`), so there is nothing to install.

It speaks two wire formats:

- **OpenAI-compatible `chat/completions`**, which most hosted and local providers support.
- **Native Gemini `generateContent`**.

No model is built in. You always choose the provider and model yourself.

## Configure

| Variable | Purpose |
|---|---|
| `MAYORGPT_PROVIDER` | Provider preset name (table below) |
| `MAYORGPT_MODEL` | Model identifier exactly as your provider documents it. Required. |
| `MAYORGPT_BASE_URL` | Overrides the preset URL. Required for `azure` and `openai-compatible`. |
| `MAYORGPT_API_KEY` | API key. If unset, the provider's usual variable is used. Local servers need none. |

Each setting also has a flag (`--provider`, `--model`, `--base-url`). Keys are read from the environment only, never from a flag, so they stay out of shell history. Never commit keys; copy `.env.example` to `.env` (keep it out of Git) and load it with `set -a; source .env; set +a`.

## Providers

| Preset | API | Key variable (fallback) | Default base URL |
|---|---|---|---|
| `openai` | chat/completions | `OPENAI_API_KEY` | `https://api.openai.com/v1` |
| `gemini` | generateContent | `GEMINI_API_KEY` or `GOOGLE_API_KEY` | `https://generativelanguage.googleapis.com/v1beta` |
| `xai` (Grok) | chat/completions | `XAI_API_KEY` | `https://api.x.ai/v1` |
| `mistral` | chat/completions | `MISTRAL_API_KEY` | `https://api.mistral.ai/v1` |
| `deepseek` | chat/completions | `DEEPSEEK_API_KEY` | `https://api.deepseek.com` |
| `groq` | chat/completions | `GROQ_API_KEY` | `https://api.groq.com/openai/v1` |
| `together` | chat/completions | `TOGETHER_API_KEY` | `https://api.together.xyz/v1` |
| `fireworks` | chat/completions | `FIREWORKS_API_KEY` | `https://api.fireworks.ai/inference/v1` |
| `perplexity` | chat/completions | `PERPLEXITY_API_KEY` | `https://api.perplexity.ai` |
| `openrouter` | chat/completions | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` |
| `cohere` | chat/completions (compatibility API) | `COHERE_API_KEY` | `https://api.cohere.ai/compatibility/v1` |
| `qwen` | chat/completions (compatible mode) | `DASHSCOPE_API_KEY` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| `azure` | chat/completions | `AZURE_OPENAI_API_KEY` (sent as `api-key`) | set `MAYORGPT_BASE_URL` |
| `openai-compatible` | chat/completions | optional | set `MAYORGPT_BASE_URL` |
| `ollama` | chat/completions | none | `http://localhost:11434/v1` |
| `lmstudio` | chat/completions | none | `http://localhost:1234/v1` |
| `vllm` | chat/completions | optional | `http://localhost:8000/v1` |
| `llamacpp` | chat/completions | optional | `http://localhost:8080/v1` |

These are presets, not guarantees. Providers change URLs, regions and authentication; confirm against the provider's current documentation and override with `MAYORGPT_BASE_URL` when needed. Run `python integrations/api/mayorgpt_llm.py --list-providers` to print the table.

## Run

```bash
export MAYORGPT_PROVIDER=openrouter
export MAYORGPT_MODEL=<model identifier from your provider>
export OPENROUTER_API_KEY=...            # or MAYORGPT_API_KEY

python integrations/api/mayorgpt_llm.py \
  --agent city-manager --prompt executive-brief \
  --context-pack sample-springfield-example \
  --user "Draft a one-page brief on the Elm Street water main break." \
  --attach incident-notes.txt
```

Local model with no key:

```bash
export MAYORGPT_PROVIDER=ollama MAYORGPT_MODEL=<name shown by your local server>
python integrations/api/mayorgpt_llm.py --agent city-clerk --user "Draft minutes from the attached notes." --attach notes.txt
```

Add skills with `--skills budget-variance-analysis,grant-compliance-check`. Use `--user -` to read the request from standard input. `--max-tokens` and `--temperature` are only sent if you set them.

## Check before sending (no network)

```bash
python integrations/api/mayorgpt_llm.py --agent mayor --print-prompt        # the assembled system prompt
python integrations/api/mayorgpt_llm.py --agent mayor --user "hi" --dry-run # the exact request, keys redacted
```

## Notes

- Do not send protected data (SSNs, payroll detail, sealed records, privileged legal advice) to any hosted API unless your city's AI policy and the vendor agreement allow it. For sensitive work use a local or government-approved deployment. See `docs/safety-and-governance.md`.
- Outputs are drafts for human review, not legal, fiscal or procedural determinations.
- To produce the same content for a chat UI or another tool, use `python scripts/export_bundle.py --help`.
