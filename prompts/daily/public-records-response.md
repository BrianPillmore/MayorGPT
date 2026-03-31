---
name: public-records-response
title: Public Records / FOIA Response
type: prompt
category: daily
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Public Records / FOIA Response

## Use when

You have received a public records or FOIA request and need to triage it, identify responsive records and custodians, apply any applicable exemptions, and draft a timely written response.

## Inputs to gather

- original request text and submission date
- applicable state public records law and local policy
- statutory response deadline
- known responsive records (or initial assessment of what may exist)
- any potentially exempt categories (attorney-client, personnel, ongoing investigation, etc.)
- name and role of the requester (if public)

## Expected output

A triage summary with responsive-records inventory, exemption analysis, draft response letter, and internal checklist for meeting the legal deadline.

## Built-in checks

- confirm response deadline under state law
- do not over-redact or under-produce
- separate withholding grounds (exemption vs. privilege vs. third-party notice)
- flag records that require legal review before release
- do not reveal the existence of records that are themselves confidential

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with public records and FOIA request triage and response drafting.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [state public records act, local policy, response-deadline rules, fee schedule, redaction procedures]
SOURCE_MATERIALS: [original request text, date received, known records inventory, any prior correspondence]
</context>

<task>
A public records or FOIA request has been received and must be triaged and answered within the legal deadline.
Produce a triage summary, responsive-records inventory with exemption flags, a draft response letter, and a deadline-management checklist.
</task>

<inputs>
- original request text and submission date
- applicable state public records law and local policy
- statutory response deadline
- known responsive records or preliminary inventory assessment
- potentially exempt categories (attorney-client, personnel, ongoing investigation, security, deliberative process)
- requester name and role if public
</inputs>

<checks>
- confirm response deadline under state law and calendar it
- do not over-redact or under-produce
- separate legal exemption from mere sensitivity — sensitivity alone is not a basis for withholding
- flag any records requiring city attorney review before release
- note whether a fee estimate or clarification request to the requester is appropriate
- do not confirm or deny the existence of records that are independently privileged or exempt
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
