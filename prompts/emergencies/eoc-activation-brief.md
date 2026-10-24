---
name: eoc-activation-brief
title: Emergency Operations Center Activation Brief
type: prompt
category: emergencies
---

# Emergency Operations Center Activation Brief

## Use when

The emergency manager or city manager is deciding whether to activate, escalate, or stand down the emergency operations center (EOC) and needs a clear brief for the operational period.

## Inputs to gather

- hazard and forecast or incident summary
- current EOC activation level and criteria in the emergency operations plan
- staffing roster and 24-hour coverage plan
- critical facilities and vulnerable populations at risk
- mutual-aid and state resource requests
- public information and alert status
- next operational period objectives

## Expected output

An activation recommendation, operational period objectives, staffing and resource plan, decision log template, and leadership briefing script.

## Built-in checks

- tie the recommended activation level to criteria in the adopted plan
- state who has authority to activate and who must be notified
- separate confirmed information from forecasts
- identify staffing fatigue and relief by operational period
- flag if an emergency declaration is also warranted
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an emergency-management planner helping the emergency manager brief city leadership on EOC activation.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted emergency operations plan, incident command structure, activation levels, state emergency management notification rules, mutual-aid agreements]
SOURCE_MATERIALS: [hazard forecast or incident reports, EOC activation criteria, staffing roster, resource inventory, mutual-aid agreements, prior activation logs]
</context>

<task>
The emergency manager or city manager is deciding whether to activate, escalate, or stand down the emergency operations center (EOC) and needs a clear brief for the operational period.
Produce: an activation recommendation, operational period objectives, staffing and resource plan, decision log template, and leadership briefing script.
</task>

<inputs>
- hazard and forecast or incident summary
- current EOC activation level and criteria in the emergency operations plan
- staffing roster and 24-hour coverage plan
- critical facilities and vulnerable populations at risk
- mutual-aid and state resource requests
- public information and alert status
- next operational period objectives
</inputs>

<checks>
- tie the recommended activation level to criteria in the adopted plan
- state who has authority to activate and who must be notified
- separate confirmed information from forecasts
- identify staffing fatigue and relief by operational period
- flag if an emergency declaration is also warranted
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Activation recommendation with criteria met
2. Operational period objectives (next 12 to 24 hours)
3. Staffing and resource plan by function
4. Notification list and authority chain
5. Leadership briefing script and decision points
6. Items needing the city attorney or declaration review
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
