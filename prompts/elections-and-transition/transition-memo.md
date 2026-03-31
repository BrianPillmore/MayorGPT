---
name: transition-memo
title: Transition Memo
type: prompt
category: elections-and-transition
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Transition Memo

## Use when

A newly elected official or incoming administration needs a handoff packet.

## Inputs to gather

- current issues
- calendar
- major contracts/projects
- fiscal status
- staff contacts

## Expected output

A transition memo organized into first 30/90/180 day issues and key decisions ahead.

## Built-in checks

- be candid
- prioritize decision points
- separate urgent from important

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with transition memo.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A newly elected official or incoming administration needs a handoff packet.
Produce a transition memo organized into first 30/90/180 day issues and key decisions ahead.
</task>

<inputs>
- current issues
- calendar
- major contracts/projects
- fiscal status
- staff contacts
</inputs>

<checks>
- be candid
- prioritize decision points
- separate urgent from important
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
