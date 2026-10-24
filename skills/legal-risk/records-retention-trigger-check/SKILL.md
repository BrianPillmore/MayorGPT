---
name: records-retention-trigger-check
description: Determine retention periods, event triggers, and destruction holds for a category of city records before disposal or response.
argument-hint: [record-category]
---

# Records Retention Trigger Check

**Purpose:** Decide whether records may be disposed of, must be kept, or must be frozen. Retention schedules come from state archives law and the city's adopted schedule; **do not cite or invent periods. Look up the actual schedule.**

## Required inputs
- Record category, format (paper, email, text, video, database), and date range
- The city's adopted retention schedule and state minimum schedule
- Pending or anticipated claims, audits, records requests, or investigations
- Grant, bond, or contract retention requirements

## Workflow
1. **Classify** the record under the schedule series (e.g., financial, personnel, contract, permit, minutes, police, correspondence). Content, not format, determines series; email is not a single series.
2. **Identify the trigger** that starts the clock: creation date, end of fiscal year, contract expiration or close-out, case closure, termination of employment, project completion, grant close-out, or superseded date. Wrong trigger gives wrong disposal date.
3. **Apply the period** and compute the earliest disposal date. Note permanent or archival series (ordinances, minutes, resolutions, charters are typically permanent; verify).
4. **Check overrides that suspend disposal:** litigation hold or reasonably anticipated litigation (`litigation-hold-checklist`), pending public-records request (`records-request-triage`), audit or investigation, grant requirements, and statute-of-limitations considerations.
5. **Duplicates and transitory records:** convenience copies and drafts often have shorter retention only if the schedule says so; the official record copy has a designated owner.
6. **Digital issues:** auto-deletion rules, chat and text apps, personal devices, vendor-hosted data, migration, readable formats.
7. **Disposal process:** documented authorization by the records officer, certificate of destruction, secure destruction for confidential items, and recording what was destroyed and when.
8. **Gaps:** if no series fits, ask the state archives or attorney; do not default to deletion.

## Output structure
- Record table: series | trigger | period | earliest disposal date | holds | action
- Holds and overrides found
- Disposal authorization checklist
- Unknowns for follow-up

## Red flags / escalate to the city attorney
- Any hold, claim, request, or audit touching the records
- Records already destroyed that were responsive or subject to a hold
- Personal-account communications about city business
- Request to purge to avoid a public records request

## Common mistakes
- Using a fixed number of years without a trigger event
- Auto-deleting email system-wide
- Destroying originals after a scan without approval to do so

*Not legal advice.*
