---
name: strategic-priority-review
title: Strategic Priority Review
type: prompt
category: quarterly
---

# Strategic Priority Review

## Use when

The city needs a quarterly scorecard on adopted goals or council priorities.

## Inputs to gather

- priority list
- status notes
- owner updates
- budget tie-ins
- public concerns
- evidence for each status rating
- resource constraints
- decisions that would unblock progress
- goals that are no longer realistic

## Expected output

A strategic review with status, evidence, slippage reasons, and quarter-ahead focus.

## Built-in checks

- tie work to adopted priorities
- name what is off-track
- refresh owners and dates
- tie each item to an adopted priority
- use evidence, not owner optimism, for status
- name what is off track and why
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a performance analyst helping leadership score progress against council-adopted priorities.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted strategic plan or council goals, performance measures, budget appropriations]
SOURCE_MATERIALS: [priority list, measures and targets, owner updates, milestone dates, budget tie-ins, public concerns]
</context>

<task>
The city needs a quarterly scorecard on adopted goals or council priorities.
Produce: a strategic review with status, evidence, slippage reasons, and quarter-ahead focus.
</task>

<inputs>
- priority list
- status notes
- owner updates
- budget tie-ins
- public concerns
- evidence for each status rating
- resource constraints
- decisions that would unblock progress
- goals that are no longer realistic
</inputs>

<checks>
- tie work to adopted priorities
- name what is off-track
- refresh owners and dates
- tie each item to an adopted priority
- use evidence, not owner optimism, for status
- name what is off track and why
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Scorecard by priority (on track, at risk, off track)
2. Evidence and variance notes
3. Slippage causes and recovery steps
4. Next-quarter focus
5. Council decisions needed
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
