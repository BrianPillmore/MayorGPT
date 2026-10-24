# Prompts

MayorGPT currently includes **85 reusable prompts** organized by the rhythm of city work and
major municipal functions.

Every prompt file follows the same structure: Use when, Inputs to gather, Expected output, Built-in
checks, and a copy/paste XML prompt with `<role>`, `<context>`, `<task>`, `<inputs>`, `<checks>`, and
`<required_output>` blocks. Replace the bracketed fields with local rules and source materials.

Prompts do not supply legal citations. State law and local charters vary; each prompt tells the model
to flag variance rather than invent authority. Have the city attorney confirm before official use.

Browse by folder:
- [daily](daily/)
- [weekly](weekly/)
- [monthly](monthly/)
- [quarterly](quarterly/)
- [annual](annual/)
- [elections-and-transition](elections-and-transition/)
- [emergencies](emergencies/)
- [legislation-and-procurement](legislation-and-procurement/)
- [people-and-hr](people-and-hr/)
- [public-engagement](public-engagement/)
- [intergovernmental](intergovernmental/)

## Daily (10)

| Prompt | Use when |
|---|---|
| [Constituent Response](daily/constituent-response.md) | You need a calm, useful response to a resident complaint, question, compliment, or service request. |
| [Councilmember Daily Brief](daily/councilmember-daily-brief.md) | A councilmember needs a concise update on hot issues, resident concerns, and upcoming decision points. |
| [Difficult Email Response](daily/difficult-email.md) | You need to respond to an angry, accusatory, or politically sensitive email without escalating conflict. |
| [Executive Brief](daily/executive-brief.md) | You need a one-page briefing for the mayor, city manager, or council on a fast-moving issue. |
| [Inbox Prioritizer](daily/inbox-prioritizer.md) | An elected or executive office needs help sorting email into action buckets. |
| [Media Talking Points](daily/media-talking-points.md) | A leader or spokesperson needs concise public-facing talking points for media or stakeholder calls. |
| [Meeting Prep](daily/meeting-prep.md) | You need talking points, questions, and motion pathways before a council or board meeting. |
| [Public Records / FOIA Response](daily/public-records-response.md) | You have received a public records or FOIA request and need to triage it, identify responsive records and custodians, apply any applicable exemptions, and draft a timely written response. |
| [Quick Policy Explainer](daily/quick-policy-explainer.md) | You need to explain a city policy, ordinance, process, or decision in plain English. |
| [Service Request Triage](daily/service-request-triage.md) | The city needs to route resident or internal service requests quickly and consistently. |

## Weekly (8)

| Prompt | Use when |
|---|---|
| [City Manager Operations Review](weekly/city-manager-operations-review.md) | The manager’s office needs a weekly operational review across departments. |
| [Community Engagement Summary](weekly/community-engagement-summary.md) | You need to summarize what the city heard from residents over the past week. |
| [Council Weekly Brief](weekly/council-weekly-brief.md) | The governing body needs a weekly strategic and operational snapshot. |
| [Department Director 1:1 Prep](weekly/department-director-1on1.md) | You need an agenda and follow-up tracker for recurring manager/director check-ins. |
| [Development Pipeline Review](weekly/development-pipeline-review.md) | Leadership wants a weekly picture of pending development activity and pressure points. |
| [Interagency Coordination](weekly/interagency-coordination.md) | The city is working on a shared project or cross-jurisdictional issue with a county, regional authority, state agency, or special district and needs to align roles, communication, and deliverables. |
| [Legislative Monitor](weekly/legislative-monitor.md) | The city needs a running summary of state or regional legislation that could affect operations or authority. |
| [Project Status Dashboard Narrative](weekly/project-status-dashboard-narrative.md) | A dashboard needs human-readable narrative for leaders or the public. |

## Monthly (9)

| Prompt | Use when |
|---|---|
| [Agenda Cycle](monthly/agenda-cycle.md) | The city is building a regular or special meeting agenda packet. |
| [Board & Commission Appointments](monthly/board-commission-appointments.md) | The city is filling vacancies or preparing appointment action for boards or commissions. |
| [Budget Amendment Memo](monthly/budget-amendment-memo.md) | A department or the finance office needs council approval to amend the adopted budget (transfer, supplemental appropriation, or reallocation) and needs a clear, compliant memo. |
| [Communications Calendar](monthly/communications-calendar.md) | The city needs a proactive monthly communication plan tied to projects, meetings, and events. |
| [Monthly Financial Review](monthly/financial-review.md) | Leadership needs a monthly look at revenues, expenditures, variances, cash, and claims. |
| [Grant Pipeline Review](monthly/grant-pipeline-review.md) | The city wants a monthly snapshot of grants pursued, awarded, at-risk, or worth pursuing. |
| [Monthly Performance Memo](monthly/performance-memo.md) | Leadership wants a monthly performance narrative across service areas. |
| [Staff Report Builder](monthly/staff-report.md) | You need a clean, decision-ready staff report for council, a board, or a commission. |
| [Utility Rate Watch](monthly/utility-rate-watch.md) | Utility leadership or council needs a recurring rate and system pressure scan. |

