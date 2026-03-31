# Notes: Post-Tornado Emergency Example

## What made this output strong

1. **The search-not-complete caveat was front and center.** This is the most consequential fact in the first hours of a tornado response. The AI surfaced it in the first paragraph of the brief and repeated it in the Unconfirmed/Pending section. A mayor who does not know this before speaking to media can unknowingly say something that will be publicly retracted within hours.

2. **Confirmed vs. reported distinction was enforced column by column.** The status labels in the confirmed facts table are not decorative. They tell the decision-maker exactly how confident they should be in each data point. In a real EOC, the Emergency Manager should verify these labels against the actual dispatch log before handing the brief to the mayor.

3. **The decision table separated urgent from situational.** The Mayor arriving at the EOC at hour three does not need to make 20 decisions. She needs to make 3–4 decisions tonight. The table identifies those and explains the guidance available for each. Everything else can wait.

4. **The "not prepared to characterize" injury language is specific.** This is not a generic hedge — it is the precise language that avoids the error of using "no fatalities at this time" when search operations are incomplete. Small language choices in crisis communications have outsized consequences.

5. **The school-status commitment had a built-in verification check.** The internal note said: "Do not make this commitment unless you have confirmed with the fire marshal that the inspection will actually happen by morning." The AI flagged the dependency. The human reviewer must confirm it.

## Common mistakes to avoid

- **Do not use this output without verifying every confirmed fact against the EOC log.** The AI echoes what the input says. If the input has an error (wrong injury count, wrong shelter capacity), the output will have the same error.
- **Do not release Part A (the incident brief) publicly.** The incident brief contains unconfirmed information, casualty risk statements, and resource gap assessments that are not appropriate for public release. It is an internal decision-support document.
- **Do not skip the city attorney review of the emergency proclamation.** The proclamation is not included in this example output because it requires jurisdiction-specific legal language. Use `prompts/emergencies/emergency-proclamation.md` as a starting point and require attorney review before the mayor signs.
- **Do not collapse the EM brief and the PIO message house into one document.** Operationally, these serve different purposes. The EM brief can contain information that should NOT be in the public message. Keeping them separate is a discipline that pays off when a message house draft accidentally includes an unconfirmed injury count.

## FEMA documentation note

From the moment of EOC activation, every decision, cost, and action should be documented for potential FEMA reimbursement. Key items to document from the start:
- EOC activation time and personnel
- Mutual aid requests (timing, agency, units, costs)
- Overtime authorization and personnel assignments
- Equipment deployed
- Shelter costs
- Emergency procurement actions

The `emergency-incident-brief` skill will prompt documentation awareness, but a human EOC records keeper must actually maintain the log. AI cannot document the ground truth — it can only help structure the brief from what humans report.

## Variations

### For a less severe incident (no injuries, limited damage)
Use `skills/operations/emergency-incident-brief/` with the same EM agent for any service disruption or incident requiring executive notification — not just tornado events. The skill is appropriate for major water outages, structure fires with displacement, and significant infrastructure failures.

### For the 72-hour window
Once the immediate life safety phase is resolved, switch to:
- `prompts/emergencies/tornado-recovery.md` for the recovery planning structure
- `skills/operations/storm-recovery-action-plan/` for the 72-hour action plan
- `prompts/emergencies/after-action-review.md` once operations are complete

### For the emergency proclamation
Use `prompts/emergencies/emergency-proclamation.md`. Attach your state's emergency management statute and your city charter authority provisions. Require city attorney review before the mayor signs.
