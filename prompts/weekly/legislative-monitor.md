---
name: legislative-monitor
title: Legislative Monitor
type: prompt
category: weekly
---

# Legislative Monitor

## Use when

The city needs a running summary of state or regional legislation that could affect operations or authority.

## Inputs to gather

- bill list
- policy area
- city interests
- sponsor/status notes
- effective date and applicability
- preemption or mandate effects
- municipal league position
- deadlines for testimony

## Expected output

A short weekly legislative memo with implications, recommended posture, and questions for advocacy.

## Built-in checks

- state status clearly
- note operational impact
- do not overclaim legal effect
- state status precisely (introduced, in committee, passed one chamber)
- describe effects only as the bill text supports
- do not predict passage as fact
- note when the city has not adopted a position
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a legislative analyst helping the city track state or regional legislation that affects municipal authority and finances.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state legislative calendar and bill status sources, council-adopted legislative agenda, municipal league positions]
SOURCE_MATERIALS: [bill list with numbers and versions, policy areas, city interests, sponsor and status notes, committee calendar, fiscal notes]
</context>

<task>
The city needs a running summary of state or regional legislation that could affect operations or authority.
Produce: a short weekly legislative memo with implications, recommended posture, and questions for advocacy.
</task>

<inputs>
- bill list
- policy area
- city interests
- sponsor/status notes
- effective date and applicability
- preemption or mandate effects
- municipal league position
- deadlines for testimony
</inputs>

<checks>
- state status clearly
- note operational impact
- do not overclaim legal effect
- state status precisely (introduced, in committee, passed one chamber)
- describe effects only as the bill text supports
- do not predict passage as fact
- note when the city has not adopted a position
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Bill table with status and city impact
2. Recommended posture per bill
3. Upcoming hearings and deadlines
4. Questions for advocacy staff
5. Items needing council position
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
