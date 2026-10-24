---
name: staff-report
title: Staff Report Builder
type: prompt
category: monthly
---

# Staff Report Builder

## Use when

You need a clean, decision-ready staff report for council, a board, or a commission.

## Inputs to gather

- issue
- background
- legal/process requirements
- fiscal impact
- recommended action
- authority and decision body
- required findings or criteria
- funding source and appropriation
- prior related actions

## Expected output

A staff report with summary, background, analysis, options, recommendation, attachments, and action language.

## Built-in checks

- align recommendation to authority
- state fiscal impact clearly
- use neutral analysis before recommendation
- present neutral analysis before the recommendation
- align the recommendation with the body's actual authority
- state fiscal impact in dollars and recurring versus one-time
- attach or list every source document
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal staff-report writer helping a department prepare a decision-ready report for council, a board, or a commission.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted staff-report template, charter and code authority for the action, required findings, open meetings and notice requirements]
SOURCE_MATERIALS: [issue statement, background, legal requirements, fiscal impact, alternatives considered, public input, recommended action, attachments]
</context>

<task>
You need a clean, decision-ready staff report for council, a board, or a commission.
Produce: a staff report with summary, background, analysis, options, recommendation, attachments, and action language.
</task>

<inputs>
- issue
- background
- legal/process requirements
- fiscal impact
- recommended action
- authority and decision body
- required findings or criteria
- funding source and appropriation
- prior related actions
</inputs>

<checks>
- align recommendation to authority
- state fiscal impact clearly
- use neutral analysis before recommendation
- present neutral analysis before the recommendation
- align the recommendation with the body's actual authority
- state fiscal impact in dollars and recurring versus one-time
- attach or list every source document
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Summary and recommended action
2. Background and analysis
3. Options with pros and cons
4. Fiscal impact
5. Draft motion language
6. Attachment list and review sign-offs
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
