---
name: emergency-proclamation
title: Emergency Proclamation
type: prompt
category: emergencies
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Emergency Proclamation

## Use when

The city is considering or preparing an emergency declaration or supporting order.

## Inputs to gather

- incident facts
- authority source
- geography affected
- time window
- requested powers or actions

## Expected output

A draft proclamation plus a legal/process checklist and public explanation.

## Built-in checks

- state authority clearly
- limit scope to what is needed
- flag publication/ratification needs

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with emergency proclamation.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is considering or preparing an emergency declaration or supporting order.
Produce a draft proclamation plus a legal/process checklist and public explanation.
</task>

<inputs>
- incident facts
- authority source
- geography affected
- time window
- requested powers or actions
</inputs>

<checks>
- state authority clearly
- limit scope to what is needed
- flag publication/ratification needs
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
