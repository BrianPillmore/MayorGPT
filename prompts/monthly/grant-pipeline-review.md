---
name: grant-pipeline-review
title: Grant Pipeline Review
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Grant Pipeline Review

## Use when

The city wants a monthly snapshot of grants pursued, awarded, at-risk, or worth pursuing.

## Inputs to gather

- grant list
- statuses
- deadlines
- matches
- department priorities

## Expected output

A pipeline review with next applications, compliance deadlines, award risks, and decisions needed.

## Built-in checks

- flag match and staffing burden
- note reporting deadlines
- retire poor-fit opportunities

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with grant pipeline review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city wants a monthly snapshot of grants pursued, awarded, at-risk, or worth pursuing.
Produce a pipeline review with next applications, compliance deadlines, award risks, and decisions needed.
</task>

<inputs>
- grant list
- statuses
- deadlines
- matches
- department priorities
</inputs>

<checks>
- flag match and staffing burden
- note reporting deadlines
- retire poor-fit opportunities
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
