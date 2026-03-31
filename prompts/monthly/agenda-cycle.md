---
name: agenda-cycle
title: Agenda Cycle
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Agenda Cycle

## Use when

The city is building a regular or special meeting agenda packet.

## Inputs to gather

- proposed items
- draft staff reports
- ordinances/resolutions
- attachments
- posting deadlines

## Expected output

A draft agenda order, packet checklist, missing items list, and item-by-item readiness status.

## Built-in checks

- confirm hearing/publication needs
- flag incomplete fiscal impact
- spot missing exhibits

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with agenda cycle.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is building a regular or special meeting agenda packet.
Produce a draft agenda order, packet checklist, missing items list, and item-by-item readiness status.
</task>

<inputs>
- proposed items
- draft staff reports
- ordinances/resolutions
- attachments
- posting deadlines
</inputs>

<checks>
- confirm hearing/publication needs
- flag incomplete fiscal impact
- spot missing exhibits
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
