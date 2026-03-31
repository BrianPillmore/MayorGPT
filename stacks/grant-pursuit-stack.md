# Grant Pursuit Stack

## Best for
Identifying grant opportunities, writing competitive applications, managing grant compliance, and reporting on the grant pipeline to leadership and Council.

## When to activate
Pull this stack when a new federal or state program is announced and needs eligibility screening, when an application deadline is approaching, when a department has a project that may be grantable and needs a feasibility check, when a grant report or compliance deliverable is due, or when the City Manager or Council wants a pipeline overview.

## Combine
- Agent: `agents/departments/grants-and-intergovernmental-affairs-director.md`
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Prompt: `prompts/monthly/grant-pipeline-review`
- Prompt: `prompts/legislation-and-procurement/grant-application-narrative`
- Skills: `grant-opportunity-screen`, `grant-compliance-check`, `revenue-forecast-scenario`

## Sequence
1. **Grants Director agent + grant-opportunity-screen** — when a new program notice or NOFA lands, run the opportunity screen first. Attach the program guidance, NOFA, or CFDA summary. The screen determines eligibility, match requirements, competitive factors, and staff capacity implications before any writing begins.
2. **Finance Director agent + revenue-forecast-scenario** — for grants with a local match requirement, model the match financing scenarios. Attach the fund balance report and CIP funding plan so the scenario reflects actual available match capacity.
3. **Grants Director agent + grant-application-narrative** (prompt) — draft the narrative sections of the application. Attach the NOFA requirements, the opportunity screen output, any prior applications for the same or similar program, and the project's underlying data or feasibility study.
4. **Finance Director agent** — review the budget and financial exhibits for the application. Requires the grant budget template from the funder and the city's adopted budget for the relevant fiscal year.
5. **Grants Director agent + grant-compliance-check** — once a grant is awarded, use this skill to build the compliance calendar and reporting framework. Attach the grant agreement, any special conditions, and the applicable federal or state regulations (2 CFR 200 for federal awards).
6. **Grants Director agent + grant-pipeline-review** (prompt) — on a monthly basis, produce the pipeline report for City Manager and Council. Attach the current opportunity tracker and status updates from each active award.

## Watch for
- **Eligibility assumptions without full program reading**: AI can quickly pattern-match a project to a program description, but eligibility often turns on detailed program rules, threshold requirements, or state-level pass-through policies that are buried in the full guidance. Always attach and cite the complete NOFA or program guidance, not just a summary.
- **Match commitment without budget authority**: Grant applications that commit local match funds create a financial obligation. Finance Director must confirm that match funding is available and appropriated before an application is submitted. AI should flag match requirements; humans must authorize them.
- **Compliance calendar gaps**: Federal grants under 2 CFR 200 carry specific subrecipient monitoring, procurement, and reporting obligations that vary by program. The grant-compliance-check skill builds the framework, but program-specific special conditions must be reviewed by the Grants Director and, for complex awards, City Attorney.
- **Narrative overpromising**: Competitive grant narratives benefit from confident, outcome-focused language, but AI drafts can overstate project readiness, organizational capacity, or projected outcomes. Every quantitative claim in the narrative must be traceable to an attached source document before submission.
- **Infrastructure grants that finance low-value-per-acre development**: Grants that fund new roads, utilities, or site infrastructure to attract or serve development that will generate under $200,000 per acre in assessed value create permanent maintenance obligations that the resulting tax revenue may never recover. Before pursuing such a grant, calculate whether the development being served can cover its infrastructure cost over a 30-year horizon. If it cannot, the grant finances near-term construction but shifts a long-term maintenance liability onto the city's general fund — the grant is subsidizing the Growth Ponzi cycle, not breaking it. Evaluate whether the grant is financing fiscally productive development or simply deferring the cost of a structural fiscal problem.
