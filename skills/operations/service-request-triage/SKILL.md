---
name: service-request-triage
description: Triage resident or internal service requests into the right department, urgency, response language, and escalation path.
argument-hint: [request-text]
---

## Purpose
Classify an incoming request (311, email, call note, council referral) by responsible department, urgency tier, and next action, and draft a reply that sets honest expectations. Triage assigns work; it does not decide legal outcomes.

## Required inputs
- Request text, channel, date/time, and contact information (or anonymous).
- Location (address, intersection, parcel) and any photos.
- Existing open tickets at the location, prior history, and known outages or projects.
- The city's service level standards (target response and resolution times by category) and department responsibility matrix, including county, state, utility, and HOA jurisdictions.

## Workflow
1. Extract facts: what, where, since when, who is affected, any hazard. Separate observation from opinion.
2. Safety screen first. Emergencies go to 911 or the emergency dispatch immediately: fire, gas smell, downed power lines, people in danger, sewage backup into homes, water main break flooding, major road blockage, structural collapse. Do not queue them as tickets.
3. Assign an urgency tier: Tier 1 immediate hazard (minutes to hours), Tier 2 urgent service loss (same or next business day), Tier 3 standard (per published service level), Tier 4 planned or policy (route to project, CIP, or policy owner).
4. Route to the right owner: public works (streets, signs, potholes, storm drains), utilities (water/sewer), parks, police non-emergency, code enforcement, building, fire prevention, animal control, solid waste, or another agency. Identify when the asset belongs to another jurisdiction (state highway, county road, private utility) and give the exact contact.
5. Check duplicates and clusters: multiple requests at one location or a pattern (repeat flooding, signal outages) indicate a system issue and should be flagged to a supervisor.
6. Consider equity and access: language needs, accessibility, vulnerable residents (medical device power, seniors), and consistent service across neighborhoods.
7. Reply draft: acknowledge, state what the city can and cannot do, the next step, a realistic timeframe tied to the service level, and a reference number. Avoid promising specific dates unless dispatch confirms.
8. Records: log the decision and reason; note legal sensitivity (claims, threats, public records).

## Output structure
| Field | Value |
Rows: Summary | Location | Hazard? | Tier | Department/owner | Duplicate? | Target response | Reply text | Escalation
Include: resident-facing reply (plain language, under 150 words) and an internal note.

## Red flags / escalate
- Immediate danger or vulnerable-person risk: call 911 and notify the supervisor.
- Threats of violence or self-harm.
- Legal claims, injury, property damage: route to risk management/city attorney and preserve evidence.
- Discrimination or ADA complaints: route per policy.
- Council or media inquiries: notify the manager's office.
- Repeat failures or patterns of response disparity.

## Common mistakes
- Treating tone as urgency.
- Sending safety items through the normal queue.
- Over-promising timelines.
- Closing tickets without confirming resolution.
- Ignoring asset ownership.

## State-law variance
Public records handling of resident contact data and claim-notice requirements vary by state.
