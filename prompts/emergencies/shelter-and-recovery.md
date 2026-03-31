---
name: shelter-and-recovery
title: Shelter and Recovery Support
type: prompt
category: emergencies
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
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

## Expected output

Resident guidance in plain English plus internal coordination notes.

## Built-in checks

- make instructions concrete
- verify locations and hours
- include accessibility and language needs

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping with shelter and recovery support.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, code, policy, state law, templates, tone preferences]
SOURCE_MATERIALS: [agenda, reports, emails, maps, contracts, budget sheets, comments, incident notes]
</context>

<task>
The city needs resident-facing guidance for shelter, donations, debris, cleanup, or support services.
Produce resident guidance in plain english plus internal coordination notes.
</task>

<inputs>
- available services
- partner agencies
- locations
- hours
- eligibility notes
</inputs>

<checks>
- make instructions concrete
- verify locations and hours
- include accessibility and language needs
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
