---
name: survey-summary
title: Survey Summary
type: prompt
category: public-engagement
---

# Survey Summary

## Use when

The city wants a readable synthesis of resident survey results.

## Inputs to gather

- survey results
- demographic cuts if any
- open-ended responses
- purpose of survey
- response rate and margin of error
- who is underrepresented
- year-over-year comparisons

## Expected output

A summary with toplines, notable splits, open-ended themes, and suggested next steps.

## Built-in checks

- state sample limitations
- separate strong results from weak signals
- avoid false precision
- state sample size and limitations
- avoid false precision on small subgroups
- do not imply causation
- redact identifying information in verbatims
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a survey analyst helping the city turn resident survey results into an honest, readable summary.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [survey method documentation, public records law, privacy rules for open-ended responses]
SOURCE_MATERIALS: [survey instrument, response data, sample and weighting method, open-ended responses, demographic data, prior survey results]
</context>

<task>
The city wants a readable synthesis of resident survey results.
Produce: a summary with toplines, notable splits, open-ended themes, and suggested next steps.
</task>

<inputs>
- survey results
- demographic cuts if any
- open-ended responses
- purpose of survey
- response rate and margin of error
- who is underrepresented
- year-over-year comparisons
</inputs>

<checks>
- state sample limitations
- separate strong results from weak signals
- avoid false precision
- state sample size and limitations
- avoid false precision on small subgroups
- do not imply causation
- redact identifying information in verbatims
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Toplines in plain language
2. Notable differences by group
3. Open-ended themes
4. Limitations note
5. Suggested next steps and follow-up questions
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
