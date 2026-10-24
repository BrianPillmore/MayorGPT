---
name: rfp-scope
title: RFP Scope of Work
type: prompt
category: legislation-and-procurement
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
- submission format and due date
- questions-and-addenda process
- evaluation weights
- contact restrictions during the solicitation

## Expected output

A scope of work plus evaluation criteria and vendor question list.

## Built-in checks

- write measurable deliverables
- avoid bias toward one vendor
- name minimum qualifications
- avoid brand names or specs that favor one vendor
- publish evaluation criteria and weights before issuing
- have procurement and the city attorney review before release
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a procurement analyst helping a department write a clear, competitive solicitation scope.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [procurement code and thresholds, state competitive solicitation rules, standard terms and insurance requirements, accessibility and local-preference rules]
SOURCE_MATERIALS: [project need, deliverables, schedule, budget range, evaluation priorities, minimum qualifications, required terms, prior scopes]
</context>

<task>
The city needs a clear solicitation scope for services or products.
Produce: a scope of work plus evaluation criteria and vendor question list.
</task>

<inputs>
- project need
- deliverables
- schedule
- budget range if known
- evaluation priorities
- submission format and due date
- questions-and-addenda process
- evaluation weights
- contact restrictions during the solicitation
</inputs>

<checks>
- write measurable deliverables
- avoid bias toward one vendor
- name minimum qualifications
- avoid brand names or specs that favor one vendor
- publish evaluation criteria and weights before issuing
- have procurement and the city attorney review before release
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Scope of work
2. Minimum qualifications and evaluation criteria with weights
3. Schedule and submission instructions
4. Vendor question list for pre-bid
5. Issues for procurement or legal review
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
