---
name: grant-application-narrative
title: Grant Application Narrative
type: prompt
category: legislation-and-procurement
---

# Grant Application Narrative

## Use when

The city needs to draft the narrative section of a competitive grant application, including the statement of need, project description, goals and objectives, and evaluation approach.

## Inputs to gather

- grant program name, funder, and NOFO/NOFA citation
- project description and goals
- statement of community need with supporting data
- proposed activities, timeline, and budget summary
- performance measures and evaluation approach
- match or cost-share requirement
- any required certifications or assurances

## Expected output

A complete narrative draft aligned to the funder's evaluation criteria, an internal gap-and-weakness analysis, and a list of missing data points that must be confirmed before submission.

## Built-in checks

- address every required narrative section in the NOFO/NOFA
- tie the statement of need to local data, not just national averages
- align goals and activities to the funder's stated priorities
- do not overstate city capacity or prior experience
- flag match or cost-share obligations that require council authorization
- note any assurances that carry ongoing programmatic or reporting requirements

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping draft a competitive grant application narrative.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, state and federal grant regulations, match availability, council authorization requirements]
SOURCE_MATERIALS: [NOFO/NOFA text, project description, community needs data, budget summary, prior applications if any]
</context>

<task>
The city is preparing a competitive grant application and needs a strong narrative draft.
Produce a complete narrative draft aligned to the funder's evaluation criteria, an internal gap-and-weakness analysis, and a list of missing data points that must be confirmed before submission.
</task>

<inputs>
- grant program name, funder, and NOFO/NOFA citation and page or word limits
- project description, goals, and intended beneficiaries
- statement of community need with supporting local data
- proposed activities, implementation timeline, and budget summary
- performance measures and evaluation approach
- match or cost-share requirement and source
- any required certifications, assurances, or attachments
</inputs>

<checks>
- verify all required narrative sections from the NOFO/NOFA are addressed
- anchor the statement of need in local data and community-specific evidence, not just national statistics
- align project goals and activities explicitly to the funder's stated program priorities
- do not overstate city capacity, staff qualifications, or prior grant performance
- flag match or cost-share obligations that will require council resolution or budget amendment
- identify assurances or certifications that carry ongoing reporting, audit, or programmatic requirements
- note any single points of failure in the implementation plan
</checks>

<required_output>
1. Narrative draft mapped to each funder criterion
2. Gap-and-weakness analysis
3. Missing data list
4. Match and authorization needs
5. Assurances with ongoing obligations
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
