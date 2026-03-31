---
name: survey-summary
title: Survey Summary
type: prompt
category: public-engagement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Survey Summary

## Use when

The city wants a readable synthesis of resident survey results.

## Inputs to gather

- survey results
- demographic cuts if any
- open-ended responses
- purpose of survey

## Expected output

A summary with toplines, notable splits, open-ended themes, and suggested next steps.

## Built-in checks

- state sample limitations
- separate strong results from weak signals
- avoid false precision

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with survey summary.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city wants a readable synthesis of resident survey results.
Produce a summary with toplines, notable splits, open-ended themes, and suggested next steps.
</task>

<inputs>
- survey results
- demographic cuts if any
- open-ended responses
- purpose of survey
</inputs>

<checks>
- state sample limitations
- separate strong results from weak signals
- avoid false precision
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
