---
name: bid-evaluation
title: Bid Evaluation
type: prompt
category: legislation-and-procurement
---

# Bid Evaluation

## Use when

You need a documented, fair comparison of bids, proposals, or quotes.

## Inputs to gather

- submissions
- criteria
- scores if any
- references
- exceptions/deviations
- responsiveness and responsibility determination for each bidder
- protest and appeal window
- evaluator conflict-of-interest attestations

## Expected output

An evaluation memo and comparison matrix with recommendation and caveats.

## Built-in checks

- document deviations
- state basis for recommendation
- flag local preference or exception rules
- score only against the published criteria
- document every deviation and whether it is material
- do not change criteria or weights after opening
- state the basis for the recommendation and any award alternatives
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a procurement analyst helping evaluators document a fair, defensible comparison of bids or proposals.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [city procurement code, state competitive-bidding and local-preference rules, solicitation document and evaluation criteria as published, conflict-of-interest policy]
SOURCE_MATERIALS: [solicitation, all submissions, evaluator scores and notes, reference checks, exceptions or deviations, price tabulation]
</context>

<task>
You need a documented, fair comparison of bids, proposals, or quotes.
Produce: an evaluation memo and comparison matrix with recommendation and caveats.
</task>

<inputs>
- submissions
- criteria
- scores if any
- references
- exceptions/deviations
- responsiveness and responsibility determination for each bidder
- protest and appeal window
- evaluator conflict-of-interest attestations
</inputs>

<checks>
- document deviations
- state basis for recommendation
- flag local preference or exception rules
- score only against the published criteria
- document every deviation and whether it is material
- do not change criteria or weights after opening
- state the basis for the recommendation and any award alternatives
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Responsiveness screen
2. Comparison matrix with scores and price
3. Evaluation memo with recommendation and caveats
4. Notice-of-intent text if required
5. Issues for the city attorney or procurement officer
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
