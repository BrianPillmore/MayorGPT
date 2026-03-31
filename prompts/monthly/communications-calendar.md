---
name: communications-calendar
title: Communications Calendar
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Communications Calendar

## Use when

The city needs a proactive monthly communication plan tied to projects, meetings, and events.

## Inputs to gather

- projects
- events
- holidays
- meeting dates
- known public issues

## Expected output

A channel-by-channel monthly communications calendar with message themes and owner assignments.

## Built-in checks

- balance proactive and reactive content
- account for approval needs
- avoid overpromising deadlines

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with communications calendar.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a proactive monthly communication plan tied to projects, meetings, and events.
Produce a channel-by-channel monthly communications calendar with message themes and owner assignments.
</task>

<inputs>
- projects
- events
- holidays
- meeting dates
- known public issues
</inputs>

<checks>
- balance proactive and reactive content
- account for approval needs
- avoid overpromising deadlines
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
