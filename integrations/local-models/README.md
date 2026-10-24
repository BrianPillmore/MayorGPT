# Local and open-weight models

Running a model on your own hardware keeps prompts and documents inside your network. For anything sensitive, this is the safest route, and it can work with no internet connection at all.

Open-weight families you can run locally include Meta Llama, Qwen, DeepSeek, Mistral and Google Gemma, among others. Quality, speed and context length vary a lot with model size and your hardware. Test on non-sensitive sample material first, and check each model's licence for your intended use.

## Get the prompt

```bash
python scripts/export_bundle.py --agent finance-director-budget-officer --format text > role.txt
python scripts/export_bundle.py --agent finance-director-budget-officer --format openai-messages --user "..." > request.json
```

Smaller models follow shorter prompts better. Start with the default portable role block and add the context pack and one playbook only when needed.

## Ollama

Create a Modelfile that bakes the role in as the system prompt. Replace `<base model>` with a model you have pulled.

```
FROM <base model>
PARAMETER temperature 0.3
SYSTEM """
<paste the contents of role.txt here>
"""
```

```bash
ollama create mayorgpt-finance -f Modelfile
ollama run mayorgpt-finance
```

Many local runtimes use a small default context window; raise it (for example with the `num_ctx` parameter) if prompts plus documents are truncated. Check your runtime's documentation.

Or use the API client against the running server:

```bash
export MAYORGPT_PROVIDER=ollama MAYORGPT_MODEL=<name from 'ollama list'>
python integrations/api/mayorgpt_llm.py --agent finance-director-budget-officer --user "Explain the variances." --attach variance.txt
```

## LM Studio

1. Load a model and open the chat. Paste `role.txt` into the system prompt field and save it as a preset.
2. Or start the local server and use `MAYORGPT_PROVIDER=lmstudio` with the model name it shows.

## llama.cpp and vLLM

Both expose an OpenAI-compatible server.

```bash
export MAYORGPT_PROVIDER=llamacpp     # or: vllm
export MAYORGPT_MODEL=<model name the server reports>
python integrations/api/mayorgpt_llm.py --agent city-clerk --user "..." --dry-run
```

Use `MAYORGPT_BASE_URL` if your server is on another host or port. With `llama-cli` you can pass the prompt text as a system prompt file; see its help.

## Air-gapped use for sensitive data

1. Download the model weights and runtime on an approved machine, verify checksums, and move them by approved media.
2. Copy this repository over as well. Everything in `scripts/` and `integrations/api/` is standard-library Python and needs no network or package installs.
3. Run with the network disabled. Confirm the runtime does not call out for updates or telemetry.
4. Store inputs and outputs under your records retention rules; local drafts may still be public records.
5. Keep human review gates for legal, fiscal, HR and public-release documents.

## Size and limit tips

- Check each model's context length and your available memory. Long inputs may need chunking: summarize sections, then combine.
- Prefer attaching extracted text over scans or PDFs unless your tooling extracts text reliably.
- Verify every number and citation against the source; smaller models invent details more often.

## Skills

Use `--skills name1,name2` at export time, or paste one `SKILL.md` body at a time. Fewer, shorter skills work better on smaller models. See `integrations/skills-installer/README.md`.
