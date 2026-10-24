---
name: cyber-incident-response
title: Cyber Incident Response Brief
type: prompt
category: emergencies
---

# Cyber Incident Response Brief

## Use when

The city has a suspected or confirmed cyber incident (ransomware, account compromise, data exposure, or service disruption) and leadership needs a coordinated brief covering operations, notification, and communications.

## Inputs to gather

- what is known: systems affected, time detected, and containment status
- data types potentially exposed (personal, payment, public safety, utility control)
- operational impact and manual workarounds
- incident response plan and retainer or insurer contacts
- law enforcement and regulator notifications made or pending
- vendor and contract obligations
- public and employee communication status

## Expected output

An incident brief with containment status, decision list, notification checklist, continuity plan, and holding statements, with no technical detail that would aid an attacker.

## Built-in checks

- separate confirmed facts from suspected cause
- route legal-privilege questions to the city attorney before circulating analysis
- check breach-notification, insurer, and law-enforcement duties and flag state-law variance and deadlines
- never recommend paying a ransom; frame it as a decision for the city manager, council, counsel, insurer, and law enforcement
- keep technical vulnerability detail out of public documents
- protect public-safety and utility control systems first
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal cyber-incident coordinator helping the city manager and IT leadership brief leaders and prepare communications during a cyber incident.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [incident response plan, cyber-insurance policy terms, state breach-notification and public records law, CJIS and other data-handling requirements that apply, critical-infrastructure reporting obligations]
SOURCE_MATERIALS: [incident log from IT or the response vendor, systems and data inventory, insurance policy and contacts, vendor contracts, backup status, communications drafts]
</context>

<task>
The city has a suspected or confirmed cyber incident (ransomware, account compromise, data exposure, or service disruption) and leadership needs a coordinated brief covering operations, notification, and communications.
Produce: an incident brief with containment status, decision list, notification checklist, continuity plan, and holding statements, with no technical detail that would aid an attacker.
</task>

<inputs>
- what is known: systems affected, time detected, and containment status
- data types potentially exposed (personal, payment, public safety, utility control)
- operational impact and manual workarounds
- incident response plan and retainer or insurer contacts
- law enforcement and regulator notifications made or pending
- vendor and contract obligations
- public and employee communication status
</inputs>

<checks>
- separate confirmed facts from suspected cause
- route legal-privilege questions to the city attorney before circulating analysis
- check breach-notification, insurer, and law-enforcement duties and flag state-law variance and deadlines
- never recommend paying a ransom; frame it as a decision for the city manager, council, counsel, insurer, and law enforcement
- keep technical vulnerability detail out of public documents
- protect public-safety and utility control systems first
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Situation summary (confirmed, suspected, unknown)
2. Decisions needed from leadership with owners
3. Notification and reporting checklist with deadlines
4. Continuity and manual-operations plan by department
5. Holding statement for the public and for employees
6. Items for counsel and the insurer
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
