---
name: infrastructure-liability-assessment
description: Help a city understand its infrastructure liability — the deferred maintenance and replacement obligations on city-owned assets — and calculate the hidden annual deficit.
argument-hint: [asset-category or city-name]
---

## Purpose
Quantify the gap between what the city's infrastructure requires each year and what the city actually spends, by asset class. The result is a structural measure, not a budget line, and can be the basis for an asset-management policy, rate design, or CIP strategy.

## Required inputs
- Capital asset register and ACFR capital asset note (historical cost, accumulated depreciation by class).
- Asset inventories: lane-miles, pipe length by material/age, facilities square footage, vehicles, bridges, signals, stormwater assets.
- Condition data: pavement condition index, pipe inspections or break history, facility condition assessments, bridge sufficiency ratings.
- Annual maintenance and renewal spending by class, including enterprise funds and capital programs.
- Replacement unit costs (recent bids, indexes) and the city's asset management policy.

## Workflow
1. Inventory by class: roads and bridges, water, wastewater, stormwater, buildings, fleet, IT, parks, signals/lighting.
2. Replacement value: use current unit costs from recent bids, not book value. Historical cost in the ACFR understates obligation. Flag the date and basis of each unit cost.
3. Useful life by class from local experience or standards: broad planning ranges (roads roughly 20 to 50 years depending on type and treatment cycle, pipe roughly 50 to 100 years by material, facilities 40 to 50, fleet 7 to 15) must be labeled as assumptions and replaced with condition data where available.
4. Required annual investment = replacement value divided by useful life (a straight-line proxy); improve it with a condition-based lifecycle model where available.
5. Actual annual investment: operating maintenance plus capital renewal for existing assets only (exclude new capacity).
6. Annual gap = required minus actual. Sum across classes. Project 10 and 20 year accumulation under flat spending and under a funded catch-up path.
7. Deferred maintenance backlog: cost to bring assets in poor condition to acceptable condition, by class, using condition data; state coverage of the assessment.
8. Risk overlay: consequence of failure by asset (critical mains, bridges, public safety buildings). Prioritize the highest-risk gaps first.
9. Funding pathways: enterprise rates, dedicated levy, reduced new construction, divestment of low-value assets, grants, and a phased catch-up schedule.

## Output structure
| Asset class | Inventory | Replacement value | Useful life | Required $/yr | Actual $/yr | Gap $/yr | Spend as % of required | Backlog |
Add: total hidden deficit, 10 and 20 year accumulation, risk ranking, and phased funding options.

## Red flags / escalate
- Spending under roughly half of required investment in a class (many cities fall well short; verify locally).
- Critical assets with no condition data.
- Enterprise funds subsidizing the general fund at the expense of renewal.
- Regulatory exposure (consent orders, lead service lines, dam/bridge safety, ADA).
- Use of GASB 34 modified approach: confirm condition-level policy compliance with the auditor.

## Common mistakes
- Using book value as replacement cost.
- Counting expansion capital as renewal.
- Averaging across asset classes and hiding critical gaps.
- Treating the backlog as a one-time fix without closing the annual gap.

## State-law variance
Mandatory asset management plans and reporting differ by state and funding programs.
