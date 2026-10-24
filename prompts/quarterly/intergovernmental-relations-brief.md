---
name: intergovernmental-relations-brief
title: Intergovernmental Relations Brief
type: prompt
category: quarterly
---

# Intergovernmental Relations Brief

## Use when

The mayor or manager needs a concise regional/state/federal relationship brief.

## Inputs to gather

- partner list
- current asks
- upcoming meetings
- funding/policy issues
- coalition notes
- status of each ask and who owns it
- upcoming decision dates
- partner positions known or inferred (label inferred)
- commitments made to partners

## Expected output

A brief with partner status, current asks, sensitivities, and next engagement steps.

## Built-in checks

- state asks precisely
- show mutual benefit
- note political or timing sensitivities
- state each ask precisely
- label what is confirmed versus inferred about partner positions
- flag timing and political sensitivities and conflicts among partners
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an intergovernmental-affairs analyst helping the mayor or manager track regional, state, and federal relationships.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [council-adopted legislative agenda, lobbying and public-funds rules, interlocal agreements, regional body governance rules]
SOURCE_MATERIALS: [partner list, current asks, upcoming meetings, funding and policy issues, coalition notes, contact history]
</context>

<task>
The mayor or manager needs a concise regional/state/federal relationship brief.
Produce: a brief with partner status, current asks, sensitivities, and next engagement steps.
</task>

<inputs>
- partner list
- current asks
- upcoming meetings
- funding/policy issues
- coalition notes
- status of each ask and who owns it
- upcoming decision dates
- partner positions known or inferred (label inferred)
- commitments made to partners
</inputs>

<checks>
- state asks precisely
- show mutual benefit
- note political or timing sensitivities
- state each ask precisely
- label what is confirmed versus inferred about partner positions
- flag timing and political sensitivities and conflicts among partners
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Partner status table
2. Current asks with owner and date
3. Sensitivities and risks
4. Next engagement steps
5. Items needing council authorization
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
