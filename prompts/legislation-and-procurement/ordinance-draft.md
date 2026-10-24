---
name: ordinance-draft
title: Ordinance Draft
type: prompt
category: legislation-and-procurement
---

# Ordinance Draft

## Use when

You need to draft or revise an ordinance.

## Inputs to gather

- policy goal
- authority source
- existing code text
- enforcement approach
- effective date needs
- sections of code to be amended or repealed
- definitions needed
- exemptions and savings clause
- public notice and hearing requirements

## Expected output

A draft ordinance with purpose, operative language, procedural notes, and issue flags.

## Built-in checks

- state amendment target clearly
- define enforcement and effective date
- flag publication/hearing needs
- identify the section being amended and show strike/underline style when possible
- state enforcement, penalty, and effective date
- do not cite statutes or cases that were not provided; flag state-law variance and preemption questions
- mark that the draft needs city attorney review before introduction
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal legislative drafter helping prepare an ordinance for review by the city attorney.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code, enabling state statute supplied by the city attorney, adoption procedure (readings, hearings, publication), codification style guide]
SOURCE_MATERIALS: [policy goal, authority source, existing code text, enforcement approach, penalties, fiscal impact, effective date needs, stakeholder input]
</context>

<task>
You need to draft or revise an ordinance.
Produce: a draft ordinance with purpose, operative language, procedural notes, and issue flags.
</task>

<inputs>
- policy goal
- authority source
- existing code text
- enforcement approach
- effective date needs
- sections of code to be amended or repealed
- definitions needed
- exemptions and savings clause
- public notice and hearing requirements
</inputs>

<checks>
- state amendment target clearly
- define enforcement and effective date
- flag publication/hearing needs
- identify the section being amended and show strike/underline style when possible
- state enforcement, penalty, and effective date
- do not cite statutes or cases that were not provided; flag state-law variance and preemption questions
- mark that the draft needs city attorney review before introduction
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Draft ordinance with title, findings, operative text, and effective date
2. Section-by-section explanation
3. Procedure and notice checklist
4. Issue flags for the city attorney
5. Fiscal and implementation notes
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
