---
name: contract-approval-memo
title: Contract Approval Memo
type: prompt
category: legislation-and-procurement
---

# Contract Approval Memo

## Use when

A contract is moving to council or executive approval.

## Inputs to gather

- draft contract
- scope
- amount
- funding source
- procurement path
- risk issues
- renewal and termination terms
- total multi-year cost
- grant or restricted-fund conditions
- vendor performance history

## Expected output

An approval memo summarizing scope, cost, procurement path, key terms, and review status.

## Built-in checks

- state dollar value clearly
- show funding source
- note legal/procurement review completion
- state the dollar value and term at the top
- show the appropriation and funding source
- confirm procurement path and legal review are complete, or say what is outstanding
- flag indemnity, auto-renewal, and termination-for-convenience terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a contracts analyst helping staff prepare an approval memo for council or executive action on a contract.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [procurement code and signing-authority thresholds, state contracting rules, council action requirements, budget appropriation status]
SOURCE_MATERIALS: [draft contract, scope, amount and term, funding source and appropriation, procurement path, insurance and indemnity terms, legal and procurement review status]
</context>

<task>
A contract is moving to council or executive approval.
Produce: an approval memo summarizing scope, cost, procurement path, key terms, and review status.
</task>

<inputs>
- draft contract
- scope
- amount
- funding source
- procurement path
- risk issues
- renewal and termination terms
- total multi-year cost
- grant or restricted-fund conditions
- vendor performance history
</inputs>

<checks>
- state dollar value clearly
- show funding source
- note legal/procurement review completion
- state the dollar value and term at the top
- show the appropriation and funding source
- confirm procurement path and legal review are complete, or say what is outstanding
- flag indemnity, auto-renewal, and termination-for-convenience terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Summary of action requested
2. Scope, cost, and funding table
3. Procurement path and review status
4. Key terms and risks
5. Draft motion language
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
