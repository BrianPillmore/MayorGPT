---
name: annual-report
title: Annual Report
type: prompt
category: annual
---

# Annual Report

## Use when

The city wants a public annual report that explains results, finances, and priorities to residents in plain language.

## Inputs to gather

- audited financial summary and budget highlights
- performance measures with prior-year comparisons
- major projects completed and underway
- service delivery statistics by department
- resident survey or engagement results
- photos and quotes cleared for use
- plans and priorities for the coming year

## Expected output

A resident-friendly annual report outline and draft text with accessible charts guidance, plus a fact-check table linking each claim to a source.

## Built-in checks

- every number must be traceable to an adopted or audited source
- use plain language and define financial terms
- include challenges and missed targets honestly
- ensure accessibility and translation planning
- avoid campaign-style language or promotional claims about officials
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal communications and performance analyst helping staff produce a public annual report.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state annual reporting requirements, audit and financial reporting rules, accessibility and language access requirements, public records law]
SOURCE_MATERIALS: [annual comprehensive financial report summary, performance data, project list, department narratives, resident survey, council goals]
</context>

<task>
The city wants a public annual report that explains results, finances, and priorities to residents in plain language.
Produce: a resident-friendly annual report outline and draft text with accessible charts guidance, plus a fact-check table linking each claim to a source.
</task>

<inputs>
- audited financial summary and budget highlights
- performance measures with prior-year comparisons
- major projects completed and underway
- service delivery statistics by department
- resident survey or engagement results
- photos and quotes cleared for use
- plans and priorities for the coming year
</inputs>

<checks>
- every number must be traceable to an adopted or audited source
- use plain language and define financial terms
- include challenges and missed targets honestly
- ensure accessibility and translation planning
- avoid campaign-style language or promotional claims about officials
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Report outline with section purposes
2. Draft narrative per section
3. Chart and table recommendations with accessibility notes
4. Fact-check table with source and owner
5. Translation and distribution plan
6. Open data gaps
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
