---
name: budget-adoption-book
title: Budget Adoption Book
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Budget Adoption Book

## Use when

You need a polished summary for workshops or adoption.

## Inputs to gather

- proposed budget
- major changes
- fund summaries
- capital plan
- fee/rate changes

## Expected output

An adoption-ready summary book with narrative, highlights, trade-offs, and public-facing explanations.

## Built-in checks

- plain language first
- show major changes and why
- separate policy choice from required cost growth

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with budget adoption book.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a polished summary for workshops or adoption.
Produce an adoption-ready summary book with narrative, highlights, trade-offs, and public-facing explanations.
</task>

<inputs>
- proposed budget
- major changes
- fund summaries
- capital plan
- fee/rate changes
</inputs>

<checks>
- plain language first
- show major changes and why
- separate policy choice from required cost growth
</checks>

<required_output>
1. Brief issue framing
2. Draft work product
3. Key risks / missing information
4. Recommended next step
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- For Claude, keep long source material above the task block when possible and put the ask near the end of the prompt.
