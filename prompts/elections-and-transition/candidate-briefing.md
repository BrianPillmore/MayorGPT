---
name: candidate-briefing
title: Candidate Briefing
type: prompt
category: elections-and-transition
---

# Candidate Briefing

## Use when

The city wants a neutral, educational briefing for candidates or prospective candidates.

## Inputs to gather

- governance structure
- meeting schedule
- major issues
- ethics/legal boundaries
- fiscal facts
- whether all candidates receive the same material at the same time
- sensitive items that should not be shared (litigation, personnel, security)
- clerk and election official contact details

## Expected output

A neutral briefing deck or memo explaining roles, process, and major city issues.

## Built-in checks

- stay nonpartisan
- separate fact from advocacy
- avoid campaign advice
- present the same facts to every candidate
- exclude confidential, closed-session, and security-sensitive information
- do not characterize any candidate or position
- point to the clerk or election authority for filing and election-law questions
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a neutral municipal staff analyst helping the city prepare an educational briefing for candidates and prospective candidates.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [election-period neutrality rules, public records law, local ethics code, city candidate-information policy]
SOURCE_MATERIALS: [charter and governance summary, meeting calendar, budget overview, major projects and issues list, filing information from the clerk]
</context>

<task>
The city wants a neutral, educational briefing for candidates or prospective candidates.
Produce: a neutral briefing deck or memo explaining roles, process, and major city issues.
</task>

<inputs>
- governance structure
- meeting schedule
- major issues
- ethics/legal boundaries
- fiscal facts
- whether all candidates receive the same material at the same time
- sensitive items that should not be shared (litigation, personnel, security)
- clerk and election official contact details
</inputs>

<checks>
- stay nonpartisan
- separate fact from advocacy
- avoid campaign advice
- present the same facts to every candidate
- exclude confidential, closed-session, and security-sensitive information
- do not characterize any candidate or position
- point to the clerk or election authority for filing and election-law questions
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Briefing document: roles, process, calendar
2. Fact sheet on fiscal condition and major projects
3. Ethics and public-resource boundaries
4. FAQ
5. Distribution and equal-access plan
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
