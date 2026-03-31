# Example 2: Mid-Year Budget Shortfall Discovery

## Scenario

The City of Larkspur Creek (pop. 22,000) is nine months into fiscal year 2025-26 (October–June budget year). The Finance Director's monthly close for February shows a $1.4 million projected General Fund shortfall against a $24.6 million adopted budget — driven by a combination of lower-than-projected sales tax receipts and overruns in the Police Department's overtime line. The City Manager needs a clear analysis memo and a set of options before briefing the council at the March work session in 12 days.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/statutory-roles/finance-director-budget-officer.md` | Owns the variance analysis; fiscal discipline, assumption transparency, one-time vs. recurring distinction |
| Supporting agent | `agents/executive-office/city-manager.md` | Receives the analysis; needs options framed for council briefing |
| Prompt | `prompts/monthly/financial-review.md` | Drives the monthly financial review format |
| Skill | `skills/finance/budget-variance-analysis/SKILL.md` | Step-by-step variance triage: timing noise vs. structural gap, scenario table, next steps |

**Optional additions:**
- `skills/finance/revenue-forecast-scenario/` to model sales tax recovery scenarios through year-end
- `skills/data-and-research/kpi-dashboard-narrative/` to frame the council briefing narrative

## Why this combination works

The finance-director agent enforces fiscal discipline: it will separate one-time events from recurring structural problems, show its assumptions, and flag internal-control or procurement issues. The `budget-variance-analysis` skill structures the triage so the output distinguishes timing variances (money that will correct by year-end) from genuine shortfalls requiring management action. The city-manager agent, used in a second pass, frames the options for council consumption — translating fiscal language into a decision brief the governing body can act on.

## Key cautions

- **Do not present AI-generated revenue projections as final.** The scenario table output is a starting framework. The Finance Director must validate every number against the actual general ledger and current revenue trend data.
- **Distinguish management authority from council action.** Some budget adjustments can be made by the manager within adopted authority; others require a formal budget amendment by ordinance or resolution. The AI should flag this distinction, but the city attorney and charter must confirm the threshold.
- **Personnel overtime has HR dimensions.** If the police overtime overrun involves specific individuals, that information is personnel-sensitive and should not be included in AI prompts in identifiable form.
- **Do not release a variance memo to council before the city manager reviews it.** The output from this workflow is a working draft, not a final product.

## How to set it up

1. Activate the `finance-director-budget-officer` agent as the primary role.
2. Activate the `budget-variance-analysis` skill.
3. Attach the source materials in `input.md` (budget-to-actual report, revenue trend data, department overrun summary).
4. Run the `financial-review` prompt to structure the deliverable.
5. Use the city-manager agent in a follow-on pass to translate the memo into a council briefing frame.
6. Review `output.md` to calibrate expectations.
