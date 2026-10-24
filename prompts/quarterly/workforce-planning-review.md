---
name: workforce-planning-review
title: Workforce Planning Review
type: prompt
category: quarterly
---

# Workforce Planning Review

## Use when

The city needs a quarterly view of vacancies, retention, succession, and training needs.

## Inputs to gather

- vacancies
- turnover
- retirement risk
- training needs
- critical roles
- time-to-fill and offer-acceptance data
- pay competitiveness
- succession candidates
- service levels affected by vacancies

## Expected output

A workforce memo with pressure points, succession risks, and recommended actions.

## Built-in checks

- identify mission-critical roles
- flag retention hot spots
- link staffing risk to service levels
- identify mission-critical roles and single points of failure
- link vacancies to service impact
- avoid inferring protected characteristics from retirement or age data
- flag bargaining and budget implications
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a workforce analyst helping HR and leadership assess vacancies, retention, and succession.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [personnel rules, collective bargaining agreements, compensation policy, pension or retirement-system rules, equal employment opportunity requirements]
SOURCE_MATERIALS: [vacancy and turnover data by department, retirement eligibility, exit-interview themes, training budget, critical-role list, recruitment pipeline, overtime]
</context>

<task>
The city needs a quarterly view of vacancies, retention, succession, and training needs.
Produce: a workforce memo with pressure points, succession risks, and recommended actions.
</task>

<inputs>
- vacancies
- turnover
- retirement risk
- training needs
- critical roles
- time-to-fill and offer-acceptance data
- pay competitiveness
- succession candidates
- service levels affected by vacancies
</inputs>

<checks>
- identify mission-critical roles
- flag retention hot spots
- link staffing risk to service levels
- identify mission-critical roles and single points of failure
- link vacancies to service impact
- avoid inferring protected characteristics from retirement or age data
- flag bargaining and budget implications
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Pressure points by department
2. Succession and retention risks
3. Recommended actions with cost
4. Training priorities
5. Metrics to track next quarter
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
