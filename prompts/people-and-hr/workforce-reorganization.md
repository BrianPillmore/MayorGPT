---
name: workforce-reorganization
title: Workforce Reorganization
type: prompt
category: people-and-hr
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Workforce Reorganization

## Use when

The city is considering reporting-line, staffing, or organizational redesign.

## Inputs to gather

- current org chart
- pain points
- service goals
- budget constraints
- critical roles

## Expected output

An options memo with org alternatives, pros/cons, and implementation issues.

## Built-in checks

- show service impact
- flag classification/HR/legal review needs
- avoid abstract theory detached from staffing reality

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with workforce reorganization.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is considering reporting-line, staffing, or organizational redesign.
Produce an options memo with org alternatives, pros/cons, and implementation issues.
</task>

<inputs>
- current org chart
- pain points
- service goals
- budget constraints
- critical roles
</inputs>

<checks>
- show service impact
- flag classification/HR/legal review needs
- avoid abstract theory detached from staffing reality
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
