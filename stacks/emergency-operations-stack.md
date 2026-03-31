# Emergency Operations Stack

## Best for
Incident briefs, proclamations, message discipline, response coordination, and after-action learning.

## When to activate
Pull this stack the moment a declared or imminent emergency requires coordinated city response: severe weather, utility failure, hazmat incident, civil unrest, mass casualty event, or any situation where the City Manager or Mayor may need to sign a proclamation. Also activate for planned large-scale events with significant operational coordination.

## Combine
- Agent: `agents/departments/emergency-manager.md`
- Agent: `agents/departments/fire-chief.md`
- Agent: `agents/departments/police-chief.md`
- Agent: `agents/executive-office/public-information-officer.md`
- Prompt folder: `prompts/emergencies/`
- Skills: `emergency-incident-brief`, `storm-recovery-action-plan`, `crisis-message-house`, `shelter-and-recovery` (prompt), `after-action-review`

## Sequence
1. **Emergency Manager agent + emergency-incident-brief** — as soon as the incident opens, produce the first situation report. Attach whatever verified information is available from first responders; note explicitly what is unconfirmed.
2. **Fire Chief / Police Chief agents** — for life-safety aspects, activate the relevant department head agent to layer in operational details and resource status. Each agent should add to the incident brief, not produce a separate document.
3. **PIO agent + crisis-message-house** — once the operational picture is established, build the message house: one core message, supporting facts, anticipated questions, and boundaries of what will and will not be said publicly.
4. **Emergency Manager agent + storm-recovery-action-plan** — for weather or infrastructure events, use this skill to build the recovery sequencing plan. Requires the incident brief and resource inventory.
5. **Emergency Manager agent + after-action-review** — within 2 weeks of incident close, produce the after-action report. Attach the incident log, situation reports, and any documentation of decisions and resource deployments.

## Watch for
- **Unverified information in public messaging**: Emergency situations generate rumors faster than facts. The PIO agent must work only from confirmed incident brief content; never allow preliminary reports to flow directly into the crisis-message-house output.
- **Proclamation authority gaps**: Local emergency proclamations must cite specific state statutory authority. AI-drafted proclamations should always be reviewed by City Attorney before signature; the wrong citation can invalidate protective orders or funding eligibility.
- **Message drift across updates**: Each successive situation report should state what changed since the last one. Without that discipline, compounding AI-drafted updates can contradict each other, creating public confusion and media problems.
- **After-action softening**: AI tends to frame after-action findings diplomatically. Human leadership must ensure that lessons learned are specific and actionable, not aspirational platitudes, especially for operational failures that affected life safety.
