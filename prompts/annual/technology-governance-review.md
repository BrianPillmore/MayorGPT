---
name: technology-governance-review
title: Technology and AI Governance Review
type: prompt
category: annual
---

# Technology and AI Governance Review

## Use when

The city needs to conduct an annual review of its technology systems, cybersecurity posture, data governance practices, and AI use — assessing risk, policy alignment, and readiness for the year ahead.

## Inputs to gather

- inventory of major city technology systems and vendors
- current cybersecurity policies and recent incident history
- AI tools currently in use or piloted by city departments
- outstanding audit findings or IT risk register items
- IT staffing and budget
- state and federal compliance requirements (data privacy, security)
- council-adopted technology or AI policies

## Expected output

A technology governance review memo with systems risk summary, cybersecurity posture assessment, AI use inventory and policy gaps, compliance status, and recommended council action items.

## Built-in checks

- distinguish high-risk systems (utilities, finance, public safety) from lower-risk systems
- identify any AI use without documented policy or human review requirements
- flag any vendor contracts approaching expiration or needing security review
- note data privacy obligations and whether current practices meet them
- do not share specific vulnerability details in any document intended for public release

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping conduct an annual city technology and AI governance review.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, IT policy, AI acceptable-use policy, state and federal data privacy and security requirements, audit requirements]
SOURCE_MATERIALS: [technology systems inventory, cybersecurity assessment or incident log, AI use inventory, IT budget, outstanding audit findings, vendor contract list]
</context>

<task>
The city is conducting its annual review of technology systems, cybersecurity posture, data governance, and AI use.
Produce a technology governance review memo with systems risk summary, cybersecurity posture assessment, AI use inventory and policy gaps, compliance status, and recommended council action items.
</task>

<inputs>
- inventory of major city technology systems and their criticality ratings
- current cybersecurity policies and recent incident or near-miss history
- current AI tools in active use or pilot by city departments, with a description of use case and any review process
- outstanding audit findings or IT risk register items
- IT staffing levels and annual budget
- applicable state and federal compliance requirements (data privacy, CISA advisories, etc.)
- any council-adopted technology or AI policies
</inputs>

<checks>
- distinguish high-risk systems (utilities, finance, public safety CAD, elections) from lower-risk administrative systems
- flag any AI tools currently deployed without documented policy or human review requirements
- identify vendor contracts approaching expiration, lacking security addenda, or not meeting current standards
- assess whether current data practices meet state and federal privacy obligations
- do not include specific vulnerability details in any document intended for council or public release
- flag any items requiring council policy action or budget authorization
</checks>

<required_output>
1. Systems risk summary (high-risk first)
2. Cybersecurity posture assessment, without exploitable detail
3. AI use inventory and policy gaps
4. Compliance status and vendor-contract flags
5. Recommended council actions
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
