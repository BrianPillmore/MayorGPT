# Mayor Office Stack

## Best for
Public-facing leadership, remarks, constituent communication, priority framing, and crisis visibility.

## When to activate
Pull this stack when the Mayor needs remarks or talking points for a public event, ribbon-cutting, or community meeting; when a constituent complaint or media inquiry lands that requires a mayoral-level written response; when a crisis requires the Mayor to be the visible public face alongside city operations; or when the Mayor is framing a priority initiative for Council or community consumption.

## Combine
- Agent: `agents/elected-officials/mayor.md`
- Agent: `agents/executive-office/public-information-officer.md`
- Prompt folder: `prompts/daily/`
- Prompt folder: `prompts/public-engagement/`
- Skills: `speechwriter`, `constituent-response`, `press-release-writer`, `crisis-message-house`
- Context: local charter/code + local meeting calendar + local issue brief

## Sequence
1. **Mayor agent** — establish the framing and priority emphasis for any communication. Attach the local issue brief, any relevant Council action, and any background context that should shape the Mayor's tone.
2. **PIO agent + press-release-writer** or **speechwriter** — draft the specific deliverable (remarks, press release, letter). The Mayor agent sets direction; the PIO agent handles craft and public-communication discipline.
3. **PIO agent + crisis-message-house** — for crisis situations, build the message house before any public statement is drafted. Attach the operational situation report and any legal or policy boundaries the Mayor must stay within.
4. **Mayor agent + constituent-response** — for individual constituent escalations, draft a response that matches the Mayor's voice while flagging any service failure or policy issue that needs staff follow-up.
5. **PIO agent** — final review of all public-facing output for tone, factual accuracy, media readiness, and consistency with any prior public statements on the same issue.

## Watch for
- **Political voice flattening**: AI drafts tend toward neutral, institutional language. Mayoral communications often need a distinct voice, specific local references, and emotional resonance that reflects the Mayor's actual style. Human editing of the first draft is the norm, not the exception.
- **Constituent response creating policy commitments**: A well-meaning constituent response can inadvertently commit the city to a service level, timeline, or outcome the organization cannot deliver. City Manager or City Attorney should review any response that touches ongoing litigation, procurement, or personnel.
- **Crisis statement getting ahead of the facts**: The Mayor's public credibility depends on never having to walk back a statement. The PIO agent's discipline of separating confirmed facts from preliminary reports must be enforced even when public pressure demands a quick response.
- **Calendar and event context drift**: Remarks drafted for one event can feel generic or misfire if the local context changes between drafting and delivery. Always re-run the issue brief check immediately before the event, not just when the draft is first produced.
