---
name: department-director-1on1
title: Department Director 1:1 Prep
type: prompt
category: weekly
---

# Department Director 1:1 Prep

## Use when

You need an agenda and follow-up tracker for recurring manager/director check-ins.

## Inputs to gather

- department status
- last follow-up items
- staffing and budget issues
- projects
- items overdue from last time
- director's requests for decisions
- cross-department dependencies
- development and recognition notes

## Expected output

A 1:1 agenda, key questions, decision points, and next-step tracker.

## Built-in checks

- keep it focused
- track unresolved items
- surface risks early
- keep the agenda to a few priorities
- track unresolved items with dates
- keep performance concerns factual and document them appropriately
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a management-coaching assistant helping the city manager or assistant manager run effective weekly director check-ins.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [personnel rules, delegation of authority, council direction log]
SOURCE_MATERIALS: [department status, last meeting's action items, staffing and budget issues, project milestones, council requests, performance concerns]
</context>

<task>
You need an agenda and follow-up tracker for recurring manager/director check-ins.
Produce: a 1:1 agenda, key questions, decision points, and next-step tracker.
</task>

<inputs>
- department status
- last follow-up items
- staffing and budget issues
- projects
- items overdue from last time
- director's requests for decisions
- cross-department dependencies
- development and recognition notes
</inputs>

<checks>
- keep it focused
- track unresolved items
- surface risks early
- keep the agenda to a few priorities
- track unresolved items with dates
- keep performance concerns factual and document them appropriately
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. 1:1 agenda
2. Key questions for the director
3. Decisions to make or defer
4. Action tracker with owners and dates
5. Follow-up message
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
