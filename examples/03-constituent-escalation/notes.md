# Notes: Constituent Escalation Example

## What made this output strong

1. **Two-part structure: public letter + internal notes.** This is the core value of the `constituent-response` skill. The public letter is constrained; the internal notes are candid. Every mayor's office should expect this two-part output. If the AI only produces the letter, ask explicitly: "Now give me internal notes on what should not be in the letter and why, plus an action list."

2. **The letter acknowledges without admitting.** "I take responsibility for the city's failure to communicate" is the right formulation. It is human and accountable without creating a specific legal admission. The AI correctly avoided "we failed to provide a safe road" or "the city was negligent" — those phrasings open tort exposure. The city attorney still needs to review the letter before it goes out.

3. **The follow-up commitment is specific but bounded.** "You will hear from the City Manager's office within ten business days" commits to a real action. It does not promise to rebuild the water system, hire crew, or change service levels. This is the distinction between "commit to process" and "commit to outcome" that the skill is designed to enforce.

4. **The Presidents' Day explanation was correctly excluded.** The internal notes explain why. This kind of editorial judgment — knowing what NOT to include — is where AI assistance genuinely saves a mayor's office from self-inflicted damage.

5. **The NextDoor sequencing was handled.** The internal notes correctly sequence the response: personal letter first, brief public acknowledgment second. Getting this backwards is a common mistake.

## Common mistakes to avoid

- **Do not skip the city attorney review.** Constituent response letters about service failures are in the zone of potential tort litigation. The attorney needs to see the letter before it is sent, especially when there is a social media escalation.
- **Do not use this output as-is without briefing the City Manager.** The output commits the City Manager to a 10-business-day follow-up. The City Manager needs to agree to that before the mayor sends the letter. This is a coordination step the AI cannot complete.
- **Do not include internal notes in the letter.** This sounds obvious, but in a real workflow under time pressure, people sometimes combine the two sections. Keep them strictly separate. Part B is never for the resident.

## Variations

### When the issue is more serious (injury, property damage, active litigation)
If the service failure involved a safety incident (someone tripped in the unmarked hole, a car was damaged), route this through the city attorney first, not through this workflow. The `constituent-response` skill is designed for service-level complaints, not active tort matters. The output should be reviewed by legal before any communication is sent.

### When the complaint comes in via email or social media (not a formal letter)
Use the same combination. Adjust the format to match the channel — email response rather than formal letter, shorter and slightly less formal in tone. The internal notes discipline is the same.

### When the mayor wants to respond on social media directly
The mayor agent and `crisis-message-house` skill together can produce a short, vetted social media statement. Keep it brief: one or two sentences acknowledging the complaint and directing to the personal letter or the city's service contact. Never litigate a constituent complaint in a public comment thread.

### For volume constituent response (10+ similar complaints)
If multiple residents report the same issue (as the NextDoor thread suggests), escalate to:
- `skills/public-engagement/faq-builder/` to draft a community FAQ
- `prompts/public-engagement/community-faq.md` to structure the public response
- `agents/executive-office/public-information-officer.md` as the voice for a coordinated public statement
