# Budget Season Stack

## Best for
Budget kickoff, workshops, adoption books, variance review, CIP ranking, and audit follow-up.

## When to activate
Pull this stack when the annual budget calendar opens, when mid-year variance numbers land, when a department submits a supplemental request that needs vetting, when the CIP list needs prioritization before a workshop, or when an audit finding requires a written management response.

## Combine
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Agent: `agents/executive-office/city-manager.md`
- Agent: `agents/external-advisors/municipal-advisor.md`
- Prompt folder: `prompts/annual/`
- Skills: `budget-variance-analysis`, `revenue-forecast-scenario`, `cip-prioritizer`, `debt-financing-brief`, `audit-response-builder`

## Sequence
1. **Finance Director agent + revenue-forecast-scenario** — establish the revenue baseline and scenario range before any spending decisions. Attach prior-year actuals, current-year estimates, and assessor/sales-tax projections.
2. **Finance Director agent + budget-variance-analysis** — run mid-year or year-end variance analysis against adopted budget. Requires the GL trial balance export and the adopted budget by fund.
3. **City Manager agent + cip-prioritizer** — once revenue envelope is set, rank CIP requests using the scoring criteria. Attach department CIP submittals and the current adopted CIP.
4. **Municipal Advisor agent + debt-financing-brief** — evaluate financing options for any CIP items that need bonding. Requires preliminary project cost estimates and the city's current debt schedule.
5. **Finance Director agent + audit-response-builder** — draft management responses to audit findings. Requires the draft audit report with findings and the corrective action plan from the responsible department.

## Watch for
- **Revenue optimism creep**: AI-assisted forecasts can anchor to recent high-growth years. Always run a downside scenario and have Finance Director agent narrate both sides before the City Manager sees the envelope.
- **CIP scope inflation**: Departments often reframe wish-list items as critical infrastructure once AI is helping write justifications. Cross-check every CIP narrative against the asset management plan or existing condition assessment.
- **Audit response softening**: The audit-response-builder may draft language that is more conciliatory than the auditor will accept. Human Finance staff must confirm that every finding has a specific corrective action, owner, and deadline.
- **Fund confusion**: Municipal budgets run across multiple funds (General, Enterprise, Capital, Debt Service). Verify that every AI-drafted analysis clearly labels which fund it addresses before sharing with Council.
