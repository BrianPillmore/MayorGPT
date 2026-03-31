---
name: project-status-dashboard-narrative
title: Project Status Dashboard Narrative
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Project Status Dashboard Narrative

## Use when

A dashboard needs human-readable narrative for leaders or the public.

## Inputs to gather

- project list
- status colors
- key milestones
- budget/schedule notes

## Expected output

Narrative summaries that explain status, changes, blockers, and what happens next.

## Built-in checks

- avoid color-only reporting
- explain red/yellow conditions
- show recovery steps

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with project status dashboard narrative.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A dashboard needs human-readable narrative for leaders or the public.
Produce narrative summaries that explain status, changes, blockers, and what happens next.
</task>

<inputs>
- project list
- status colors
- key milestones
- budget/schedule notes
</inputs>

<checks>
- avoid color-only reporting
- explain red/yellow conditions
- show recovery steps
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
