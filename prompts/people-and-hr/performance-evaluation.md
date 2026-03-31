---
name: performance-evaluation
title: Performance Evaluation
type: prompt
category: people-and-hr
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Performance Evaluation

## Use when

A supervisor needs help drafting a balanced, specific evaluation.

## Inputs to gather

- job expectations
- accomplishments
- issues
- metrics
- development goals

## Expected output

A performance review draft with strengths, opportunities, and development goals.

## Built-in checks

- be specific
- use evidence
- end with actionable development goals

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with performance evaluation.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A supervisor needs help drafting a balanced, specific evaluation.
Produce a performance review draft with strengths, opportunities, and development goals.
</task>

<inputs>
- job expectations
- accomplishments
- issues
- metrics
- development goals
</inputs>

<checks>
- be specific
- use evidence
- end with actionable development goals
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
