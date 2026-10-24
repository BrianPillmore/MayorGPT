---
name: interlocal-agreement
title: Interlocal Agreement Review
type: prompt
category: legislation-and-procurement
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
- governance (who decides, how disputes resolve)
- liability, indemnity, and insurance
- staffing and asset ownership
- records and data-sharing

## Expected output

A review memo plus revision suggestions and approval checklist.

## Built-in checks

- clarify roles, cost, term, indemnity, termination, and records obligations
- check the city has authority to enter the agreement and any required approvals; flag state-law variance
- do not assume immunity or caps apply without attorney confirmation
- identify exit costs
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an intergovernmental-agreements analyst helping review or draft an interlocal or cooperative agreement.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state interlocal-cooperation law, charter authority to contract, council approval and filing or recording requirements, insurance and immunity rules]
SOURCE_MATERIALS: [draft agreement, party list, service description, cost-sharing formula, term and termination clauses, governance and dispute provisions, prior agreements]
</context>

<task>
The city is evaluating or drafting an interlocal or cooperative agreement.
Produce: a review memo plus revision suggestions and approval checklist.
</task>

<inputs>
- draft agreement
- parties
- services or cost sharing
- term
- termination
- governance (who decides, how disputes resolve)
- liability, indemnity, and insurance
- staffing and asset ownership
- records and data-sharing
</inputs>

<checks>
- clarify roles, cost, term, indemnity, termination, and records obligations
- check the city has authority to enter the agreement and any required approvals; flag state-law variance
- do not assume immunity or caps apply without attorney confirmation
- identify exit costs
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Plain-language summary of the deal
2. Issue table with proposed revisions
3. Approval and filing checklist
4. Risks to the city
5. Questions for the other parties
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
