---
name: resolution-draft
title: Resolution Draft
type: prompt
category: legislation-and-procurement
---

# Resolution Draft

## Use when

You need a resolution for appointments, policy statements, approvals, or formal findings.

## Inputs to gather

- action requested
- background
- authority
- recitals needed
- effective timing
- whether the action actually requires an ordinance
- named parties, amounts, and dates
- exhibits to attach

## Expected output

A clean draft resolution with recitals and action language.

## Built-in checks

- use resolution when ordinance is unnecessary
- make action language specific
- confirm signatures/attestation blocks
- use a resolution only where an ordinance is not required; confirm with the city attorney
- make the operative language specific and bounded
- include signature and attestation blocks
- do not use recitals to assert facts that are not documented
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal legislative drafter helping prepare a resolution for council action.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter and code on when a resolution versus an ordinance is required, rules of procedure, attestation and signature requirements]
SOURCE_MATERIALS: [action requested, background, authority source, recitals, effective timing, funding impact, attachments]
</context>

<task>
You need a resolution for appointments, policy statements, approvals, or formal findings.
Produce: a clean draft resolution with recitals and action language.
</task>

<inputs>
- action requested
- background
- authority
- recitals needed
- effective timing
- whether the action actually requires an ordinance
- named parties, amounts, and dates
- exhibits to attach
</inputs>

<checks>
- use resolution when ordinance is unnecessary
- make action language specific
- confirm signatures/attestation blocks
- use a resolution only where an ordinance is not required; confirm with the city attorney
- make the operative language specific and bounded
- include signature and attestation blocks
- do not use recitals to assert facts that are not documented
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Draft resolution with recitals and resolved clauses
2. Plain-language summary for the agenda
3. Exhibit and attachment list
4. Procedure notes
5. Issues for legal review
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
