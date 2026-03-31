---
name: new-council-onboarding
title: New Council Onboarding
type: prompt
category: elections-and-transition
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# New Council Onboarding

## Use when

The city is onboarding one or more newly elected councilmembers.

## Inputs to gather

- charter/code basics
- meeting rules
- current priorities
- board assignments
- ethics requirements

## Expected output

An onboarding plan, reading list, and first-meeting prep packet.

## Built-in checks

- cover role boundaries
- include calendar and contacts
- flag training requirements

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with new council onboarding.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is onboarding one or more newly elected councilmembers.
Produce an onboarding plan, reading list, and first-meeting prep packet.
</task>

<inputs>
- charter/code basics
- meeting rules
- current priorities
- board assignments
- ethics requirements
</inputs>

<checks>
- cover role boundaries
- include calendar and contacts
- flag training requirements
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
