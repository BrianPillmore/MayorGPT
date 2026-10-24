---
name: board-appointment-check
description: Screen board and commission appointments for eligibility, term logic, ward/residency rules, and attendance concerns.
argument-hint: [board-name]
---

# Board Appointment Check

**Purpose:** Before a nomination reaches the dais, confirm the person is eligible, the seat is actually vacant, the term math is right, and no conflict or incompatibility problem will void the appointment.

## Required inputs
- Board's enabling provision (charter, ordinance, or state statute) and bylaws
- Roster: member, seat, appointing authority, term start/end, appointment date
- Candidate application and any disclosures
- Attendance records for incumbents (for reappointment or removal questions)

## Workflow
1. **Identify the seat.** Is it a regular term, unexpired term (fill-the-balance), or alternate? Confirm who appoints (mayor with council consent, council alone, manager, outside agency) and the vote required.
2. **Check eligibility.** Typical criteria to verify against your own law: residency (city, ward, district) and when it must begin; elector or voter registration; age; professional or seat-specific qualifications (e.g., architect on a design board); employment limits.
3. **Check incompatibility and dual-office rules.** Can the person hold another public office or city employment? State law often bars incompatible offices; a spouse or business relationship with staff or applicants may trigger recusal rules.
4. **Compute terms.** Start/end dates, staggering, holdover rule (does the member serve until a successor is appointed?), term limits and whether partial terms count.
5. **Attendance and removal.** If reviewing an incumbent, compare absences with the bylaw threshold, check whether excused absences count, and confirm removal authority and process (notice, hearing, vote).
6. **Procedure.** Was the vacancy publicly noticed as required? Were applications open? Does the nomination need an agenda item with the name stated? Oath, financial-disclosure filing, and training deadlines after appointment.
7. **Roster impact.** Check quorum and balance rules (political-party or geographic balance, if any).

## Output structure
- Eligibility table: criterion | source | candidate status | evidence needed
- Term calculation (dates shown)
- Procedural steps and timeline (notice, vote, oath, onboarding)
- Open issues and recommended draft action (feed to `resolution-drafter`)

## Red flags / escalate to the city attorney
- Candidate holds another public office or city contract
- Residency or ward status unverified or disputed
- Seat appears filled or term expired by operation of law
- Removal of a member for cause or for exercise of speech/political activity
- Any rule conflict between charter and ordinance on who appoints

## Common mistakes
- Appointing to a full term when only the unexpired term is open
- Ignoring holdover provisions, so two people claim a seat
- Skipping the public vacancy notice
- Forgetting oath and disclosure filings, which can invalidate early votes

*Verify against your charter and state law; this is a screening aid, not legal advice.*
