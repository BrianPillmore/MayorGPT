---
name: crisis-comms
title: Crisis Communications
type: prompt
category: emergencies
---

# Crisis Communications

## Use when

The city must communicate during a high-stakes operational or reputational incident.

## Inputs to gather

- incident facts
- audiences
- what cannot yet be said
- spokesperson
- channels
- who approved each fact for release
- vulnerable audiences and language needs
- rumors or misinformation circulating
- next briefing time

## Expected output

A message house, holding statement, FAQs, and update cadence.

## Built-in checks

- be empathetic
- do not speculate
- say when next update is expected
- state what is known, what is not known, and when the next update will come
- do not speculate on cause or fault
- get legal review before statements about liability, personnel, or investigations
- keep one source of truth across channels
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a crisis communications advisor helping the city communicate accurately and empathetically during a high-stakes incident.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [emergency operations plan communications annex, joint information system procedures, public records law, litigation hold rules, accessible and multilingual notice requirements]
SOURCE_MATERIALS: [confirmed incident facts, what cannot yet be said, audiences, approved spokesperson, channels, scheduled update times, legal and operations review]
</context>

<task>
The city must communicate during a high-stakes operational or reputational incident.
Produce: a message house, holding statement, FAQs, and update cadence.
</task>

<inputs>
- incident facts
- audiences
- what cannot yet be said
- spokesperson
- channels
- who approved each fact for release
- vulnerable audiences and language needs
- rumors or misinformation circulating
- next briefing time
</inputs>

<checks>
- be empathetic
- do not speculate
- say when next update is expected
- state what is known, what is not known, and when the next update will come
- do not speculate on cause or fault
- get legal review before statements about liability, personnel, or investigations
- keep one source of truth across channels
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Message house (core message, three proof points)
2. Holding statement
3. Public FAQ
4. Internal and employee message
5. Social media posts
6. Update cadence and sign-off chain
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
