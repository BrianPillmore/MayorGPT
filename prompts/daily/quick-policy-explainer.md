---
name: quick-policy-explainer
title: Quick Policy Explainer
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Quick Policy Explainer

## Use when

You need to explain a city policy, ordinance, process, or decision in plain English.

## Inputs to gather

- policy text
- audience
- common misunderstandings
- what changed if anything

## Expected output

A plain-language explanation, FAQ bullets, and one-paragraph public summary.

## Built-in checks

- translate jargon
- note what the policy does and does not do
- cite source documents if asked

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with quick policy explainer.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need to explain a city policy, ordinance, process, or decision in plain English.
Produce a plain-language explanation, faq bullets, and one-paragraph public summary.
</task>

<inputs>
- policy text
- audience
- common misunderstandings
- what changed if anything
</inputs>

<checks>
- translate jargon
- note what the policy does and does not do
- cite source documents if asked
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
