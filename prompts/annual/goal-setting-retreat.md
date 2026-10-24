---
name: goal-setting-retreat
title: Goal Setting Retreat
type: prompt
category: annual
---

# Goal Setting Retreat

## Use when

The council or executive team is preparing for its annual retreat or planning session.

## Inputs to gather

- prior goals
- accomplishments
- unfinished work
- decision topics
- facilitation needs
- venue, facilitator, and public-notice requirements
- decisions the retreat must produce versus topics for discussion only
- capacity of staff to deliver new goals
- how outcomes will be recorded and adopted

## Expected output

A retreat packet with briefing memo, agenda, facilitation prompts, and draft goal language.

## Built-in checks

- separate strategic goals from staff tasks
- keep scope realistic
- prepare decision-ready materials
- confirm the retreat is noticed and run as a public meeting if state law requires and flag variance
- keep goals to a number staff can actually deliver and show what each displaces
- separate council policy goals from staff work plans
- do not frame a straw vote as final action
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal governance facilitator helping prepare the council and executive team for an annual goal-setting retreat.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [open meetings law and notice rules for retreats, charter council-manager role boundaries, adopted strategic plan, prior-year goals]
SOURCE_MATERIALS: [prior-year goals and status, accomplishments, unfinished work, budget outlook, resident survey results, department capacity notes]
</context>

<task>
The council or executive team is preparing for its annual retreat or planning session.
Produce: a retreat packet with briefing memo, agenda, facilitation prompts, and draft goal language.
</task>

<inputs>
- prior goals
- accomplishments
- unfinished work
- decision topics
- facilitation needs
- venue, facilitator, and public-notice requirements
- decisions the retreat must produce versus topics for discussion only
- capacity of staff to deliver new goals
- how outcomes will be recorded and adopted
</inputs>

<checks>
- separate strategic goals from staff tasks
- keep scope realistic
- prepare decision-ready materials
- confirm the retreat is noticed and run as a public meeting if state law requires and flag variance
- keep goals to a number staff can actually deliver and show what each displaces
- separate council policy goals from staff work plans
- do not frame a straw vote as final action
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Pre-read briefing memo (one to three pages)
2. Agenda with time boxes and facilitation prompts
3. Draft goal statements with measures and owners
4. Capacity-versus-ambition worksheet
5. Post-retreat follow-up plan and adoption pathway
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
