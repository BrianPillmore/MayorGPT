---
name: ordinance-draft
title: Ordinance Draft
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Ordinance Draft

## Use when

You need to draft or revise an ordinance.

## Inputs to gather

- policy goal
- authority source
- existing code text
- enforcement approach
- effective date needs

## Expected output

A draft ordinance with purpose, operative language, procedural notes, and issue flags.

## Built-in checks

- state amendment target clearly
- define enforcement and effective date
- flag publication/hearing needs

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with ordinance draft.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need to draft or revise an ordinance.
Produce a draft ordinance with purpose, operative language, procedural notes, and issue flags.
</task>

<inputs>
- policy goal
- authority source
- existing code text
- enforcement approach
- effective date needs
</inputs>

<checks>
- state amendment target clearly
- define enforcement and effective date
- flag publication/hearing needs
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
