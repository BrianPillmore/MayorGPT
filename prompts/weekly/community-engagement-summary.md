---
name: community-engagement-summary
title: Community Engagement Summary
type: prompt
category: weekly
---

# Community Engagement Summary

## Use when

You need to summarize what the city heard from residents over the past week.

## Inputs to gather

- emails
- public comments
- social trends
- event notes
- survey snippets
- volume versus prior weeks
- representation of neighborhoods and languages
- verified versus unverified claims

## Expected output

A theme-based summary with representative concerns, sentiment, and suggested follow-up.

## Built-in checks

- identify recurring issues
- separate anecdote from trend
- avoid amplifying fringe noise
- do not amplify a small number of loud voices
- mark misinformation and the needed correction
- protect personal information
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a community-engagement analyst helping the city understand what residents said this week.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records law, privacy rules, social-media policy, language access requirements]
SOURCE_MATERIALS: [emails and calls, public comments, social media trends, event notes, survey snippets, service-request data]
</context>

<task>
You need to summarize what the city heard from residents over the past week.
Produce: a theme-based summary with representative concerns, sentiment, and suggested follow-up.
</task>

<inputs>
- emails
- public comments
- social trends
- event notes
- survey snippets
- volume versus prior weeks
- representation of neighborhoods and languages
- verified versus unverified claims
</inputs>

<checks>
- identify recurring issues
- separate anecdote from trend
- avoid amplifying fringe noise
- do not amplify a small number of loud voices
- mark misinformation and the needed correction
- protect personal information
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Themes with counts and representative quotes
2. Sentiment and change from prior week
3. Misinformation or correction needs
4. Suggested follow-up by department
5. Gaps in who was heard
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
