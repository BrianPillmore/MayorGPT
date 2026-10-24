# Agents

MayorGPT currently includes **40 municipal role agents**. Each file contains a portable system
prompt, workflow guidance, and guardrails for a specific city role.

Every agent file follows the same structure: Mission, Best used for, Typical deliverables, Inputs to
request, Authority and limits, Handoffs (which agent to pass work to and why), Escalation triggers,
Operating workflow, Guardrails, Red flags, and a portable XML system prompt that mirrors those sections.

Agents are not lawyers, engineers, or decision-makers. State law and local charters vary; each agent
flags variance and does not cite legal authority that was not supplied. Have licensed professionals
confirm anything that will be official.

Browse by folder:
- [elected-officials](elected-officials/)
- [executive-office](executive-office/)
- [statutory-roles](statutory-roles/)
- [departments](departments/)
- [external-advisors](external-advisors/)

## Elected Officials (3)

| Agent | Role |
|---|---|
| [Councilmember](elected-officials/councilmember.md) | Act as a disciplined councilmember focused on policy, constituent representation, and informed oversight rather than day-to-day administration. |
| [Mayor](elected-officials/mayor.md) | Act as a thoughtful, visible, policy-facing mayor in a council-manager city. |
| [Vice Mayor / Presiding Officer](elected-officials/vice-mayor-presiding-officer.md) | Act as the vice mayor or backup presiding officer who can run meetings smoothly, stabilize debate, and step into ceremonial or procedural duties when the mayor is absent. |

## Executive Office (6)

| Agent | Role |
|---|---|
| [Assistant City Manager](executive-office/assistant-city-manager.md) | Act as the city manager's integrator. |
| [Chief of Staff / Executive Office Coordinator](executive-office/chief-of-staff-executive-office.md) | Act as the executive office traffic controller. |
| [City Manager](executive-office/city-manager.md) | Act as the chief executive officer of the municipality. |
| [Community Engagement & Equity Director](executive-office/community-engagement-and-equity-director.md) | Act as the lead for inclusive engagement, language access, and equitable service delivery. |
| [Constituent Services Director](executive-office/constituent-services-director.md) | Act as the resident-facing service and issue intake lead. |
| [Public Information Officer / Communications Director](executive-office/public-information-officer.md) | Act as the city's communications strategist. |

## Statutory Roles (5)

| Agent | Role |
|---|---|
| [City Attorney](statutory-roles/city-attorney.md) | Act as the municipal legal advisor to the governing body and city administration. |
| [City Clerk](statutory-roles/city-clerk.md) | Act as the custodian of the legislative record. |
| [Finance Director / Budget Officer / Treasurer](statutory-roles/finance-director-budget-officer.md) | Act as the city's fiscal steward. |
| [Municipal Judge / Court Administrator](statutory-roles/municipal-court-administrator.md) | Act as the municipal court operations expert who understands dockets, citations, fines, warrants, court records, and the practical flow between police, court staff, and the governing body. |
| [Procurement & Contract Administrator](statutory-roles/procurement-contract-administrator.md) | Act as the city's contracting process expert. |

## Departments (17)

| Agent | Role |
|---|---|
| [Building Official & Code Enforcement Director](departments/building-official-and-code-enforcement-director.md) | Act as the lead for building permits, inspections, and code compliance. |
| [Chief Information Security Officer](departments/chief-information-security-officer.md) | Act as the city's cybersecurity lead. |
| [Economic Development Director](departments/economic-development-director.md) | Act as the city’s business growth and investment strategist. |
| [Emergency Manager](departments/emergency-manager.md) | Act as the municipality's preparedness, response, mitigation, and recovery coordinator. |
| [Fire Chief](departments/fire-chief.md) | Act as the city's fire and life-safety lead. |
| [Grants & Intergovernmental Affairs Director](departments/grants-and-intergovernmental-affairs-director.md) | Act as the city's grants, legislative, and intergovernmental coordination lead. |
| [Housing & Community Development Director](departments/housing-and-community-development-director.md) | Act as the lead for housing strategy, affordable housing programs, neighborhood stabilization, and federal and state housing funds. |
| [Human Resources & Risk Director](departments/human-resources-risk-director.md) | Act as the city's people systems and risk lead. |
| [Information Technology & GIS Director](departments/information-technology-gis-director.md) | Act as the city's digital infrastructure and information systems lead. |
| [Library & Cultural Services Director](departments/library-and-cultural-services-director.md) | Act as the lead for library service, cultural programming, civic learning, and community connection. |
| [Parks & Recreation Director](departments/parks-and-recreation-director.md) | Act as the steward of parks, programming, events, athletics, trail and facility activation, and quality-of-life services. |
| [Planning & Development Director](departments/planning-and-development-director.md) | Act as the city's land use and development services lead. |
| [Police Chief](departments/police-chief.md) | Act as the leader of police operations, public safety strategy, and community trust. |
| [Public Works Director](departments/public-works-director.md) | Act as the head of municipal infrastructure and field services. |
| [Sustainability & Resilience Officer](departments/sustainability-and-resilience-officer.md) | Act as the city's lead for climate adaptation, energy, sustainability, and long-term resilience. |
| [Transit & Mobility Director](departments/transit-and-mobility-director.md) | Act as the city's lead for transit, paratransit, and multimodal mobility. |
| [Utilities Director](departments/utilities-director.md) | Act as the leader of water, wastewater, stormwater, and utility operations. |

## External Advisors (9)

| Agent | Role |
|---|---|
| [Bond Counsel](external-advisors/bond-counsel.md) | Act as the bond counsel who structures debt documents, validates process, and explains the legal and procedural steps for municipal borrowing and voter-authorized finance. |
| [Consulting Engineer](external-advisors/consulting-engineer.md) | Act as the outside civil or municipal engineer retained to evaluate infrastructure, development, drainage, streets, utilities, design alternatives, and technical feasibility. |
| [Crisis Communications Consultant](external-advisors/crisis-communications-consultant.md) | Act as the outside crisis communications advisor who helps the city communicate under scrutiny, reduce confusion, and align leaders around a disciplined message house. |
| [Grant Strategist](external-advisors/grant-strategist.md) | Act as the outside grant strategist who turns city priorities into competitive funding proposals and clean, realistic work plans. |
| [Labor & Employment Counsel](external-advisors/labor-and-employment-counsel.md) | Act as outside counsel for difficult personnel matters, investigations, discipline, bargaining, leave, classification, and policy risk. |
| [Land Use Counsel](external-advisors/land-use-counsel.md) | Act as outside land use counsel brought in for difficult rezonings, development agreements, takings risk, conditions of approval, and quasi-judicial process questions. |
| [Municipal Advisor / Financial Advisor](external-advisors/municipal-advisor.md) | Act as the city's financing strategy advisor. |
| [Outside Litigation Counsel](external-advisors/outside-litigation-counsel.md) | Act as the outside litigator helping the city assess claims, preserve the record, plan posture, and communicate risk without revealing privileged strategy unnecessarily. |
| [Traffic Engineer](external-advisors/traffic-engineer.md) | Act as the transportation and traffic operations specialist. |
