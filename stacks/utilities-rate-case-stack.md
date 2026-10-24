# Utilities Rate Case Stack

## Best for
Water, wastewater, stormwater, and solid waste rate studies and adjustments, from cost-of-service analysis through public notice and Council adoption.

## When to activate
Pull this stack when a rate study is commissioned, when a utility is not recovering its cost of service, when a bond covenant or capital plan requires revenue increases, or when a rate adjustment proposal is heading to Council. Applies primarily to city-owned utilities; investor-owned or state-regulated utilities follow commission processes.

## Combine
- Agent: `agents/departments/utilities-director.md`
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Agent: `agents/statutory-roles/city-attorney.md`
- Agent: `agents/external-advisors/municipal-advisor.md`
- Agent: `agents/external-advisors/consulting-engineer.md`
- Agent: `agents/external-advisors/bond-counsel.md`
- Agent: `agents/executive-office/public-information-officer.md`
- Prompt: `prompts/monthly/utility-rate-watch.md`
- Skills: `user-fee-policy-review`, `revenue-forecast-scenario`, `infrastructure-liability-assessment`, `debt-financing-brief`, `franchise-utility-review`, `public-hearing-prep`, `public-comment-summarizer`, `faq-builder`

## Sequence
1. **Utilities Director agent + infrastructure-liability-assessment** — document the capital need and asset condition. Attach asset inventory, condition assessments, and the capital plan.
2. **Finance Director agent + revenue-forecast-scenario** — model revenue under current rates and several adjustment scenarios, with explicit assumptions on consumption, growth, and delinquency. Attach the rate model and financial statements.
3. **Municipal Advisor agent + debt-financing-brief** — assess debt service coverage and covenant implications. Attach bond documents. Bond Counsel confirms covenant interpretation (Gate 4).
4. **Finance Director agent + user-fee-policy-review** — review cost-of-service and cost-allocation logic against the city's fee policy. Rate-setting legal requirements, including notice and protest procedures, vary widely by state; the City Attorney must supply the governing authority.
5. **City Attorney agent** — review procedural requirements: notice periods, hearing format, and any state constraints on rate-setting. Attach statute and charter excerpts.
6. **PIO agent + faq-builder** — prepare resident-facing explanation: what is changing, why, bill impact examples, and assistance programs. Check against `evals/constituent-communications-accessibility-rubric.md`.
7. **Planning/Utilities + public-hearing-prep, then public-comment-summarizer** — prepare for the hearing and summarize comments for Council with clear counts of themes, not just sentiment.
8. **Orchestrator** — assemble the output bundle, including the disagreement log (for instance, differing rate-increase phasing views) and the accountability trace.

## Watch for
- **Model black boxes**: Rate models are spreadsheet-driven. AI should explain and stress-test the model, not substitute for it. A qualified rate consultant or finance staff validates all calculations.
- **Legal constraints on rates**: Many states restrict how utility revenue may be used or transferred to the general fund and require specific notice or protest procedures. Do not assume a rule from another state applies.
- **Bill impact framing**: Show impacts for typical low, median, and high users, and for customers on assistance programs. A single average hides who is hurt.
- **Deferred maintenance**: Keeping rates flat while assets decline transfers cost to future ratepayers. Present the cost of delay alongside the cost of increase.
- **Affordability and equity**: Document affordability analysis and assistance options, but do not promise programs that Council has not adopted.
