---
name: development-pipeline-review
title: Development Pipeline Review
type: prompt
category: weekly
---

# Development Pipeline Review

## Use when

Leadership wants a weekly picture of pending development activity and pressure points.

## Inputs to gather

- active applications
- case status
- major developers
- utility/traffic issues
- public concerns
- statutory review deadlines
- quasi-judicial matters where officials should avoid contact
- infrastructure capacity constraints
- fiscal impact of near-term projects

## Expected output

A pipeline memo summarizing near-term cases, constraints, and decisions likely to reach council.

## Built-in checks

- note hearing schedule
- flag infrastructure gaps
- distinguish rumor from filed application
- distinguish filed applications from rumors
- note hearing schedule and review deadlines and flag state-law variance
- keep quasi-judicial communications on the record
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a development-services analyst helping leadership watch pending development applications and infrastructure pressure.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [zoning code and review timelines, state shot-clock and approval-deadline rules, quasi-judicial procedure and ex parte rules, public records law]
SOURCE_MATERIALS: [active applications, case status, hearing dates, utility and traffic reviews, developer contact notes, public comments, pending annexations or agreements]
</context>

<task>
Leadership wants a weekly picture of pending development activity and pressure points.
Produce: a pipeline memo summarizing near-term cases, constraints, and decisions likely to reach council.
</task>

<inputs>
- active applications
- case status
- major developers
- utility/traffic issues
- public concerns
- statutory review deadlines
- quasi-judicial matters where officials should avoid contact
- infrastructure capacity constraints
- fiscal impact of near-term projects
</inputs>

<checks>
- note hearing schedule
- flag infrastructure gaps
- distinguish rumor from filed application
- distinguish filed applications from rumors
- note hearing schedule and review deadlines and flag state-law variance
- keep quasi-judicial communications on the record
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Near-term cases with status
2. Constraints and dependencies
3. Decisions likely to reach council
4. Public concern summary
5. Items for the city attorney
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
