---
name: community-faq
title: Community FAQ Builder
type: prompt
category: public-engagement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Community FAQ Builder

## Use when

Residents keep asking the same questions and the city needs a public FAQ.

## Inputs to gather

- topic
- source materials
- common questions
- known misconceptions

## Expected output

A public-facing FAQ with plain-language answers and pointers to source documents or contacts.

## Built-in checks

- use simple language
- state what is not yet known
- do not overlegalize the tone

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with community faq builder.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Residents keep asking the same questions and the city needs a public FAQ.
Produce a public-facing faq with plain-language answers and pointers to source documents or contacts.
</task>

<inputs>
- topic
- source materials
- common questions
- known misconceptions
</inputs>

<checks>
- use simple language
- state what is not yet known
- do not overlegalize the tone
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
