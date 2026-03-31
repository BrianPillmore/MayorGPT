---
name: audit-response
title: Audit Response
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Audit Response

## Use when

The city needs to respond to audit findings, comments, or management recommendations.

## Inputs to gather

- audit findings
- management comments
- control notes
- owner assignments
- deadlines

## Expected output

A response memo with corrective actions, owners, dates, and communication language.

## Built-in checks

- do not be defensive
- state control improvement clearly
- assign owners and dates

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with audit response.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs to respond to audit findings, comments, or management recommendations.
Produce a response memo with corrective actions, owners, dates, and communication language.
</task>

<inputs>
- audit findings
- management comments
- control notes
- owner assignments
- deadlines
</inputs>

<checks>
- do not be defensive
- state control improvement clearly
- assign owners and dates
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
