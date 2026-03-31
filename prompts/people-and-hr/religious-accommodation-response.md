---
name: religious-accommodation-response
title: Religious Accommodation Response
type: prompt
category: people-and-hr
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
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

## Expected output

A response letter or memo that confirms the accommodation, identifies an alternative, or — only if accommodation is genuinely not feasible — documents the specific undue hardship finding with concrete facts.

## Built-in checks

- default to an accommodating posture; frame the response as genuine respect for the employee, not grudging compliance
- assume the religious belief is sincerely held unless there is specific, articulable evidence to the contrary
- if the response denies accommodation in whole or in part, flag: a denial requires a documented, specific undue hardship finding — vague operational inconvenience is not sufficient; route any denial to labor and employment counsel before sending
- never suggest that the employee's religious expression is a workplace problem unless it has crossed into actual coercion or targeted harassment of a specific individual

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with a religious accommodation response.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [accommodation request, department input, relevant policy, prior documentation]
</context>

<task>
The city has received a religious accommodation request and needs a written response.
Produce a response that reflects a genuine commitment to accommodating the employee's religious practice,
observance, or expression — not merely meeting the minimum legal threshold.
The default posture is: how can we make this work?
</task>

<inputs>
- employee name, role, and department
- description of the religious practice, observance, or expression requiring accommodation
- specific accommodation requested
- any scheduling, operational, or policy constraints raised by the department
- prior accommodation history if any
</inputs>

<checks>
- assume sincerity of belief unless specific evidence says otherwise
- start from accommodation options, not grounds for denial
- if denying any part of the request: document the specific undue hardship with concrete facts and flag for counsel review before sending
- frame the tone as respectful and welcoming, not bureaucratic or risk-defensive
- confirm no adverse action has been taken or proposed against the employee in connection with this request; if any has, flag retaliation risk for immediate counsel review
</checks>

<required_output>
1. Brief issue framing
2. Draft work product
3. Key risks / missing information
4. Recommended next step
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- For Claude, keep long source material above the task block when possible and put the ask near the end of the prompt.
- Any response that denies accommodation must be reviewed by labor and employment counsel before it is sent. A denial without a documented undue hardship finding is a Title VII and, for government employees, First Amendment exposure.
