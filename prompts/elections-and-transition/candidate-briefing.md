---
name: candidate-briefing
title: Candidate Briefing
type: prompt
category: elections-and-transition
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Candidate Briefing

## Use when

The city wants a neutral, educational briefing for candidates or prospective candidates.

## Inputs to gather

- governance structure
- meeting schedule
- major issues
- ethics/legal boundaries
- fiscal facts

## Expected output

A neutral briefing deck or memo explaining roles, process, and major city issues.

## Built-in checks

- stay nonpartisan
- separate fact from advocacy
- avoid campaign advice

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with candidate briefing.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city wants a neutral, educational briefing for candidates or prospective candidates.
Produce a neutral briefing deck or memo explaining roles, process, and major city issues.
</task>

<inputs>
- governance structure
- meeting schedule
- major issues
- ethics/legal boundaries
- fiscal facts
</inputs>

<checks>
- stay nonpartisan
- separate fact from advocacy
- avoid campaign advice
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
