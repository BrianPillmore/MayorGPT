---
name: legislative-monitor
title: Legislative Monitor
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Legislative Monitor

## Use when

The city needs a running summary of state or regional legislation that could affect operations or authority.

## Inputs to gather

- bill list
- policy area
- city interests
- sponsor/status notes

## Expected output

A short weekly legislative memo with implications, recommended posture, and questions for advocacy.

## Built-in checks

- state status clearly
- note operational impact
- do not overclaim legal effect

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with legislative monitor.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a running summary of state or regional legislation that could affect operations or authority.
Produce a short weekly legislative memo with implications, recommended posture, and questions for advocacy.
</task>

<inputs>
- bill list
- policy area
- city interests
- sponsor/status notes
</inputs>

<checks>
- state status clearly
- note operational impact
- do not overclaim legal effect
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
