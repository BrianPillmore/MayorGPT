---
name: hiring-scorecard
title: Hiring Scorecard
type: prompt
category: people-and-hr
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Hiring Scorecard

## Use when

The city needs a structured interview and evaluation tool for hiring.

## Inputs to gather

- job description
- must-have competencies
- leadership traits
- panel size

## Expected output

A scorecard, question set, and interview packet.

## Built-in checks

- use job-related criteria only
- avoid discriminatory questions
- separate must-haves from stretch qualities

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with hiring scorecard.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a structured interview and evaluation tool for hiring.
Produce a scorecard, question set, and interview packet.
</task>

<inputs>
- job description
- must-have competencies
- leadership traits
- panel size
</inputs>

<checks>
- use job-related criteria only
- avoid discriminatory questions
- separate must-haves from stretch qualities
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
