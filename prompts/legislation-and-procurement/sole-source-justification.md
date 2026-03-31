---
name: sole-source-justification
title: Sole-Source Procurement Justification
type: prompt
category: legislation-and-procurement
model_compatibility:
  - Claude
  - ChatGPT
  - Gemini
  - Open-weight LLMs
claude_fit: high
---

# Sole-Source Procurement Justification

## Use when

The city intends to award a contract without competitive bidding and must document the legal basis and factual rationale for a sole-source or emergency procurement.

## Inputs to gather

- vendor name and contract description
- estimated contract value
- legal basis for sole-source (proprietary technology, emergency, unique expertise, etc.)
- market research conducted or attempted
- department requesting the waiver
- prior contracts with this vendor if any
- any council or procurement authority approval required

## Expected output

A complete sole-source justification memorandum suitable for the procurement file and council packet, plus a legal-basis checklist and a list of information gaps to resolve before signing.

## Built-in checks

- confirm the stated basis meets the city's procurement code and state law requirements
- document market research efforts even if minimal
- do not frame convenience, preference, or prior relationship as a legal sole-source basis
- flag if contract value exceeds the city manager's or procurement officer's signing authority
- note whether council resolution or public notice is required
- flag any appearance-of-favoritism or ethics concern

## Copy/paste prompt

```xml
<role>
You are a municipal government assistant helping document the rationale for a non-competitive sole-source procurement.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [charter, procurement code, state competitive bidding law, signing authority thresholds, council authorization requirements]
SOURCE_MATERIALS: [vendor proposal or quote, market research notes, department justification memo, prior contract history if any]
</context>

<task>
The city is preparing a sole-source or emergency procurement justification.
Produce a complete justification memorandum suitable for the procurement file and council packet, a legal-basis checklist, and a list of information gaps to resolve before the contract is signed.
</task>

<inputs>
- vendor name and description of goods or services
- estimated contract value and term
- legal basis for sole-source under city procurement code and state law
- market research conducted, attempted, or waived with reason
- department requesting the waiver and department director name
- prior contract history with this vendor
- council or procurement authority approval threshold and whether it applies
</inputs>

<checks>
- confirm stated legal basis satisfies city procurement code and state competitive bidding law
- verify market research is documented even if limited or waived
- do not frame prior relationship, staff preference, or scheduling convenience as a legal sole-source basis
- flag if contract value exceeds signing authority and requires council action
- note whether public notice of award is required under transparency rules
- flag any appearance-of-favoritism, conflict of interest, or ethics concern
- confirm the justification memo will be retained in the procurement file
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
