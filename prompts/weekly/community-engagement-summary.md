---
name: community-engagement-summary
title: Community Engagement Summary
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
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

## Expected output

A theme-based summary with representative concerns, sentiment, and suggested follow-up.

## Built-in checks

- identify recurring issues
- separate anecdote from trend
- avoid amplifying fringe noise

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with community engagement summary.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need to summarize what the city heard from residents over the past week.
Produce a theme-based summary with representative concerns, sentiment, and suggested follow-up.
</task>

<inputs>
- emails
- public comments
- social trends
- event notes
- survey snippets
</inputs>

<checks>
- identify recurring issues
- separate anecdote from trend
- avoid amplifying fringe noise
</checks>

<required_output>
1. Brief issue framing
2. Draft work product
3. Key risks / missing information
4. Recommended next step
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- For Claude, keep long source material above the task block when possible and put the ask near the end of the prompt.
