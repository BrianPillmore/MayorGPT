---
name: after-action-review
title: After Action Review
type: prompt
category: emergencies
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# After Action Review

## Use when

The city is wrapping an incident and wants structured learning rather than blame.

## Inputs to gather

- timeline
- what worked
- what failed
- resource issues
- public feedback

## Expected output

An after-action report with observations, corrective actions, owners, and deadlines.

## Built-in checks

- stay factual
- name systemic fixes
- assign owners and due dates

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with after action review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city is wrapping an incident and wants structured learning rather than blame.
Produce an after-action report with observations, corrective actions, owners, and deadlines.
</task>

<inputs>
- timeline
- what worked
- what failed
- resource issues
- public feedback
</inputs>

<checks>
- stay factual
- name systemic fixes
- assign owners and due dates
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
