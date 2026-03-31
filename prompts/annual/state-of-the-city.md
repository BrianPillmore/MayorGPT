---
name: state-of-the-city
title: State of the City
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# State of the City

## Use when

The mayor or manager needs an annual community narrative.

## Inputs to gather

- major wins
- major challenges
- data points
- project list
- public tone

## Expected output

A speech or report that balances celebration, honesty, and the year ahead.

## Built-in checks

- be specific
- avoid hype
- show residents why the story matters

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with state of the city.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The mayor or manager needs an annual community narrative.
Produce a speech or report that balances celebration, honesty, and the year ahead.
</task>

<inputs>
- major wins
- major challenges
- data points
- project list
- public tone
</inputs>

<checks>
- be specific
- avoid hype
- show residents why the story matters
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
