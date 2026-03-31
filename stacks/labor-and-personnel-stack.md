# Labor and Personnel Stack

## Best for
Hiring processes, disciplinary actions, workplace investigations, performance reviews, workforce planning, and labor relations strategy.

## When to activate
Pull this stack when a department head opens a recruitment, when a disciplinary process requires written documentation, when a formal workplace investigation is initiated, when performance review cycles begin, or when workforce planning data needs to be analyzed for a budget presentation or Council report.

## Combine
- Agent: `agents/departments/human-resources-risk-director.md`
- Agent: `agents/executive-office/city-manager.md`
- Agent: `agents/statutory-roles/city-attorney.md`
- Prompt folder: `prompts/people-and-hr/`
- Skills: `hiring-panel-kit`, `investigation-intake`, `disciplinary-memo-builder`, `performance-review-writer`

## Sequence
1. **HR Director agent + hiring-panel-kit** — for recruitments, build the hiring panel materials: job-specific interview questions, scoring rubrics, and reference check frameworks. Attach the position description and any applicable civil service rules or collective bargaining provisions.
2. **HR Director agent + performance-review-writer** — during review cycles, draft structured performance review language based on supervisor input. Attach the prior review, position description, and supervisor's factual notes. Do not attach other employees' reviews in the same session.
3. **HR Director agent + investigation-intake** — when a complaint or incident triggers a formal investigation, use this skill to structure the intake documentation: scope, complainant statement framework, respondent notice language, and witness identification. Attach only the initial complaint or incident report.
4. **City Attorney agent** — before any disciplinary action, investigation report, or separation agreement is finalized, City Attorney must review. Attach the draft document and the relevant personnel policy or collective bargaining agreement.
5. **City Manager agent + disciplinary-memo-builder** — for formal disciplinary actions that require CM involvement, draft the action memo with appropriate progressive discipline framing, factual basis, and appeal rights notice. Requires City Attorney review from step 4 before finalization.

## Watch for
- **Privacy and confidentiality above all**: This stack handles the most sensitive employee information in city government. Never attach documents from one employee's file when working on another employee's matter. Do not paste SSNs, medical information, EAP records, or accommodation requests into any AI session. Output from this stack should be treated as confidential personnel records from the moment it is generated.
- **Conclusory language in disciplinary documents**: AI-drafted disciplinary memos often shift toward conclusory characterizations ("the employee was dishonest") rather than factual recitation ("the employee stated X on [date]; surveillance footage showed Y"). Every finding must be tied to a specific, documented fact. City Attorney review is mandatory, not optional.
- **Due process gates**: Depending on the employee's status (at-will, civil service, union), specific procedural steps must occur before discipline is imposed — Skelly hearings, Garrity warnings, pre-termination notice. The disciplinary-memo-builder will flag applicable gates, but HR and City Attorney must confirm the right process for the specific employee classification under your jurisdiction's rules.
- **Non-discriminatory language discipline**: Review all AI-generated hiring questions, evaluation language, and disciplinary documents for any criteria that could constitute a protected-class proxy. The hiring-panel-kit is designed to minimize this risk, but human HR review remains essential before any materials are used with candidates or employees.
