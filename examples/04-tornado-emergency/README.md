# Example 4: Post-Tornado Emergency (First 48 Hours)

## Scenario

At 6:47 PM on April 14, 2026, an EF-2 tornado touched down in the City of Millvale (pop. 31,000), crossing the northeast residential quadrant for approximately 2.3 miles before lifting. Preliminary reports within the first hour indicate significant structural damage to two residential neighborhoods, downed power lines across seven streets, one school building with roof damage, and at least three confirmed injuries. The City's Emergency Operations Center (EOC) is activated. It is now 9:30 PM, approximately 2 hours 43 minutes after impact.

The Emergency Manager needs an initial incident brief for the City Manager and Mayor, and the Public Information Officer needs a first public statement.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/departments/emergency-manager.md` | Owns the EOC; converts field reports into decision-ready briefs; differentiates confirmed from evolving |
| Supporting agent | `agents/executive-office/public-information-officer.md` | Handles the public statement; coordinates messaging with the EM |
| Prompt | `prompts/emergencies/incident-brief.md` | Structures the operational brief format |
| Prompt | `prompts/emergencies/crisis-comms.md` | Structures the public communication deliverable |
| Skill | `skills/operations/emergency-incident-brief/SKILL.md` | Step-by-step brief: facts, impacts, actions underway, resource asks, message guidance |
| Skill | `skills/public-engagement/crisis-message-house/SKILL.md` | Message discipline: holding statement, key messages, tough Q&A |

**Optional additions:**
- `prompts/emergencies/emergency-proclamation.md` if a local emergency declaration is being drafted
- `skills/operations/storm-recovery-action-plan/` for the 72-hour recovery planning horizon
- `agents/departments/public-works-director.md` for debris clearance and infrastructure status

## Why this combination works

The emergency-manager agent is built for time pressure: plain language, confirmed vs. evolving distinction, practical action lists, resource gap flags. The `emergency-incident-brief` skill structures the operational output so the City Manager and Mayor receive a decision-ready brief, not a raw field report dump. The `crisis-message-house` skill provides the messaging discipline the PIO needs to brief media and the public without speculating on damage levels or injury counts that are still being confirmed.

The two-agent approach (EM for operations, PIO for public) is essential. One voice sets the facts; the other sets the tone. They should not be collapsed into a single output.

## Key cautions

- **Never release injury counts until confirmed by the medical examiner or hospital.** Early field reports of injuries routinely undercount. A public statement that says "three injuries" when the actual count is higher will be corrected publicly and damage trust at the worst possible time.
- **The "confirmed vs. unconfirmed" distinction is not optional.** The Emergency Manager's brief must label every fact as confirmed, reported, or unconfirmed. The AI will do this if instructed — verify that every data point in the brief carries a status label.
- **Declarations have legal consequences.** A local emergency proclamation triggers specific legal authorities and obligations under state law. Use `prompts/emergencies/emergency-proclamation.md` as a starting point, but the city attorney must review the declaration before the mayor signs it.
- **FEMA documentation starts now.** If there is any possibility of federal disaster assistance, document all costs, decisions, and actions from the moment of EOC activation. The `emergency-incident-brief` output should be preserved as an official incident record.

## How to set it up

1. Activate the `emergency-manager` agent as the primary role.
2. Activate the `emergency-incident-brief` skill.
3. Attach all available field reports, dispatch logs, and department status updates — even if incomplete.
4. Request the incident brief first, then switch to the `public-information-officer` agent and `crisis-message-house` skill for the public statement.
5. Review `output.md` to calibrate what good looks like under time pressure.
