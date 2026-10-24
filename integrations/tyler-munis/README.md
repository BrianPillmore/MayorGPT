# Tyler Munis Integration

Tyler Munis is one of the most widely used ERP platforms in municipal government, covering general ledger, budget management, accounts payable, purchasing, payroll, and utility billing. MayorGPT does not connect directly to Munis — there is no API integration. Instead, this guide explains how to export the right data from Munis, prepare it for AI-assisted analysis, and pair it with the appropriate MayorGPT skills.

## Budget documents to export and attach

The following Munis exports are the most useful inputs for MayorGPT financial workflows. Export these as Excel (.xlsx) or CSV unless a PDF is the only option.

**For budget analysis and variance review:**
- Budget vs. Actual by Department (GL Trial Balance report, filtered to current fiscal year)
- Revenue Budget vs. Actual by Fund (Revenue Analysis report)
- Amended Budget by fund and department (Budget Amendment Summary)
- Prior-year actuals for comparison (prior fiscal year GL close)

**For CIP and capital budget work:**
- CIP Project Status report (project-to-date expenditures vs. budget by project number)
- Capital Outlay by Department (filtered from GL Trial Balance)
- Grant Fund activity by project (Revenue and Expenditure by Fund, filtered to grant fund numbers)

**For cash and reserve analysis:**
- Fund Balance Summary (Balance Sheet by Fund, as of the most recent close)
- Monthly Cash Position report (if your Munis instance generates one)
- Debt Service Schedule (from the Debt Management module or a manual export)

**For grant and intergovernmental work:**
- Grant Revenue and Expenditure by Project (Project Accounting module)
- Reimbursement request history (Accounts Payable detail filtered by grant vendor)

**For purchasing and procurement context:**
- Open Purchase Order report by department
- Vendor payment history (useful for sole-source and cooperative purchasing documentation)

## How to format financial data for AI

Raw Munis exports often contain formatting that makes AI analysis harder. Before attaching, do the following:

- **Remove subtotal and grand total rows that Munis auto-inserts**, or clearly label them. AI can misread subtotals as individual line items and produce inflated totals.
- **Keep column headers on row 1.** Munis sometimes puts report title information in the first several rows with the actual header on row 5 or 6. Delete the title rows or move the header up.
- **Add a "Fund" column if the export covers multiple funds.** Munis sometimes lists the fund name only in a section header row, not in each data row. Add the fund name as a column before attaching so the AI can filter and compare by fund.
- **Round to whole dollars.** Cent-level precision in a budget variance memo adds noise without value. Round before attaching unless cent precision is genuinely required (e.g., a reconciliation).
- **Label the time period in the filename or a header cell.** "GL Trial Balance.xlsx" is ambiguous. "GL-Trial-Balance-FY2026-Q2-close.xlsx" tells the AI what period the data covers without requiring the user to explain it in the prompt.
- **Separate funds into tabs if attaching multi-fund exports.** The General Fund, enterprise funds, and debt service funds have different financial structures. A single flat export that mixes them requires the AI to do structural work that is better done in Excel before attaching.

## What NOT to paste into AI sessions

The following Munis data categories should never be pasted into a general-purpose AI session, even temporarily. Some may also be restricted from AI use entirely by your jurisdiction's IT and legal policies — confirm before proceeding.

- **Employee payroll detail**: Individual employee names, salaries, deductions, direct deposit information, W-2 data, or any Munis Payroll module output that identifies individual employees. Aggregate payroll by department or position class is acceptable; individual employee data is not.
- **Social Security numbers**: Munis stores SSNs for payroll tax purposes. These should never appear in any AI input.
- **Employee benefits enrollment data**: Health insurance elections, FSA contributions, retirement plan details, or any data from the Benefits module that identifies an individual.
- **Vendor taxpayer identification numbers (TINs/EINs)**: These appear in 1099 reporting contexts in Munis. Remove or mask them before attaching any 1099-related export.
- **Utility billing account details**: If your Munis instance includes the Utility Billing module, do not paste data that links a specific address or account number to a named individual, balance due, or payment history.
- **Pending litigation or claim payment data**: Accounts Payable records related to settlements, claims, or insurance recoveries may be privileged or sensitive. Confirm with City Attorney before using in AI analysis.

## MayorGPT skills that pair best with Munis exports

| Munis export | Recommended skill | Stack |
|---|---|---|
| GL Trial Balance (budget vs. actual) | `budget-variance-analysis` | Budget Season Stack |
| Revenue Budget vs. Actual | `revenue-forecast-scenario` | Budget Season Stack |
| CIP Project Status | `cip-prioritizer` | Budget Season Stack |
| Fund Balance Summary | `revenue-forecast-scenario` | Budget Season Stack |
| Debt Service Schedule | `debt-financing-brief` | Budget Season Stack |
| Audit finding detail | `audit-response-builder` | Budget Season Stack |
| KPI / service data export | `kpi-dashboard-narrative` | City Manager Stack |
| Grant Project Accounting export | `grant-compliance-check` | Grant Pursuit Stack |
| Open Purchase Order report | `staff-report-builder` (procurement section) | City Manager Stack |

## Suggested workflow

1. Identify the MayorGPT skill and stack appropriate for your task.
2. Pull the corresponding Munis exports listed above.
3. Apply the formatting preparation steps in this guide.
4. Open a session in your approved AI tool, configured with the appropriate agent and stack (see `integrations/README.md`).
5. Attach the prepared Munis export and any supporting documents (adopted budget, prior-year comparison, grant agreement).
6. Run the skill prompt. Review the output against the raw Munis data before using it in any memo or report.
7. Have Finance Director or Budget Officer review any output before it goes to City Manager, Council, or the public.

Munis data is authoritative. AI analysis of Munis data is a working draft. The human reviewer — not the AI — is responsible for confirming that the numbers match the source.
