# Example 7: Grant Award and Compliance Setup

## Scenario

The fictional City of Brookfield Landing (pop. 17,500) has been awarded a state-administered, federally funded pass-through grant of $1.2 million for a sidewalk and lighting project, with a 20 percent local match. The award letter and grant agreement arrived this week. The Grants Director must set up compliance before anyone spends a dollar, and brief the City Manager and Council.

All names and figures are fictional. Federal grant rules are referenced only in general terms; program-specific terms control.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/departments/grants-and-intergovernmental-affairs-director.md` | Owns the grant file |
| Supporting agent | `agents/statutory-roles/finance-director-budget-officer.md` | Match, appropriation, and accounting |
| Supporting agent | `agents/statutory-roles/procurement-contract-administrator.md` | Procurement requirements |
| Prompt | `prompts/monthly/grant-pipeline-review.md` | Ongoing pipeline reporting |
| Skill | `skills/finance/grant-compliance-check/SKILL.md` | Builds the compliance calendar and obligations list |
| Skill | `skills/data-and-research/contract-obligation-extractor/SKILL.md` | Extracts obligations from the agreement |

## Why this combination works

Awards fail at execution more often than at application. Extracting obligations from the actual agreement, assigning an owner and a due date to each, and surfacing risks (match timing, procurement, reporting) before spending begins is the highest-value use of AI here.

## Key cautions

- **The agreement controls.** AI summaries do not replace reading the grant agreement and the incorporated regulations and program terms.
- **Federal pass-through rules apply through the state agency.** Which rules and thresholds apply depends on the funding source and the pass-through terms. The Finance Director and, where needed, the City Attorney confirm.
- **Do not start spending or procuring before the agreement's effective date and notice-to-proceed terms.**
- **Match must be real.** Confirm appropriation authority before relying on a match source.

## How to set it up

1. Attach the full agreement, award letter, special conditions, and project budget.
2. Run the obligation extractor, then the compliance check skill.
3. Review the output with Finance and Procurement; assign owners.
4. Compare to `output.md`.
