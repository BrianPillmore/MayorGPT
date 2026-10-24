---
name: consent-calendar-screen
description: Screen proposed consent-calendar items for eligibility, hidden controversy, fiscal thresholds, and legal-notice problems before the agenda is published.
argument-hint: [meeting-date]
---

# Consent Calendar Screen

**Purpose:** The consent calendar approves many items in a single vote without discussion. This skill decides which items truly belong there and which must be pulled to the regular agenda.

## Required inputs
- Draft consent list with staff reports
- Council rules on consent eligibility and how items are pulled
- Procurement and fiscal thresholds; prior council direction on any item

## Workflow
1. **Eligibility test for each item:** routine, non-controversial, previously discussed or clearly authorized by policy, and not requiring a hearing, findings, or a separate vote. Typical eligible items: approval of minutes, routine bills, pre-authorized contract renewals, accepting grants within policy.
2. **Hard exclusions to verify locally:** public hearings, ordinances on first or second reading if rules require separate votes, quasi-judicial matters, land-use decisions, appointments in some cities, sole-source contracts above threshold, settlement approvals (also see closed-session rules), and items needing a supermajority or roll call by member.
3. **Hidden controversy scan:** media coverage, constituent emails, prior split votes, neighborhood objections, an applicant or vendor who is a known flashpoint, or an item with a recent change in amount.
4. **Fiscal check:** amounts, funding source, match requirements, budget-amendment need; whether the aggregate exceeds a threshold calling for discussion.
5. **Conflict check:** members who must recuse from any item need a way to vote separately (see `ethics-conflict-check`). The "pull" mechanism must allow one member to remove an item.
6. **Wording:** each item's title must describe the action. Avoid bundling unrelated approvals in one line.
7. **Announce the process:** chair's script covering how items are pulled and when public comment on consent items occurs.

## Output structure
- Table: item | eligible (Y/N) | reason | recommended placement | owner
- Items to pull and why
- Chair's script and motion: "I move approval of the consent calendar, items __ through __, except items __."

## Red flags / escalate to the city attorney
- Items that need findings, notice, or a hearing slipped in as routine
- A conflicted member's item combined with others
- Contracts with change orders that exceed original authority

## Common mistakes
- Using consent to avoid debate on a politically sensitive item
- Burying dollar amounts in an attachment
- Forgetting that recording rules (roll-call by member) may still apply

*Check local rules; not legal advice.*
