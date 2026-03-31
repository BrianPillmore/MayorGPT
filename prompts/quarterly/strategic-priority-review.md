---
name: strategic-priority-review
title: Strategic Priority Review
type: prompt
category: quarterly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Strategic Priority Review

## Use when

The city needs a quarterly scorecard on adopted goals or council priorities.

## Inputs to gather

- priority list
- status notes
- owner updates
- budget tie-ins
- public concerns

## Expected output

A strategic review with status, evidence, slippage reasons, and quarter-ahead focus.

## Built-in checks

- tie work to adopted priorities
- name what is off-track
- refresh owners and dates

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with strategic priority review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a quarterly scorecard on adopted goals or council priorities.
Produce a strategic review with status, evidence, slippage reasons, and quarter-ahead focus.
</task>

<inputs>
- priority list
- status notes
- owner updates
- budget tie-ins
- public concerns
</inputs>

<checks>
- tie work to adopted priorities
- name what is off-track
- refresh owners and dates
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
