---
name: language-access-and-inclusive-outreach-plan
title: Language Access and Inclusive Outreach Plan
type: prompt
category: public-engagement
---

# Language Access and Inclusive Outreach Plan

## Use when

The city is planning outreach for a project, emergency, or service change and needs to reach residents who speak other languages, have disabilities, lack internet access, or are otherwise hard to reach.

## Inputs to gather

- topic, decision timeline, and what input will influence
- languages and communities in the service area (census, school, and service-request data)
- disability and accessibility needs
- trusted community partners and venues
- existing translation and interpreter resources and budget
- channels residents actually use
- prior engagement results

## Expected output

An outreach plan with audience segments, channels, translation and accessibility actions, partner roles, budget, and measures of reach.

## Built-in checks

- plan accessibility and translation from the start, not as an afterthought
- use qualified translators and interpreters and review machine translation before publishing
- confirm language-access obligations with the city attorney and flag state and federal variance
- pay or support community partners fairly
- track who was reached, not just how many
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal community-engagement planner helping the city design inclusive, accessible, multilingual outreach.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted language access plan, ADA and accessibility standards, public meeting notice rules, procurement rules for interpreters and translators]
SOURCE_MATERIALS: [language and demographic data, past engagement summaries, partner list, budget, communications channel data, project schedule]
</context>

<task>
The city is planning outreach for a project, emergency, or service change and needs to reach residents who speak other languages, have disabilities, lack internet access, or are otherwise hard to reach.
Produce: an outreach plan with audience segments, channels, translation and accessibility actions, partner roles, budget, and measures of reach.
</task>

<inputs>
- topic, decision timeline, and what input will influence
- languages and communities in the service area (census, school, and service-request data)
- disability and accessibility needs
- trusted community partners and venues
- existing translation and interpreter resources and budget
- channels residents actually use
- prior engagement results
</inputs>

<checks>
- plan accessibility and translation from the start, not as an afterthought
- use qualified translators and interpreters and review machine translation before publishing
- confirm language-access obligations with the city attorney and flag state and federal variance
- pay or support community partners fairly
- track who was reached, not just how many
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Audience and language segments
2. Channel and event plan with accessibility measures
3. Translation and interpretation workflow
4. Partner roles and compensation
5. Timeline and budget
6. Reach and quality measures
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
