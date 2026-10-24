---
name: agenda-cycle
title: Agenda Cycle
type: prompt
category: monthly
---

# Agenda Cycle

## Use when

The city is building a regular or special meeting agenda packet.

## Inputs to gather

- proposed items
- draft staff reports
- ordinances/resolutions
- attachments
- posting deadlines
- item sponsor and department
- required notices and hearing dates
- legal and fiscal review status
- consent versus regular classification

## Expected output

A draft agenda order, packet checklist, missing items list, and item-by-item readiness status.

## Built-in checks

- confirm hearing/publication needs
- flag incomplete fiscal impact
- spot missing exhibits
- confirm posting and publication deadlines and flag state-law variance
- flag items with missing fiscal impact, legal review, or exhibits
- do not add an item after posting without checking late-item rules
- keep action language consistent with the posted title
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a city clerk's-office analyst helping assemble a compliant, complete meeting agenda packet.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [open meetings law and posting deadlines, rules of procedure, charter hearing and publication requirements, consent-agenda policy]
SOURCE_MATERIALS: [item submissions, draft staff reports, ordinances and resolutions, attachments, posting and publication deadlines, prior agenda]
</context>

<task>
The city is building a regular or special meeting agenda packet.
Produce: a draft agenda order, packet checklist, missing items list, and item-by-item readiness status.
</task>

<inputs>
- proposed items
- draft staff reports
- ordinances/resolutions
- attachments
- posting deadlines
- item sponsor and department
- required notices and hearing dates
- legal and fiscal review status
- consent versus regular classification
</inputs>

<checks>
- confirm hearing/publication needs
- flag incomplete fiscal impact
- spot missing exhibits
- confirm posting and publication deadlines and flag state-law variance
- flag items with missing fiscal impact, legal review, or exhibits
- do not add an item after posting without checking late-item rules
- keep action language consistent with the posted title
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Draft agenda in order
2. Item readiness table (ready, needs work, pull)
3. Packet checklist and missing items
4. Posting and publication calendar
5. Questions for the manager and city attorney
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
