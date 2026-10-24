---
name: media-talking-points
title: Media Talking Points
type: prompt
category: daily
---

# Media Talking Points

## Use when

A leader or spokesperson needs concise public-facing talking points for media or stakeholder calls.

## Inputs to gather

- topic
- audience
- facts confirmed
- sensitive facts
- quote source if any
- interview format and deadline
- who has approved release of each fact
- prior inconsistent statements
- what the spokesperson must not say

## Expected output

Core messages, quotable language, do-not-say notes, and likely Q&A.

## Built-in checks

- do not speculate
- stay on-record appropriate
- show empathy when needed
- every statement of fact must be confirmed and cleared for release
- do not speculate on cause, fault, or outcome
- do not comment on pending litigation, personnel matters, or active investigations unless counsel approves
- lead with the impact on residents and what they should do
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a public information officer helping a spokesperson prepare accurate, on-record talking points for media or stakeholder calls.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records and open meetings law, personnel and litigation confidentiality, city media policy, authorized-spokesperson designation]
SOURCE_MATERIALS: [topic summary, confirmed facts, sensitive facts, prior statements, reporter or outlet and question topics, legal and operations review notes]
</context>

<task>
A leader or spokesperson needs concise public-facing talking points for media or stakeholder calls.
Produce: core messages, quotable language, do-not-say notes, and likely Q&A.
</task>

<inputs>
- topic
- audience
- facts confirmed
- sensitive facts
- quote source if any
- interview format and deadline
- who has approved release of each fact
- prior inconsistent statements
- what the spokesperson must not say
</inputs>

<checks>
- do not speculate
- stay on-record appropriate
- show empathy when needed
- every statement of fact must be confirmed and cleared for release
- do not speculate on cause, fault, or outcome
- do not comment on pending litigation, personnel matters, or active investigations unless counsel approves
- lead with the impact on residents and what they should do
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Three core messages
2. Quotable lines
3. Do-not-say list with reasons
4. Likely questions with draft answers
5. Bridge phrases for questions outside the spokesperson's role
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
