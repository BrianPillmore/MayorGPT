---
name: transition-memo
title: Transition Memo
type: prompt
category: elections-and-transition
---

# Transition Memo

## Use when

A newly elected official or incoming administration needs a handoff packet.

## Inputs to gather

- current issues
- calendar
- major contracts/projects
- fiscal status
- staff contacts
- time-critical decisions in the first 30 days
- vacancies and acting appointments
- pending claims and negotiations
- commitments made by the outgoing officeholder

## Expected output

A transition memo organized into first 30/90/180 day issues and key decisions ahead.

## Built-in checks

- be candid
- prioritize decision points
- separate urgent from important
- be candid about problems
- separate urgent items from important ones
- do not include privileged legal advice or personnel details in a memo that will pass to non-eligible recipients
- flag commitments that bind the incoming officeholder
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal chief-of-staff analyst helping prepare a candid handoff memo for an incoming official or administration.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records law, confidentiality limits on closed-session and personnel information, charter appointment powers, transition-period rules]
SOURCE_MATERIALS: [current issues list, calendar of deadlines, major contracts and projects, fiscal condition, litigation list (summary only), staff roster and contacts]
</context>

<task>
A newly elected official or incoming administration needs a handoff packet.
Produce: a transition memo organized into first 30/90/180 day issues and key decisions ahead.
</task>

<inputs>
- current issues
- calendar
- major contracts/projects
- fiscal status
- staff contacts
- time-critical decisions in the first 30 days
- vacancies and acting appointments
- pending claims and negotiations
- commitments made by the outgoing officeholder
</inputs>

<checks>
- be candid
- prioritize decision points
- separate urgent from important
- be candid about problems
- separate urgent items from important ones
- do not include privileged legal advice or personnel details in a memo that will pass to non-eligible recipients
- flag commitments that bind the incoming officeholder
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Executive summary of the five biggest issues
2. 30/90/180-day action list
3. Key decisions and deadlines calendar
4. Contracts, projects, and risks table
5. Relationship and contact map
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
