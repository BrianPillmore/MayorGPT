---
name: audit-response
title: Audit Response
type: prompt
category: annual
---

# Audit Response

## Use when

The city needs to respond to audit findings, comments, or management recommendations.

## Inputs to gather

- audit findings
- management comments
- control notes
- owner assignments
- deadlines
- finding classification (material weakness, significant deficiency, compliance, or advisory) as stated by the auditor
- root cause for each finding
- prior-year repeat findings
- resources needed to correct

## Expected output

A response memo with corrective actions, owners, dates, and communication language.

## Built-in checks

- do not be defensive
- state control improvement clearly
- assign owners and dates
- quote the auditor's finding accurately before responding
- distinguish agree, partially agree, and disagree and give a factual basis for any disagreement
- each corrective action needs one named owner, a date, and a way to verify completion
- flag repeat findings and any finding with legal or grant-repayment exposure
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal finance and compliance analyst helping management draft a clear, non-defensive response to external or internal audit findings.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [audit report and management-letter format, state auditor requirements, internal-control framework adopted by the city, council or audit-committee reporting rules]
SOURCE_MATERIALS: [audit report and finding text, prior-year findings and status, control narratives, department responses, corrective-action owners and dates]
</context>

<task>
The city needs to respond to audit findings, comments, or management recommendations.
Produce: a response memo with corrective actions, owners, dates, and communication language.
</task>

<inputs>
- audit findings
- management comments
- control notes
- owner assignments
- deadlines
- finding classification (material weakness, significant deficiency, compliance, or advisory) as stated by the auditor
- root cause for each finding
- prior-year repeat findings
- resources needed to correct
</inputs>

<checks>
- do not be defensive
- state control improvement clearly
- assign owners and dates
- quote the auditor's finding accurately before responding
- distinguish agree, partially agree, and disagree and give a factual basis for any disagreement
- each corrective action needs one named owner, a date, and a way to verify completion
- flag repeat findings and any finding with legal or grant-repayment exposure
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Finding-by-finding response table (finding, management position, corrective action, owner, due date)
2. Executive summary for council or the audit committee
3. Resident-safe summary if the audit will be public
4. Tracking plan for verifying closure
5. Items needing legal or auditor clarification
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
