# Council Stack

## Best for
Agenda review, item prep, motions, public hearing prep, appointments, and policy oversight.

## When to activate
Pull this stack when the draft agenda arrives, when a Council member needs background on a complex item before a meeting, when a public hearing requires written findings, when a board or commission appointment is being processed, or when Council wants to draft a resolution or policy direction.

## Combine
- Agent: `agents/elected-officials/councilmember.md`
- Agent: `agents/statutory-roles/city-clerk.md`
- Agent: `agents/statutory-roles/city-attorney.md`
- Prompt folder: `prompts/monthly/`
- Skills: `agenda-packet-builder`, `council-meeting-brief`, `motion-language-crafter`, `board-appointment-check`, `public-hearing-prep`

## Sequence
1. **City Clerk agent + agenda-packet-builder** — once the agenda is finalized, build the packet structure and identify any missing attachments, fiscal notes, or legal review flags. Attach the draft agenda and any submitted staff reports.
2. **City Attorney agent** — for any item with legal exposure (contracts, ordinances, claims, closed session), have City Attorney agent review and flag issues before the packet is published. Requires the relevant ordinance text, contract draft, or claim documents.
3. **Councilmember agent + council-meeting-brief** — produce a Council-ready briefing for complex or contentious items. Attach the full staff report, any public comments received, and relevant background studies.
4. **City Clerk agent + board-appointment-check** — when processing board or commission appointments, verify eligibility requirements, current vacancies, and term limits. Attach the relevant board ordinance and current membership roster.
5. **Councilmember agent + motion-language-crafter** — once Council is ready to act, draft precise motion language that matches the staff recommendation or captures an amendment. Attach the staff report's recommended action section.

## Watch for
- **Findings without evidence**: For quasi-judicial items like variances or conditional use permits, AI-drafted findings must be tied to specific evidence in the record. Generic findings that could apply to any project are legally vulnerable.
- **Open meetings exposure**: AI assistance does not change open meetings law. Council members using AI to pre-coordinate votes or develop positions outside a noticed meeting creates Sunshine Law risk. Keep AI use in the preparation lane, not the deliberation lane.
- **Motion imprecision**: The motion-language-crafter can produce clean prose that is ambiguous about effective dates, delegation scope, or funding sources. City Attorney agent should review any motion that authorizes expenditure, delegates authority, or amends existing policy.
- **Appointment eligibility gaps**: Board appointment eligibility criteria vary by state law and local ordinance. The board-appointment-check skill surfaces issues but is not a substitute for the City Clerk confirming residency, conflict-of-interest, and term limit compliance against the actual application.
