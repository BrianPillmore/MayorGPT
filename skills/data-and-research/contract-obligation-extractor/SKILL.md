---
name: contract-obligation-extractor
description: Extract deadlines, deliverables, payment triggers, notice clauses, and renewal points from a contract.
argument-hint: [contract-name]
---

## Purpose
Convert a contract into a working obligation register so the city meets its own duties, enforces the vendor's, and acts before notice windows, auto-renewals, and insurance expirations pass. This is an extraction and calendar tool, not a legal interpretation; ambiguous clauses go to the city attorney.

## Required inputs
- Full executed contract with all exhibits, amendments, change orders, task orders, and referenced documents (RFP, proposal, insurance requirements).
- Contract administrator and department owner; funding source and appropriation.
- Procurement file basics (method, threshold, approval date) and any grant flow-down terms.

## Workflow
1. Identify parties, effective date, term, renewal options, and the order of precedence among documents.
2. Extract obligations of each party: scope and deliverables with due dates, acceptance criteria, performance standards and service levels, reporting, personnel or subcontractor approvals, and key-person provisions.
3. Money terms: price, rate schedule, escalators (with index and cap), not-to-exceed, invoicing and payment timing (and statutory prompt-payment interest), retainage, milestone payments, expenses, liquidated damages, and credits.
4. Notice and option dates: renewal or non-renewal notice windows, termination for convenience or cause (notice period, cure period), price adjustment dates, and audit rights. Compute the actual calendar date of each trigger and set an advance reminder.
5. Risk allocation: indemnification, limitation of liability, insurance types and limits with certificate expiry dates, bonds (bid, performance, payment) and expiry, warranties, and dispute resolution and venue.
6. Compliance: prevailing wage, E-Verify or similar where required, non-discrimination, federal flow-downs (2 CFR 200 Appendix II) for grant-funded contracts, public records provisions, data protection and security, and ownership of work product and data.
7. Appropriation and authority: non-appropriation clause, signature authority, and council approval record. Flag auto-renew clauses that obligate funds beyond the fiscal year.
8. Build the register and calendar; note gaps (missing exhibits, unsigned amendments) and conflicts between documents.

## Output structure
| # | Clause | Party | Obligation | Trigger / date | Reminder date | Owner | $ effect | Risk |
Add: key terms summary (one page), critical dates calendar, insurance/bond tracker, and unresolved ambiguities for counsel.

## Red flags / escalate
- Auto-renewal with a short notice window or multi-year commitments without non-appropriation language.
- Unlimited indemnity or liability caps that exclude key risks.
- Termination or exclusivity terms that restrict city options.
- Missing insurance or expired certificates.
- Data ownership, AI/analytics rights, or public records conflicts in technology contracts.
- Missing required federal clauses on grant-funded work.

## Common mistakes
- Relying on the cover summary rather than the full text.
- Ignoring amendments and exhibits.
- Computing deadlines without business-day and notice-delivery rules.
- Treating vendor proposals as part of the contract without checking incorporation.

## State-law variance
Prompt-payment, auto-renewal, indemnity limits, and contract authority rules vary by state.
