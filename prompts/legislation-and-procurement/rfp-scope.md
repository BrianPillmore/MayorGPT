---
name: rfp-scope
title: RFP Scope of Work
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# RFP Scope of Work

## Use when

The city needs a clear solicitation scope for services or products.

## Inputs to gather

- project need
- deliverables
- schedule
- budget range if known
- evaluation priorities

## Expected output

A scope of work plus evaluation criteria and vendor question list.

## Built-in checks

- write measurable deliverables
- avoid bias toward one vendor
- name minimum qualifications

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with rfp scope of work.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs a clear solicitation scope for services or products.
Produce a scope of work plus evaluation criteria and vendor question list.
</task>

<inputs>
- project need
- deliverables
- schedule
- budget range if known
- evaluation priorities
</inputs>

<checks>
- write measurable deliverables
- avoid bias toward one vendor
- name minimum qualifications
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
