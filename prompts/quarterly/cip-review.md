---
name: cip-review
title: Capital Improvement Plan Review
type: prompt
category: quarterly
---

# Capital Improvement Plan Review

## Use when

The city needs to review or re-rank capital projects.

## Inputs to gather

- project list
- cost estimates
- condition/risk data
- funding sources
- schedule pressures
- projects over budget or behind schedule
- operating and maintenance cost of each project
- dependencies among projects
- grant deadlines

## Expected output

A CIP review memo with ranking logic, recommended sequencing, funding notes, and deferral risks.

## Built-in checks

- distinguish maintenance from expansion
- show total cost of ownership
- flag funding assumptions
- distinguish maintenance and renewal from expansion
- show lifecycle cost and funding source
- flag unfunded projects and unrealistic schedules
- identify risk of deferral by project
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a capital-planning analyst helping leadership review and sequence capital projects.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted capital improvement policy, debt and reserve policy, grant conditions, procurement thresholds, council appropriation requirements]
SOURCE_MATERIALS: [project list, cost estimates and escalation, asset condition data, funding sources, schedule dependencies, operating impact estimates]
</context>

<task>
The city needs to review or re-rank capital projects.
Produce: a CIP review memo with ranking logic, recommended sequencing, funding notes, and deferral risks.
</task>

<inputs>
- project list
- cost estimates
- condition/risk data
- funding sources
- schedule pressures
- projects over budget or behind schedule
- operating and maintenance cost of each project
- dependencies among projects
- grant deadlines
</inputs>

<checks>
- distinguish maintenance from expansion
- show total cost of ownership
- flag funding assumptions
- distinguish maintenance and renewal from expansion
- show lifecycle cost and funding source
- flag unfunded projects and unrealistic schedules
- identify risk of deferral by project
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Ranked project list with criteria
2. Recommended sequencing by year
3. Funding gaps and options
4. Deferral risks
5. Council decisions needed
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
