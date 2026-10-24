---
name: hiring-scorecard
title: Hiring Scorecard
type: prompt
category: people-and-hr
---

# Hiring Scorecard

## Use when

The city needs a structured interview and evaluation tool for hiring.

## Inputs to gather

- job description
- must-have competencies
- leadership traits
- panel size
- weighting of competencies
- panel training and conflict-of-interest screening
- reasonable accommodation process in interviews

## Expected output

A scorecard, question set, and interview packet.

## Built-in checks

- use job-related criteria only
- avoid discriminatory questions
- separate must-haves from stretch qualities
- avoid questions about protected characteristics, family, health, or pay history where restricted
- separate minimum qualifications from preferred qualities
- ask every candidate the same core questions
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an HR recruitment advisor helping build a structured, job-related interview and scoring tool.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [equal employment opportunity law, civil service or merit rules, local residency preferences, veterans preference rules, pay-history and background-check restrictions in the state]
SOURCE_MATERIALS: [job description and classification, essential functions, required qualifications, competencies, panel composition, recruitment timeline]
</context>

<task>
The city needs a structured interview and evaluation tool for hiring.
Produce: a scorecard, question set, and interview packet.
</task>

<inputs>
- job description
- must-have competencies
- leadership traits
- panel size
- weighting of competencies
- panel training and conflict-of-interest screening
- reasonable accommodation process in interviews
</inputs>

<checks>
- use job-related criteria only
- avoid discriminatory questions
- separate must-haves from stretch qualities
- avoid questions about protected characteristics, family, health, or pay history where restricted
- separate minimum qualifications from preferred qualities
- ask every candidate the same core questions
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Scorecard with weighted competencies
2. Structured question set with scoring anchors
3. Panel instructions and note-taking guide
4. Reference check template
5. Documentation retention reminder
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
