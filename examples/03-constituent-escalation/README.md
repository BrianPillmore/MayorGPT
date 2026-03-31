# Example 3: Constituent Letter Escalated to Mayor's Office

## Scenario

A resident of the City of Weston Falls (pop. 48,000) sent a detailed complaint letter to City Hall on February 28, 2026, about a water main break on her street that went unrepaired for 11 days. The letter was initially received by the Utilities Department, which sent a form acknowledgment. The resident then posted on the NextDoor neighborhood platform, tagging the mayor and three council members by name. Her post received 84 reactions and 31 comments, some from residents with similar complaints. The mayor's chief of staff flagged it as requiring a personal mayoral response.

The mayor needs a response letter that acknowledges the failure, explains what happened, and rebuilds trust — without overpromising future service levels or exposing the city to liability.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Agent | `agents/elected-officials/mayor.md` | Sets the voice — thoughtful, visible, constituent-facing; avoids operational directives |
| Prompt | `prompts/public-engagement/community-faq.md` or `prompts/public-engagement/town-hall-briefing.md` | Structures the engagement tone and format |
| Skill | `skills/public-engagement/constituent-response/SKILL.md` | Drives the response discipline: acknowledge, explain, commit to process (not outcome), internal routing |

**Optional additions:**
- `skills/operations/utility-outage-comms/` for language on the operational side
- `agents/executive-office/public-information-officer.md` for a coordinated public statement if the NextDoor post continues to grow

## Why this combination works

The mayor agent sets the right voice: visible and empathetic without directing staff operationally or making promises requiring council or budget action. The `constituent-response` skill enforces the critical discipline of separating the public-facing letter from internal routing notes — the resident gets acknowledgment and a clear next step; staff gets a clear internal action list. Together they prevent the two most common failure modes: form-letter tone that further inflames the resident, and over-promising that creates liability.

## Key cautions

- **Do not describe internal operational failures in the public letter.** Specific language about why the repair took 11 days (crew shortage, dispatch error, parts supply issue) belongs in an internal root-cause review, not in a mayoral letter that could be quoted or screen-captured.
- **Do not promise a specific repair timeline or service standard improvement.** Those commitments require manager and council involvement. The letter can commit to follow-up, not to outcomes.
- **The social media escalation changes the calculation.** The resident's NextDoor post means this response may be screenshotted and shared. Review the letter with that in mind before sending.
- **Check for open records implications.** The resident's complaint letter and the city's response are likely public records. Do not include in the response anything you would not want disclosed.

## How to set it up

1. Activate the `mayor` agent.
2. Activate the `constituent-response` skill.
3. Attach the resident's original letter, the Utilities Department form acknowledgment, and a brief factual summary of the repair timeline from Public Works.
4. Request both a public-facing letter draft and a separate set of internal routing notes.
5. Review `output.md` to calibrate tone, framing, and what the internal notes should look like.
