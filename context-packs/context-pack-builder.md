---
name: context-pack-builder
title: City Context Pack Builder
type: prompt
category: setup
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# City Context Pack Builder

## Purpose

Use this prompt to have an AI model generate a completed `README.md` and `SOURCE_NOTES.md`
for your city by reading your local documents. The output slots directly into
`context-packs/[your-city]/`.

---

## Documents to gather before running this prompt

Collect as many of the following as possible. The more you attach, the more accurate the pack.

### Essential
- [ ] **City charter** — full text or key sections (form of government, mayor/council powers,
  city manager/CAO authority, clerk, attorney, fiscal year, audit, emergency ordinance threshold,
  term limits, initiative/referendum/recall if any)
- [ ] **Municipal code** — sections covering meeting schedule, parliamentary authority,
  procurement/bidding thresholds, ethics/conflict-of-interest rules

### Strongly recommended
- [ ] **Current adopted budget** — fund structure, fiscal year dates, reserve policies
- [ ] **Adopted strategic plan or council priorities** — current goals and priority initiatives
- [ ] **Standard agenda packet template** — shows meeting format, staff report structure,
  how items are noticed

### Helpful additions
- [ ] **State competitive bidding or procurement statute** — to verify local thresholds
  against state law
- [ ] **Board and commission roster** — lists advisory bodies and appointment process
- [ ] **Current org chart** — shows department structure and who reports to whom

---

## Copy/paste prompt

```xml
<role>
You are a municipal government AI configuration specialist. Your job is to read the attached
city documents and produce a completed context pack for use with MayorGPT.
</role>

<context>
CITY: [CITY, STATE]
GOVERNANCE_MODEL: [council-manager / mayor-council / commission / other — fill in if known]
ATTACHED_DOCUMENTS: [list the documents you are attaching]
</context>

<task>
Read every attached document carefully. Then produce two files:

FILE 1 — README.md
Using the TEMPLATE/README.md structure as your guide, fill in every bracketed placeholder
with accurate information from the attached documents. Where a section does not apply to
this city, note that clearly. Where the documents are ambiguous or silent, flag it with
[VERIFY — source unclear]. Do not invent facts not found in the documents.

FILE 2 — SOURCE_NOTES.md
Using the TEMPLATE/SOURCE_NOTES.md structure, check off each item you confirmed from
the documents, add brief notes on where each fact came from (e.g., "Charter § 4.2"),
and list any items that need verification.
</task>

<checks>
- Every governance fact must trace to a specific document and section.
- Flag ambiguities rather than guessing.
- Do not include any situation-specific, personnel-specific, or politically sensitive
  details — this pack should be reusable across issue types.
- Keep the pack forward-looking and generic enough to use for any future task,
  not tied to a current controversy or decision.
</checks>

<required_output>
1. Completed README.md (ready to save to context-packs/[city-name]/README.md)
2. Completed SOURCE_NOTES.md (ready to save to context-packs/[city-name]/SOURCE_NOTES.md)
3. A short list of facts that could not be confirmed and need human verification
</required_output>
```

---

## After generating

1. Review both files carefully before saving — confirm every fact against your source documents.
2. Save to `context-packs/[your-city-name]/`.
3. Do **not** commit raw source documents (charter PDFs, budget files) to the public repo —
   keep those local and attach them at prompt time.
4. Update `SOURCE_NOTES.md` any time the charter, code, or key policies change.
