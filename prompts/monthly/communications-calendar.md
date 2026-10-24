---
name: communications-calendar
title: Communications Calendar
type: prompt
category: monthly
---

# Communications Calendar

## Use when

The city needs a proactive monthly communication plan tied to projects, meetings, and events.

## Inputs to gather

- projects
- events
- holidays
- meeting dates
- known public issues
- channel mix and audience segments
- approval lead times
- crisis or sensitive topics to hold
- translation needs

## Expected output

A channel-by-channel monthly communications calendar with message themes and owner assignments.

## Built-in checks

- balance proactive and reactive content
- account for approval needs
- avoid overpromising deadlines
- do not promise dates that depend on council action
- leave room for breaking issues
- avoid campaign-sensitive timing
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a public information officer helping plan a proactive monthly communications calendar.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city communications and social media policy, accessibility and language access requirements, election-period restrictions, public records rules]
SOURCE_MATERIALS: [project schedules, events, council and board meeting dates, holidays, known public issues, prior month performance, approval chain]
</context>

<task>
The city needs a proactive monthly communication plan tied to projects, meetings, and events.
Produce: a channel-by-channel monthly communications calendar with message themes and owner assignments.
</task>

<inputs>
- projects
- events
- holidays
- meeting dates
- known public issues
- channel mix and audience segments
- approval lead times
- crisis or sensitive topics to hold
- translation needs
</inputs>

<checks>
- balance proactive and reactive content
- account for approval needs
- avoid overpromising deadlines
- do not promise dates that depend on council action
- leave room for breaking issues
- avoid campaign-sensitive timing
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Monthly calendar by channel and date
2. Message themes with proof points
3. Owner and approval assignments
4. Gaps and risks
5. Metrics to track
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
