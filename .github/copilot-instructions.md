Follow the instructions in AGENTS.md at the repository root.

- This repository is Markdown content (agents, prompts, skills, context packs) for city government, plus standard-library Python scripts.
- Treat generated content as drafts for human review. Never invent citations, statutes or dollar amounts.
- Keep protected personal data out of all files. Do not hard-code model IDs or secrets.
- After changes run: python scripts/build_catalog.py, python scripts/validate_repo.py, pytest tests.
