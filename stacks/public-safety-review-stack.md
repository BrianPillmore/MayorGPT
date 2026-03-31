# Public Safety Review Stack

## Best for
Police, fire, and EMS performance reviews, community safety data analysis, quarterly public safety briefings, and after-action learning from major incidents or patterns.

## When to activate
Pull this stack when quarterly public safety KPIs are due for Council, when a community safety concern (crime trends, response time degradation, repeat incident locations) needs structured analysis, when a department is preparing its annual performance report, or when a major incident or pattern of incidents triggers a public accountability review.

## Combine
- Agent: `agents/departments/police-chief.md`
- Agent: `agents/departments/fire-chief.md`
- Agent: `agents/departments/emergency-manager.md`
- Prompt: `prompts/quarterly/public-safety-review`
- Skills: `emergency-incident-brief`, `kpi-dashboard-narrative`, `service-request-triage`

## Sequence
1. **Emergency Manager agent + kpi-dashboard-narrative** — open the review by establishing the cross-departmental performance picture. Attach the quarterly KPI data for police, fire, and EMS in a single export so the narrative draws from a unified dataset.
2. **Police Chief agent + kpi-dashboard-narrative** — produce the law enforcement narrative: calls for service, response times, crime categories, clearance rates, use-of-force summary, and any community engagement metrics. Attach the department's NIBRS or UCR data extract.
3. **Fire Chief agent + kpi-dashboard-narrative** — produce the fire and EMS narrative: incident volume by type, response time performance against NFPA benchmarks, apparatus availability, and training hours. Attach the CAD/RMS data export.
4. **Emergency Manager agent + service-request-triage** — identify cross-departmental service gaps, repeat problem locations, and resource alignment issues. Attach the combined service request and incident log.
5. **Emergency Manager agent + emergency-incident-brief** — for any major incident during the review period, produce a structured incident summary for inclusion in the public report. Attach the after-action documentation.

## Watch for
- **Metric selection bias**: Departments naturally emphasize metrics where they perform well. The KPI set should be defined by policy (Council-adopted performance standards or a published service level agreement), not chosen by the department at reporting time. Verify the metrics in the attached data match the adopted standard.
- **Use-of-force and complaint data sensitivity**: AI-drafted public safety narratives should not identify individual officers, summarize open internal affairs investigations, or characterize contested incidents. Have City Attorney review any section that discusses complaints, discipline, or use-of-force.
- **Response time measurement inconsistency**: Police and fire/EMS may measure response time intervals differently (dispatch-to-arrive vs. call-to-arrive). Ensure the narrative explicitly states which measurement methodology is used so Council and the public can compare data accurately.
- **Community perception versus operational data divergence**: Strong performance metrics alongside poor community trust scores are a warning sign, not a contradiction to paper over. Surface the divergence explicitly and let leadership decide how to address it publicly.
