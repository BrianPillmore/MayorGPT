---
name: development-pipeline-review
title: Development Pipeline Review
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Development Pipeline Review

## Use when

Leadership wants a weekly picture of pending development activity and pressure points.

## Inputs to gather

- active applications
- case status
- major developers
- utility/traffic issues
- public concerns

## Expected output

A pipeline memo summarizing near-term cases, constraints, and decisions likely to reach council.

## Built-in checks

- note hearing schedule
- flag infrastructure gaps
- distinguish rumor from filed application

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with development pipeline review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Leadership wants a weekly picture of pending development activity and pressure points.
Produce a pipeline memo summarizing near-term cases, constraints, and decisions likely to reach council.
</task>

<inputs>
- active applications
- case status
- major developers
- utility/traffic issues
- public concerns
</inputs>

<checks>
- note hearing schedule
- flag infrastructure gaps
- distinguish rumor from filed application
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
