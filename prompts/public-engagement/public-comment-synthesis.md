---
name: public-comment-synthesis
title: Public Comment Synthesis
type: prompt
category: public-engagement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Public Comment Synthesis

## Use when

You need to summarize public comment from hearings, meetings, or written submissions.

## Inputs to gather

- comment set
- topic
- speaker list if needed
- staff issues

## Expected output

A theme-based synthesis with representative points, misconceptions, and response options.

## Built-in checks

- do not flatten minority concerns
- distinguish factual correction from disagreement
- keep direct quotes accurate if used

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with public comment synthesis.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need to summarize public comment from hearings, meetings, or written submissions.
Produce a theme-based synthesis with representative points, misconceptions, and response options.
</task>

<inputs>
- comment set
- topic
- speaker list if needed
- staff issues
</inputs>

<checks>
- do not flatten minority concerns
- distinguish factual correction from disagreement
- keep direct quotes accurate if used
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
