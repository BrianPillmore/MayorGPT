---
name: agenda-packet-builder
description: Build a city council or board agenda packet with readiness checks, missing attachments, hearing/publication flags, and item-by-item support notes.
argument-hint: [meeting-date or meeting-type]
---

# Agenda Packet Builder

**Purpose:** Assemble a packet the clerk can publish by the posting deadline and the council can act on without surprises. Use `packet-template.md` for layout and `checklist.md` for the final gate.

## Required inputs
- Meeting type (regular, special, adjourned, work session) and date/time/location, including remote-access details
- Draft item list with sponsor, department, and requested action for each item
- Local rules: agenda deadline, posting period, packet-distribution rule, consent-calendar rules
- Which items need a published or mailed notice (hearings, ordinances, land use, bids)

## Workflow
1. **Back-calculate deadlines.** Starting from the meeting date, list: staff-report due date, legal review, fiscal review, clerk's agenda lock, posting deadline, packet release. Posting periods are set by state open-meetings law and local code; verify yours (special meetings usually have a shorter, stricter period).
2. **Classify each item** as consent, regular action, public hearing, discussion/presentation, closed session, or appointment. Consent items must be non-controversial and need no discussion; flag any item with known opposition or a fiscal threshold above local limits.
3. **Confirm legal basis per item.** Does the action require an ordinance (readings), a resolution, a motion, or a minute order? Is a published hearing notice, mailed notice, or supermajority vote required?
4. **Check attachments.** Staff report, draft ordinance/resolution, contract with exhibits, maps, fiscal note, environmental/review determination, prior minutes if relevant. Note version and file-name conflicts.
5. **Check agenda wording.** Each title must describe the action well enough that a reader knows what may be decided; meeting laws generally bar action on matters not fairly described. Avoid "discuss and take possible action" vagueness where state law disfavors it.
6. **Closed-session items:** cite the statutory ground and route to `executive-session-checklist`.
7. **Public comment placement and time limits** per local rules (see `public-hearing-prep`).
8. **Produce the readiness table** and the packet in order: call to order, approvals of minutes/agenda, public comment, consent, hearings, regular items, reports, adjournment.

## Output structure
1. Deadline timeline (table)
2. Item readiness table: item | action type | legal basis | notice needed | attachments in/missing | owner | status (Green/Yellow/Red)
3. Draft agenda in final order
4. Open issues, ranked

## Red flags / escalate to the city attorney
- Item description narrower or vaguer than the action staff actually wants
- Hearing item with missing, late, or defective notice
- Consent-calendar item with fiscal, contested, or land-use impact
- Late addition after posting (check your law on supplemental or emergency additions)
- Closed-session item without a cited legal ground
- Conflict of interest by a sponsoring member (see `ethics-conflict-check`)

## Common mistakes
- Counting calendar days when the rule counts business days (or vice versa)
- Posting the agenda but not the packet when local code requires both
- Attaching a draft contract without its exhibits or insurance certificate
- Leaving the "recommended motion" out, so the chair improvises on the dais

*Framework only; verify all deadlines against state law and local code. Not legal advice.*
