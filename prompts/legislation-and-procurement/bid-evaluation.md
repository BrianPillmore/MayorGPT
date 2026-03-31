---
name: bid-evaluation
title: Bid Evaluation
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Bid Evaluation

## Use when

You need a documented, fair comparison of bids, proposals, or quotes.

## Inputs to gather

- submissions
- criteria
- scores if any
- references
- exceptions/deviations

## Expected output

An evaluation memo and comparison matrix with recommendation and caveats.

## Built-in checks

- document deviations
- state basis for recommendation
- flag local preference or exception rules

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with bid evaluation.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
You need a documented, fair comparison of bids, proposals, or quotes.
Produce an evaluation memo and comparison matrix with recommendation and caveats.
</task>

<inputs>
- submissions
- criteria
- scores if any
- references
- exceptions/deviations
</inputs>

<checks>
- document deviations
- state basis for recommendation
- flag local preference or exception rules
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
