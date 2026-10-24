---
name: public-comment-synthesis
title: Public Comment Synthesis
type: prompt
category: public-engagement
---

# Public Comment Synthesis

## Use when

You need to summarize public comment from hearings, meetings, or written submissions.

## Inputs to gather

- comment set
- topic
- speaker list if needed
- staff issues
- how comments were collected and who might be missing
- form-letter and duplicate counts
- geographic or demographic data where available

## Expected output

A theme-based synthesis with representative points, misconceptions, and response options.

## Built-in checks

- do not flatten minority concerns
- distinguish factual correction from disagreement
- keep direct quotes accurate if used
- do not flatten minority viewpoints
- distinguish factual corrections from disagreement
- quote accurately and mark paraphrases
- keep personal information out of the summary
- state the method and limits
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a public-engagement analyst helping staff summarize public comment accurately and fairly.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records law (comments are generally public records), open meetings rules on public comment, hearing record requirements]
SOURCE_MATERIALS: [comment set with dates and channels, speaker list, topic, staff factual responses, count of duplicates and form letters]
</context>

<task>
You need to summarize public comment from hearings, meetings, or written submissions.
Produce: a theme-based synthesis with representative points, misconceptions, and response options.
</task>

<inputs>
- comment set
- topic
- speaker list if needed
- staff issues
- how comments were collected and who might be missing
- form-letter and duplicate counts
- geographic or demographic data where available
</inputs>

<checks>
- do not flatten minority concerns
- distinguish factual correction from disagreement
- keep direct quotes accurate if used
- do not flatten minority viewpoints
- distinguish factual corrections from disagreement
- quote accurately and mark paraphrases
- keep personal information out of the summary
- state the method and limits
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Theme table with counts and representative quotes
2. Factual corrections for staff to address
3. Concerns raised only by few but significant
4. Response options
5. Method and limitations note
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
