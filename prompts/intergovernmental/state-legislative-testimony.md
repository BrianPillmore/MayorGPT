---
name: state-legislative-testimony
title: State Legislative Testimony
type: prompt
category: intergovernmental
---

# State Legislative Testimony

## Use when

The city needs to prepare written or oral testimony on state legislation that would affect municipal authority, revenue, services, or operations — either in support, opposition, or with requested amendments.

## Inputs to gather

- bill number, title, and current version text
- sponsoring legislator and committee of referral
- hearing date and format (oral, written, remote)
- city's position (support, oppose, support with amendments)
- specific impacts on the city (fiscal, operational, legal authority)
- any state municipal league or association position
- local examples or data that illustrate city impact

## Expected output

A testimony draft (written and/or oral summary), a fiscal and operational impact analysis, recommended amendments if the city seeks modifications, and a list of supporting municipalities or stakeholders.

## Built-in checks

- confirm city has formally adopted a position before testifying
- quantify fiscal impact with local data where possible
- do not misrepresent the bill's text or intent
- note any preemption of local authority and its constitutional dimensions
- flag any conflict between the city's position and the state municipal league's position
- flag testimony length and format requirements for the specific committee

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping prepare city testimony on state legislation.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city's adopted legislative agenda, council resolution or direction, charter home-rule authority, state municipal association guidance]
SOURCE_MATERIALS: [bill text, fiscal note if available, committee hearing notice, city's prior testimony on related bills, local data and examples]
</context>

<task>
The city is preparing written or oral testimony on a state bill that affects municipal operations, authority, or revenue.
Produce a testimony draft, a fiscal and operational impact analysis, recommended amendments if applicable, and a list of supporting jurisdictions or stakeholders.
</task>

<inputs>
- bill number, title, and current engrossed version text
- sponsoring legislator and committee of referral
- hearing date, format, and testimony submission requirements
- city's formal position (support / oppose / support with amendments)
- specific fiscal, operational, or legal authority impacts on this city
- applicable state municipal league or association position and any coalition activity
- local examples, data, or constituent stories that illustrate city impact
</inputs>

<checks>
- confirm the city has formally adopted a position (council resolution or delegated authority) before testifying
- quantify fiscal impact using local data, not just statewide estimates
- accurately represent the bill's actual text and current version — do not characterize based on earlier drafts
- flag any local authority preemption and its home-rule or constitutional dimensions
- note any divergence between city position and state municipal league position, and explain why
- confirm testimony length, format, and submission deadline for this specific committee
</checks>

<required_output>
1. Testimony draft (written and oral version)
2. Fiscal and operational impact analysis
3. Recommended amendments
4. Supporting municipalities and stakeholders
5. Format and timing notes for the committee
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
