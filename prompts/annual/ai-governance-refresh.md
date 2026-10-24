---
name: ai-governance-refresh
title: AI Governance Refresh
type: prompt
category: annual
---

# AI Governance Refresh

## Use when

The city wants an annual refresh of acceptable-use, review, and oversight practices for AI.

## Inputs to gather

- current policy
- tools used
- incidents or concerns
- training needs
- governance goals
- tool-by-tool inventory with department owner and data types touched
- public-facing or resident-affecting uses (chatbots, translation, triage)
- records-retention and public-records treatment of prompts and outputs
- vendor terms on data use and model training

## Expected output

A policy refresh memo, training priorities, and implementation checklist.

## Built-in checks

- address records/privacy/security
- identify approval thresholds
- clarify human review expectations
- identify which uses touch resident data, personnel decisions, or public safety and mark them high-risk
- name who approves new tools and at what threshold
- confirm human review is required before AI output is published or used in a decision about a person
- do not recommend a ban or approval of a specific vendor without the contract terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal technology-policy analyst helping a city refresh its annual AI governance policy and oversight practices.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [adopted AI or acceptable-use policy, records retention schedule, state public records law, state privacy and procurement rules, union or labor-notice obligations]
SOURCE_MATERIALS: [current AI policy text, tool and vendor inventory, incident or complaint log, training records, IT/legal review notes]
</context>

<task>
The city wants an annual refresh of acceptable-use, review, and oversight practices for AI.
Produce: a policy refresh memo, training priorities, and implementation checklist.
</task>

<inputs>
- current policy
- tools used
- incidents or concerns
- training needs
- governance goals
- tool-by-tool inventory with department owner and data types touched
- public-facing or resident-affecting uses (chatbots, translation, triage)
- records-retention and public-records treatment of prompts and outputs
- vendor terms on data use and model training
</inputs>

<checks>
- address records/privacy/security
- identify approval thresholds
- clarify human review expectations
- identify which uses touch resident data, personnel decisions, or public safety and mark them high-risk
- name who approves new tools and at what threshold
- confirm human review is required before AI output is published or used in a decision about a person
- do not recommend a ban or approval of a specific vendor without the contract terms
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Findings summary: what the current policy covers and misses
2. Proposed policy changes in redline-ready bullets
3. Approval thresholds and human-review rules table
4. Training and communication plan with owners and dates
5. Open questions for the city attorney and IT director
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
