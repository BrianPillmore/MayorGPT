---
name: risk-register-update
title: Risk Register Update
type: prompt
category: quarterly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Risk Register Update

## Use when

Leadership needs a practical refresh of operational, fiscal, legal, reputational, and safety risks.

## Inputs to gather

- current risk list
- incidents
- audit notes
- claims/issues
- department input

## Expected output

An updated risk register with severity, trend, mitigation owners, and next actions.

## Built-in checks

- name top risks clearly
- show trend direction
- do not bury reputational or compliance issues

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with risk register update.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Leadership needs a practical refresh of operational, fiscal, legal, reputational, and safety risks.
Produce an updated risk register with severity, trend, mitigation owners, and next actions.
</task>

<inputs>
- current risk list
- incidents
- audit notes
- claims/issues
- department input
</inputs>

<checks>
- name top risks clearly
- show trend direction
- do not bury reputational or compliance issues
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
