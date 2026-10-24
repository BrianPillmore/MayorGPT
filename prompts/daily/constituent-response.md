---
name: constituent-response
title: Constituent Response
type: prompt
category: daily
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
- whether the sender is a repeat contact
- whether the issue is a service defect, a policy disagreement, or a legal claim
- any deadline the resident cited

## Expected output

A reply draft, internal escalation note, and any follow-up questions or promises to avoid.

## Built-in checks

- separate policy issue from service issue
- do not overpromise
- protect personal information
- offer a next step
- if the message mentions a safety hazard, discrimination, a threat, or a claim for damages, flag it for immediate routing instead of a routine reply
- never commit to a date or outcome the department has not confirmed
- treat the reply as a public record
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a constituent-services writer helping a city office reply to a resident with a calm, accurate, useful message.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city service standards, public records implications of email, confidentiality rules, council-staff communication protocol]
SOURCE_MATERIALS: [resident message, service-request history, department notes on facts and constraints, prior correspondence, preferred signature and tone]
</context>

<task>
You need a calm, useful response to a resident complaint, question, compliment, or service request.
Produce: a reply draft, internal escalation note, and any follow-up questions or promises to avoid.
</task>

<inputs>
- resident message
- known facts
- department notes
- prior response if any
- desired tone
- whether the sender is a repeat contact
- whether the issue is a service defect, a policy disagreement, or a legal claim
- any deadline the resident cited
</inputs>

<checks>
- separate policy issue from service issue
- do not overpromise
- protect personal information
- offer a next step
- if the message mentions a safety hazard, discrimination, a threat, or a claim for damages, flag it for immediate routing instead of a routine reply
- never commit to a date or outcome the department has not confirmed
- treat the reply as a public record
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Reply draft ready to send
2. Internal escalation note with owner and urgency
3. Follow-up questions for the department
4. Commitments to avoid
5. Suggested tracking tag
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
