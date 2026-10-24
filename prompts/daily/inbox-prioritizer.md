---
name: inbox-prioritizer
title: Inbox Prioritizer
type: prompt
category: daily
---

# Inbox Prioritizer

## Use when

An elected or executive office needs help sorting email into action buckets.

## Inputs to gather

- email batch
- known priorities
- sensitive senders
- deadlines
- messages involving litigation, personnel, safety, media, or elected officials
- items with a hard deadline today or tomorrow
- duplicates or threads that can be merged

## Expected output

A prioritized list grouped into respond, delegate, watch, schedule, and archive.

## Built-in checks

- flag legal/media issues
- separate FYI from action
- preserve tone and confidentiality
- safety, legal, and media items rise to the top regardless of sender
- do not draft replies to confidential matters without confirming who may see them
- do not delete or archive anything subject to a records hold
- flag anything that appears to be a records request
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an executive-office assistant helping triage a batch of email into action buckets while protecting confidentiality.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records and retention rules for email, privilege and personnel confidentiality, executive-office priority list, sensitive-sender list]
SOURCE_MATERIALS: [email batch (subject, sender, summary), current priorities, VIP and sensitive-sender list, calendar, pending deadlines]
</context>

<task>
An elected or executive office needs help sorting email into action buckets.
Produce: a prioritized list grouped into respond, delegate, watch, schedule, and archive.
</task>

<inputs>
- email batch
- known priorities
- sensitive senders
- deadlines
- messages involving litigation, personnel, safety, media, or elected officials
- items with a hard deadline today or tomorrow
- duplicates or threads that can be merged
</inputs>

<checks>
- flag legal/media issues
- separate FYI from action
- preserve tone and confidentiality
- safety, legal, and media items rise to the top regardless of sender
- do not draft replies to confidential matters without confirming who may see them
- do not delete or archive anything subject to a records hold
- flag anything that appears to be a records request
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Respond-today list with a suggested action
2. Delegate list with suggested owner
3. Watch and schedule lists with dates
4. Archive candidates
5. Flags for legal, media, or safety review
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
