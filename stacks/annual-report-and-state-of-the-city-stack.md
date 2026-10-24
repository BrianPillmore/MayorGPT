# Annual Report and State of the City Stack

## Best for
Producing the annual report, the State of the City address, and the supporting public materials from verified performance and financial data.

## When to activate
Pull this stack when the annual report cycle opens, when the Mayor or City Manager is preparing a State of the City address, or when Council wants a year-in-review document tied to adopted goals. Start at least six to eight weeks before the delivery date so data can be verified.

## Combine
- Agent: `agents/executive-office/chief-of-staff-executive-office.md`
- Agent: `agents/elected-officials/mayor.md`
- Agent: `agents/executive-office/public-information-officer.md`
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Prompt: `prompts/annual/state-of-the-city.md`
- Prompt: `prompts/monthly/performance-memo.md`
- Skills: `kpi-dashboard-narrative`, `demographic-brief-builder`, `speechwriter`, `press-release-writer`, `social-post-series`, `faq-builder`

## Sequence
1. **Chief of Staff agent (orchestrator)** — define the audience, format, and calendar. Issue a data request to every department: adopted goals, year-end KPIs, completed projects, and known misses. Record the request using the handoff format in `ORCHESTRATION_PROTOCOL.md` (Gate 1).
2. **Finance Director agent** — produce a verified fiscal summary from the audited or year-end financial figures. State whether numbers are audited, unaudited, or projected. Attach the annual financial report or year-end close package.
3. **Chief of Staff agent + kpi-dashboard-narrative** — convert department KPIs into a plain-language performance narrative. Attach the KPI data and the prior year's report so trends are real. Include misses and flat results, not only wins.
4. **Chief of Staff agent + demographic-brief-builder** — add a short community-context section (population, housing, jobs) with a cited source and vintage for every figure.
5. **Mayor agent + speechwriter** (using the `state-of-the-city` prompt) — draft the address from the preserved specialist outputs above. Attach the mayor's stated priorities and any commitments already made publicly.
6. **PIO agent + press-release-writer / social-post-series / faq-builder** — derive the release, social series, and FAQ only from the approved report and speech text, never from earlier drafts.
7. **Fact-check pass (human)** — every number, project status, and promise in the speech and report is checked against a source document. Complete the accountability trace and Gates 3 and 4.

## Watch for
- **Unverified numbers in a high-visibility speech**: Speeches are quoted for years. Every statistic needs a source document and a date. Do not let the model "round up" or generalize a result.
- **Cherry-picked narrative**: A year-in-review that omits missed targets erodes credibility. Require a "what did not go as planned" section in the report even if the speech is more selective.
- **Campaign and governance boundary**: If the address falls near an election, have the City Attorney review it for electioneering concerns under your state's law (rules vary significantly by state).
- **Promises made by the model**: AI drafts may invent commitments ("we will complete X by next year"). Strip any commitment not already adopted by Council or approved by the Mayor.
- **Credit and attribution**: Do not name residents, employees, or businesses without confirming consent and accurate details.
- **Accessibility and language access**: Publish the report in an accessible format with alt text and plain-language summary; consider translation needs (see `evals/constituent-communications-accessibility-rubric.md`).
