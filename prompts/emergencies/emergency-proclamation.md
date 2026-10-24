---
name: emergency-proclamation
title: Emergency Proclamation
type: prompt
category: emergencies
---

# Emergency Proclamation

## Use when

The city is considering or preparing an emergency declaration or supporting order.

## Inputs to gather

- incident facts
- authority source
- geography affected
- time window
- requested powers or actions
- who signs and who ratifies and by when
- specific emergency powers requested (curfew, procurement waiver, price limits)
- related state or county declarations
- termination criteria

## Expected output

A draft proclamation plus a legal/process checklist and public explanation.

## Built-in checks

- state authority clearly
- limit scope to what is needed
- flag publication/ratification needs
- cite only the authority the city attorney has supplied; flag state-law variance on who may declare and ratification timing
- limit scope and duration to what is needed
- each requested power must tie to a stated need
- require legal review before any order restricting movement, assembly, or property
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal legal and emergency-management analyst helping draft a local emergency declaration and supporting orders.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code emergency powers, state emergency management law, who may declare and who must ratify, duration limits, publication requirements]
SOURCE_MATERIALS: [incident facts, authority source supplied by the city attorney, geography, time window, requested emergency powers, mutual-aid needs, prior declarations]
</context>

<task>
The city is considering or preparing an emergency declaration or supporting order.
Produce: a draft proclamation plus a legal/process checklist and public explanation.
</task>

<inputs>
- incident facts
- authority source
- geography affected
- time window
- requested powers or actions
- who signs and who ratifies and by when
- specific emergency powers requested (curfew, procurement waiver, price limits)
- related state or county declarations
- termination criteria
</inputs>

<checks>
- state authority clearly
- limit scope to what is needed
- flag publication/ratification needs
- cite only the authority the city attorney has supplied; flag state-law variance on who may declare and ratification timing
- limit scope and duration to what is needed
- each requested power must tie to a stated need
- require legal review before any order restricting movement, assembly, or property
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Draft proclamation with findings
2. Legal and process checklist (signature, ratification, filing, publication)
3. Plain-language public explanation
4. List of orders that require separate action
5. Termination and review plan
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
