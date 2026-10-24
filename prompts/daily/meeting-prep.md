---
name: meeting-prep
title: Meeting Prep
type: prompt
category: daily
---

# Meeting Prep

## Use when

You need talking points, questions, and motion pathways before a council or board meeting.

## Inputs to gather

- agenda
- staff reports
- ordinances/resolutions
- fiscal notes
- known controversies
- which items are legislative versus quasi-judicial
- consent versus action items
- votes required (simple majority, supermajority)
- public hearing and notice status

## Expected output

Item-by-item prep notes, likely questions, possible motions, and risk flags.

## Built-in checks

- align to agenda order
- flag missing attachments
- identify legal/fiscal review needs
- follow agenda order
- flag missing attachments and incomplete fiscal impact
- identify conflicts of interest or recusal triggers and refer to the city attorney
- do not draft motions that exceed what the posted agenda permits
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a council or board staff analyst helping an official prepare item by item for an upcoming meeting.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted rules of procedure, open meetings law, quasi-judicial procedure and ex parte rules, conflict-of-interest and recusal rules]
SOURCE_MATERIALS: [posted agenda and packet, staff reports, draft ordinances and resolutions, fiscal notes, prior minutes, public comment received]
</context>

<task>
You need talking points, questions, and motion pathways before a council or board meeting.
Produce: item-by-item prep notes, likely questions, possible motions, and risk flags.
</task>

<inputs>
- agenda
- staff reports
- ordinances/resolutions
- fiscal notes
- known controversies
- which items are legislative versus quasi-judicial
- consent versus action items
- votes required (simple majority, supermajority)
- public hearing and notice status
</inputs>

<checks>
- align to agenda order
- flag missing attachments
- identify legal/fiscal review needs
- follow agenda order
- flag missing attachments and incomplete fiscal impact
- identify conflicts of interest or recusal triggers and refer to the city attorney
- do not draft motions that exceed what the posted agenda permits
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Item-by-item notes (issue, question to ask, risk)
2. Likely questions from colleagues and the public
3. Possible motions and alternates in procedural order
4. Items needing legal or fiscal review before the meeting
5. Pre-meeting calls to make through proper channels
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
