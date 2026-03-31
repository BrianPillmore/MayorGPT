---
name: campaign-to-governance-boundary
title: Campaign to Governance Boundary
type: prompt
category: elections-and-transition
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Campaign to Governance Boundary

## Use when

A candidate or officeholder needs help respecting the line between campaigning and official acts.

## Inputs to gather

- draft communication
- audience
- timing
- use of city resources
- event context

## Expected output

A boundary memo noting what is safe, risky, or requires legal/policy review.

## Built-in checks

- protect public resources
- separate campaign from city business
- flag ethics concerns

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with campaign to governance boundary.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A candidate or officeholder needs help respecting the line between campaigning and official acts.
Produce a boundary memo noting what is safe, risky, or requires legal/policy review.
</task>

<inputs>
- draft communication
- audience
- timing
- use of city resources
- event context
</inputs>

<checks>
- protect public resources
- separate campaign from city business
- flag ethics concerns
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
