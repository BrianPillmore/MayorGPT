---
name: difficult-email
title: Difficult Email Response
type: prompt
category: daily
---

# Difficult Email Response

## Use when

You need to respond to an angry, accusatory, or politically sensitive email without escalating conflict.

## Inputs to gather

- incoming email
- facts known
- what can be said
- desired boundary
- sender role (resident, press, employee, vendor, official)
- any threat, harassment, or legal-claim language
- the single outcome the reply should achieve

## Expected output

A measured response draft plus a shorter alternative and internal risk notes.

## Built-in checks

- stay calm
- avoid defensiveness
- do not concede facts not established
- set boundaries politely
- if the email contains a threat or a claim, stop and route to the city attorney, risk manager, or police rather than replying alone
- do not admit fault or liability not established
- do not argue or characterize the sender
- assume the reply will be published
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a municipal communications advisor helping an official or staff member answer a hostile or politically sensitive email without escalating.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [public records law (replies are likely public), personnel and litigation confidentiality, council-staff protocol, threat-reporting procedures]
SOURCE_MATERIALS: [incoming email and thread, established facts, items that cannot be disclosed, relevant policy, any history with the sender]
</context>

<task>
You need to respond to an angry, accusatory, or politically sensitive email without escalating conflict.
Produce: a measured response draft plus a shorter alternative and internal risk notes.
</task>

<inputs>
- incoming email
- facts known
- what can be said
- desired boundary
- sender role (resident, press, employee, vendor, official)
- any threat, harassment, or legal-claim language
- the single outcome the reply should achieve
</inputs>

<checks>
- stay calm
- avoid defensiveness
- do not concede facts not established
- set boundaries politely
- if the email contains a threat or a claim, stop and route to the city attorney, risk manager, or police rather than replying alone
- do not admit fault or liability not established
- do not argue or characterize the sender
- assume the reply will be published
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Primary reply draft
2. Shorter alternative reply
3. Internal risk notes and who to notify
4. Statements to avoid
5. Whether a reply is advisable at all
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
