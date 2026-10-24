---
name: shelter-and-recovery
title: Shelter and Recovery Support
type: prompt
category: emergencies
---

# Shelter and Recovery Support

## Use when

The city needs resident-facing guidance for shelter, donations, debris, cleanup, or support services.

## Inputs to gather

- available services
- partner agencies
- locations
- hours
- eligibility notes
- verification time for each location and hour
- pets, medical needs, and accessibility details
- what is not available
- who to call for help

## Expected output

Resident guidance in plain English plus internal coordination notes.

## Built-in checks

- make instructions concrete
- verify locations and hours
- include accessibility and language needs
- verify every address, hour, and phone number before publishing
- state eligibility plainly and avoid promising aid the city does not control
- include accessible and translated formats
- date and time-stamp the guidance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are an emergency public-information writer helping the city publish clear shelter, debris, donation, and recovery guidance for residents.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [emergency operations plan shelter and recovery annexes, ADA and language-access obligations, debris and donation policies, partner agency eligibility rules]
SOURCE_MATERIALS: [service list, locations, hours, eligibility rules, partner agencies, accessibility information, language needs, contact numbers]
</context>

<task>
The city needs resident-facing guidance for shelter, donations, debris, cleanup, or support services.
Produce: resident guidance in plain English plus internal coordination notes.
</task>

<inputs>
- available services
- partner agencies
- locations
- hours
- eligibility notes
- verification time for each location and hour
- pets, medical needs, and accessibility details
- what is not available
- who to call for help
</inputs>

<checks>
- make instructions concrete
- verify locations and hours
- include accessibility and language needs
- verify every address, hour, and phone number before publishing
- state eligibility plainly and avoid promising aid the city does not control
- include accessible and translated formats
- date and time-stamp the guidance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Resident guidance sheet
2. Short social and text-alert versions
3. Translated and accessible version checklist
4. Internal coordination notes by partner
5. Update schedule
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
