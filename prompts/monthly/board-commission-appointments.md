---
name: board-commission-appointments
title: Board & Commission Appointments
type: prompt
category: monthly
---

# Board & Commission Appointments

## Use when

The city is filling vacancies or preparing appointment action for boards or commissions.

## Inputs to gather

- vacancies
- applications
- term details
- ward/eligibility needs
- attendance history if relevant
- balance requirements (ward, expertise, statutory seats)
- expiring terms and holdovers
- conflict-of-interest screening
- oath and training requirements

## Expected output

An appointment memo, eligibility screen, interview questions, and draft action language.

## Built-in checks

- check residency/ward rules
- flag attendance issues
- avoid unsupported rankings
- verify each applicant against objective eligibility criteria only
- check residency, ward, and term-limit rules
- do not rank candidates without stated criteria
- flag attendance problems with the applicable removal procedure
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a city clerk's-office analyst helping prepare board and commission appointments.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code on board composition, residency and eligibility rules, term limits, open meetings and nondiscrimination requirements, appointment authority (mayor, council, or both)]
SOURCE_MATERIALS: [vacancy list, applications, term dates, eligibility requirements, attendance records, conflict-of-interest disclosures]
</context>

<task>
The city is filling vacancies or preparing appointment action for boards or commissions.
Produce: an appointment memo, eligibility screen, interview questions, and draft action language.
</task>

<inputs>
- vacancies
- applications
- term details
- ward/eligibility needs
- attendance history if relevant
- balance requirements (ward, expertise, statutory seats)
- expiring terms and holdovers
- conflict-of-interest screening
- oath and training requirements
</inputs>

<checks>
- check residency/ward rules
- flag attendance issues
- avoid unsupported rankings
- verify each applicant against objective eligibility criteria only
- check residency, ward, and term-limit rules
- do not rank candidates without stated criteria
- flag attendance problems with the applicable removal procedure
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Appointment memo by board
2. Eligibility screen table
3. Interview question set
4. Draft motion or resolution language
5. Orientation and oath checklist
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
