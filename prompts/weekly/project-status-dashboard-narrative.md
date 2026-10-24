---
name: project-status-dashboard-narrative
title: Project Status Dashboard Narrative
type: prompt
category: weekly
---

# Project Status Dashboard Narrative

## Use when

A dashboard needs human-readable narrative for leaders or the public.

## Inputs to gather

- project list
- status colors
- key milestones
- budget/schedule notes
- definition of red, yellow, and green
- what changed since the last update
- dependencies on other projects or agencies

## Expected output

Narrative summaries that explain status, changes, blockers, and what happens next.

## Built-in checks

- avoid color-only reporting
- explain red/yellow conditions
- show recovery steps
- never rely on color alone; state the reason for each yellow or red
- show recovery steps and dates
- keep public narrative free of confidential procurement or legal details
- reconcile narrative with dashboard figures
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a project-reporting analyst helping write plain-language narrative for a project status dashboard.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted capital and project policies, procurement and grant milestones, public records rules for public dashboards]
SOURCE_MATERIALS: [project list, status ratings, milestone dates, budget and schedule variance, risks, change orders, next steps]
</context>

<task>
A dashboard needs human-readable narrative for leaders or the public.
Produce: narrative summaries that explain status, changes, blockers, and what happens next.
</task>

<inputs>
- project list
- status colors
- key milestones
- budget/schedule notes
- definition of red, yellow, and green
- what changed since the last update
- dependencies on other projects or agencies
</inputs>

<checks>
- avoid color-only reporting
- explain red/yellow conditions
- show recovery steps
- never rely on color alone; state the reason for each yellow or red
- show recovery steps and dates
- keep public narrative free of confidential procurement or legal details
- reconcile narrative with dashboard figures
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Summary of overall portfolio
2. Per-project narrative (status, change, blocker, next step)
3. Red and yellow recovery plans
4. Budget and schedule variance notes
5. Items for leadership attention
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
