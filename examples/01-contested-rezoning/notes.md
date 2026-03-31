# Notes: Contested Rezoning Example

## What made this output strong

1. **The recommendation was to continue, not guess.** When infrastructure studies are incomplete, the right answer is a continuance recommendation — not a tentative approval or a hedged denial. The AI correctly read the incomplete record and made the procedurally sound call.

2. **The criteria were run in order.** The zoning code criteria are the legal standard. Running them explicitly, labeling each as met/not met/cannot assess, and explaining why is what creates a legally defensible record. Do not let the AI summarize criteria — make it apply them one at a time.

3. **The 2021 denial was surfaced and flagged.** Prior council action on the same parcel is a critical fact that affects both the legal defensibility of an approval and the political context of the commission's deliberation. An AI that misses this is a liability.

4. **The spot zoning flag was specific.** It named the distance (1,200 feet), noted the surrounding pattern, and correctly identified that the applicant's argument may be sufficient *if* the FLUM issue is resolved — but not on its own. This is analytical precision, not reflexive opposition.

5. **Motion language was included.** Ready-to-read motion language is a real service to the presiding officer and the clerk. It should be reviewed for accuracy but provides a strong starting point.

## Common mistakes to avoid

- **Do not run this workflow without attaching the actual code criteria.** If you do not paste in the RM-2 approval criteria from the municipal code, the AI will produce a generic framework. The criteria section is only as good as the code language you supply.
- **Do not treat infrastructure status as confirmed.** The AI will echo what the input says. If the input says "pending," the output will say "pending." That is correct behavior — do not override it by summarizing "generally adequate" to get a smoother draft.
- **Do not skip the city attorney review gate.** Spot zoning is a state-law question. The AI can identify the pattern and frame the issue, but the city attorney must advise on the legal standard in your jurisdiction.

## Variations

### If council already amended the FLUM
If the Future Land Use Map was previously amended to Medium-Density Residential (unlike this scenario), the consistency analysis flips considerably. Remove the FLUM inconsistency finding and run the criteria again. The spot zoning concern may still remain depending on the surrounding pattern.

### If you want findings language instead of a staff report
After the infrastructure studies come back clean and staff is ready to recommend approval, swap in:
- Skill: `skills/planning-and-growth/land-use-findings-builder/`
- Prompt: `prompts/legislation-and-procurement/resolution-draft.md`

This will produce adoptable findings and conditions language rather than a staff report narrative.

### If the application is for a special use permit, not a rezoning
Use the same combination but change the criteria checklist to reflect your SUP standards. The `zoning-case-analysis` skill is designed to work for any permit type — the criteria source material drives the analysis.

## Time estimate
- Input preparation (gathering source materials): 20–30 minutes
- Prompt setup and first draft: 5–10 minutes
- Human review, editing, and filling in missing items: 45–90 minutes depending on staff familiarity with the case

The AI accelerates the structure, citation, and option-framing. The planning director still owns the recommendation and the policy judgment.
