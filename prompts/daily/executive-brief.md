---
name: executive-brief
title: Executive Brief
type: prompt
category: daily
---

# Executive Brief

## Use when

You need a one-page briefing for the mayor, city manager, or council on a fast-moving issue.

## Inputs to gather

- topic
- known facts
- decision needed
- deadline
- attachments
- who decides and under what authority
- cost range and funding source
- what happens if no decision is made by the deadline
- what is not yet known and who will find out

## Expected output

A short executive brief with issue, background, options, recommendation, risks, and next steps.

## Built-in checks

- front-load the decision
- use plain language
- highlight unknowns
- show time sensitivity
- lead with the decision needed and the deadline
- label facts, assumptions, and opinions separately
- present at least two options plus do-nothing
- do not include privileged legal advice in a brief that will circulate beyond its intended readers
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a chief-of-staff style analyst helping prepare a one-page decision brief for the mayor, city manager, or council.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [delegation of authority, council action requirements, confidentiality and privilege rules for closed-session material]
SOURCE_MATERIALS: [topic summary, known facts, source documents, decision deadline, stakeholders, fiscal estimates, legal input received]
</context>

<task>
You need a one-page briefing for the mayor, city manager, or council on a fast-moving issue.
Produce: a short executive brief with issue, background, options, recommendation, risks, and next steps.
</task>

<inputs>
- topic
- known facts
- decision needed
- deadline
- attachments
- who decides and under what authority
- cost range and funding source
- what happens if no decision is made by the deadline
- what is not yet known and who will find out
</inputs>

<checks>
- front-load the decision
- use plain language
- highlight unknowns
- show time sensitivity
- lead with the decision needed and the deadline
- label facts, assumptions, and opinions separately
- present at least two options plus do-nothing
- do not include privileged legal advice in a brief that will circulate beyond its intended readers
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Decision statement and deadline
2. Background in five lines or fewer
3. Options with cost, risk, and tradeoffs
4. Recommendation with rationale
5. Unknowns and next steps with owners
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
