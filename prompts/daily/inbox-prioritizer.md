---
name: inbox-prioritizer
title: Inbox Prioritizer
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Inbox Prioritizer

## Use when

An elected or executive office needs help sorting email into action buckets.

## Inputs to gather

- email batch
- known priorities
- sensitive senders
- deadlines

## Expected output

A prioritized list grouped into respond, delegate, watch, schedule, and archive.

## Built-in checks

- flag legal/media issues
- separate FYI from action
- preserve tone and confidentiality

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with inbox prioritizer.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
An elected or executive office needs help sorting email into action buckets.
Produce a prioritized list grouped into respond, delegate, watch, schedule, and archive.
</task>

<inputs>
- email batch
- known priorities
- sensitive senders
- deadlines
</inputs>

<checks>
- flag legal/media issues
- separate FYI from action
- preserve tone and confidentiality
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
