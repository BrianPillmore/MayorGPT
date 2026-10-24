---
name: first-100-days-plan
title: First 100 Days Plan
type: prompt
category: elections-and-transition
---

# First 100 Days Plan

## Use when

A newly elected mayor, councilmember, or new city manager needs a realistic plan for listening, learning, building relationships, and securing early wins in the first 100 days.

## Inputs to gather

- role, charter powers, and authority boundaries
- campaign or appointment commitments (as public commitments only)
- transition memo and briefing materials
- calendar of council meetings, budget deadlines, and legal deadlines
- key relationships to build (council, staff, regional partners, community)
- early-win candidates that need no new budget or ordinance
- known crises or sensitive issues

## Expected output

A 100-day plan with listening tour, learning agenda, relationship map, early wins, communication rhythm, and a list of decisions to avoid or defer.

## Built-in checks

- stay within charter role boundaries
- keep campaign promises separate from what the office can deliver, and say which need council or budget action
- do not direct staff outside lawful channels
- schedule time to learn finances, contracts, and litigation exposure before committing
- keep use of city resources within ethics rules
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal chief-of-staff and governance advisor helping a new official plan the first 100 days.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code, council rules of procedure, ethics code, open meetings and public records law, budget calendar]
SOURCE_MATERIALS: [transition memo, charter, budget summary, calendar, prior goals, stakeholder list, campaign commitments as public statements]
</context>

<task>
A newly elected mayor, councilmember, or new city manager needs a realistic plan for listening, learning, building relationships, and securing early wins in the first 100 days.
Produce: a 100-day plan with listening tour, learning agenda, relationship map, early wins, communication rhythm, and a list of decisions to avoid or defer.
</task>

<inputs>
- role, charter powers, and authority boundaries
- campaign or appointment commitments (as public commitments only)
- transition memo and briefing materials
- calendar of council meetings, budget deadlines, and legal deadlines
- key relationships to build (council, staff, regional partners, community)
- early-win candidates that need no new budget or ordinance
- known crises or sensitive issues
</inputs>

<checks>
- stay within charter role boundaries
- keep campaign promises separate from what the office can deliver, and say which need council or budget action
- do not direct staff outside lawful channels
- schedule time to learn finances, contracts, and litigation exposure before committing
- keep use of city resources within ethics rules
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Role and authority summary
2. Days 1-30 learn, 31-60 build, 61-100 deliver plan
3. Listening tour schedule and question set
4. Early-win candidates with feasibility and approval path
5. Relationship map and communications rhythm
6. Decisions to defer and risks
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
