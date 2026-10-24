# Example 8: Labor Negotiation Preparation

## Scenario

The fictional City of Pinecrest (pop. 42,000) is preparing to open contract negotiations with the union representing its public works and maintenance employees. The contract expires in six months. The City Manager needs a preparation package for the executive negotiating team: an issue scan, a fiscal framing, and a list of questions for labor counsel. The package is for internal and counsel use only.

All names and figures are fictional. Collective bargaining law, scope of bargaining, and confidentiality of negotiation materials vary significantly by state.

## What combination to use

| Layer | Selection | Why |
|---|---|---|
| Primary agent | `agents/departments/human-resources-risk-director.md` | Owns labor relations preparation |
| Supporting agent | `agents/external-advisors/labor-and-employment-counsel.md` | Legal strategy and compliance |
| Supporting agent | `agents/statutory-roles/finance-director-budget-officer.md` | Cost modeling |
| Skill | `skills/legal-risk/labor-employment-issue-scan/SKILL.md` | Issue scan against current contract and law |
| Skill | `skills/finance/revenue-forecast-scenario/SKILL.md` | Multi-year fiscal scenarios |
| Skill | `skills/legal-risk/executive-session-checklist/SKILL.md` | If Council gives direction in closed session |

## Why this combination works

Negotiation prep requires three separate lenses: legal constraints (what is bargainable and what is lawful), fiscal capacity (what the budget can sustain over multiple years), and operational needs (what the departments need from the contract). Keeping them as discrete, preserved outputs follows `stacks/ORCHESTRATION_PROTOCOL.md`.

## Key cautions

- **Privilege and confidentiality.** Negotiation strategy and Council direction may be protected in closed session or by attorney-client privilege; rules differ by state. Use an AI account approved for confidential material under your city policy (see `docs/data-privacy-and-pii-handling.md`) or do not use AI for the strategy portion.
- **Do not put individual employee personnel data into prompts.** Use position-level or aggregate data.
- **AI does not set bargaining position.** It structures issues and options; Council and the management team decide.
- **Public records risk.** Drafts may be records; confirm with the City Attorney whether and when negotiation materials are exempt.
