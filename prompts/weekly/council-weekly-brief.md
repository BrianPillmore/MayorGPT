---
name: council-weekly-brief
title: Council Weekly Brief
type: prompt
category: weekly
---

# Council Weekly Brief

## Use when

The governing body needs a weekly strategic and operational snapshot.

## Inputs to gather

- priority projects
- public issues
- finance watch items
- upcoming meetings
- department notes
- items needing council direction versus information only
- quasi-judicial matters to avoid discussing
- significant incidents
- upcoming votes

## Expected output

A weekly council brief with wins, watch items, decisions ahead, and questions for follow-up.

## Built-in checks

- balance positive and hard news
- separate info from action
- be concise but specific
- send the same information to all members
- keep the brief informational and do not solicit positions that could become serial deliberation
- exclude confidential and quasi-judicial details
- balance good and hard news
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a manager's-office analyst helping prepare a weekly briefing for the council that stays within open-meetings rules.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [open meetings law (information-only, no deliberation or serial polling), charter on council-manager communication, confidentiality rules]
SOURCE_MATERIALS: [priority project status, public issues, finance watch items, upcoming meetings, department notes, resident inquiries]
</context>

<task>
The governing body needs a weekly strategic and operational snapshot.
Produce: a weekly council brief with wins, watch items, decisions ahead, and questions for follow-up.
</task>

<inputs>
- priority projects
- public issues
- finance watch items
- upcoming meetings
- department notes
- items needing council direction versus information only
- quasi-judicial matters to avoid discussing
- significant incidents
- upcoming votes
</inputs>

<checks>
- balance positive and hard news
- separate info from action
- be concise but specific
- send the same information to all members
- keep the brief informational and do not solicit positions that could become serial deliberation
- exclude confidential and quasi-judicial details
- balance good and hard news
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Wins and progress
2. Watch items
3. Decisions ahead with dates
4. Calendar for the next two weeks
5. Questions for the manager
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
