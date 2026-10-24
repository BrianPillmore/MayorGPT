---
name: public-safety-staffing-analysis
description: Analyze police, fire, EMS, or dispatch staffing requests using workload, response-time, and relief-factor data rather than ratios alone, and show the multi-year cost.
argument-hint: [department-and-request]
---

## Purpose
Evaluate a request for added or reallocated public safety positions with workload evidence, service-level targets, and full recurring cost. Staffing decisions are among the largest recurring commitments in a city budget, and per-capita ratios alone are not a sound basis.

## Required inputs
- Department request: positions, rank/type, justification, and proposed deployment.
- Workload data (12 to 36 months): calls for service by hour/day/zone and priority, unit-hour utilization, time on task, response times at the 90th percentile (not just the average), and out-of-service intervals.
- For fire/EMS: apparatus and station locations, incident types, mutual aid given/received, NFPA 1710 or 1720 compliance if the city has adopted the standard, and ISO-related considerations.
- For police: patrol workload (proactive time), clearance and case load per investigator, and community-policing objectives; for dispatch: call-taking time and abandonment.
- Pay scale, benefits, pension, overtime, minimum staffing rules, vacancies, attrition, and collective bargaining terms.

## Workflow
1. Define the service-level standard the staffing is meant to achieve (for example response-time targets by priority, proactive time share, apparatus staffing per unit) and the evidence for that standard.
2. Calculate demand by hour and zone, then required unit-hours. For patrol, a commonly used planning concept is allowing a share of time for proactive work; label the chosen share as a policy choice, not a fact.
3. Apply a relief (shift-relief) factor: the number of positions required to staff one 24/7 post, derived from actual leave, training, sick, and vacancy data, not a generic number. Compute from the department's own data.
4. Compare sworn/uniform FTE to the requirement; consider alternatives: civilianization, co-responder models, call diversion, technology, shift redesign, and mutual aid agreements. Estimate the share of calls that could be handled differently.
5. Compute the full cost: salary, benefits, pension, overtime, training, equipment, vehicle, recruitment, and academy time (new hires take months to become productive). Show year 1 and steady-state recurring cost, plus the pension liability effect.
6. Overtime and vacancies: if overtime is high because of vacancies, hiring may cost less than overtime; if staffing is full and overtime remains, review scheduling and policy.
7. Funding and sustainability: grants with retention requirements (such as federal hiring grants that require keeping positions after funding ends), local revenue source, and the cliff year.
8. Bargaining and legal: staffing minimums in labor agreements, mandatory bargaining on staffing impacts, civil service rules, and consent decrees.
9. Recommendation: phased positions, targets, and metrics for evaluating results after 12 to 24 months.

## Output structure
| Metric | Current | Target | Gap | Evidence |
Add: workload by hour heat table, FTE requirement vs. actual, options table (hire/civilianize/diversion/mutual aid) with year 1 and recurring cost, and evaluation metrics. 

## Red flags / escalate
- Request based on ratios or peer counts without workload data.
- Grant-funded positions with retention obligations and no local funding plan.
- Minimum staffing or bargaining implications.
- Response-time data that is incomplete or inconsistent across systems.
- Use-of-force, consent decree, or civil service constraints: city attorney and HR.
- Fire/EMS safety standards (two-in/two-out, apparatus staffing) at risk.

## Common mistakes
- Using population ratios as the sole benchmark.
- Using average response time instead of percentile.
- Omitting pension and overtime effects.
- Forgetting academy lag and attrition.
- Assuming new positions fix a retention problem.

## State-law variance
Collective bargaining rights, civil service, pension rules, and staffing mandates differ by state.
