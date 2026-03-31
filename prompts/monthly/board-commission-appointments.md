---
name: board-commission-appointments
title: Board & Commission Appointments
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Board & Commission Appointments

## Use when

The city is filling vacancies or preparing appointment action for boards or commissions.

## Inputs to gather

- vacancies
- applications
- term details
- ward/eligibility needs
- attendance history if relevant

## Expected output

An appointment memo, eligibility screen, interview questions, and draft action language.

## Built-in checks

- check residency/ward rules
- flag attendance issues
- avoid unsupported rankings

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with board & commission appointments.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is filling vacancies or preparing appointment action for boards or commissions.
Produce an appointment memo, eligibility screen, interview questions, and draft action language.
</task>

<inputs>
- vacancies
- applications
- term details
- ward/eligibility needs
- attendance history if relevant
</inputs>

<checks>
- check residency/ward rules
- flag attendance issues
- avoid unsupported rankings
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
