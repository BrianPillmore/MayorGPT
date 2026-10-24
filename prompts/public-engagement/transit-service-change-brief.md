---
name: transit-service-change-brief
title: Transit Service Change Brief
type: prompt
category: public-engagement
---

# Transit Service Change Brief

## Use when

The city or its transit provider is proposing a route, schedule, fare, or mobility service change and needs to brief decision-makers and inform riders.

## Inputs to gather

- proposed change and effective date
- ridership, productivity, and on-time data by route
- riders affected including transit-dependent and disabled riders
- funding sources, operating cost, and federal or state grant conditions
- alternatives considered
- required public notice, hearing, and civil rights analysis steps
- rider communications plan

## Expected output

A briefing with options, rider impact, cost, required process steps, and a rider-facing notice draft.

## Built-in checks

- confirm which public notice, hearing, and civil rights analyses apply to the change and who performs them; flag federal and state variance and defer to the transit agency and city attorney
- show who loses service as well as who gains
- include paratransit and accessibility effects
- do not present ridership projections as certain
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal transit and mobility analyst helping staff brief officials and inform riders about a service change.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [transit agency policies and board procedures, federal and state transit grant conditions as supplied, civil rights and accessibility requirements as advised by counsel, interlocal agreements]
SOURCE_MATERIALS: [ridership and performance data, route maps, budget data, grant terms, rider survey and comments, service standards, interlocal agreements]
</context>

<task>
The city or its transit provider is proposing a route, schedule, fare, or mobility service change and needs to brief decision-makers and inform riders.
Produce: a briefing with options, rider impact, cost, required process steps, and a rider-facing notice draft.
</task>

<inputs>
- proposed change and effective date
- ridership, productivity, and on-time data by route
- riders affected including transit-dependent and disabled riders
- funding sources, operating cost, and federal or state grant conditions
- alternatives considered
- required public notice, hearing, and civil rights analysis steps
- rider communications plan
</inputs>

<checks>
- confirm which public notice, hearing, and civil rights analyses apply to the change and who performs them; flag federal and state variance and defer to the transit agency and city attorney
- show who loses service as well as who gains
- include paratransit and accessibility effects
- do not present ridership projections as certain
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Change summary and rationale
2. Rider impact by group and area
3. Options with cost and tradeoffs
4. Required notice and review steps
5. Rider notice draft in plain language
6. Monitoring plan after the change
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
