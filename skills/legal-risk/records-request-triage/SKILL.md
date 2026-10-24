---
name: records-request-triage
description: Triage a public records request into likely custodians, date ranges, exclusions, sensitive material, and response steps.
argument-hint: [request]
---

# Records Request Triage

**Purpose:** Early-stage intake: understand the request, start the clock, find the custodians, and flag sensitivity before drafting a response. For the full response letter and exemption analysis use `public-records-response`. Statutory deadlines, fees, and exemptions vary by state.

## Required inputs
- Request text, date and channel received, requester information
- State act and city records policy; retention schedule
- Org chart or department list; systems inventory

## Workflow
1. **Start the clock:** note date received and compute the statutory response and extension dates (verify business vs. calendar days). Calendar internal deadlines two to three days earlier.
2. **Is it a valid request?** Written form, reasonably described records, correct recipient; routing to the designated records officer. Questions are not always "records requests"; the act may not require creating records or answering questions.
3. **Parse scope:** subject, date range, record types (email, text, video, spreadsheets, calendars, drafts), persons named, and keywords.
4. **Map custodians and systems:** departments, individual employees, elected officials, vendors holding city data, backup or archive. Include personal accounts if used for city business.
5. **Retention check:** do the records still exist per the schedule? If scheduled for destruction, pause destruction on responsive records (see `records-retention-trigger-check`).
6. **Sensitivity screen:** privileged communications, personnel/medical, law-enforcement or investigation records, security plans, juvenile or victim data, Social Security and account numbers, bids in progress, third-party trade secrets. Mark for attorney review rather than withholding by default.
7. **Burden and clarification:** if broad, contact the requester to refine scope; document the exchange and whether the clock pauses.
8. **Assign and track:** owner, due dates, search log, estimate of volume and cost.

## Output structure
- Intake summary (one paragraph) and deadline table
- Custodian/system matrix: who | system | search method | date range | due
- Sensitivity flags
- Draft clarification note (if needed)
- Next steps with owners

## Red flags / escalate to the city attorney
- Request linked to litigation, claims, or personnel complaint
- Requester is media, an opponent, or counsel (does not change duties; heightens scrutiny)
- Request for personal-device records, body-camera video, or investigation files
- Records scheduled for destruction

## Common mistakes
- Missing the first acknowledgment deadline
- Searching only the main email system
- Narrowing the request without the requester's agreement

*Not legal advice.*
