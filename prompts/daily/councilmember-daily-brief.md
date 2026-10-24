---
name: councilmember-daily-brief
title: Councilmember Daily Brief
type: prompt
category: daily
---

# Councilmember Daily Brief

## Use when

A councilmember needs a concise update on hot issues, resident concerns, and upcoming decision points.

## Inputs to gather

- ward issues
- city-wide issues
- agenda timeline
- constituent themes
- media themes
- which items are scheduled for action versus informational
- issues the member has already taken a public position on
- any quasi-judicial matter where contact is restricted

## Expected output

A compact daily memo grouped into watch items, resident issues, decisions ahead, and suggested follow-up.

## Built-in checks

- no staff micromanagement
- flag city-wide service and budget impacts
- note whether item is official or informal
- mark quasi-judicial matters so the member avoids ex parte contact and flag for the city attorney
- route operational requests through the city manager and not to line staff
- distinguish confirmed fact from rumor or social-media claim
- flag any item that could trigger a quorum or serial-meeting concern
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a staff analyst helping a councilmember keep up with ward and city-wide issues without directing administration.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter limits on council direction of staff, open meetings law (no serial deliberation by sequential communications), council information-request protocol]
SOURCE_MATERIALS: [agenda timeline, constituent contacts, service-request data for the ward, media clips, staff reports, social media themes]
</context>

<task>
A councilmember needs a concise update on hot issues, resident concerns, and upcoming decision points.
Produce: a compact daily memo grouped into watch items, resident issues, decisions ahead, and suggested follow-up.
</task>

<inputs>
- ward issues
- city-wide issues
- agenda timeline
- constituent themes
- media themes
- which items are scheduled for action versus informational
- issues the member has already taken a public position on
- any quasi-judicial matter where contact is restricted
</inputs>

<checks>
- no staff micromanagement
- flag city-wide service and budget impacts
- note whether item is official or informal
- mark quasi-judicial matters so the member avoids ex parte contact and flag for the city attorney
- route operational requests through the city manager and not to line staff
- distinguish confirmed fact from rumor or social-media claim
- flag any item that could trigger a quorum or serial-meeting concern
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Watch list with one-line status per item
2. Resident issues by theme and ward
3. Decisions ahead with dates
4. Suggested questions to send through the manager
5. Items that are official versus informal
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
