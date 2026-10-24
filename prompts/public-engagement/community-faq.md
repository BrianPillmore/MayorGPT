---
name: community-faq
title: Community FAQ Builder
type: prompt
category: public-engagement
---

# Community FAQ Builder

## Use when

Residents keep asking the same questions and the city needs a public FAQ.

## Inputs to gather

- topic
- source materials
- common questions
- known misconceptions
- audience and languages
- date of last update
- which answers are final versus pending

## Expected output

A public-facing FAQ with plain-language answers and pointers to source documents or contacts.

## Built-in checks

- use simple language
- state what is not yet known
- do not overlegalize the tone
- say what is not yet known and when it will be
- attribute each answer to a source document
- do not overlegalize or promise outcomes
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a public information writer helping the city publish an honest, plain-language FAQ on a topic residents keep asking about.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records and open meetings law, language access and accessibility requirements, adopted policy text]
SOURCE_MATERIALS: [topic documents, questions received, known misconceptions, staff subject-matter input, decision timeline, contacts]
</context>

<task>
Residents keep asking the same questions and the city needs a public FAQ.
Produce: a public-facing FAQ with plain-language answers and pointers to source documents or contacts.
</task>

<inputs>
- topic
- source materials
- common questions
- known misconceptions
- audience and languages
- date of last update
- which answers are final versus pending
</inputs>

<checks>
- use simple language
- state what is not yet known
- do not overlegalize the tone
- say what is not yet known and when it will be
- attribute each answer to a source document
- do not overlegalize or promise outcomes
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. FAQ with short answers
2. Source and contact links
3. Items marked pending
4. Maintenance plan with review date
5. Social-media version
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
