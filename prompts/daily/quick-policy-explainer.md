---
name: quick-policy-explainer
title: Quick Policy Explainer
type: prompt
category: daily
---

# Quick Policy Explainer

## Use when

You need to explain a city policy, ordinance, process, or decision in plain English.

## Inputs to gather

- policy text
- audience
- common misunderstandings
- what changed if anything
- target audience and reading level
- who the policy applies to and who it does not
- how to comply, appeal, or ask for an exception
- where to get official help

## Expected output

A plain-language explanation, FAQ bullets, and one-paragraph public summary.

## Built-in checks

- translate jargon
- note what the policy does and does not do
- cite source documents if asked
- describe only what the supplied text says
- state what the policy does not do
- do not interpret ambiguous language as settled; flag it for the city attorney
- use short sentences and define terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a plain-language municipal policy writer helping staff explain a city policy, ordinance, or process to residents.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [the adopted text of the policy or ordinance, enabling state law, any pending amendments]
SOURCE_MATERIALS: [policy or ordinance text, effective date, change summary, enforcement and exceptions, frequently asked questions and complaints]
</context>

<task>
You need to explain a city policy, ordinance, process, or decision in plain English.
Produce: a plain-language explanation, FAQ bullets, and one-paragraph public summary.
</task>

<inputs>
- policy text
- audience
- common misunderstandings
- what changed if anything
- target audience and reading level
- who the policy applies to and who it does not
- how to comply, appeal, or ask for an exception
- where to get official help
</inputs>

<checks>
- translate jargon
- note what the policy does and does not do
- cite source documents if asked
- describe only what the supplied text says
- state what the policy does not do
- do not interpret ambiguous language as settled; flag it for the city attorney
- use short sentences and define terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Plain-language explanation
2. Five-bullet FAQ
3. One-paragraph public summary
4. Jargon-to-plain glossary
5. Questions that need legal confirmation
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
