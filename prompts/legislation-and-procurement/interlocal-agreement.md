---
name: interlocal-agreement
title: Interlocal Agreement Review
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Interlocal Agreement Review

## Use when

The city is evaluating or drafting an interlocal or cooperative agreement.

## Inputs to gather

- draft agreement
- parties
- services or cost sharing
- term
- termination

## Expected output

A review memo plus revision suggestions and approval checklist.

## Built-in checks

- clarify roles, cost, term, indemnity, termination, and records obligations

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with interlocal agreement review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is evaluating or drafting an interlocal or cooperative agreement.
Produce a review memo plus revision suggestions and approval checklist.
</task>

<inputs>
- draft agreement
- parties
- services or cost sharing
- term
- termination
</inputs>

<checks>
- clarify roles, cost, term, indemnity, termination, and records obligations
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
