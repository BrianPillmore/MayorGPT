---
name: legislative-agenda
title: Legislative Agenda
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Legislative Agenda

## Use when

The city is setting its annual policy and advocacy priorities with outside governments.

## Inputs to gather

- priority issues
- draft asks
- partner landscape
- data points
- current law constraints

## Expected output

A concise legislative agenda with talking points and priority tiers.

## Built-in checks

- state requests in actionable terms
- support with local impact
- avoid conflicting asks

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with legislative agenda.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is setting its annual policy and advocacy priorities with outside governments.
Produce a concise legislative agenda with talking points and priority tiers.
</task>

<inputs>
- priority issues
- draft asks
- partner landscape
- data points
- current law constraints
</inputs>

<checks>
- state requests in actionable terms
- support with local impact
- avoid conflicting asks
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
