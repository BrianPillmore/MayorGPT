# New Administration Transition Stack

## Best for
Moving from election results to a functioning new Mayor, Council, or City Manager: briefings, onboarding, early-days priorities, and the line between campaign promises and governance.

## When to activate
Pull this stack after certification of an election, when a new Mayor or Council members are sworn in, or when a new City Manager is hired. Also useful for a mid-term vacancy appointment.

## Combine
- Agent: `agents/executive-office/city-manager.md`
- Agent: `agents/executive-office/chief-of-staff-executive-office.md`
- Agent: `agents/statutory-roles/city-clerk.md`
- Agent: `agents/statutory-roles/city-attorney.md`
- Agent: `agents/elected-officials/mayor.md`
- Agent: `agents/elected-officials/councilmember.md`
- Prompt: `prompts/elections-and-transition/candidate-briefing.md`
- Prompt: `prompts/elections-and-transition/transition-memo.md`
- Prompt: `prompts/elections-and-transition/new-council-onboarding.md`
- Prompt: `prompts/elections-and-transition/campaign-to-governance-boundary.md`
- Prompt: `prompts/annual/goal-setting-retreat.md`
- Skills: `election-calendar-planner`, `board-training-builder`, `open-meeting-risk-check`, `ethics-conflict-check`, `charter-code-crosscheck`, `board-appointment-check`

## Sequence
1. **Clerk agent + election-calendar-planner** — build the post-election calendar: certification, oath dates, first meeting, filings. Attach the state election calendar and city charter provisions. Calendar items are statutory; confirm each with the Clerk.
2. **City Manager agent + transition-memo** — prepare the transition memo: pending decisions, open litigation (summary only), contracts expiring, budget status, and deadlines in the first 90 days. Attach department status reports.
3. **City Attorney agent + open-meeting-risk-check + ethics-conflict-check** — brief new members on open meetings, public records, conflict-of-interest, and gift/disclosure rules. Rules differ by state; the City Attorney supplies local content.
4. **Chief of Staff agent + new-council-onboarding** — assemble the onboarding binder and schedule: department tours, governance structure, how agenda items flow. Use `board-training-builder` for commission and board training.
5. **Mayor / Councilmember agents + campaign-to-governance-boundary** — convert campaign commitments into a list classified as: within city authority, requires Council action, requires another government, or outside city power.
6. **City Manager agent + goal-setting-retreat** — structure the goal-setting retreat so priorities are set in a properly noticed public meeting, then feed adopted goals to the budget process.
7. **Clerk agent + board-appointment-check** — review upcoming board and commission appointments and vacancies.

## Watch for
- **Serial communications during onboarding**: Briefings given one-on-one to multiple Council members can create open meetings risk in some states. Have the City Attorney set ground rules before briefings start.
- **Confidential material**: Transition memos must not include privileged litigation strategy or personnel details beyond what the recipient is entitled to receive. Check with the City Attorney.
- **Campaign material as city record**: Campaign communications and city communications are different legal categories; do not use city resources, including AI accounts, for campaign work.
- **Overpromising early wins**: Do not let AI-drafted 100-day plans commit the city to items outside its legal or fiscal authority.
- **Institutional memory**: Document the rationale behind past decisions in the memo, not just the outcomes.
