---
name: constituent-response
title: Constituent Response
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Constituent Response

## Use when

You need a calm, useful response to a resident complaint, question, compliment, or service request.

## Inputs to gather

- resident message
- known facts
- department notes
- prior response if any
- desired tone

## Expected output

A reply draft, internal escalation note, and any follow-up questions or promises to avoid.

## Built-in checks

- separate policy issue from service issue
- do not overpromise
- protect personal information
- offer a next step

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with constituent response.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a calm, useful response to a resident complaint, question, compliment, or service request.
Produce a reply draft, internal escalation note, and any follow-up questions or promises to avoid.
</task>

<inputs>
- resident message
- known facts
- department notes
- prior response if any
- desired tone
</inputs>

<checks>
- separate policy issue from service issue
- do not overpromise
- protect personal information
- offer a next step
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
