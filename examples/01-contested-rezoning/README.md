# Example 1: Contested Rezoning with Neighborhood Opposition

## Scenario

The City of Halcyon Ridge (pop. 38,000) is processing a rezoning application for a 14-acre parcel at 4401 Meridian Bluff Road. The applicant, Cortland Development Group, is requesting a change from R-1 (Single-Family Residential, 4 du/ac) to RM-2 (Medium-Density Residential, 18 du/ac) to build 210 apartment units. A neighborhood association has organized opposition and submitted a formal petition with 147 signatures.

The Planning Commission holds its public hearing in 18 days. The Planning Director needs a decision-ready staff report.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Agent | `agents/departments/planning-and-development-director.md` | Owns the staff report; sets voice, criteria discipline, and recommendation posture |
| Prompt | `prompts/monthly/staff-report.md` | Structures the deliverable format: summary, background, analysis, options, recommendation, action language |
| Skill | `skills/planning-and-growth/zoning-case-analysis/SKILL.md` | Drives the step-by-step criteria review, comp plan crosswalk, infrastructure check, and notice flags |
| Context | City's comp plan chapter, zoning code Article 4, public works utility capacity memo, the applicant's project narrative |

**Optional additions:**
- `skills/planning-and-growth/comp-plan-crosswalk/` to formalize the consistency analysis
- `skills/planning-and-growth/land-use-findings-builder/` once a recommendation is reached, to draft adoptable findings language

## Why this combination works

The planning-and-development-director agent keeps the output procedurally grounded: it will distinguish staff recommendation from council decision, surface infrastructure and precedent concerns, and avoid substituting subjective preference for adopted code criteria. The `zoning-case-analysis` skill drives the structured walkthrough — application review, criteria match, infrastructure check, public input synthesis — so nothing gets skipped under deadline pressure. The `staff-report` prompt formats the deliverable so it is ready to attach to an agenda packet.

## Key cautions

- **Spot zoning risk.** A single parcel upzone surrounded by R-1 is a textbook spot zoning fact pattern. The analysis must show the decision has a rational basis tied to adopted criteria, not just the applicant's preference.
- **Notice accuracy.** Mailed notice to property owners within the required radius must be verified before the hearing. An AI draft cannot confirm the notice list was pulled correctly — flag this for the city clerk.
- **Infrastructure capacity.** The output will flag water/sewer/traffic impacts, but capacity letters from Public Works and the utility must be attached as exhibits. The AI cannot supply those.
- **Findings language is not final.** Any conditions of approval or denial findings must be reviewed by the city attorney before adoption.

## How to set it up

1. Paste the `planning-and-development-director` portable system prompt into the Claude system field.
2. Activate the `zoning-case-analysis` skill (paste SKILL.md content or reference the skill directory).
3. Attach the source materials listed in `input.md`.
4. Use the `staff-report` prompt template as the user turn, filling in the bracketed fields.
5. Review `output.md` to calibrate what a thorough, well-annotated draft looks like.
