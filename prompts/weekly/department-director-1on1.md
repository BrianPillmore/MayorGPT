---
name: department-director-1on1
title: Department Director 1:1 Prep
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Department Director 1:1 Prep

## Use when

You need an agenda and follow-up tracker for recurring manager/director check-ins.

## Inputs to gather

- department status
- last follow-up items
- staffing and budget issues
- projects

## Expected output

A 1:1 agenda, key questions, decision points, and next-step tracker.

## Built-in checks

- keep it focused
- track unresolved items
- surface risks early

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with department director 1:1 prep.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need an agenda and follow-up tracker for recurring manager/director check-ins.
Produce a 1:1 agenda, key questions, decision points, and next-step tracker.
</task>

<inputs>
- department status
- last follow-up items
- staffing and budget issues
- projects
</inputs>

<checks>
- keep it focused
- track unresolved items
- surface risks early
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
