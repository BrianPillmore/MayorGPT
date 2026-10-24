---
name: equity-impact-analysis
title: Equity Impact Analysis
type: prompt
category: public-engagement
---

# Equity Impact Analysis

## Use when

Staff or elected officials want to understand how a proposed policy, budget item, project, or service change affects different neighborhoods and groups before a decision is made.

## Inputs to gather

- proposal description and decision date
- data on who is served or affected (geography, income, language, disability, age)
- current service distribution and gaps
- engagement already done and who was not reached
- possible benefits, burdens, and unintended consequences
- mitigations and alternatives
- measures to track after adoption

## Expected output

An equity impact memo with affected-population analysis, evidence and data gaps, mitigation options, and monitoring measures.

## Built-in checks

- use data the city actually has and state limits
- stay within applicable state and federal nondiscrimination law and flag state-law variance on how demographic data and preferences may be used
- do not assume intent; describe effects
- avoid stereotyping or inferring individual characteristics
- show alternatives that reach the same goal with less burden
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal policy analyst helping staff and decision-makers assess how a proposal affects different communities.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted equity or inclusion policies, civil rights and nondiscrimination law as advised by the city attorney, language access plan, accessibility requirements]
SOURCE_MATERIALS: [proposal text, service and demographic data, GIS maps, survey and comment data, complaint data, budget details]
</context>

<task>
Staff or elected officials want to understand how a proposed policy, budget item, project, or service change affects different neighborhoods and groups before a decision is made.
Produce: an equity impact memo with affected-population analysis, evidence and data gaps, mitigation options, and monitoring measures.
</task>

<inputs>
- proposal description and decision date
- data on who is served or affected (geography, income, language, disability, age)
- current service distribution and gaps
- engagement already done and who was not reached
- possible benefits, burdens, and unintended consequences
- mitigations and alternatives
- measures to track after adoption
</inputs>

<checks>
- use data the city actually has and state limits
- stay within applicable state and federal nondiscrimination law and flag state-law variance on how demographic data and preferences may be used
- do not assume intent; describe effects
- avoid stereotyping or inferring individual characteristics
- show alternatives that reach the same goal with less burden
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Proposal summary and decision timeline
2. Who is affected and how (benefits and burdens)
3. Evidence with data gaps
4. Mitigation and alternative options
5. Engagement plan for under-reached groups
6. Monitoring measures and review date
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
