---
name: disciplinary-memo
title: Disciplinary Memo
type: prompt
category: people-and-hr
---

# Disciplinary Memo

## Use when

You need a memo for corrective action or discipline.

## Inputs to gather

- facts
- policy violated
- prior coaching
- employee response if any
- proposed action
- whether the employee is represented
- protected-class, leave, or whistleblower context
- investigation status
- comparable discipline for similar conduct

## Expected output

A professional, factual memo with expectations and next steps.

## Built-in checks

- stay factual
- avoid inflammatory phrasing
- protect due process and consistency
- stay factual and cite the policy violated
- check consistency with past discipline
- if protected activity, leave, a complaint, or a protected class is involved, route to HR and labor counsel before issuing
- do not issue until HR confirms process steps; flag state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an HR advisor helping a supervisor draft a factual, consistent corrective-action or disciplinary memo.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [personnel rules, collective bargaining agreement, due-process and Weingarten-type representation rules where applicable, state employment law, progressive-discipline policy]
SOURCE_MATERIALS: [incident facts and dates, policy violated, prior coaching and discipline, employee statements, witness notes, proposed action, comparable cases]
</context>

<task>
You need a memo for corrective action or discipline.
Produce: a professional, factual memo with expectations and next steps.
</task>

<inputs>
- facts
- policy violated
- prior coaching
- employee response if any
- proposed action
- whether the employee is represented
- protected-class, leave, or whistleblower context
- investigation status
- comparable discipline for similar conduct
</inputs>

<checks>
- stay factual
- avoid inflammatory phrasing
- protect due process and consistency
- stay factual and cite the policy violated
- check consistency with past discipline
- if protected activity, leave, a complaint, or a protected class is involved, route to HR and labor counsel before issuing
- do not issue until HR confirms process steps; flag state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Draft memo with facts, policy, expectations, and consequences
2. Process checklist (notice, representation, response opportunity)
3. Consistency check against comparable cases
4. Risks for HR and counsel
5. Meeting talking points
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
