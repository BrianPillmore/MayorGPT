---
name: meeting-prep
title: Meeting Prep
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Meeting Prep

## Use when

You need talking points, questions, and motion pathways before a council or board meeting.

## Inputs to gather

- agenda
- staff reports
- ordinances/resolutions
- fiscal notes
- known controversies

## Expected output

Item-by-item prep notes, likely questions, possible motions, and risk flags.

## Built-in checks

- align to agenda order
- flag missing attachments
- identify legal/fiscal review needs

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with meeting prep.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need talking points, questions, and motion pathways before a council or board meeting.
Produce item-by-item prep notes, likely questions, possible motions, and risk flags.
</task>

<inputs>
- agenda
- staff reports
- ordinances/resolutions
- fiscal notes
- known controversies
</inputs>

<checks>
- align to agenda order
- flag missing attachments
- identify legal/fiscal review needs
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
