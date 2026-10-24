---
name: grant-pipeline-review
title: Grant Pipeline Review
type: prompt
category: monthly
---

# Grant Pipeline Review

## Use when

The city wants a monthly snapshot of grants pursued, awarded, at-risk, or worth pursuing.

## Inputs to gather

- grant list
- statuses
- deadlines
- matches
- department priorities
- recurring costs created by each award
- closeout dates and allowable-cost windows
- audit exposure (single audit thresholds)
- awards at risk of lapse

## Expected output

A pipeline review with next applications, compliance deadlines, award risks, and decisions needed.

## Built-in checks

- flag match and staffing burden
- note reporting deadlines
- retire poor-fit opportunities
- flag match, maintenance-of-effort, and staffing burdens
- list reporting and closeout deadlines
- retire poor-fit opportunities rather than carrying them
- do not count unallowable costs as match
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a grants analyst helping the city review its pipeline of pursued, awarded, and prospective grants.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [federal uniform guidance and program terms for each award, state grant rules, council authorization for applications and match, city grants policy]
SOURCE_MATERIALS: [grant tracker, application and award status, deadlines, match and cost-share, reporting dates, department priorities, staff capacity]
</context>

<task>
The city wants a monthly snapshot of grants pursued, awarded, at-risk, or worth pursuing.
Produce: a pipeline review with next applications, compliance deadlines, award risks, and decisions needed.
</task>

<inputs>
- grant list
- statuses
- deadlines
- matches
- department priorities
- recurring costs created by each award
- closeout dates and allowable-cost windows
- audit exposure (single audit thresholds)
- awards at risk of lapse
</inputs>

<checks>
- flag match and staffing burden
- note reporting deadlines
- retire poor-fit opportunities
- flag match, maintenance-of-effort, and staffing burdens
- list reporting and closeout deadlines
- retire poor-fit opportunities rather than carrying them
- do not count unallowable costs as match
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Pipeline table by status
2. Next applications with go/no-go recommendation
3. Compliance and reporting calendar
4. Award risks
5. Decisions needed
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
