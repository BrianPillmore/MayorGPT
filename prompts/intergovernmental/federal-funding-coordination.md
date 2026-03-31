---
name: federal-funding-coordination
title: Federal Funding Coordination
type: prompt
category: intergovernmental
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Federal Funding Coordination

## Use when

The city is pursuing, managing, or reporting on a federal grant or infrastructure funding opportunity and must coordinate with a state pass-through agency, federal program office, or congressional delegation.

## Inputs to gather

- federal program name, authorizing statute, and awarding agency
- state pass-through agency if applicable
- application or award status and key dates
- city project description and budget
- match or cost-share requirements
- federal Davis-Bacon, NEPA, Buy America, or other compliance requirements
- assigned federal program officer or state contact
- any outstanding conditions of award

## Expected output

A federal funding coordination brief with status summary, compliance obligation checklist, upcoming milestone calendar, intergovernmental communication plan, and a list of open issues requiring resolution.

## Built-in checks

- confirm compliance obligations triggered by the funding (Davis-Bacon, NEPA, Section 106, Buy America, civil rights)
- do not count costs as match unless they are allowable under the specific program
- flag any grant conditions that modify how the city may use city funds on the project
- identify the city's SAM.gov registration and UEI status
- note congressional notification requirements or local hire commitments
- flag any scope or budget changes that require prior federal approval

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping coordinate a federal grant or infrastructure funding opportunity with state and federal partners.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, procurement code, council authorization requirements, state pass-through rules, grant agreement terms and conditions]
SOURCE_MATERIALS: [NOFO/NOFA or program guidance, award letter or grant agreement, budget detail, compliance checklist, state agency correspondence, SAM.gov registration status]
</context>

<task>
The city is coordinating a federal grant or infrastructure funding opportunity with a state pass-through agency or federal program office.
Produce a coordination brief with status summary, compliance obligation checklist, upcoming milestone calendar, intergovernmental communication plan, and a list of open issues requiring resolution.
</task>

<inputs>
- federal program name, authorizing legislation, and awarding agency
- state pass-through agency name and assigned contact, if applicable
- current application or award status and key upcoming dates
- project description, total budget, and federal/local funding split
- match or cost-share requirement and approved sources
- federal compliance requirements triggered (Davis-Bacon, NEPA, Buy America, Section 106, civil rights assurances)
- assigned federal program officer and state contact information
- outstanding award conditions, special provisions, or open items
</inputs>

<checks>
- confirm which federal compliance requirements are triggered and whether city has a documented compliance plan for each
- verify match costs are allowable under the specific program — not all local expenditures qualify
- flag any grant conditions that restrict the city's authority over how it uses its own funds on the project
- confirm SAM.gov registration is current and UEI is active
- note any congressional or state notification requirements and whether they have been completed
- flag scope or budget changes that require prior federal or state approval before the city proceeds
- identify reporting deadlines and whether city systems can capture required performance data
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
