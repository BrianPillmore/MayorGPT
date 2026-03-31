---
name: executive-brief
title: Executive Brief
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Executive Brief

## Use when

You need a one-page briefing for the mayor, city manager, or council on a fast-moving issue.

## Inputs to gather

- topic
- known facts
- decision needed
- deadline
- attachments

## Expected output

A short executive brief with issue, background, options, recommendation, risks, and next steps.

## Built-in checks

- front-load the decision
- use plain language
- highlight unknowns
- show time sensitivity

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with executive brief.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a one-page briefing for the mayor, city manager, or council on a fast-moving issue.
Produce a short executive brief with issue, background, options, recommendation, risks, and next steps.
</task>

<inputs>
- topic
- known facts
- decision needed
- deadline
- attachments
</inputs>

<checks>
- front-load the decision
- use plain language
- highlight unknowns
- show time sensitivity
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
