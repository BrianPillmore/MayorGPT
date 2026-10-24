---
name: cip-prioritizer
description: Rank capital projects using risk, condition, service impact, regulatory pressure, funding fit, and delivery realism.
argument-hint: [cip-list]
---

## Purpose
Turn a raw capital improvement plan (CIP) request list into a ranked, funded-or-unfunded program that a council can adopt. Ranking must separate what is urgent (risk and mandates), what is strategic, and what is merely requested, and must show the operating and maintenance tail of every project.

## Required inputs
- Project list with scope, cost estimate (and estimate class/date), department sponsor, and asset affected.
- Condition data (pavement PCI, pipe condition or break history, facility condition index, vehicle age/mileage) where it exists.
- Regulatory drivers (consent orders, permit limits, ADA transition plan, lead service line inventory, dam/bridge inspection findings).
- Funding sources by project: enterprise fund, restricted revenue, grant (with match and deadline), debt capacity, general fund pay-go.
- Existing scoring policy, if the city has one. Use it as the base and note deviations.

## Workflow
1. Classify each project: rehabilitation of existing asset, replacement of end-of-life asset, regulatory/safety mandate, or new capacity/new asset.
2. Score with a transparent rubric (typical weights, adjust to policy): risk of failure and consequence 25, regulatory/safety 20, condition 15, service/level-of-service impact 15, funding fit 10, delivery readiness 10, strategic/plan alignment 5. Show raw scores so council can change weights.
3. Maintenance-first adjustment: deferred maintenance on existing assets scores above equivalent-cost new construction, because deferral typically converts a repair into a replacement. For every new asset, state the annual operating and maintenance cost it adds in perpetuity and who funds it.
4. Test delivery realism: design status, right-of-way, permits, utility conflicts, bid climate, and staff capacity. Identify the number of projects the engineering staff can actually deliver per year.
5. Match funding to project: restricted money only for eligible uses, enterprise funds for enterprise assets, and grants only if match and timing are secured. Flag projects funded by "TBD."
6. Check the program as a whole: share of budget to rehabilitation vs. new, concentration in one geography (equity check), and the debt service burden on future operating budgets.
7. Produce tiers: Tier 1 fund now, Tier 2 fund if resources appear, Tier 3 defer, and Defer-with-risk (what happens if we wait).

## Output structure
| Rank | Project | Type | Cost | Score (by criterion) | Funding source/status | O&M tail ($/yr) | Delivery risk | Tier |

Add: program mix summary (rehab/replace/new share), five-year funding gap, risks of deferral, and decision points for council.

## Red flags / escalate
- Cost estimates older than one to two years or without contingency.
- Mandated projects with no identified funding.
- Grant-dependent projects without an awarded agreement.
- CIP favoring new assets while condition data shows rising backlog.
- Debt service from the plan pushing past the city's debt policy limits (see debt-financing-brief).
- Projects that bypass the CIP process through budget amendment.

## Common mistakes
- Ranking by who asked loudest rather than by consequence of failure.
- Ignoring the O&M tail.
- Treating all estimates as equal precision.
- Scoring a project "ready" when the right-of-way is unresolved.
- Using restricted money for ineligible work.

## State-law variance
CIP adoption requirements, bonding authority, and competitive bidding thresholds vary by state.
