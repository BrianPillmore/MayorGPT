# Downtown Redevelopment Stack

## Best for
Evaluating and structuring a downtown redevelopment initiative: concept, fiscal productivity, incentives, infrastructure, public engagement, and development agreement.

## When to activate
Pull this stack when a downtown plan or catalytic site is being considered, when a developer requests incentives or a public partnership for a downtown project, or when Council wants a fiscally grounded downtown strategy before committing public dollars.

## Combine
- Agent: `agents/departments/economic-development-director.md`
- Agent: `agents/departments/planning-and-development-director.md`
- Agent: `agents/departments/public-works-director.md`
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Agent: `agents/external-advisors/land-use-counsel.md`
- Agent: `agents/external-advisors/bond-counsel.md`
- Agent: `agents/executive-office/public-information-officer.md`
- Prompt: `prompts/weekly/development-pipeline-review.md`
- Skills: `downtown-project-concept`, `fiscal-impact-analysis`, `economic-development-incentive-memo`, `street-design-fiscal-analysis`, `infrastructure-liability-assessment`, `economic-gardening-analysis`, `development-agreement-review`, `housing-policy-options`, `public-comment-summarizer`

## Sequence
1. **Economic Development Director agent + downtown-project-concept** — frame the concept: site, intended uses, and the problem being solved. Attach plans, parcel data, and market information.
2. **Planning Director agent + fiscal-impact-analysis** — estimate revenue and service cost per acre for the concept compared with current use. State assumptions and ranges.
3. **Public Works Director agent + street-design-fiscal-analysis + infrastructure-liability-assessment** — estimate infrastructure capital cost and long-term maintenance liability. Attach utility and street condition data.
4. **Economic Development Director agent + economic-gardening-analysis** — test whether supporting existing local businesses could deliver comparable value more cheaply.
5. **Finance Director agent + economic-development-incentive-memo** — evaluate any requested incentive: public cost, "but for" test, clawbacks, and payback period. Bond Counsel reviews any financing structure; incentive legality varies by state.
6. **Land Use Counsel agent + development-agreement-review** — review term sheet for vesting, performance obligations, remedies, and public-benefit commitments.
7. **PIO agent + public-comment-summarizer** — plan engagement and summarize input for decision-makers.
8. **Orchestrator** — compile bundle, disagreement log, and accountability trace; schedule Council briefing.

## Watch for
- **Fiscal analysis by anecdote**: Insist on per-acre or per-unit comparisons with sources. A glossy rendering is not an analysis.
- **Incentives without a "but for" test**: Document whether the project would proceed without public support.
- **Hidden long-term liabilities**: New streets, utilities, and structured parking carry replacement costs that outlive any incentive period.
- **Displacement and equity**: Consider existing small businesses and residents; AI may omit them unless asked.
- **Premature commitments**: Preliminary conversations with developers can create expectations. Route communications through the designated lead and the City Attorney.
- **Public-private legal limits**: Gift-of-public-funds, public purpose, and procurement rules differ by state; flag for the City Attorney and bond counsel.
