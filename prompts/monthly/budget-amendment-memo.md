---
name: budget-amendment-memo
title: Budget Amendment Memo
type: prompt
category: monthly
---

# Budget Amendment Memo

## Use when

A department or the finance office needs council approval to amend the adopted budget (transfer, supplemental appropriation, or reallocation) and needs a clear, compliant memo.

## Inputs to gather

- amendment amount, funds, and accounts affected
- reason and urgency
- funding source (fund balance, new revenue, grant, reallocation)
- recurring versus one-time effect
- budget authority rules (department head, manager, council thresholds)
- fund balance and reserve effect
- prior amendments this fiscal year

## Expected output

An amendment memo with fiscal effect, legal authority, alternatives, and draft council action language.

## Built-in checks

- confirm which level of approval the amount requires under the charter and budget policy and flag state-law variance
- label recurring versus one-time effects
- show effect on reserves and policy minimums
- do not use an amendment to evade a procurement or appropriation limit
- attach supporting documents
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal budget analyst helping staff prepare a budget amendment for council approval.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and budget law, adopted financial policies, appropriation and transfer authority, state budget law, grant agreement terms]
SOURCE_MATERIALS: [adopted budget, current budget-to-actual report, request memo, grant award, council history of related actions, reserve policy]
</context>

<task>
A department or the finance office needs council approval to amend the adopted budget (transfer, supplemental appropriation, or reallocation) and needs a clear, compliant memo.
Produce: an amendment memo with fiscal effect, legal authority, alternatives, and draft council action language.
</task>

<inputs>
- amendment amount, funds, and accounts affected
- reason and urgency
- funding source (fund balance, new revenue, grant, reallocation)
- recurring versus one-time effect
- budget authority rules (department head, manager, council thresholds)
- fund balance and reserve effect
- prior amendments this fiscal year
</inputs>

<checks>
- confirm which level of approval the amount requires under the charter and budget policy and flag state-law variance
- label recurring versus one-time effects
- show effect on reserves and policy minimums
- do not use an amendment to evade a procurement or appropriation limit
- attach supporting documents
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Action requested and amount
2. Reason and funding source
3. Fiscal and reserve effect (recurring and one-time)
4. Authority and approval path
5. Alternatives considered
6. Draft motion or resolution language
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
