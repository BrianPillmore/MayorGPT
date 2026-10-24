---
name: council-of-governments-brief
title: Council of Governments / MPO Meeting Brief
type: prompt
category: intergovernmental
---

# Council of Governments / MPO Meeting Brief

## Use when

The mayor, manager, or council member needs to prepare for a regional council of governments (COG) or metropolitan planning organization (MPO) meeting — understanding the agenda, the city's positions, and the likely positions of other member governments.

## Inputs to gather

- COG or MPO meeting agenda and materials
- agenda items that affect the city directly
- city's current positions on regional issues
- any formal action or vote expected at the meeting
- history of prior COG/MPO decisions on key items
- relationships and known positions of other member jurisdictions

## Expected output

A pre-meeting brief with item-by-item analysis, recommended city positions, anticipated allies and opponents, talking points for the city's representative, and any required council authorization.

## Built-in checks

- distinguish advisory from binding COG or MPO actions
- do not commit city funding or policy without council authorization
- identify which items require formal city council action before the representative can vote
- note any conflict of interest between city and regional interests
- flag any items with federal transportation funding implications (MPO TIP, STIP)

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping prepare for a regional council of governments or MPO meeting.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, council-adopted legislative agenda, COG bylaws or MPO procedures, interlocal agreements]
SOURCE_MATERIALS: [meeting agenda and packet, prior meeting minutes, city's legislative agenda, regional plans or TIP documents]
</context>

<task>
The city's representative is preparing for a regional COG or MPO meeting.
Produce a pre-meeting brief with item-by-item analysis, recommended city positions, anticipated ally and opponent mapping, talking points for the city's representative, and a list of any required prior council authorization.
</task>

<inputs>
- COG or MPO meeting agenda and supporting materials
- agenda items that directly affect the city's interests or budget
- city's current positions on pending regional issues
- any formal votes expected at the meeting
- prior decisions by this body on the relevant items
- known positions or interests of other member jurisdictions
</inputs>

<checks>
- distinguish advisory recommendations from binding COG or MPO actions
- confirm whether any vote requires prior city council authorization or direction
- do not commit city financial contributions or policy positions without council authorization
- note any tension between city interests and broader regional or county interests
- flag items with federal transportation funding implications (TIP, STIP amendments)
- identify any items that should be reported back to council after the meeting
</checks>

<required_output>
1. Item-by-item analysis
2. Recommended city positions
3. Allies and opponents
4. Talking points for the representative
5. Council authorization needed before the vote
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
