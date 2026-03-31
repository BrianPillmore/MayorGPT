---
name: media-talking-points
title: Media Talking Points
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Media Talking Points

## Use when

A leader or spokesperson needs concise public-facing talking points for media or stakeholder calls.

## Inputs to gather

- topic
- audience
- facts confirmed
- sensitive facts
- quote source if any

## Expected output

Core messages, quotable language, do-not-say notes, and likely Q&A.

## Built-in checks

- do not speculate
- stay on-record appropriate
- show empathy when needed

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with media talking points.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A leader or spokesperson needs concise public-facing talking points for media or stakeholder calls.
Produce core messages, quotable language, do-not-say notes, and likely q&a.
</task>

<inputs>
- topic
- audience
- facts confirmed
- sensitive facts
- quote source if any
</inputs>

<checks>
- do not speculate
- stay on-record appropriate
- show empathy when needed
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
