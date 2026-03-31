---
name: utility-rate-watch
title: Utility Rate Watch
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Utility Rate Watch

## Use when

Utility leadership or council needs a recurring rate and system pressure scan.

## Inputs to gather

- operating costs
- capital needs
- customer impacts
- benchmark data
- compliance issues

## Expected output

A rate watch memo with pressures, scenarios, timing options, and customer communication needs.

## Built-in checks

- show customer and system impacts
- flag compliance drivers
- separate current rates from future options

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with utility rate watch.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Utility leadership or council needs a recurring rate and system pressure scan.
Produce a rate watch memo with pressures, scenarios, timing options, and customer communication needs.
</task>

<inputs>
- operating costs
- capital needs
- customer impacts
- benchmark data
- compliance issues
</inputs>

<checks>
- show customer and system impacts
- flag compliance drivers
- separate current rates from future options
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
