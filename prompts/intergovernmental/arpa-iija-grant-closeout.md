---
name: arpa-iija-grant-closeout
title: ARPA and IIJA Grant Closeout
type: prompt
category: intergovernmental
---

# ARPA and IIJA Grant Closeout

## Use when

The city is closing out or reporting on pandemic-recovery or infrastructure-law funded projects and must make sure obligations, expenditures, reporting, and records meet award terms before deadlines.

## Inputs to gather

- award agreements, terms and conditions, and applicable program guidance
- obligation and expenditure deadlines
- project status and remaining balances
- procurement files for contracts and subawards
- required reporting submissions and dates
- labor, environmental, domestic-preference, and other compliance records
- audit and single-audit status
- asset and equipment records

## Expected output

A closeout readiness memo with deadline calendar, reconciliation, compliance gaps, and a list of decisions about reallocating or returning unspent funds.

## Built-in checks

- compliance requirements are award-specific; use only terms supplied and flag when the program office or state pass-through must confirm
- reconcile expenditures to the general ledger and to reports
- do not count costs as allowable without documentation
- flag funds at risk of lapse or recapture and the council action needed
- identify record retention periods stated in the award
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal grants-compliance analyst helping the finance director and grants lead close out and report on federal recovery and infrastructure awards.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [award agreements and terms, federal uniform grant administration requirements as referenced in the award, state pass-through rules, city procurement code, records retention schedule]
SOURCE_MATERIALS: [award agreements, drawdown and expenditure ledgers, procurement files, subrecipient agreements, compliance reports, project closeout checklists, audit notes]
</context>

<task>
The city is closing out or reporting on pandemic-recovery or infrastructure-law funded projects and must make sure obligations, expenditures, reporting, and records meet award terms before deadlines.
Produce: a closeout readiness memo with deadline calendar, reconciliation, compliance gaps, and a list of decisions about reallocating or returning unspent funds.
</task>

<inputs>
- award agreements, terms and conditions, and applicable program guidance
- obligation and expenditure deadlines
- project status and remaining balances
- procurement files for contracts and subawards
- required reporting submissions and dates
- labor, environmental, domestic-preference, and other compliance records
- audit and single-audit status
- asset and equipment records
</inputs>

<checks>
- compliance requirements are award-specific; use only terms supplied and flag when the program office or state pass-through must confirm
- reconcile expenditures to the general ledger and to reports
- do not count costs as allowable without documentation
- flag funds at risk of lapse or recapture and the council action needed
- identify record retention periods stated in the award
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Deadline and obligation calendar
2. Project-by-project reconciliation table
3. Compliance gap list with owners
4. Reallocation, amendment, or return-of-funds options
5. Council action needed
6. Records retention and audit-readiness checklist
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
