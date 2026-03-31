---
name: interagency-coordination
title: Interagency Coordination
type: prompt
category: weekly
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Interagency Coordination

## Use when

The city is working on a shared project or cross-jurisdictional issue with a county, regional authority, state agency, or special district and needs to align roles, communication, and deliverables.

## Inputs to gather

- project or issue description
- partner agencies involved and their roles
- city lead and contact list
- current status and known friction points
- shared deadlines or grant milestones
- any interlocal agreement or MOU in place

## Expected output

A coordination summary with role-responsibility matrix, open issues list, proposed communication cadence, and draft talking points for the next interagency touchpoint.

## Built-in checks

- clarify which agency has lead authority on each workstream
- do not commit city resources or positions outside of approved authority
- flag any MOU or interlocal agreement gaps
- distinguish city obligations from partner obligations

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with interagency and intergovernmental coordination.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, existing interlocal agreements, grant conditions]
SOURCE_MATERIALS: [project description, partner agency list, current status notes, prior correspondence, MOU or agreement text]
</context>

<task>
The city is collaborating with one or more county, regional, or state partners on a shared project or issue.
Produce a coordination summary with a role-responsibility matrix, open issues list, proposed communication cadence, and draft talking points for the next interagency meeting.
</task>

<inputs>
- project or issue description
- partner agencies involved and their respective roles
- city lead and key contacts at each partner agency
- current status and known friction points or gaps
- shared deadlines, grant milestones, or regulatory triggers
- any interlocal agreement, MOU, or grant agreement in place
</inputs>

<checks>
- clarify which agency holds lead authority on each workstream
- do not commit city resources, positions, or policy outside approved authority
- flag any MOU or interlocal agreement gaps that could create liability
- distinguish city deliverables from partner deliverables
- note any council or board actions required before the city can formally proceed
</checks>

<required_output>
1. Brief issue framing
2. Draft work product
3. Key risks / missing information
4. Recommended next step
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- For Claude, keep long source material above the task block when possible and put the ask near the end of the prompt.
