---
name: risk-register-update
title: Risk Register Update
type: prompt
category: quarterly
---

# Risk Register Update

## Use when

Leadership needs a practical refresh of operational, fiscal, legal, reputational, and safety risks.

## Inputs to gather

- current risk list
- incidents
- audit notes
- claims/issues
- department input
- likelihood and impact scoring scale
- risk owners
- mitigation status and cost
- risks that crossed a threshold this quarter

## Expected output

An updated risk register with severity, trend, mitigation owners, and next actions.

## Built-in checks

- name top risks clearly
- show trend direction
- do not bury reputational or compliance issues
- name top risks clearly and show trend
- do not bury compliance or reputational risks
- every risk needs an owner and a next action
- route claims and litigation-sensitive items to the city attorney or risk manager
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal risk analyst helping leadership refresh the enterprise risk register.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city risk-management policy, insurance pool or carrier terms, audit findings, claims history, regulatory deadlines]
SOURCE_MATERIALS: [prior risk register, incidents, claims, audit notes, department input, near misses, regulatory changes, insurance renewal data]
</context>

<task>
Leadership needs a practical refresh of operational, fiscal, legal, reputational, and safety risks.
Produce: an updated risk register with severity, trend, mitigation owners, and next actions.
</task>

<inputs>
- current risk list
- incidents
- audit notes
- claims/issues
- department input
- likelihood and impact scoring scale
- risk owners
- mitigation status and cost
- risks that crossed a threshold this quarter
</inputs>

<checks>
- name top risks clearly
- show trend direction
- do not bury reputational or compliance issues
- name top risks clearly and show trend
- do not bury compliance or reputational risks
- every risk needs an owner and a next action
- route claims and litigation-sensitive items to the city attorney or risk manager
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Top-ten risk summary
2. Updated register with score, trend, owner, mitigation
3. New and retired risks with reasons
4. Escalations for the manager or council
5. Next-quarter actions
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
