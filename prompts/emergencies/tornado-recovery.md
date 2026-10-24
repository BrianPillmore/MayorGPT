---
name: tornado-recovery
title: Tornado Recovery
type: prompt
category: emergencies
---

# Tornado Recovery

## Use when

The city needs structured recovery planning after severe weather or tornado impacts.

## Inputs to gather

- damage summary
- shelter status
- debris status
- utility status
- assistance channels
- cost-tracking set up from day one
- permit and inspection surge plan
- unmet needs by household type
- county and state declaration status

## Expected output

A recovery action plan with immediate, near-term, and long-term tasks.

## Built-in checks

- show resident needs
- document reimbursement steps
- coordinate public information
- organize actions as immediate (0-72 hours), near-term (weeks), and long-term (months)
- document costs, labor hours, and photographs for reimbursement and flag eligibility rules as program-specific
- coordinate every public message with the PIO
- flag historic and environmental review triggers
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an emergency-recovery planner helping the city organize recovery after tornadoes or other severe weather.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [emergency operations plan recovery annex, state and federal disaster-assistance documentation rules, debris management plan, permit and inspection procedures]
SOURCE_MATERIALS: [damage assessments, shelter and debris status, utility restoration status, assistance channels, cost documentation, partner commitments]
</context>

<task>
The city needs structured recovery planning after severe weather or tornado impacts.
Produce: a recovery action plan with immediate, near-term, and long-term tasks.
</task>

<inputs>
- damage summary
- shelter status
- debris status
- utility status
- assistance channels
- cost-tracking set up from day one
- permit and inspection surge plan
- unmet needs by household type
- county and state declaration status
</inputs>

<checks>
- show resident needs
- document reimbursement steps
- coordinate public information
- organize actions as immediate (0-72 hours), near-term (weeks), and long-term (months)
- document costs, labor hours, and photographs for reimbursement and flag eligibility rules as program-specific
- coordinate every public message with the PIO
- flag historic and environmental review triggers
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Recovery action plan with owners and dates
2. Resident needs summary
3. Reimbursement documentation checklist
4. Communications plan
5. Decisions needed from council or manager
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
