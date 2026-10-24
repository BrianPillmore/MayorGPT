---
name: incident-brief
title: Incident Brief
type: prompt
category: emergencies
---

# Incident Brief

## Use when

You need a rapid, leader-ready summary during an incident.

## Inputs to gather

- confirmed facts
- operational status
- resource needs
- public impact
- next update time
- incident type, location, and start time
- operational period and next briefing time
- critical facilities and vulnerable populations affected
- mutual-aid and state requests pending

## Expected output

A situation report with facts, impacts, actions underway, asks, and message guidance.

## Built-in checks

- separate confirmed from unconfirmed
- note update cadence
- show public impacts first
- mark every statement confirmed or unconfirmed with source and time
- show public impacts and safety actions first
- do not release names, medical details, or investigative facts
- state the update cadence
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an emergency-management analyst helping produce a rapid situation report for city leaders during an active incident.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [incident command structure, emergency operations plan, reporting cadence, public information protocols]
SOURCE_MATERIALS: [verified incident reports, operational status by function, resource requests, public impact data, communications log, operational period]
</context>

<task>
You need a rapid, leader-ready summary during an incident.
Produce: a situation report with facts, impacts, actions underway, asks, and message guidance.
</task>

<inputs>
- confirmed facts
- operational status
- resource needs
- public impact
- next update time
- incident type, location, and start time
- operational period and next briefing time
- critical facilities and vulnerable populations affected
- mutual-aid and state requests pending
</inputs>

<checks>
- separate confirmed from unconfirmed
- note update cadence
- show public impacts first
- mark every statement confirmed or unconfirmed with source and time
- show public impacts and safety actions first
- do not release names, medical details, or investigative facts
- state the update cadence
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Headline status (one sentence)
2. Confirmed facts and impacts
3. Actions underway and resources committed
4. Asks and decisions needed from leadership
5. Message guidance and next update time
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
