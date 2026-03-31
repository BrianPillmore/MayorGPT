---
name: ai-governance-refresh
title: AI Governance Refresh
type: prompt
category: annual
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# AI Governance Refresh

## Use when

The city wants an annual refresh of acceptable-use, review, and oversight practices for AI.

## Inputs to gather

- current policy
- tools used
- incidents or concerns
- training needs
- governance goals

## Expected output

A policy refresh memo, training priorities, and implementation checklist.

## Built-in checks

- address records/privacy/security
- identify approval thresholds
- clarify human review expectations

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with ai governance refresh.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city wants an annual refresh of acceptable-use, review, and oversight practices for AI.
Produce a policy refresh memo, training priorities, and implementation checklist.
</task>

<inputs>
- current policy
- tools used
- incidents or concerns
- training needs
- governance goals
</inputs>

<checks>
- address records/privacy/security
- identify approval thresholds
- clarify human review expectations
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
