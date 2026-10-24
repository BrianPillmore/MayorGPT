---
name: town-hall-briefing
title: Town Hall Briefing
type: prompt
category: public-engagement
---

# Town Hall Briefing

## Use when

You need a structured prep packet for a public meeting, town hall, or listening session.

## Inputs to gather

- topic
- audience
- venue/format
- likely concerns
- known facts
- decision timeline and what input will change
- translation and accommodation requests
- staff and subject-matter experts attending
- ground rules

## Expected output

An event brief with agenda, messages, ground rules, likely questions, and follow-up plan.

## Built-in checks

- make the purpose clear
- prepare for hard questions
- plan follow-up and note-taking
- state the purpose and what will be done with input
- prepare answers for hard questions and say when the answer is unknown
- check whether a quorum of the body attending triggers meeting rules and flag state-law variance
- plan note-taking and follow-up
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an engagement planner helping the mayor, manager, or staff prepare for a town hall or listening session.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [open meetings law if a quorum may attend, accessibility and language access requirements, facility use and security rules, campaign-activity restrictions]
SOURCE_MATERIALS: [topic and purpose, audience, venue and format, known concerns, fact sheet, speaker roster, security and accessibility plan]
</context>

<task>
You need a structured prep packet for a public meeting, town hall, or listening session.
Produce: an event brief with agenda, messages, ground rules, likely questions, and follow-up plan.
</task>

<inputs>
- topic
- audience
- venue/format
- likely concerns
- known facts
- decision timeline and what input will change
- translation and accommodation requests
- staff and subject-matter experts attending
- ground rules
</inputs>

<checks>
- make the purpose clear
- prepare for hard questions
- plan follow-up and note-taking
- state the purpose and what will be done with input
- prepare answers for hard questions and say when the answer is unknown
- check whether a quorum of the body attending triggers meeting rules and flag state-law variance
- plan note-taking and follow-up
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Event brief with agenda and ground rules
2. Key messages and fact sheet
3. Likely hard questions with draft answers
4. Logistics and accessibility checklist
5. Follow-up plan within a stated number of days
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
