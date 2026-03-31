---
name: performance-memo
title: Monthly Performance Memo
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Monthly Performance Memo

## Use when

Leadership wants a monthly performance narrative across service areas.

## Inputs to gather

- KPIs
- service levels
- trends
- incident notes
- department commentary

## Expected output

A short memo explaining what moved, why it moved, and what management is doing next.

## Built-in checks

- avoid data dump
- name drivers
- connect metrics to decisions

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with monthly performance memo.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Leadership wants a monthly performance narrative across service areas.
Produce a short memo explaining what moved, why it moved, and what management is doing next.
</task>

<inputs>
- KPIs
- service levels
- trends
- incident notes
- department commentary
</inputs>

<checks>
- avoid data dump
- name drivers
- connect metrics to decisions
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
