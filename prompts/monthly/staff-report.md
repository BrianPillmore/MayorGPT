---
name: staff-report
title: Staff Report Builder
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Staff Report Builder

## Use when

You need a clean, decision-ready staff report for council, a board, or a commission.

## Inputs to gather

- issue
- background
- legal/process requirements
- fiscal impact
- recommended action

## Expected output

A staff report with summary, background, analysis, options, recommendation, attachments, and action language.

## Built-in checks

- align recommendation to authority
- state fiscal impact clearly
- use neutral analysis before recommendation

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with staff report builder.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a clean, decision-ready staff report for council, a board, or a commission.
Produce a staff report with summary, background, analysis, options, recommendation, attachments, and action language.
</task>

<inputs>
- issue
- background
- legal/process requirements
- fiscal impact
- recommended action
</inputs>

<checks>
- align recommendation to authority
- state fiscal impact clearly
- use neutral analysis before recommendation
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
