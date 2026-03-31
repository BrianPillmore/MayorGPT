---
name: town-hall-briefing
title: Town Hall Briefing
type: prompt
category: public-engagement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Town Hall Briefing

## Use when

You need a structured prep packet for a public meeting, town hall, or listening session.

## Inputs to gather

- topic
- audience
- venue/format
- likely concerns
- known facts

## Expected output

An event brief with agenda, messages, ground rules, likely questions, and follow-up plan.

## Built-in checks

- make the purpose clear
- prepare for hard questions
- plan follow-up and note-taking

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with town hall briefing.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a structured prep packet for a public meeting, town hall, or listening session.
Produce an event brief with agenda, messages, ground rules, likely questions, and follow-up plan.
</task>

<inputs>
- topic
- audience
- venue/format
- likely concerns
- known facts
</inputs>

<checks>
- make the purpose clear
- prepare for hard questions
- plan follow-up and note-taking
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
