---
name: councilmember-daily-brief
title: Councilmember Daily Brief
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Councilmember Daily Brief

## Use when

A councilmember needs a concise update on hot issues, resident concerns, and upcoming decision points.

## Inputs to gather

- ward issues
- city-wide issues
- agenda timeline
- constituent themes
- media themes

## Expected output

A compact daily memo grouped into watch items, resident issues, decisions ahead, and suggested follow-up.

## Built-in checks

- no staff micromanagement
- flag city-wide service and budget impacts
- note whether item is official or informal

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with councilmember daily brief.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A councilmember needs a concise update on hot issues, resident concerns, and upcoming decision points.
Produce a compact daily memo grouped into watch items, resident issues, decisions ahead, and suggested follow-up.
</task>

<inputs>
- ward issues
- city-wide issues
- agenda timeline
- constituent themes
- media themes
</inputs>

<checks>
- no staff micromanagement
- flag city-wide service and budget impacts
- note whether item is official or informal
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
