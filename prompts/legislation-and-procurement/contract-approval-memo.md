---
name: contract-approval-memo
title: Contract Approval Memo
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Contract Approval Memo

## Use when

A contract is moving to council or executive approval.

## Inputs to gather

- draft contract
- scope
- amount
- funding source
- procurement path
- risk issues

## Expected output

An approval memo summarizing scope, cost, procurement path, key terms, and review status.

## Built-in checks

- state dollar value clearly
- show funding source
- note legal/procurement review completion

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with contract approval memo.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
A contract is moving to council or executive approval.
Produce an approval memo summarizing scope, cost, procurement path, key terms, and review status.
</task>

<inputs>
- draft contract
- scope
- amount
- funding source
- procurement path
- risk issues
</inputs>

<checks>
- state dollar value clearly
- show funding source
- note legal/procurement review completion
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
