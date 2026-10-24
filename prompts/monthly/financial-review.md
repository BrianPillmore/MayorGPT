---
name: financial-review
title: Monthly Financial Review
type: prompt
category: monthly
---

# Monthly Financial Review

## Use when

Leadership needs a monthly look at revenues, expenditures, variances, cash, and claims.

## Inputs to gather

- revenue reports
- expense reports
- fund balances
- major claims
- known anomalies
- prior-year same-month comparison
- revenue sources most sensitive to the economy
- encumbrances and open purchase orders
- overtime and vacancy savings

## Expected output

A monthly finance memo explaining trendlines, outliers, and actions needed.

## Built-in checks

- separate timing variance from real variance
- note one-time items
- flag procurement or control concerns
- separate timing variance from true variance
- label one-time items
- flag unusual transactions, overspending, or procurement concerns for the finance director
- do not forecast beyond what the data supports
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal finance analyst helping leadership interpret monthly revenues, expenditures, and cash position.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted budget and amendments, fund accounting structure, reserve and investment policies, internal controls, state reporting requirements]
SOURCE_MATERIALS: [monthly revenue and expenditure reports, budget-to-actual by fund, cash and investment balances, large claims and payables, known anomalies]
</context>

<task>
Leadership needs a monthly look at revenues, expenditures, variances, cash, and claims.
Produce: a monthly finance memo explaining trendlines, outliers, and actions needed.
</task>

<inputs>
- revenue reports
- expense reports
- fund balances
- major claims
- known anomalies
- prior-year same-month comparison
- revenue sources most sensitive to the economy
- encumbrances and open purchase orders
- overtime and vacancy savings
</inputs>

<checks>
- separate timing variance from real variance
- note one-time items
- flag procurement or control concerns
- separate timing variance from true variance
- label one-time items
- flag unusual transactions, overspending, or procurement concerns for the finance director
- do not forecast beyond what the data supports
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Summary of position and trend
2. Variance table with driver and action
3. Cash and fund balance notes
4. Risks and corrective actions
5. Decisions needed from the manager or council
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
