---
name: intergovernmental-relations-brief
title: Intergovernmental Relations Brief
type: prompt
category: quarterly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Intergovernmental Relations Brief

## Use when

The mayor or manager needs a concise regional/state/federal relationship brief.

## Inputs to gather

- partner list
- current asks
- upcoming meetings
- funding/policy issues
- coalition notes

## Expected output

A brief with partner status, current asks, sensitivities, and next engagement steps.

## Built-in checks

- state asks precisely
- show mutual benefit
- note political or timing sensitivities

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with intergovernmental relations brief.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The mayor or manager needs a concise regional/state/federal relationship brief.
Produce a brief with partner status, current asks, sensitivities, and next engagement steps.
</task>

<inputs>
- partner list
- current asks
- upcoming meetings
- funding/policy issues
- coalition notes
</inputs>

<checks>
- state asks precisely
- show mutual benefit
- note political or timing sensitivities
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
