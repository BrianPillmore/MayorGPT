---
name: cybersecurity-posture-review
title: Cybersecurity Posture Review
type: prompt
category: quarterly
---

# Cybersecurity Posture Review

## Use when

Leadership needs a quarterly, non-technical view of the city's cybersecurity posture, incidents, training, vendor risk, and resource needs.

## Inputs to gather

- incident and near-miss summary
- patching, backup, and recovery test status
- multifactor authentication and access review coverage
- employee training and phishing test results
- critical vendor and cloud-service risk reviews
- cyber-insurance requirements and renewal status
- operational technology (utilities, traffic, public safety) exposure
- open audit or assessment findings and budget needs

## Expected output

A leadership memo with risk summary, trend, control coverage, top three risks, and funded or unfunded actions, free of exploitable detail.

## Built-in checks

- keep exploitable detail out of anything that might become a public record and consult the city attorney on what is exempt from disclosure in the state
- use risk-based language that leaders can act on
- separate IT systems from operational technology
- check that backups have been tested, not only taken
- tie asks to insurance, audit, or regulatory requirements
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal cybersecurity governance analyst helping IT leadership brief the city manager and council.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city information security policy, cyber-insurance terms, state records and data-protection law, criminal-justice and payment-data handling requirements that apply, incident response plan]
SOURCE_MATERIALS: [security dashboard or assessment summary, incident log, training reports, vendor inventory, audit findings, budget requests, insurance questionnaire]
</context>

<task>
Leadership needs a quarterly, non-technical view of the city's cybersecurity posture, incidents, training, vendor risk, and resource needs.
Produce: a leadership memo with risk summary, trend, control coverage, top three risks, and funded or unfunded actions, free of exploitable detail.
</task>

<inputs>
- incident and near-miss summary
- patching, backup, and recovery test status
- multifactor authentication and access review coverage
- employee training and phishing test results
- critical vendor and cloud-service risk reviews
- cyber-insurance requirements and renewal status
- operational technology (utilities, traffic, public safety) exposure
- open audit or assessment findings and budget needs
</inputs>

<checks>
- keep exploitable detail out of anything that might become a public record and consult the city attorney on what is exempt from disclosure in the state
- use risk-based language that leaders can act on
- separate IT systems from operational technology
- check that backups have been tested, not only taken
- tie asks to insurance, audit, or regulatory requirements
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Posture summary and trend
2. Control coverage table
3. Top risks with owners and cost to fix
4. Vendor and OT concerns
5. Training and incident summary
6. Decisions and budget asks
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
