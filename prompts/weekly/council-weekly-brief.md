---
name: council-weekly-brief
title: Council Weekly Brief
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Council Weekly Brief

## Use when

The governing body needs a weekly strategic and operational snapshot.

## Inputs to gather

- priority projects
- public issues
- finance watch items
- upcoming meetings
- department notes

## Expected output

A weekly council brief with wins, watch items, decisions ahead, and questions for follow-up.

## Built-in checks

- balance positive and hard news
- separate info from action
- be concise but specific

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with council weekly brief.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The governing body needs a weekly strategic and operational snapshot.
Produce a weekly council brief with wins, watch items, decisions ahead, and questions for follow-up.
</task>

<inputs>
- priority projects
- public issues
- finance watch items
- upcoming meetings
- department notes
</inputs>

<checks>
- balance positive and hard news
- separate info from action
- be concise but specific
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
