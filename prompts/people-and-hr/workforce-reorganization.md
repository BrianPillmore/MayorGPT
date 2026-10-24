---
name: workforce-reorganization
title: Workforce Reorganization
type: prompt
category: people-and-hr
---

# Workforce Reorganization

## Use when

The city is considering reporting-line, staffing, or organizational redesign.

## Inputs to gather

- current org chart
- pain points
- service goals
- budget constraints
- critical roles
- span of control and workload
- positions affected by class and bargaining unit
- transition risks and timing
- cost or savings by option

## Expected output

An options memo with org alternatives, pros/cons, and implementation issues.

## Built-in checks

- show service impact
- flag classification/HR/legal review needs
- avoid abstract theory detached from staffing reality
- show service impact for each option
- flag bargaining, classification, notice, and legal review requirements and state-law variance
- do not name individuals in options
- test options against actual staffing and skills
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an organizational-design analyst helping leadership evaluate a reorganization of reporting lines or staffing.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code on administrative organization and council approval, collective bargaining and meet-and-confer obligations, classification and civil service rules, notice and layoff rules]
SOURCE_MATERIALS: [current org chart, workload data, service goals, pain points, budget limits, critical roles, labor agreements, employee feedback]
</context>

<task>
The city is considering reporting-line, staffing, or organizational redesign.
Produce: an options memo with org alternatives, pros/cons, and implementation issues.
</task>

<inputs>
- current org chart
- pain points
- service goals
- budget constraints
- critical roles
- span of control and workload
- positions affected by class and bargaining unit
- transition risks and timing
- cost or savings by option
</inputs>

<checks>
- show service impact
- flag classification/HR/legal review needs
- avoid abstract theory detached from staffing reality
- show service impact for each option
- flag bargaining, classification, notice, and legal review requirements and state-law variance
- do not name individuals in options
- test options against actual staffing and skills
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Problem statement
2. Options with pros, cons, cost, and service effect
3. Recommended option and implementation steps
4. Labor, HR, and legal review needs
5. Communication plan
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
