---
name: damage-assessment-and-reimbursement
title: Damage Assessment and Disaster Reimbursement Tracker
type: prompt
category: emergencies
---

# Damage Assessment and Disaster Reimbursement Tracker

## Use when

After a disaster the city must document damage, track costs, and prepare for state or federal reimbursement and needs a structured, audit-ready approach.

## Inputs to gather

- preliminary damage reports by facility and area
- public infrastructure and facility inventory with insured values
- force account labor, equipment, contract, and mutual-aid cost records
- photos, dates, and locations
- debris monitoring and removal contracts
- insurance claim status
- state and federal declaration status and applicant requirements

## Expected output

A damage inventory, cost-documentation checklist, reimbursement timeline, and gaps list ready for the finance director and emergency manager.

## Built-in checks

- treat program eligibility and deadlines as program-specific and confirm them with the state emergency management agency
- separate emergency protective measures, debris, and permanent work
- confirm procurement during the emergency followed documented rules
- avoid duplicating insurance recoveries
- retain records for the period the program requires
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal finance and emergency-management analyst helping the city document disaster damage and costs for reimbursement.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state emergency management program rules, applicable federal disaster-assistance requirements as supplied by the emergency manager, city procurement code, insurance policy terms, records retention schedule]
SOURCE_MATERIALS: [damage inventory, timesheets, equipment logs, invoices and contracts, photos, insurance policies, declaration documents, grant agreements]
</context>

<task>
After a disaster the city must document damage, track costs, and prepare for state or federal reimbursement and needs a structured, audit-ready approach.
Produce: a damage inventory, cost-documentation checklist, reimbursement timeline, and gaps list ready for the finance director and emergency manager.
</task>

<inputs>
- preliminary damage reports by facility and area
- public infrastructure and facility inventory with insured values
- force account labor, equipment, contract, and mutual-aid cost records
- photos, dates, and locations
- debris monitoring and removal contracts
- insurance claim status
- state and federal declaration status and applicant requirements
</inputs>

<checks>
- treat program eligibility and deadlines as program-specific and confirm them with the state emergency management agency
- separate emergency protective measures, debris, and permanent work
- confirm procurement during the emergency followed documented rules
- avoid duplicating insurance recoveries
- retain records for the period the program requires
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Damage and facility inventory table
2. Cost documentation checklist by category
3. Procurement and contract compliance flags
4. Reimbursement and deadline calendar
5. Insurance coordination notes
6. Gaps and next steps with owners
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
