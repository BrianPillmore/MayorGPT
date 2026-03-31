---
name: city-manager-operations-review
title: City Manager Operations Review
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# City Manager Operations Review

## Use when

The manager’s office needs a weekly operational review across departments.

## Inputs to gather

- department updates
- staffing issues
- project status
- incidents
- budget variances

## Expected output

An operations review memo with cross-department blockers, deadlines, and executive decisions needed.

## Built-in checks

- name owners
- focus on risks and dependencies
- do not hide slippage

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with city manager operations review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The manager’s office needs a weekly operational review across departments.
Produce an operations review memo with cross-department blockers, deadlines, and executive decisions needed.
</task>

<inputs>
- department updates
- staffing issues
- project status
- incidents
- budget variances
</inputs>

<checks>
- name owners
- focus on risks and dependencies
- do not hide slippage
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
