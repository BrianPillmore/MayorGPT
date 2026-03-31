---
name: goal-setting-retreat
title: Goal Setting Retreat
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Goal Setting Retreat

## Use when

The council or executive team is preparing for its annual retreat or planning session.

## Inputs to gather

- prior goals
- accomplishments
- unfinished work
- decision topics
- facilitation needs

## Expected output

A retreat packet with briefing memo, agenda, facilitation prompts, and draft goal language.

## Built-in checks

- separate strategic goals from staff tasks
- keep scope realistic
- prepare decision-ready materials

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with goal setting retreat.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The council or executive team is preparing for its annual retreat or planning session.
Produce a retreat packet with briefing memo, agenda, facilitation prompts, and draft goal language.
</task>

<inputs>
- prior goals
- accomplishments
- unfinished work
- decision topics
- facilitation needs
</inputs>

<checks>
- separate strategic goals from staff tasks
- keep scope realistic
- prepare decision-ready materials
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
