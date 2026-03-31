# Land Use Hearing Stack

## Best for
Rezoning and development cases, findings, public hearing prep, and development agreement review.

## When to activate
Pull this stack when a significant rezoning, variance, conditional use permit, or development agreement reaches the staff review stage, when the Planning Commission agenda is being built and staff reports are due, or when a development agreement term sheet arrives and needs structured legal and planning analysis before negotiations advance.

## Combine
- Agent: `agents/departments/planning-and-development-director.md`
- Agent: `agents/external-advisors/land-use-counsel.md`
- Agent: `agents/external-advisors/traffic-engineer.md`
- Agent: `agents/external-advisors/consulting-engineer.md`
- Prompt folder: `prompts/legislation-and-procurement/`
- Skills: `zoning-case-analysis`, `land-use-findings-builder`, `public-hearing-prep`, `development-agreement-review`, `comp-plan-crosswalk`

## Sequence
1. **Planning Director agent + zoning-case-analysis** — open each case with a structured analysis of the application against the zoning code. Attach the application, site plan, zoning map, and applicable code sections.
2. **Planning Director agent + comp-plan-crosswalk** — check consistency with the comprehensive plan. Attach the relevant comp plan goals, policies, and any adopted area or corridor plans that apply to the site.
3. **Traffic Engineer agent** — review traffic study methodology and conclusions. Attach the applicant's traffic impact analysis and the city's level-of-service standards.
4. **Land Use Counsel agent + development-agreement-review** — for cases involving a development agreement, review the term sheet or draft agreement for legal sufficiency, vested rights implications, and enforcement mechanisms.
5. **Planning Director agent + land-use-findings-builder** — draft the findings of fact and conclusions of law for staff recommendation. Requires the completed analysis from steps 1–3 and any conditions of approval being recommended.
6. **Planning Director agent + public-hearing-prep** — prepare the staff presentation, anticipated public comments, and Council/Commission talking points. Attach any written public comment already received.

## Watch for
- **Findings not tied to the record**: Land use decisions are subject to appeal. AI-generated findings must cite specific evidence in the administrative record, not generic planning principles. Every finding must have a corresponding record reference.
- **Spot zoning exposure**: AI analysis may not spontaneously identify when a rezoning is so small and project-specific that it constitutes illegal spot zoning under state law. Land Use Counsel should review any rezoning of three or fewer parcels.
- **Development agreement vesting overreach**: AI may draft development agreement provisions that vest entitlements beyond what state law allows. Always have Land Use Counsel confirm what can legally be vested and for how long.
- **Traffic study recency and methodology**: Traffic impact analyses can become stale rapidly in growing cities. Confirm that the traffic study uses current count data and the correct methodology required by your state DOT or local standards before the hearing.
