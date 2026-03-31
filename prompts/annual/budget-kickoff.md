---
name: budget-kickoff
title: Budget Kickoff
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Budget Kickoff

## Use when

The city is opening its annual budget cycle and needs clear instructions and framing.

## Inputs to gather

- financial outlook
- manager priorities
- council goals
- calendar
- submission requirements

## Expected output

A budget kickoff memo, calendar, department instructions, and key assumptions.

## Built-in checks

- state recurring constraints
- name decision criteria
- explain calendar and review gates

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with budget kickoff.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is opening its annual budget cycle and needs clear instructions and framing.
Produce a budget kickoff memo, calendar, department instructions, and key assumptions.
</task>

<inputs>
- financial outlook
- manager priorities
- council goals
- calendar
- submission requirements
</inputs>

<checks>
- state recurring constraints
- name decision criteria
- explain calendar and review gates
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
