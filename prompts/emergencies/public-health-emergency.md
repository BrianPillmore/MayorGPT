---
name: public-health-emergency
title: Public Health Emergency Response
type: prompt
category: emergencies
---

# Public Health Emergency Response

## Use when

The city is responding to a disease outbreak, water quality failure, mass casualty event, or other public health emergency requiring coordinated city action alongside the county or state health authority.

## Inputs to gather

- nature of the public health threat (disease, contaminant, mass casualty, etc.)
- number and location of cases or affected individuals
- lead public health authority and their current guidance
- city assets and roles available (facilities, staff, equipment, communications)
- vulnerable populations at highest risk
- state and federal notifications required
- current public messaging if any

## Expected output

A city role summary, inter-agency coordination checklist, public messaging draft, resource deployment list, and a timeline of required notifications and actions.

## Built-in checks

- city government typically supports rather than leads on public health — clarify roles
- do not issue medical guidance outside of official health authority recommendations
- protect privacy of affected individuals consistent with HIPAA and state law
- do not speculate on cause until health authority has confirmed findings
- flag whether emergency declaration or special powers are warranted

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping coordinate the city's role in a public health emergency.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, state public health law, emergency operations plan, HIPAA considerations, county/state health authority protocols]
SOURCE_MATERIALS: [health authority guidance, incident reports, case count and location data, city asset inventory, prior communications]
</context>

<task>
The city is responding to a public health emergency in coordination with county, state, and federal public health authorities.
Produce a city role summary, interagency coordination checklist, public messaging draft, resource deployment list, and timeline of required notifications and actions.
</task>

<inputs>
- nature and severity of the public health threat
- confirmed case count, location, and affected demographics if known
- lead public health authority and their current guidance and instructions to the city
- city facilities, personnel, and assets available for response
- vulnerable populations at highest risk
- required state and federal notifications and their deadlines
- any current public messaging already issued
</inputs>

<checks>
- confirm city's supporting role vs. health authority's lead role and do not conflate them
- do not issue medical guidance that goes beyond or contradicts official health authority recommendations
- protect individual privacy consistent with HIPAA and applicable state law
- do not speculate on cause or source until health authority has made confirmed findings
- flag if scale of event warrants a municipal emergency declaration or activation of emergency operations center
- note any resource gaps requiring mutual aid or state/federal assistance requests
</checks>

<required_output>
1. City role statement (lead versus support)
2. Inter-agency coordination checklist
3. Public messaging draft aligned to health authority
4. Resource deployment list
5. Notification and action timeline
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
