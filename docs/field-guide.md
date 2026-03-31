# Field Guide: Quick Reference

When you are in a situation and need to know what to reach for, use this table. Each row covers a common municipal task, the right combination to start with, and the one caution most likely to matter.

## Situation → Agent → Prompt → Skill → Key Caution

| Situation | Agent | Prompt | Skill | Key Caution |
|---|---|---|---|---|
| Rezoning staff report needed before a public hearing | `planning-and-development-director` | `prompts/monthly/staff-report.md` | `zoning-case-analysis` | Run every adoption criterion explicitly. Do not guess at infrastructure capacity — flag it as unconfirmed if studies are pending. |
| Mid-year budget shortfall discovered | `finance-director-budget-officer` | `prompts/monthly/financial-review.md` | `budget-variance-analysis` | Separate timing variances from structural ones before presenting to council. Check charter thresholds for amendments requiring council action. |
| Constituent complaint escalated to mayor's office | `mayor` | `prompts/public-engagement/community-faq.md` | `constituent-response` | Produce two outputs: a public letter and separate internal notes. Do not make outcome promises; commit to process and follow-up timeline only. City attorney should review if a service failure is involved. |
| Tornado or disaster — first 48 hours | `emergency-manager` | `prompts/emergencies/incident-brief.md` | `emergency-incident-brief` | Label every fact as confirmed, reported, or unconfirmed. Never release injury counts until hospital-confirmed. Separate the operational brief from the public message house. |
| Public statement needed during a crisis | `public-information-officer` | `prompts/emergencies/crisis-comms.md` | `crisis-message-house` | Draft holding statement, key messages, and tough Q&A separately. Align PIO and elected officials on the message house before any media contact. |
| Open meetings law complaint or close call | `city-attorney` + `city-clerk` | (scenario description is sufficient) | `open-meeting-risk-check` | Never use AI output as the legal opinion. Attorney must research state-specific case law and AG opinions. Treat draft as attorney-client privileged from the moment of creation. |
| Council vote on a contract or ordinance approaching | `city-attorney` | `prompts/legislation-and-procurement/contract-approval-memo.md` | `contract-issue-spotter` | Flag procurement thresholds, competitive bidding requirements, and council authority limits. AI does not replace contract legal review. |
| Emergency declaration needed | `emergency-manager` + `city-attorney` | `prompts/emergencies/emergency-proclamation.md` | `emergency-incident-brief` | Proclamation language must be reviewed by city attorney before signing — it triggers state law authorities and obligations. |
| Ordinance or resolution needs drafting | `city-attorney` | `prompts/legislation-and-procurement/ordinance-draft.md` | `ordinance-drafter` | AI drafts require attorney review for enforceability, state law preemption, and vague standards. Do not place on agenda without legal sign-off. |
| Budget season — council work session prep | `finance-director-budget-officer` + `city-manager` | `prompts/annual/` | `cip-prioritizer` or `revenue-forecast-scenario` | Show assumptions. Separate one-time and recurring money. Confirm council action thresholds before the session. |
| After a council meeting — minutes and action items | `city-clerk` | `prompts/monthly/agenda-cycle.md` | `meeting-minutes-drafter` | Clerk owns the official record. AI draft must be reviewed against the recording before adoption. Motion language must be verbatim — do not paraphrase. |
| Employee discipline or HR investigation | `human-resources-risk-director` + `city-attorney` | `prompts/people-and-hr/` | `investigation-intake` or `disciplinary-memo-builder` | Do not include personally identifying employee information in AI prompts without an approved AI use policy. All HR outputs are sensitive and potentially subject to litigation holds. |
| Public hearing notice needs to go out | `city-clerk` | `prompts/monthly/agenda-cycle.md` | `public-hearing-prep` | Verify notice deadlines against state statute and local code. AI can draft the notice; the clerk must confirm the publication and mailing list are correct. |
| Staff report for a grant application or compliance item | `grants-and-intergovernmental-affairs-director` | `prompts/monthly/grant-pipeline-review.md` | `grant-compliance-check` | AI cannot certify compliance with federal grant requirements. Certifications must be signed by an authorized official who has reviewed the actual requirements. |
| Media inquiry or press release needed | `public-information-officer` | (scenario description) | `press-release-writer` | Mayor and City Manager should approve before release. Confirm all facts against primary sources — do not release AI-generated numbers or quotes without verification. |
| Council member needs a briefing on a complex issue | `councilmember` | `prompts/monthly/staff-report.md` | `council-meeting-brief` | Keep the briefing balanced: options with tradeoffs, not a single preferred path. Council decides policy; staff advises. |
| Development agreement needs review | `planning-and-development-director` + `city-attorney` | `prompts/legislation-and-procurement/contract-approval-memo.md` | `development-agreement-review` | AI can identify missing provisions and flag risk areas, but legal sufficiency review belongs to the city attorney. Do not execute without attorney sign-off. |

## Pattern reminders

- **Agent** sets the voice, role boundary, and review posture.
- **Prompt** defines the deliverable format.
- **Skill** runs the step-by-step execution discipline.
- **Context pack** supplies the local facts the AI cannot know.
- **Attach source material.** AI performs substantially better — and flags uncertainty more accurately — when it has the actual charter, code, staff report, or budget page rather than a summary.
- **Ask for a risk/missing-information list.** Every output should end with what is unconfirmed, what still needs review, and what decisions are actually required.
