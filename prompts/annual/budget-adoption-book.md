---
name: budget-adoption-book
title: Budget Adoption Book
type: prompt
category: annual
---

# Budget Adoption Book

## Use when

You need a polished summary for workshops or adoption.

## Inputs to gather

- proposed budget
- major changes
- fund summaries
- capital plan
- fee/rate changes
- general fund balance and reserve position against policy
- staffing changes by department
- revenue assumptions and their risk
- what changed since the last workshop
- what is being deferred

## Expected output

An adoption-ready summary book with narrative, highlights, trade-offs, and public-facing explanations.

## Built-in checks

- plain language first
- show major changes and why
- separate policy choice from required cost growth
- label every figure as recurring or one-time
- separate required cost growth (contracts, pensions, mandates) from discretionary policy choices
- show tax, fee, and rate effects on a typical household or business
- do not present deferred maintenance as savings
- flag notice, hearing, and publication requirements and state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal budget communications analyst helping staff turn a proposed budget into an adoption-ready summary for council workshops and the public.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state budget-adoption and notice requirements, charter budget provisions, fund-balance and reserve policies, council-adopted financial policies, truth-in-taxation or rate-notice rules where applicable]
SOURCE_MATERIALS: [proposed budget document, change log from prior year, fund summaries, capital plan, fee and rate schedules, staffing changes, council direction from workshops]
</context>

<task>
You need a polished summary for workshops or adoption.
Produce: an adoption-ready summary book with narrative, highlights, trade-offs, and public-facing explanations.
</task>

<inputs>
- proposed budget
- major changes
- fund summaries
- capital plan
- fee/rate changes
- general fund balance and reserve position against policy
- staffing changes by department
- revenue assumptions and their risk
- what changed since the last workshop
- what is being deferred
</inputs>

<checks>
- plain language first
- show major changes and why
- separate policy choice from required cost growth
- label every figure as recurring or one-time
- separate required cost growth (contracts, pensions, mandates) from discretionary policy choices
- show tax, fee, and rate effects on a typical household or business
- do not present deferred maintenance as savings
- flag notice, hearing, and publication requirements and state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. One-page budget-in-brief in plain language
2. Major changes table with reason and fiscal effect
3. Trade-offs and options council can still change
4. Public FAQ of likely questions
5. Adoption-calendar checklist with required notices
6. Open items for the finance director
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
