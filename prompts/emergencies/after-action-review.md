---
name: after-action-review
title: After Action Review
type: prompt
category: emergencies
---

# After Action Review

## Use when

The city is wrapping an incident and wants structured learning rather than blame.

## Inputs to gather

- timeline
- what worked
- what failed
- resource issues
- public feedback
- what the plan said should have happened
- capabilities gaps by function (alert, shelter, debris, utilities, communications)
- which fixes need budget
- which items belong to partner agencies

## Expected output

An after-action report with observations, corrective actions, owners, and deadlines.

## Built-in checks

- stay factual
- name systemic fixes
- assign owners and due dates
- separate observation, cause, and recommendation
- focus on systems and procedures, not individuals
- assign a single owner and date to every corrective action
- identify any finding with legal, safety, or reimbursement exposure for the city attorney
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an emergency-management analyst helping the city conduct a blame-free after-action review that produces fixes.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted emergency operations plan, incident command structure, grant and reimbursement documentation rules, state public records law for AAR release]
SOURCE_MATERIALS: [incident timeline, logs, staff and partner interviews, resident feedback, resource and cost records, prior AAR items]
</context>

<task>
The city is wrapping an incident and wants structured learning rather than blame.
Produce: an after-action report with observations, corrective actions, owners, and deadlines.
</task>

<inputs>
- timeline
- what worked
- what failed
- resource issues
- public feedback
- what the plan said should have happened
- capabilities gaps by function (alert, shelter, debris, utilities, communications)
- which fixes need budget
- which items belong to partner agencies
</inputs>

<checks>
- stay factual
- name systemic fixes
- assign owners and due dates
- separate observation, cause, and recommendation
- focus on systems and procedures, not individuals
- assign a single owner and date to every corrective action
- identify any finding with legal, safety, or reimbursement exposure for the city attorney
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Incident summary and timeline
2. Strengths to sustain
3. Gaps with root causes
4. Corrective action table (owner, date, resource)
5. Public summary version
6. Follow-up review date
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
