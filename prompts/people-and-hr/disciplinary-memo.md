---
name: disciplinary-memo
title: Disciplinary Memo
type: prompt
category: people-and-hr
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Disciplinary Memo

## Use when

You need a memo for corrective action or discipline.

## Inputs to gather

- facts
- policy violated
- prior coaching
- employee response if any
- proposed action

## Expected output

A professional, factual memo with expectations and next steps.

## Built-in checks

- stay factual
- avoid inflammatory phrasing
- protect due process and consistency

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with disciplinary memo.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a memo for corrective action or discipline.
Produce a professional, factual memo with expectations and next steps.
</task>

<inputs>
- facts
- policy violated
- prior coaching
- employee response if any
- proposed action
</inputs>

<checks>
- stay factual
- avoid inflammatory phrasing
- protect due process and consistency
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
