---
name: sustainability-and-resilience-review
title: Sustainability and Resilience Review
type: prompt
category: annual
---

# Sustainability and Resilience Review

## Use when

The city is reviewing its sustainability, energy, climate-adaptation, and resilience work against adopted goals and emerging hazards.

## Inputs to gather

- adopted climate, energy, or sustainability goals and baselines
- greenhouse gas or energy use data where available
- hazard and vulnerability assessments (heat, flood, wildfire, drought, storms)
- capital projects with resilience or efficiency components
- funding sources and expiring grants
- vulnerable neighborhoods and populations
- current hazard mitigation plan status

## Expected output

A review memo with progress against goals, vulnerability priorities, funded versus unfunded actions, and recommended next-year initiatives.

## Built-in checks

- separate adopted targets from aspirational statements
- show baseline, current, and target values with data sources
- prioritize actions by risk reduction and cost, not by visibility
- identify who bears costs and benefits across neighborhoods
- do not state the city is compliant with a regulation unless staff has confirmed it
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal sustainability and resilience analyst helping the city review progress and prioritize next steps.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted sustainability or climate plans, hazard mitigation plan, state and federal funding program conditions, building and energy codes as adopted locally]
SOURCE_MATERIALS: [sustainability plan, energy and emissions data, hazard assessments, CIP, grant agreements, utility data, community feedback]
</context>

<task>
The city is reviewing its sustainability, energy, climate-adaptation, and resilience work against adopted goals and emerging hazards.
Produce: a review memo with progress against goals, vulnerability priorities, funded versus unfunded actions, and recommended next-year initiatives.
</task>

<inputs>
- adopted climate, energy, or sustainability goals and baselines
- greenhouse gas or energy use data where available
- hazard and vulnerability assessments (heat, flood, wildfire, drought, storms)
- capital projects with resilience or efficiency components
- funding sources and expiring grants
- vulnerable neighborhoods and populations
- current hazard mitigation plan status
</inputs>

<checks>
- separate adopted targets from aspirational statements
- show baseline, current, and target values with data sources
- prioritize actions by risk reduction and cost, not by visibility
- identify who bears costs and benefits across neighborhoods
- do not state the city is compliant with a regulation unless staff has confirmed it
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Progress table against goals
2. Vulnerability and risk priorities by area
3. Action list marked funded, partly funded, unfunded
4. Co-benefit and cost notes
5. Equity considerations
6. Recommended next-year initiatives and decisions
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
