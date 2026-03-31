---
name: difficult-email
title: Difficult Email Response
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Difficult Email Response

## Use when

You need to respond to an angry, accusatory, or politically sensitive email without escalating conflict.

## Inputs to gather

- incoming email
- facts known
- what can be said
- desired boundary

## Expected output

A measured response draft plus a shorter alternative and internal risk notes.

## Built-in checks

- stay calm
- avoid defensiveness
- do not concede facts not established
- set boundaries politely

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with difficult email response.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need to respond to an angry, accusatory, or politically sensitive email without escalating conflict.
Produce a measured response draft plus a shorter alternative and internal risk notes.
</task>

<inputs>
- incoming email
- facts known
- what can be said
- desired boundary
</inputs>

<checks>
- stay calm
- avoid defensiveness
- do not concede facts not established
- set boundaries politely
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
