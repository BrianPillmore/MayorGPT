---
name: invoice-claim-review
description: Summarize a claim, invoice batch, or approval item for executive or council review, including funding source and red flags.
argument-hint: [claim-batch]
---

## Purpose
Prepare a pre-audit review of a claims/warrant register or individual invoice so that approvers can see what is being paid, under what authority, from which fund, and what could be wrong. This is a review summary; it does not replace the finance officer's certification or the legal duty to audit claims.

## Required inputs
- Claims list or invoice images with vendor, invoice number, date, amount, fund/account, and department approver.
- Purchase orders, contracts, change orders, receiving documents, and bid or quote file for items of concern.
- Budget status for each affected account and appropriation level.
- Vendor master data: W-9, address, bank change requests, and prior payments.

## Workflow
1. Verify each item against the three-way match: purchase order or contract, receiving or acceptance evidence, and invoice. Missing receiving evidence is an exception.
2. Authority check: contract executed before service? Within the delegated spending authority of the approver? Above the competitive bidding threshold or council approval threshold (use the city's adopted thresholds; state thresholds vary)?
3. Duplicate and splitting test: same vendor, similar amounts, same dates; multiple invoices just under a purchasing threshold; invoice numbers sequential or repeated.
4. Funding test: correct fund and account? Enough appropriation? Restricted funds used only for eligible purposes (grants, gas tax, utility enterprise)? Interfund implications?
5. Vendor test: new vendor or changed bank details (verify by independent call-back to a known contact), employee or official relationship (conflict of interest), debarment for federally funded items, 1099 reporting, and sales tax exemption handling.
6. Pricing and terms: unit prices vs. contract, change orders not approved, retainage handling on construction, prompt-payment law interest, and travel or P-card items against policy.
7. Timing: late fees, discounts, year-end cutoff (accrual to correct fiscal year), and whether the item is a prior-year obligation.
8. Summarize: totals by fund, exceptions by severity, items to hold, and items recommended for approval.

## Output structure
| Claim # | Vendor | Amount | Fund/Account | Authority | 3-way match | Exception | Severity | Recommendation (approve/hold/query) |

Add: totals by fund, funding-source note, exceptions list with the question to ask, and items requiring council action (above thresholds, no contract, emergency purchase ratification).

## Red flags / escalate
- Payment without a contract or purchase order, or backdated documents.
- Vendor bank-account change request by email (possible business email compromise).
- Related-party vendors, or an approver who is also the requester.
- Splitting to avoid bidding or approval limits.
- Payment from restricted funds for ineligible purposes.
- Round-dollar, unusual, or after-hours invoices from a new vendor.
- Suspected fraud: stop, preserve records, and notify the finance director and city attorney.

## Common mistakes
- Treating department approval as proof of delivery.
- Approving to avoid late charges without resolving exceptions.
- Mixing multiple fiscal years in one cutoff.
- Not documenting why an exception was accepted.

## State-law variance
Claims audit, warrant signing, and prompt-pay rules differ by state. Emergency purchase ratification procedures vary.
