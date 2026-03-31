# Context Packs

## What a context pack is

A context pack is a short, derived summary of your city's governance structure, meeting rhythm, fiscal rules, and procurement thresholds — written for AI consumption, not for public distribution. It is not a substitute for the actual charter, code, or legal advice. It is the standing brief that keeps every AI-assisted draft from defaulting to generic municipal assumptions that do not match how your city actually works.

Without a context pack, an AI might draft a staff report recommending a contract that requires City Manager approval when your charter actually requires Council action at that dollar amount, or set a budget adoption timeline that does not match your fiscal year. The context pack catches those mismatches before they reach a human reviewer.

---

## How to build one

**Step 1 — Gather documents.** Collect as many of the following as possible before starting:

- City charter (form of government, mayor/council powers, CM authority, clerk, attorney, fiscal year, audit, emergency ordinance threshold, term limits)
- Municipal code (meeting schedule, parliamentary authority, procurement/bidding thresholds, ethics/conflict-of-interest rules)
- Current adopted budget (fund structure, fiscal year dates, reserve policies)
- Adopted strategic plan or council priorities
- Standard agenda packet template
- Board and commission roster
- Current org chart

The more you attach, the more accurate the pack. The charter and code are essential; everything else improves precision.

**Step 2 — Run the builder prompt.** Open `context-pack-builder.md`. Copy the prompt into any AI session and attach your gathered documents. The prompt instructs the model to produce a completed `README.md` and `SOURCE_NOTES.md` grounded in your documents, flagging anything it cannot confirm rather than guessing.

**Step 3 — Fill in the template directly (alternative).** If you prefer to write the pack yourself, use `TEMPLATE/README.md` as the structure and `TEMPLATE/SOURCE_NOTES.md` as the checklist. Every bracketed placeholder maps to a specific governance fact. Mark items `[VERIFY — source unclear]` where you are uncertain rather than filling in an assumption.

**Step 4 — Review before saving.** Confirm every fact in the generated pack against your source documents. Save to `context-packs/[your-city-name]/`.

**Step 5 — Do not commit raw source documents to this repo.** Charter PDFs, budget files, and code exports should stay local. Attach them at prompt time. Only the derived pack (README.md and SOURCE_NOTES.md) belongs in the repo.

---

## How to use a context pack

Reference your context pack in every agent prompt. For tasks that depend on specific governance facts (procurement authority, meeting thresholds, ordinance requirements), attach the relevant sections of the actual charter or code alongside the pack — the pack is a navigator, not the authoritative source.

Update `SOURCE_NOTES.md` any time the charter, code, or key policies change. A stale pack is worse than no pack because it generates confident-sounding errors.

---

## What's here

- `context-pack-builder.md` — the prompt for generating a pack from your local documents in a single AI session
- `TEMPLATE/README.md` — the governance summary template (fill in or use as the builder's output target)
- `TEMPLATE/SOURCE_NOTES.md` — the source verification checklist
- `yukon-ok/` — example pack for Yukon, Oklahoma (reference implementation)
