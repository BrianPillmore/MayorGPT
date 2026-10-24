---
name: kpi-dashboard-narrative
description: Turn KPI tables into a useful narrative that explains movement, drivers, and management action needed — suitable for council packets, city manager reports, or department reviews.
argument-hint: [dashboard-name or reporting-period]
---

## Purpose
Convert a table of performance measures into a short narrative that says what moved, why, whether it matters, and what management will do. A good narrative tells the reader which two or three measures need attention and does not recite every number.

## Required inputs
- KPI table with definitions, units, source system, reporting period, prior periods, and targets.
- Context: staffing changes, policy or fee changes, weather or events, system changes, backlog, and budget status.
- Audience (council, manager, department staff, public) and format limits.
- Data quality notes: missing data, definition changes, and manual vs. automated sources.

## Workflow
1. Check measure integrity first: definitions unchanged? Same denominator? Seasonal? Source system migrated? State any break in series before interpreting.
2. Compare each measure to target, prior period, and same period last year. Use the right comparison for seasonality, and note small-number volatility (a swing from 2 to 4 is not a trend).
3. Classify movement: on track, watch, off track, or not interpretable. Separate output (activity), efficiency (cost or time per unit), outcome (result for residents), and equity measures.
4. Explain drivers with evidence: workload, vacancies, process change, external factors. Distinguish known causes from hypotheses and label hypotheses.
5. Test for gaming and unintended effects: a faster closure time can come from closing tickets without resolution; check paired measures (quality, reopen rate).
6. Link to money and risk where relevant: overtime, backlog cost, grant targets, regulatory metrics, and legal deadlines (for example permit shot clocks).
7. State management action for each off-track measure: owner, action, date, and expected effect, or explicit decision to accept the result.
8. Write the narrative: headline in one sentence, three to five key points, then a short table. Use plain language and consistent units. Include a notes section on limitations.

## Output structure
Headline sentence, then:
| Measure | Definition | Prior | Current | Target | Status | Driver | Action/owner |
Add: "What needs attention" (max three), "What is going well," data-quality notes, and next reporting date. See narrative-template.md.

## Red flags / escalate
- Regulatory or legal-deadline measures off track (permit shot clocks, response times, compliance reports, water quality).
- Safety or equity measures worsening.
- Data integrity problems or suspicious improvements.
- Targets that were never adopted by council or cannot be measured.
- Metrics tied to staff evaluation or incentives.

## Common mistakes
- Explaining every measure.
- Treating correlation as cause.
- Changing definitions without disclosure.
- Using averages that hide distribution (report medians/percentiles for response times).
- Ending without an action.

## State-law variance
Mandatory performance reporting (state or grant requirements) varies; check program terms.
