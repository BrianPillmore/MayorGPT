---
name: public-safety-review
title: Public Safety Quarterly Review
type: prompt
category: quarterly
---

# Public Safety Quarterly Review

## Use when

The city needs to assess quarterly performance across police, fire, EMS, and code enforcement — identifying trends, comparing to targets, surfacing resource concerns, and briefing leadership.

## Inputs to gather

- crime statistics by category and district (UCR or NIBRS data)
- fire incident volume, response times, and loss data
- EMS call volume, response times, and outcome data
- code enforcement case counts, resolution rates, and chronic-violator status
- staffing levels vs. authorized positions for each department
- any critical incidents or use-of-force events in the quarter
- year-over-year and target comparisons

## Expected output

A quarterly public safety performance memo with department-by-department summaries, trend analysis, resource concerns, and recommended council discussion items.

## Built-in checks

- separate incident volume from outcome quality (response time, clearance rate, fire loss)
- note any staffing vacancies affecting service delivery
- do not release personally identifiable information about victims or suspects
- distinguish between statistical noise and genuine trend shifts
- flag any critical incidents requiring formal review or council briefing

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping prepare a quarterly public safety performance review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, departmental performance standards, state reporting requirements, use-of-force and critical incident policies]
SOURCE_MATERIALS: [crime statistics, fire and EMS incident reports, code enforcement data, staffing reports, prior quarter comparisons, any incident review summaries]
</context>

<task>
The city is conducting its quarterly public safety performance review for police, fire, EMS, and code enforcement.
Produce a quarterly performance memo with department-by-department summaries, trend analysis, resource concerns, and recommended council discussion items.
</task>

<inputs>
- crime statistics by category and geographic distribution (UCR/NIBRS)
- fire incident volume, response times, structure fire loss data
- EMS call volume, response times, and key outcome indicators
- code enforcement case volume, resolution rates, and chronic property lists
- authorized vs. filled staffing for each public safety department
- any critical incidents, use-of-force events, or significant liability matters in the quarter
- prior quarter and prior year comparison data
- current performance targets or benchmarks
</inputs>

<checks>
- separate incident volume from outcome quality — more calls is not the same as worse safety
- note staffing vacancies and their operational impact on each department
- protect personally identifiable information about victims, complainants, and subjects
- distinguish between statistical noise and genuine trend changes requiring management action
- flag any critical incidents that warrant formal review, council briefing, or legal action
- confirm whether any metrics trigger required state or federal reporting
</checks>

<required_output>
1. Department-by-department summaries
2. Trend analysis with noise caveats
3. Staffing and resource concerns
4. Critical incidents needing review
5. Recommended council discussion items
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
