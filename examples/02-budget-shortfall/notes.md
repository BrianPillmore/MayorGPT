# Notes: Mid-Year Budget Shortfall Example

## What made this output strong

1. **Timing vs. structural separation was forced.** The $180,000 franchise fee timing item would have inflated the shortfall estimate by 13% if not separated. The `budget-variance-analysis` skill is designed to enforce this discipline. If the AI does not make this distinction in its first draft, push back explicitly: "Separate timing variances from structural variances and explain each."

2. **The scenario table was honest about uncertainty.** The dollar range ($1.4M–$1.7M) reflects genuine uncertainty about when the police investigations close. A false-precision number ($1,492,400) presented without a range would imply more certainty than exists. Range-based scenario thinking is more useful for council decision-making than a single point estimate.

3. **Charter thresholds were named specifically.** The output cited Charter Section 7.3 by name with the 5% threshold. This is only possible because the input materials included the charter language. If you do not attach relevant charter and policy provisions, the AI will produce generic language about "council approval may be required." Generic language is not useful in a deadline-driven situation.

4. **The work session section separated "inform" from "decide."** This is a service to the City Manager and the council. Work sessions that blur deliberation and action create open-meeting law exposure. The output correctly noted that the work session should produce direction to staff, not a vote on the amendment.

## Common mistakes to avoid

- **Do not attach personnel data in identifiable form.** This example describes the police overtime as investigation-related backfill in aggregate. It does not name officers or identify specific disciplinary situations. If your source material contains personnel-identifiable information, redact it before attaching to an AI prompt.
- **Do not let the AI pick a preferred option.** The options section presents four choices with honest tradeoffs. If you ask the AI to "recommend the best option," it will pick one — but the right answer depends on community values, reserve philosophy, and political context that the AI does not have. Use the AI to frame options; use the humans to choose.
- **Validate every number.** The AI echoes what the input says. If there is an arithmetic error in the input data, the AI will reproduce it. The Finance Director must verify the scenario table against the actual general ledger before this memo goes to council.

## Variations

### Monthly financial review (not a crisis)
Use the same combination but with `prompts/monthly/financial-review.md` as the prompt. The output will be a shorter narrative dashboard rather than a crisis options memo. Useful for routine council financial updates.

### Year-end projection only (no overrun)
If the situation is revenue-side only (no department overrun), the city-manager agent may be sufficient without the finance-director agent in the mix. The `budget-variance-analysis` skill still applies.

### When the shortfall is structural and a tax increase may be needed
After the work session, if council signals interest in a revenue response, use:
- `skills/finance/user-fee-policy-review/` for fee-side options
- `skills/data-and-research/policy-research-synthesizer/` to benchmark peer cities
- `agents/executive-office/city-manager.md` to frame the policy options memo for council
