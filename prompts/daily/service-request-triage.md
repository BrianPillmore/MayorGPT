---
name: service-request-triage
title: Service Request Triage
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Service Request Triage

## Use when

The city needs to route resident or internal service requests quickly and consistently.

## Inputs to gather

- request text
- location
- urgency
- photos/docs if any
- known department ownership

## Expected output

A triage summary with owner, urgency, service category, resident-facing response, and escalation need.

## Built-in checks

- identify safety issues first
- route to correct department
- note repeat issues

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with service request triage.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs to route resident or internal service requests quickly and consistently.
Produce a triage summary with owner, urgency, service category, resident-facing response, and escalation need.
</task>

<inputs>
- request text
- location
- urgency
- photos/docs if any
- known department ownership
</inputs>

<checks>
- identify safety issues first
- route to correct department
- note repeat issues
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
