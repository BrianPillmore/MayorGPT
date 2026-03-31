---
name: financial-review
title: Monthly Financial Review
type: prompt
category: monthly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Monthly Financial Review

## Use when

Leadership needs a monthly look at revenues, expenditures, variances, cash, and claims.

## Inputs to gather

- revenue reports
- expense reports
- fund balances
- major claims
- known anomalies

## Expected output

A monthly finance memo explaining trendlines, outliers, and actions needed.

## Built-in checks

- separate timing variance from real variance
- note one-time items
- flag procurement or control concerns

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with monthly financial review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
Leadership needs a monthly look at revenues, expenditures, variances, cash, and claims.
Produce a monthly finance memo explaining trendlines, outliers, and actions needed.
</task>

<inputs>
- revenue reports
- expense reports
- fund balances
- major claims
- known anomalies
</inputs>

<checks>
- separate timing variance from real variance
- note one-time items
- flag procurement or control concerns
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
