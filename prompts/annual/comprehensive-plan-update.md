---
name: comprehensive-plan-update
title: Comprehensive Plan Update
type: prompt
category: annual
---

# Comprehensive Plan Update

## Use when

The city is initiating, managing, or tracking a periodic update to its comprehensive land use plan and needs to organize the process, communicate with the community, and ensure consistency across plan elements.

## Inputs to gather

- current plan adoption date and elements
- state statutory requirements for plan updates
- council-adopted goals or scope for the update
- consultant or staff team assigned
- public engagement strategy
- key topics driving the update (housing, transportation, climate, etc.)
- known conflicts between current plan and current conditions

## Expected output

A project overview memo with scope, timeline, public engagement milestones, state compliance checklist, inter-element consistency notes, and a list of policy questions requiring council direction.

## Built-in checks

- confirm state statutory update requirements and deadlines
- distinguish a full plan update from an amendment or element revision
- identify elements requiring new data collection vs. policy restatement
- flag consistency requirements between elements (land use and transportation, housing and utilities, etc.)
- note required public hearings and planning commission review steps

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping initiate or track a comprehensive land use plan update.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state planning enabling act, charter, plan adoption date and current elements, zoning code, regional planning context]
SOURCE_MATERIALS: [current plan text, council goal-setting notes, scope of work if any, consultant proposals, demographic and land use data]
</context>

<task>
The city is initiating or tracking a periodic update to its comprehensive land use plan.
Produce a project overview memo with scope, timeline, public engagement milestones, state compliance checklist, inter-element consistency notes, and a list of policy questions requiring council direction.
</task>

<inputs>
- current plan adoption date and which elements are covered
- applicable state statutory requirements for plan content and update frequency
- council-adopted goals or scope for this update cycle
- consultant or staff team assigned and budget available
- public engagement strategy and planned milestones
- key topics or pressures driving the update (housing, transportation, climate, economic development)
- known conflicts between current plan policies and current conditions or recent council actions
</inputs>

<checks>
- verify state statutory requirements for plan update frequency, required elements, and adoption procedures
- distinguish a full plan update from a targeted amendment or single-element revision
- identify which elements require new data collection vs. policy restatement or modest refresh
- flag consistency requirements between plan elements that must be maintained (land use and transportation, housing and utilities, etc.)
- note required public hearings, planning commission review, and any regional or state review obligations
- flag policy questions that require explicit council direction before staff can proceed
</checks>

<required_output>
1. Project overview and scope
2. Timeline with engagement milestones and hearing steps
3. State-requirement compliance checklist
4. Inter-element consistency notes
5. Policy questions needing council direction
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
