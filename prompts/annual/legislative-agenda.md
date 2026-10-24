---
name: legislative-agenda
title: Legislative Agenda
type: prompt
category: annual
---

# Legislative Agenda

## Use when

The city is setting its annual policy and advocacy priorities with outside governments.

## Inputs to gather

- priority issues
- draft asks
- partner landscape
- data points
- current law constraints
- tiering of asks (must-win, important, monitor)
- specific appropriation or statutory language requested
- named legislative champions and committees
- the municipal league position on each issue

## Expected output

A concise legislative agenda with talking points and priority tiers.

## Built-in checks

- state requests in actionable terms
- support with local impact
- avoid conflicting asks
- every ask is a concrete action, not a theme
- each ask shows local impact with data
- identify conflicts with league, county, or regional partner positions
- do not describe a bill's effect beyond what its text supports
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal intergovernmental-affairs analyst helping the city set annual state and federal advocacy priorities.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state municipal league priorities, session calendar, council-adopted advocacy policy, lobbying and public-funds rules, preemption landscape in the state]
SOURCE_MATERIALS: [council goals, prior-year agenda results, bill watch list, partner and coalition list, fiscal data on proposed asks, staff and department requests]
</context>

<task>
The city is setting its annual policy and advocacy priorities with outside governments.
Produce: a concise legislative agenda with talking points and priority tiers.
</task>

<inputs>
- priority issues
- draft asks
- partner landscape
- data points
- current law constraints
- tiering of asks (must-win, important, monitor)
- specific appropriation or statutory language requested
- named legislative champions and committees
- the municipal league position on each issue
</inputs>

<checks>
- state requests in actionable terms
- support with local impact
- avoid conflicting asks
- every ask is a concrete action, not a theme
- each ask shows local impact with data
- identify conflicts with league, county, or regional partner positions
- do not describe a bill's effect beyond what its text supports
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. One-page agenda by priority tier
2. Issue sheets with ask, local impact, and talking points
3. Coalition and champion map
4. Calendar of advocacy touchpoints
5. Items requiring council adoption before advocacy begins
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
