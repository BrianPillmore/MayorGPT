# Other assistants (Perplexity, DeepSeek, Meta AI, Cohere, Qwen, and more)

Any chat assistant that accepts a block of instructions or a first message can run MayorGPT. This generic recipe works for Perplexity, DeepSeek, Meta AI, Cohere, Qwen, and tools not listed here.

## Recipe

1. Pick an agent: `python scripts/export_bundle.py --list agents`.
2. Export it, adding a context pack, a playbook and skills if you want them:
   ```bash
   python scripts/export_bundle.py --agent <agent> --context-pack <pack> --prompt <prompt> --format text > role.txt
   ```
3. Put `role.txt` where the assistant keeps persistent instructions (custom instructions, a space, a project, an assistant or persona). If there is no such feature, paste it as the first message and say "Follow this for the whole conversation."
4. Attach source documents, or paste the relevant text.
5. Ask for the draft, a missing-information list, a risk/process list and next steps.

If the instructions field is too small, run `--format custom-gpt`. It trims the role to fit about 8,000 characters and writes the rest as files to upload, which works anywhere files can be attached.

## Platform notes

| Assistant | Where to put the role | API route |
|---|---|---|
| Perplexity | A Space's custom instructions | `MAYORGPT_PROVIDER=perplexity` |
| DeepSeek | First message, or API system message | `MAYORGPT_PROVIDER=deepseek` |
| Meta AI / Llama | First message; or run Llama locally | see `integrations/local-models/README.md` |
| Cohere | System preamble in the API or playground | `MAYORGPT_PROVIDER=cohere` |
| Qwen | First message, or API system message | `MAYORGPT_PROVIDER=qwen` |
| Any gateway or aggregator | System message | `MAYORGPT_PROVIDER=openrouter` or `openai-compatible` |

Features vary by plan and change often; check current documentation. For API use, see `integrations/api/README.md`.

## Search-augmented assistants

Assistants that search the web can cite sources, but search results may be wrong, outdated or from outside your jurisdiction. Ask for links, open them, and never rely on a statute, case or code section until you have confirmed it in the primary source.

## Size and limit tips

- Check current limits for instructions length, attachments and context window.
- Start with the default portable role block; add one playbook and only the skills you need.
- Smaller models do better with short, explicit tasks and a requested output structure.

## Data handling for government use

- Confirm where the service is hosted, who operates it, and its retention and training terms. Some providers operate under different legal regimes than your city; your policy may restrict them for anything beyond public information.
- Do not enter SSNs, payroll or HR detail, sealed records, privileged legal advice, or resident personal data unless policy and agreement allow it. For sensitive work use a local model (`integrations/local-models/README.md`).
- Outputs are drafts for human review; they may be public records.

## Skills

Include skills with `--skills name1,name2` at export time, or paste a `SKILL.md` body into the chat. See `integrations/skills-installer/README.md`.
