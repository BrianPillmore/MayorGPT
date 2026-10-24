---
name: city-manager-operations-review
title: City Manager Operations Review
type: prompt
category: weekly
---

# City Manager Operations Review

## Use when

The manager’s office needs a weekly operational review across departments.

## Inputs to gather

- department updates
- staffing issues
- project status
- incidents
- budget variances
- items carried over from last week
- council requests with deadlines
- cross-department dependencies
- items likely to reach the press

## Expected output

An operations review memo with cross-department blockers, deadlines, and executive decisions needed.

## Built-in checks

- name owners
- focus on risks and dependencies
- do not hide slippage
- name an owner and date for each blocker
- do not hide slippage or bad news
- separate decisions the manager can make from those needing council
- flag legal, safety, and media-sensitive items
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an operations analyst helping the city manager's office run a weekly cross-department review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted budget and appropriations, council direction log, delegation of authority, open meetings and public records rules]
SOURCE_MATERIALS: [department updates, staffing issues, project status, incident reports, budget variances, council requests, upcoming agenda items]
</context>

<task>
The manager’s office needs a weekly operational review across departments.
Produce: an operations review memo with cross-department blockers, deadlines, and executive decisions needed.
</task>

<inputs>
- department updates
- staffing issues
- project status
- incidents
- budget variances
- items carried over from last week
- council requests with deadlines
- cross-department dependencies
- items likely to reach the press
</inputs>

<checks>
- name owners
- focus on risks and dependencies
- do not hide slippage
- name an owner and date for each blocker
- do not hide slippage or bad news
- separate decisions the manager can make from those needing council
- flag legal, safety, and media-sensitive items
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. One-paragraph week summary
2. Cross-department blockers with owners
3. Deadlines in the next 14 days
4. Executive decisions needed
5. Risks and watch items
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
