# Example 5: Council Member Accused of Open Meetings Law Violation

## Scenario

The City of Denton Bluffs (pop. 19,000) has received a formal complaint alleging that Council Member Raymond Vasquez violated the state Open Meetings Act. The complaint, submitted by a local resident and government transparency advocate, alleges that: (1) Vasquez individually contacted four of the six other council members by email and phone over a three-day period to discuss a pending vote on a controversial contract award; and (2) that these serial communications constituted a "walking quorum" in violation of the Act. The city clerk received the complaint on March 20, 2026. The council meets again on April 7.

The City Attorney needs to assess the legal exposure, advise the council, and determine what steps the clerk and council must take. The City Clerk needs to understand the procedural requirements on her end.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/statutory-roles/city-attorney.md` | Legal risk analysis; walking quorum doctrine; advice to council |
| Supporting agent | `agents/statutory-roles/city-clerk.md` | Procedural obligations: notice, records, complaint documentation |
| Prompt | (none required — the agents drive the output from the scenario description) | |
| Skill | `skills/governance/open-meeting-risk-check/SKILL.md` | Structured walkthrough of meeting law risk, notice requirements, and authority/process issues |

**Optional additions:**
- `skills/legal-risk/ethics-conflict-check/` if the underlying contract matter also raises ethics concerns
- `skills/governance/legislative-history-brief/` to reconstruct the communication timeline as a formal record

## Why this combination works

The city-attorney agent is built for exactly this type of situation: spotting legal issues early, framing risk clearly, and advising the governing body without pretending every question has a single answer. The `open-meeting-risk-check` skill structures the analysis around the four elements that typically determine meeting law liability: quorum, deliberation, public business, and notice. The city-clerk agent adds the procedural layer — what records must be preserved, what notice obligations are triggered, and what the clerk's independent duties are in this situation.

The two-agent approach matters: the attorney's role is legal analysis and advice; the clerk's role is records and process. They are separate responsibilities with different audiences.

## Key cautions

- **This is a sensitive personnel/legal matter.** Do not input individually identifying communications content (specific email text, named private parties) into an AI system without understanding your city's AI use policy and your state's open records implications. Frame the scenario at the level of known facts and alleged conduct.
- **The city attorney must advise in writing.** AI output is a starting framework for the attorney's legal analysis — it is not a legal opinion. The attorney must review the state statute, any applicable attorney general opinions, and relevant case law before advising the council.
- **Attorney-client privilege.** The city attorney's written advice to the council on this matter may be privileged. Do not share AI-assisted draft legal analysis beyond the attorney-client group.
- **The accused council member has rights.** An AI analysis of the legal exposure should not be shared with the full public before the council has had an opportunity to review it with counsel. The council member is entitled to due process in any formal complaint process.
- **The underlying contract decision may be tainted.** If the walking quorum is confirmed, the contract award may need to be rescinded and re-voted with proper process. This has real operational consequences that go beyond the meeting law question.

## How to set it up

1. Activate the `city-attorney` agent.
2. Activate the `open-meeting-risk-check` skill.
3. Provide the scenario description (avoid including full text of private communications in the AI prompt — summarize the alleged conduct).
4. Request: (a) a legal risk memo for the City Attorney to review and refine, and (b) a procedural checklist for the City Clerk.
5. Run the `city-clerk` agent separately on the clerk's checklist to ensure the procedural obligations are complete.
6. Review `output.md` to calibrate what good looks like for this type of legal risk analysis.
