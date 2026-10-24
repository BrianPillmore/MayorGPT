---
name: utility-failure-response
title: Utility Failure Response
type: prompt
category: emergencies
---

# Utility Failure Response

## Use when

The city is managing an extended failure of a water, wastewater, stormwater, electric, or gas utility system and needs to coordinate operations, public communications, mutual aid, and regulatory notifications.

## Inputs to gather

- utility type and specific system failure description
- geographic area and population affected
- estimated duration and restoration timeline
- current operational response underway
- state/federal regulatory notification requirements
- vulnerable populations and critical facilities in the affected area
- public health risks (boil-water advisory, sewage overflow, etc.)

## Expected output

An incident coordination brief with operational priorities, regulatory notification checklist, public communications draft, vulnerable-population action items, and an escalation decision tree.

## Built-in checks

- verify regulatory notification deadlines (EPA, state primacy agency, public health department)
- do not understate risk to public health — err toward precaution
- identify backup service sources (bottled water, portable toilets, mutual aid agreements)
- confirm chain of command between public works, emergency management, and elected leadership
- flag any liability exposure from delayed public notification

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping coordinate the city's response to an extended utility system failure.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, state utility law, EPA/state regulatory requirements, emergency operations plan, mutual aid agreements]
SOURCE_MATERIALS: [incident reports, utility system maps, affected area description, current restoration estimate, prior communications]
</context>

<task>
The city is experiencing an extended failure of a critical utility system affecting residents and businesses.
Produce an incident coordination brief with operational priorities, regulatory notification checklist, public communications draft, vulnerable-population action items, and an escalation decision tree.
</task>

<inputs>
- utility type and specific failure description (water main break, pump failure, power outage, sewer overflow, etc.)
- geographic area and estimated population affected
- current restoration timeline estimate
- operational response already underway
- state or federal regulatory notification requirements and deadlines
- critical facilities in the affected area (hospitals, schools, nursing homes, dialysis centers)
- vulnerable population concentrations
- public health risks triggered (boil-water advisory needed, sewage overflow, etc.)
</inputs>

<checks>
- verify regulatory notification deadlines and confirm they are calendared
- do not understate public health risk — precautionary public notice is preferred over delayed accuracy
- identify backup or interim service options (mutual aid, bottled water distribution, temporary facilities)
- confirm chain of command between public works, emergency management, health department, and elected leadership
- flag any liability exposure from delayed or insufficient public notification
- note whether an emergency declaration or proclamation is appropriate
</checks>

<required_output>
1. Operational priorities
2. Regulatory notification checklist with deadlines
3. Public communications draft
4. Vulnerable-population and critical-facility actions
5. Escalation decision tree
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
