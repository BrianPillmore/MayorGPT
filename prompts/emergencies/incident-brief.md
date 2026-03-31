---
name: incident-brief
title: Incident Brief
type: prompt
category: emergencies
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Incident Brief

## Use when

You need a rapid, leader-ready summary during an incident.

## Inputs to gather

- confirmed facts
- operational status
- resource needs
- public impact
- next update time

## Expected output

A situation report with facts, impacts, actions underway, asks, and message guidance.

## Built-in checks

- separate confirmed from unconfirmed
- note update cadence
- show public impacts first

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with incident brief.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a rapid, leader-ready summary during an incident.
Produce a situation report with facts, impacts, actions underway, asks, and message guidance.
</task>

<inputs>
- confirmed facts
- operational status
- resource needs
- public impact
- next update time
</inputs>

<checks>
- separate confirmed from unconfirmed
- note update cadence
- show public impacts first
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