## Quarterly (7)

| Prompt | Use when |
|---|---|
| [Capital Improvement Plan Review](quarterly/cip-review.md) | The city needs to review or re-rank capital projects. |
| [Cybersecurity Posture Review](quarterly/cybersecurity-posture-review.md) | Leadership needs a quarterly, non-technical view of the city's cybersecurity posture, incidents, training, vendor risk, and resource needs. |
| [Intergovernmental Relations Brief](quarterly/intergovernmental-relations-brief.md) | The mayor or manager needs a concise regional/state/federal relationship brief. |
| [Public Safety Quarterly Review](quarterly/public-safety-review.md) | The city needs to assess quarterly performance across police, fire, EMS, and code enforcement — identifying trends, comparing to targets, surfacing resource concerns, and briefing leadership. |
| [Risk Register Update](quarterly/risk-register-update.md) | Leadership needs a practical refresh of operational, fiscal, legal, reputational, and safety risks. |
| [Strategic Priority Review](quarterly/strategic-priority-review.md) | The city needs a quarterly scorecard on adopted goals or council priorities. |
| [Workforce Planning Review](quarterly/workforce-planning-review.md) | The city needs a quarterly view of vacancies, retention, succession, and training needs. |

## Annual (11)

| Prompt | Use when |
|---|---|
| [AI Governance Refresh](annual/ai-governance-refresh.md) | The city wants an annual refresh of acceptable-use, review, and oversight practices for AI. |
| [Annual Report](annual/annual-report.md) | The city wants a public annual report that explains results, finances, and priorities to residents in plain language. |
| [Audit Response](annual/audit-response.md) | The city needs to respond to audit findings, comments, or management recommendations. |
| [Budget Adoption Book](annual/budget-adoption-book.md) | You need a polished summary for workshops or adoption. |
| [Budget Kickoff](annual/budget-kickoff.md) | The city is opening its annual budget cycle and needs clear instructions and framing. |
| [Comprehensive Plan Update](annual/comprehensive-plan-update.md) | The city is initiating, managing, or tracking a periodic update to its comprehensive land use plan and needs to organize the process, communicate with the community, and ensure consistency across plan elements. |
| [Goal Setting Retreat](annual/goal-setting-retreat.md) | The council or executive team is preparing for its annual retreat or planning session. |
| [Legislative Agenda](annual/legislative-agenda.md) | The city is setting its annual policy and advocacy priorities with outside governments. |
| [State of the City](annual/state-of-the-city.md) | The mayor or manager needs an annual community narrative. |
| [Sustainability and Resilience Review](annual/sustainability-and-resilience-review.md) | The city is reviewing its sustainability, energy, climate-adaptation, and resilience work against adopted goals and emerging hazards. |
| [Technology and AI Governance Review](annual/technology-governance-review.md) | The city needs to conduct an annual review of its technology systems, cybersecurity posture, data governance practices, and AI use — assessing risk, policy alignment, and readiness for the year ahead. |

## Elections And Transition (5)

| Prompt | Use when |
|---|---|
| [Campaign to Governance Boundary](elections-and-transition/campaign-to-governance-boundary.md) | A candidate or officeholder needs help respecting the line between campaigning and official acts. |
| [Candidate Briefing](elections-and-transition/candidate-briefing.md) | The city wants a neutral, educational briefing for candidates or prospective candidates. |
| [First 100 Days Plan](elections-and-transition/first-100-days-plan.md) | A newly elected mayor, councilmember, or new city manager needs a realistic plan for listening, learning, building relationships, and securing early wins in the first 100 days. |
| [New Council Onboarding](elections-and-transition/new-council-onboarding.md) | The city is onboarding one or more newly elected councilmembers. |
| [Transition Memo](elections-and-transition/transition-memo.md) | A newly elected official or incoming administration needs a handoff packet. |

## Emergencies (11)

| Prompt | Use when |
|---|---|
| [After Action Review](emergencies/after-action-review.md) | The city is wrapping an incident and wants structured learning rather than blame. |
| [Crisis Communications](emergencies/crisis-comms.md) | The city must communicate during a high-stakes operational or reputational incident. |
| [Cyber Incident Response Brief](emergencies/cyber-incident-response.md) | The city has a suspected or confirmed cyber incident (ransomware, account compromise, data exposure, or service disruption) and leadership needs a coordinated brief covering operations, notification, and communications. |
| [Damage Assessment and Disaster Reimbursement Tracker](emergencies/damage-assessment-and-reimbursement.md) | After a disaster the city must document damage, track costs, and prepare for state or federal reimbursement and needs a structured, audit-ready approach. |
| [Emergency Proclamation](emergencies/emergency-proclamation.md) | The city is considering or preparing an emergency declaration or supporting order. |
| [Emergency Operations Center Activation Brief](emergencies/eoc-activation-brief.md) | The emergency manager or city manager is deciding whether to activate, escalate, or stand down the emergency operations center (EOC) and needs a clear brief for the operational period. |
| [Incident Brief](emergencies/incident-brief.md) | You need a rapid, leader-ready summary during an incident. |
| [Public Health Emergency Response](emergencies/public-health-emergency.md) | The city is responding to a disease outbreak, water quality failure, mass casualty event, or other public health emergency requiring coordinated city action alongside the county or state health authority. |
| [Shelter and Recovery Support](emergencies/shelter-and-recovery.md) | The city needs resident-facing guidance for shelter, donations, debris, cleanup, or support services. |
| [Tornado Recovery](emergencies/tornado-recovery.md) | The city needs structured recovery planning after severe weather or tornado impacts. |
| [Utility Failure Response](emergencies/utility-failure-response.md) | The city is managing an extended failure of a water, wastewater, stormwater, electric, or gas utility system and needs to coordinate operations, public communications, mutual aid, and regulatory notifications. |

