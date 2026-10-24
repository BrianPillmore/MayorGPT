---
name: religious-accommodation-response
title: Religious Accommodation Response
type: prompt
category: people-and-hr
---

# Religious Accommodation Response

## Use when

The city needs to respond to a religious accommodation request from an employee or elected official.

## Inputs to gather

- employee name, role, and department
- description of the religious practice, observance, or expression requiring accommodation
- specific accommodation requested
- any scheduling, operational, or policy constraints raised by the department
- prior accommodation history if any
- alternatives that would meet the request in whole or in part
- interactive-process notes
- timeline for response
- whether the requestor is an employee, applicant, or elected official

## Expected output

A response letter or memo that confirms the accommodation, identifies an alternative, or — only if accommodation is genuinely not feasible — documents the specific undue hardship finding with concrete facts.

## Built-in checks

- default to an accommodating posture; frame the response as genuine respect for the employee, not grudging compliance
- assume the religious belief is sincerely held unless there is specific, articulable evidence to the contrary
- if the response denies accommodation in whole or in part, flag: a denial requires a documented, specific undue hardship finding — vague operational inconvenience is not sufficient; route any denial to labor and employment counsel before sending
- never suggest that the employee's religious expression is a workplace problem unless it has crossed into actual coercion or targeted harassment of a specific individual
- respond promptly and document the interactive process
- any denial requires specific facts and counsel review before it is sent
- state-law and local policy variance applies and must be flagged for counsel
- do not ask the employee to prove or justify the content of their belief beyond what counsel advises
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an HR and employment-law-aware advisor helping the city respond promptly and respectfully to a religious accommodation request.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [federal and state religious-accommodation law as summarized by labor counsel, collective bargaining agreement, city leave and scheduling policies, undue-hardship standard as advised by counsel]
SOURCE_MATERIALS: [accommodation request, job duties and schedule, operational constraints, prior accommodation history, input from the supervisor and HR]
</context>

<task>
The city needs to respond to a religious accommodation request from an employee or elected official.
Produce: a response letter or memo that confirms the accommodation, identifies an alternative, or — only if accommodation is genuinely not feasible — documents the specific undue hardship finding with concrete facts.
</task>

<inputs>
- employee name, role, and department
- description of the religious practice, observance, or expression requiring accommodation
- specific accommodation requested
- any scheduling, operational, or policy constraints raised by the department
- prior accommodation history if any
- alternatives that would meet the request in whole or in part
- interactive-process notes
- timeline for response
- whether the requestor is an employee, applicant, or elected official
</inputs>

<checks>
- default to an accommodating posture; frame the response as genuine respect for the employee, not grudging compliance
- assume the religious belief is sincerely held unless there is specific, articulable evidence to the contrary
- if the response denies accommodation in whole or in part, flag: a denial requires a documented, specific undue hardship finding — vague operational inconvenience is not sufficient; route any denial to labor and employment counsel before sending
- never suggest that the employee's religious expression is a workplace problem unless it has crossed into actual coercion or targeted harassment of a specific individual
- respond promptly and document the interactive process
- any denial requires specific facts and counsel review before it is sent
- state-law and local policy variance applies and must be flagged for counsel
- do not ask the employee to prove or justify the content of their belief beyond what counsel advises
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Response letter or memo
2. Alternatives considered with feasibility notes
3. Interactive-process documentation
4. Escalation note to labor counsel if any denial is contemplated
5. Follow-up dates
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
