---
name: cip-review
title: Capital Improvement Plan Review
type: prompt
category: quarterly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Capital Improvement Plan Review

## Use when

The city needs to review or re-rank capital projects.

## Inputs to gather

- project list
- cost estimates
- condition/risk data
- funding sources
- schedule pressures

## Expected output

A CIP review memo with ranking logic, recommended sequencing, funding notes, and deferral risks.

## Built-in checks

- distinguish maintenance from expansion
- show total cost of ownership
- flag funding assumptions

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with capital improvement plan review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs to review or re-rank capital projects.
Produce a cip review memo with ranking logic, recommended sequencing, funding notes, and deferral risks.
</task>

<inputs>
- project list
- cost estimates
- condition/risk data
- funding sources
- schedule pressures
</inputs>

<checks>
- distinguish maintenance from expansion
- show total cost of ownership
- flag funding assumptions
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