## Legislation And Procurement (8)

| Prompt | Use when |
|---|---|
| [Bid Evaluation](legislation-and-procurement/bid-evaluation.md) | You need a documented, fair comparison of bids, proposals, or quotes. |
| [Contract Approval Memo](legislation-and-procurement/contract-approval-memo.md) | A contract is moving to council or executive approval. |
| [Grant Application Narrative](legislation-and-procurement/grant-application-narrative.md) | The city needs to draft the narrative section of a competitive grant application, including the statement of need, project description, goals and objectives, and evaluation approach. |
| [Interlocal Agreement Review](legislation-and-procurement/interlocal-agreement.md) | The city is evaluating or drafting an interlocal or cooperative agreement. |
| [Ordinance Draft](legislation-and-procurement/ordinance-draft.md) | You need to draft or revise an ordinance. |
| [Resolution Draft](legislation-and-procurement/resolution-draft.md) | You need a resolution for appointments, policy statements, approvals, or formal findings. |
| [RFP Scope of Work](legislation-and-procurement/rfp-scope.md) | The city needs a clear solicitation scope for services or products. |
| [Sole-Source Procurement Justification](legislation-and-procurement/sole-source-justification.md) | The city intends to award a contract without competitive bidding and must document the legal basis and factual rationale for a sole-source or emergency procurement. |

## People And Hr (5)

| Prompt | Use when |
|---|---|
| [Disciplinary Memo](people-and-hr/disciplinary-memo.md) | You need a memo for corrective action or discipline. |
| [Hiring Scorecard](people-and-hr/hiring-scorecard.md) | The city needs a structured interview and evaluation tool for hiring. |
| [Performance Evaluation](people-and-hr/performance-evaluation.md) | A supervisor needs help drafting a balanced, specific evaluation. |
| [Religious Accommodation Response](people-and-hr/religious-accommodation-response.md) | The city needs to respond to a religious accommodation request from an employee or elected official. |
| [Workforce Reorganization](people-and-hr/workforce-reorganization.md) | The city is considering reporting-line, staffing, or organizational redesign. |

## Public Engagement (7)

| Prompt | Use when |
|---|---|
| [Community FAQ Builder](public-engagement/community-faq.md) | Residents keep asking the same questions and the city needs a public FAQ. |
| [Equity Impact Analysis](public-engagement/equity-impact-analysis.md) | Staff or elected officials want to understand how a proposed policy, budget item, project, or service change affects different neighborhoods and groups before a decision is made. |
| [Language Access and Inclusive Outreach Plan](public-engagement/language-access-and-inclusive-outreach-plan.md) | The city is planning outreach for a project, emergency, or service change and needs to reach residents who speak other languages, have disabilities, lack internet access, or are otherwise hard to reach. |
| [Public Comment Synthesis](public-engagement/public-comment-synthesis.md) | You need to summarize public comment from hearings, meetings, or written submissions. |
| [Survey Summary](public-engagement/survey-summary.md) | The city wants a readable synthesis of resident survey results. |
| [Town Hall Briefing](public-engagement/town-hall-briefing.md) | You need a structured prep packet for a public meeting, town hall, or listening session. |
| [Transit Service Change Brief](public-engagement/transit-service-change-brief.md) | The city or its transit provider is proposing a route, schedule, fare, or mobility service change and needs to brief decision-makers and inform riders. |

## Intergovernmental (4)

| Prompt | Use when |
|---|---|
| [ARPA and IIJA Grant Closeout](intergovernmental/arpa-iija-grant-closeout.md) | The city is closing out or reporting on pandemic-recovery or infrastructure-law funded projects and must make sure obligations, expenditures, reporting, and records meet award terms before deadlines. |
| [Council of Governments / MPO Meeting Brief](intergovernmental/council-of-governments-brief.md) | The mayor, manager, or council member needs to prepare for a regional council of governments (COG) or metropolitan planning organization (MPO) meeting — understanding the agenda, the city's positions, and the likely positions of other member governments. |
| [Federal Funding Coordination](intergovernmental/federal-funding-coordination.md) | The city is pursuing, managing, or reporting on a federal grant or infrastructure funding opportunity and must coordinate with a state pass-through agency, federal program office, or congressional delegation. |
| [State Legislative Testimony](intergovernmental/state-legislative-testimony.md) | The city needs to prepare written or oral testimony on state legislation that would affect municipal authority, revenue, services, or operations — either in support, opposition, or with requested amendments. |
