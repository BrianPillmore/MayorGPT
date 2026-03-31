---
name: workforce-planning-review
title: Workforce Planning Review
type: prompt
category: quarterly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Workforce Planning Review

## Use when

The city needs a quarterly view of vacancies, retention, succession, and training needs.

## Inputs to gather

- vacancies
- turnover
- retirement risk
- training needs
- critical roles

## Expected output

A workforce memo with pressure points, succession risks, and recommended actions.

## Built-in checks

- identify mission-critical roles
- flag retention hot spots
- link staffing risk to service levels

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with workforce planning review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a quarterly view of vacancies, retention, succession, and training needs.
Produce a workforce memo with pressure points, succession risks, and recommended actions.
</task>

<inputs>
- vacancies
- turnover
- retirement risk
- training needs
- critical roles
</inputs>

<checks>
- identify mission-critical roles
- flag retention hot spots
- link staffing risk to service levels
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
