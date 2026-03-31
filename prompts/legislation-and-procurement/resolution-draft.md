---
name: resolution-draft
title: Resolution Draft
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Resolution Draft

## Use when

You need a resolution for appointments, policy statements, approvals, or formal findings.

## Inputs to gather

- action requested
- background
- authority
- recitals needed
- effective timing

## Expected output

A clean draft resolution with recitals and action language.

## Built-in checks

- use resolution when ordinance is unnecessary
- make action language specific
- confirm signatures/attestation blocks

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with resolution draft.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a resolution for appointments, policy statements, approvals, or formal findings.
Produce a clean draft resolution with recitals and action language.
</task>

<inputs>
- action requested
- background
- authority
- recitals needed
- effective timing
</inputs>

<checks>
- use resolution when ordinance is unnecessary
- make action language specific
- confirm signatures/attestation blocks
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
