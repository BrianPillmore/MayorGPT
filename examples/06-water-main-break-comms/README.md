# Example 6: Water Main Break Communications

## Scenario

At 5:10 AM on a Tuesday, a 16-inch water main fails on Linden Street in the fictional City of Harlow Creek (pop. 24,000). About 1,800 service connections lose pressure. Crews are on site by 5:50 AM. The Utilities Director expects service restoration by late afternoon, and the state drinking water regulator's boil-water guidance is under discussion but not yet decided. Schools, a dialysis clinic, and a nursing home are in the affected zone.

The PIO needs a first public notice, a resident FAQ, and a short Council and Mayor update within the hour. All names, streets, and numbers are fictional.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/executive-office/public-information-officer.md` | Owns public messaging and channel discipline |
| Supporting agent | `agents/departments/utilities-director.md` | Source of confirmed operational facts |
| Prompt | `prompts/emergencies/utility-failure-response.md` | Structure for utility failure response |
| Skill | `skills/operations/utility-outage-comms/SKILL.md` | Outage notices with confirmed/unconfirmed discipline |
| Skill | `skills/public-engagement/faq-builder/SKILL.md` | Resident FAQ |
| Skill | `skills/public-engagement/crisis-message-house/SKILL.md` | Message discipline if the event escalates |

## Why this combination works

Utility outages produce a predictable stream of questions (Is my water safe? When will it be back? Where can I get water?). Separating confirmed operational facts, which come from Utilities, from public language, which comes from the PIO, prevents the common failure of announcing a restoration time or a water-safety conclusion that the regulator has not issued.

## Key cautions

- **Water-safety advisories are regulatory decisions.** Do not let an AI draft say water is "safe" or "unsafe." Use only the determination issued by the Utilities Director and the state regulator. Notification rules and timelines vary by state.
- **Vulnerable facilities need direct contact.** Dialysis, hospitals, and care facilities need phone outreach, not just a post. The AI draft can list them; staff must make the calls.
- **Language access and accessibility.** Plan translated notices and accessible formats at the start. See `evals/constituent-communications-accessibility-rubric.md`.
- **Restoration estimates are estimates.** Label them, and commit to the next update time rather than a fix time.
- **Preserve the record.** Notices, drafts, and channel posts may be public records; see `docs/ai-procurement-and-records-retention.md`.

## How to set it up

1. Obtain a confirmed fact sheet from the Utilities Director (Gate 2 equivalent for emergency speed).
2. Run the outage notice skill, then the FAQ skill, from the same fact sheet.
3. Have the Utilities Director verify every factual claim before posting; PIO signs off tone and channels.
4. Compare to `output.md`.
