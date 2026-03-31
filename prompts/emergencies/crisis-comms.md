---
name: crisis-comms
title: Crisis Communications
type: prompt
category: emergencies
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Crisis Communications

## Use when

The city must communicate during a high-stakes operational or reputational incident.

## Inputs to gather

- incident facts
- audiences
- what cannot yet be said
- spokesperson
- channels

## Expected output

A message house, holding statement, FAQs, and update cadence.

## Built-in checks

- be empathetic
- do not speculate
- say when next update is expected

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with crisis communications.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city must communicate during a high-stakes operational or reputational incident.
Produce a message house, holding statement, faqs, and update cadence.
</task>

<inputs>
- incident facts
- audiences
- what cannot yet be said
- spokesperson
- channels
</inputs>

<checks>
- be empathetic
- do not speculate
- say when next update is expected
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
