---
name: budget-kickoff
title: Budget Kickoff
type: prompt
category: annual
---

# Budget Kickoff

## Use when

The city is opening its annual budget cycle and needs clear instructions and framing.

## Inputs to gather

- financial outlook
- manager priorities
- council goals
- calendar
- submission requirements
- known mandated cost increases
- revenue risk scenarios (base, downside)
- vacancy and overtime history
- decision criteria for supplemental requests

## Expected output

A budget kickoff memo, calendar, department instructions, and key assumptions.

## Built-in checks

- state recurring constraints
- name decision criteria
- explain calendar and review gates
- state recurring versus one-time constraints
- state how supplemental requests will be ranked
- list every review gate with date and owner
- do not promise funding for any request before council direction
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal budget analyst helping the finance director and city manager launch the annual budget cycle with clear instructions and shared assumptions.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and state budget calendar, adopted financial and reserve policies, council goals, labor agreements, submission templates]
SOURCE_MATERIALS: [multi-year forecast, prior-year actuals, council goals, labor and contract commitments, department request forms, capital plan status]
</context>

<task>
The city is opening its annual budget cycle and needs clear instructions and framing.
Produce: a budget kickoff memo, calendar, department instructions, and key assumptions.
</task>

<inputs>
- financial outlook
- manager priorities
- council goals
- calendar
- submission requirements
- known mandated cost increases
- revenue risk scenarios (base, downside)
- vacancy and overtime history
- decision criteria for supplemental requests
</inputs>

<checks>
- state recurring constraints
- name decision criteria
- explain calendar and review gates
- state recurring versus one-time constraints
- state how supplemental requests will be ranked
- list every review gate with date and owner
- do not promise funding for any request before council direction
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Kickoff memo from the city manager
2. Budget calendar with deadlines and review gates
3. Department instructions and submission checklist
4. Planning assumptions table (growth, inflation, labor, fuel, utilities)
5. Risks and open policy questions for council
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
