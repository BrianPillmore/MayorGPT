---
name: new-council-onboarding
title: New Council Onboarding
type: prompt
category: elections-and-transition
---

# New Council Onboarding

## Use when

The city is onboarding one or more newly elected councilmembers.

## Inputs to gather

- charter/code basics
- meeting rules
- current priorities
- board assignments
- ethics requirements
- seating date and oath requirements
- financial disclosure and training deadlines
- technology and records accounts to set up
- key staff contacts

## Expected output

An onboarding plan, reading list, and first-meeting prep packet.

## Built-in checks

- cover role boundaries
- include calendar and contacts
- flag training requirements
- cover role boundaries between council and administration
- flag open meetings and public records training requirements
- note deadlines with dates
- do not describe powers beyond what the charter says
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a city clerk and manager's-office analyst helping onboard newly elected councilmembers.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code, open meetings and public records law, ethics and financial-disclosure requirements, oath and seating procedure, rules of procedure]
SOURCE_MATERIALS: [charter and code highlights, meeting rules, current priorities, board assignments, ethics and training requirements, orientation calendar]
</context>

<task>
The city is onboarding one or more newly elected councilmembers.
Produce: an onboarding plan, reading list, and first-meeting prep packet.
</task>

<inputs>
- charter/code basics
- meeting rules
- current priorities
- board assignments
- ethics requirements
- seating date and oath requirements
- financial disclosure and training deadlines
- technology and records accounts to set up
- key staff contacts
</inputs>

<checks>
- cover role boundaries
- include calendar and contacts
- flag training requirements
- cover role boundaries between council and administration
- flag open meetings and public records training requirements
- note deadlines with dates
- do not describe powers beyond what the charter says
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Onboarding plan by week
2. Reading list and key documents
3. First-meeting prep packet
4. Contacts and committee assignments sheet
5. Compliance deadline checklist
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
