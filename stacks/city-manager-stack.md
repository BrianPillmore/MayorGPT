# City Manager Stack

## Best for
Executive operations, cross-department follow-up, staff report coordination, and implementation planning.

## When to activate
Pull this stack at the start of each week to triage open action items, when a Council directive needs to be converted into a work plan, when department heads are producing uncoordinated staff reports for the same meeting, or when a Council member or resident escalation lands on the CM's desk and needs a structured written response.

## Combine
- Agent: `agents/executive-office/city-manager.md`
- Agent: `agents/executive-office/assistant-city-manager.md`
- Agent: `agents/statutory-roles/finance-director-budget-officer.md`
- Prompt folder: `prompts/weekly/`
- Prompt folder: `prompts/monthly/`
- Skills: `staff-report-builder`, `kpi-dashboard-narrative`, `service-request-triage`, `project-status-dashboard-narrative` (prompt), `charter-code-crosscheck`

## Sequence
1. **City Manager agent + kpi-dashboard-narrative** — open the week by turning the latest performance data into a narrative summary the CM can scan. Attach the prior period KPI export from your tracking system.
2. **Assistant City Manager agent + service-request-triage** — review open service requests and flag any that are overdue, politically sensitive, or cross-departmental. Attach the current service request queue export.
3. **City Manager agent + staff-report-builder** — for each Council item being coordinated, build or refine the staff report. Attach any department memos, fiscal impact data, and relevant code sections.
4. **City Manager agent + charter-code-crosscheck** — before any staff report goes to Council, run a crosscheck to confirm the recommended action is within authorized authority. Attach the relevant charter and code provisions.
5. **Finance Director agent** — for any staff reports with fiscal impact, have Finance Director review the numbers section. Requires adopted budget comparison and fund balance data.

## Watch for
- **Authority assumption**: AI may draft recommendations that exceed the CM's delegated authority or require Council action. The charter-code-crosscheck skill is essential, not optional, before any report goes forward.
- **Cross-department coordination gaps**: When multiple departments contribute to a staff report, the AI sees only the material you attach. Missing a department's input can produce an incomplete or contradictory recommendation.
- **Escalation tone calibration**: The City Manager agent tends toward neutral, professional language. For politically charged escalations, a human should review whether the draft response matches the actual gravity of the situation.
- **Agenda deadline drift**: Staff reports built iteratively over several sessions can miss publication deadlines. Build the publication deadline into every staff-report-builder prompt so the AI flags timing risks.
