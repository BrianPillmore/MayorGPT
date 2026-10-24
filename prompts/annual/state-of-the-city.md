---
name: state-of-the-city
title: State of the City
type: prompt
category: annual
---

# State of the City

## Use when

The mayor or manager needs an annual community narrative.

## Inputs to gather

- major wins
- major challenges
- data points
- project list
- public tone
- speaking time and format
- three to five themes the speaker wants to land
- issues that are sensitive or subject to litigation or negotiation
- credit and acknowledgments list

## Expected output

A speech or report that balances celebration, honesty, and the year ahead.

## Built-in checks

- be specific
- avoid hype
- show residents why the story matters
- every claim is supported by a number, project, or named result
- no hype superlatives or promises that need council or budget action
- address at least one real challenge candidly
- keep political advocacy and ballot or candidate content out of an official address
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal speechwriter and communications analyst helping the mayor or city manager draft an honest annual community address.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [mayor and council role boundaries, ethics and campaign-activity rules on use of public resources, speaker style guide]
SOURCE_MATERIALS: [annual accomplishments, performance data, major project list, financial highlights, hard challenges, resident feedback, quotes cleared for use]
</context>

<task>
The mayor or manager needs an annual community narrative.
Produce: a speech or report that balances celebration, honesty, and the year ahead.
</task>

<inputs>
- major wins
- major challenges
- data points
- project list
- public tone
- speaking time and format
- three to five themes the speaker wants to land
- issues that are sensitive or subject to litigation or negotiation
- credit and acknowledgments list
</inputs>

<checks>
- be specific
- avoid hype
- show residents why the story matters
- every claim is supported by a number, project, or named result
- no hype superlatives or promises that need council or budget action
- address at least one real challenge candidly
- keep political advocacy and ballot or candidate content out of an official address
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Speech draft sized to the time slot
2. Fact-check table linking each claim to a source
3. Shorter written report version for the website
4. Social posts and quotable lines
5. Likely follow-up questions and answers
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
