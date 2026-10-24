# Skills installer

MayorGPT skills are plain folders, each containing one `SKILL.md`: a short front-matter block (`name`, `description`) followed by Markdown instructions. They are not tied to any one product. Any tool or person can use them as a reusable set of instructions.

## Option 1: tools with a skills or instructions directory

Some assistants and coding tools load a folder of `<name>/SKILL.md` files, or a rules/instructions directory, and apply the right one when a request matches its description. Check your tool's documentation for the folder it reads, then copy skills there:

```bash
# see what exists
integrations/skills-installer/install_mayorgpt_skills.sh --list

# preview, then install one category into a folder of your choice
integrations/skills-installer/install_mayorgpt_skills.sh --category finance --target ./city-skills --dry-run
integrations/skills-installer/install_mayorgpt_skills.sh --category finance --target ./city-skills

# a single skill
integrations/skills-installer/install_mayorgpt_skills.sh --skill budget-variance-analysis --target ./city-skills
```

| Flag | Meaning |
|---|---|
| `--target DIR` | Destination directory. Required when installing. |
| `--list` | Print categories and skills, then exit. |
| `--category NAME` | Install every skill in a category (repeatable). |
| `--skill NAME` | Install one skill (repeatable). |
| `--dry-run` | Show what would happen; change nothing. |
| `--force` | Overwrite an installed skill that differs from the repo copy. |

The script never deletes anything, skips skills that already exist and differ (unless `--force`), and is idempotent: running it twice changes nothing. Install only the skills you need; many loaded at once dilute attention.

If your tool wants rules in a different file format or location, copy the `SKILL.md` body into that format by hand. The content is ordinary Markdown.

## Option 2: tools without a skills directory

Bundle the skills into the prompt instead. The export script appends each selected skill to the system prompt, or to the knowledge files for a Custom GPT or Gem:

```bash
python scripts/export_bundle.py --agent finance-director-budget-officer \
  --skills budget-variance-analysis,grant-compliance-check --format text > system-prompt.txt

python scripts/export_bundle.py --agent finance-director-budget-officer \
  --skill-category finance --format custom-gpt --out dist/finance-gpt
```

Use `--format markdown`, `openai-messages` or `gemini` for other destinations. The script prints a size estimate; if the result is large, include fewer skills or upload them as separate files and ask the assistant to read the relevant one.

## Option 3: paste by hand

Open a `SKILL.md`, copy the body, and paste it into the chat after your request, or attach the file. This works everywhere.

## Notes

- Skills produce working drafts for human review; they do not replace legal, fiscal or HR judgment.
- Do not paste protected personal data into any tool your city has not approved for it.
