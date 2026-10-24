---
name: demographic-brief-builder
description: Build a clear demographic or service-area brief from census or local data without overstating weak signals.
argument-hint: [area-or-topic]
---

## Purpose
Produce an accurate demographic profile for a decision (service planning, grant eligibility, equity analysis, facility siting) that states uncertainty honestly. Small-area estimates are noisy, and a misread margin of error can misdirect resources.

## Required inputs
- Geography (city, tract, block group, service area polygon) and the decision the brief supports.
- Data sources and vintages: decennial census, American Community Survey (ACS) 1-year or 5-year estimates, local administrative data (utility accounts, school enrollment, permits), and population estimates.
- Specific indicators requested (age, income, poverty, housing cost burden, language, disability, vehicle access).
- Any program eligibility thresholds (for example low- and moderate-income area tests for federal block grants).

## Workflow
1. Match source to geography and purpose. ACS 5-year estimates are the usual choice for small areas; 1-year estimates apply only to larger places. Decennial counts are exact for counted topics but ageing. State vintage on every table.
2. Report margins of error (MOE) for ACS estimates. For small areas, compute whether differences exceed combined MOE before calling something a difference or trend. Do not compare overlapping 5-year periods as independent.
3. Build the service-area estimate: when your boundary does not match census geography, use block-level allocation or area/population weighting and state the method and error.
4. Select indicators related to the decision. Present counts and rates, and the denominator.
5. Compare to city, county, and state benchmarks, and to prior periods where comparable. Avoid inferring causes.
6. Cross-check with local administrative data (school enrollment, utility connections, building permits) when census data lag or fail for fast-changing areas.
7. Treatment of sensitive groups: avoid identifying small cells (privacy), use plain-language labels, and respect disclosure rules; avoid deficit framing.
8. Write findings with confidence: strong signal, weak signal, no reliable conclusion.

## Output structure
| Indicator | Area estimate | MOE | City | County/State | Source & vintage | Reliability |
Add: three to five key findings, a limitations box, method notes for boundary mismatch, and recommended local data to confirm.

## Red flags / escalate
- Small-area estimates with MOE larger than the estimate.
- Eligibility determinations (grants) resting on survey estimates: confirm program-approved data and methods.
- Redistricting or legal uses: demographer and city attorney.
- Re-identification risk from small counts.
- Equity claims drawn from a single noisy indicator.

## Common mistakes
- Ignoring MOE.
- Comparing ACS 5-year with 1-year without caution.
- Using outdated data as current.
- Presenting percentages without counts.
- Overinterpreting changes between overlapping periods.

## State-law variance
Program eligibility datasets and state demographer estimates differ by state; check program rules.
