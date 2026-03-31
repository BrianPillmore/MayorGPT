# Multi-Agent Coordination Guide

Most municipal workflows require more than one expert perspective. MayorGPT's agents represent distinct roles with distinct authorities, voices, and disciplines. Understanding how to coordinate multiple agents on the same issue — and how to hand off context, reconcile conflicting outputs, and sequence the workflow — is one of the highest-leverage skills in the toolkit.

## Why multi-agent matters

A single agent, even a well-configured one, is limited to the perspective of its role. The planning director sees land use and process; she does not own the fiscal analysis or the legal findings. The city attorney spots legal risk; he does not own the operational implementation plan. When these perspectives are not coordinated, the gaps between them create the most expensive mistakes in local government.

Multi-agent coordination is not just about getting more output — it is about getting disciplined, role-appropriate output from each expert and then assembling it into a coherent decision package.

For the formal orchestration protocol — covering handoff format, output preservation, human review gates, and accountability tracing — see `stacks/ORCHESTRATION_PROTOCOL.md`. The examples in this guide follow that protocol.

---

## Core pattern: the handoff

The basic multi-agent pattern is:

1. **Establish a shared context document.** Before engaging any agent, write a brief context summary: what the issue is, what decisions are being made, what source materials are attached. This context is attached to every agent in the workflow.
2. **Run each agent in its lane.** Give each agent its role-specific task. Do not ask the planning director to also do the legal risk analysis. Give the legal task to the city attorney agent.
3. **Collect the outputs.** Each agent produces a section or memo. Keep them separate until the reconciliation step.
4. **Identify conflicts.** Ask explicitly: "Do any of these outputs conflict with each other?" Common conflicts: the planning director recommends approval; the city attorney flags a legal basis for denial. The finance director says the project is within budget; the procurement officer flags a contract threshold issue.
5. **Reconcile and escalate.** Conflicts that cannot be resolved by staff analysis belong to the decision-maker. Label them explicitly in the final output.
6. **Produce the integrated deliverable.** One staff report, briefing memo, or agenda packet that reflects all the expert inputs, their areas of agreement, and the unresolved conflicts that require decision-maker judgment.

---

## Example A: Complex Rezoning — Planning, Legal, and Engineering

### Scenario
A mixed-use development proposal requires: a planning analysis of code compliance and comp plan consistency; a legal review of findings language and development agreement enforceability; and a traffic/engineering assessment of infrastructure adequacy. The City Manager needs a package for the council agenda.

### Agent lineup

| Agent | Task | Output |
|---|---|---|
| `planning-and-development-director` | Code/plan consistency, staff report structure, recommendation | Staff report narrative sections I–IV |
| `city-attorney` | Findings language, legal risk flags, development agreement issues | Legal section of staff report; conditions language |
| `consulting-engineer` (or `public-works-director`) | Infrastructure capacity, traffic, utility adequacy | Infrastructure exhibit / technical memorandum |

### Skill lineup

| Skill | Used by | Purpose |
|---|---|---|
| `zoning-case-analysis` | Planning director agent | Criteria walkthrough, options framing |
| `comp-plan-crosswalk` | Planning director agent | Consistency analysis with adopted plan |
| `land-use-findings-builder` | City attorney agent | Adoptable findings of fact and conditions |
| `development-agreement-review` | City attorney agent | Agreement enforceability and missing provisions |

### Workflow sequence

**Step 1 — Shared context.** Compile: application, site plan, code sections, plan policies, prior council action, and any public comments received to date. Attach to all agents.

**Step 2 — Planning analysis first.** Run the planning director agent with `zoning-case-analysis` to get the criteria analysis and a preliminary recommendation. This produces the factual backbone that the other agents will work from.

**Step 3 — Legal analysis from planning output.** Attach the planning analysis to the city attorney agent. Ask: "Review the planning analysis for legal vulnerability, and draft findings language for the recommended action. Flag any conditions that are legally unenforceable or that require additional code authority."

**Step 4 — Engineering analysis.** Run the public-works or consulting-engineer agent on the infrastructure question: water, sewer, traffic, stormwater. This is a separate lane — do not conflate engineering capacity with planning policy compliance.

**Step 5 — Reconcile conflicts.** Common conflict pattern in rezonings: planning recommends approval based on plan policy support; legal flags that a condition the planning director wants to impose is legally unenforceable; engineering says the sewer system cannot support the proposed density. Each of these conflicts requires resolution before the staff report is finalized.

Ask explicitly: *"The planning analysis recommends approval with Condition 4 (enhanced landscaping buffer). The legal analysis says Condition 4 is not supported by a specific code section and may be unenforceable. How should this conflict be resolved?"*

The AI can offer options (remove the condition, cite a different authority, require a code amendment first). The decision belongs to the Planning Director and City Attorney, not the AI.

**Step 6 — Integrated staff report.** Combine the three outputs into a single staff report with clear section attribution and a consolidated options/recommendation section. The staff report should note where inputs were reconciled and where a conflict was escalated to council.

### Key cautions for this example
- The findings language (legal section) must be attorney-reviewed before it is placed in an agenda packet. AI-drafted findings that are legally insufficient create appeal vulnerability.
- The infrastructure assessment must be confirmed by actual utility capacity data, not AI-drafted estimates. Attach the actual capacity reports.
- The development agreement section requires attorney review for enforceability — AI can identify missing provisions, not certify legal sufficiency.

---

## Example B: Budget Adoption — Finance, Manager, and Council

### Scenario
The annual budget process is in its final month. The Finance Director has prepared the proposed budget document. The City Manager needs to write the transmittal letter, prepare a council briefing, and anticipate amendments. The council is scheduled to hold a public hearing and adopt the budget in 18 days.

### Agent lineup

| Agent | Task | Output |
|---|---|---|
| `finance-director-budget-officer` | Budget analysis, assumption documentation, revenue and expenditure summaries | Budget narrative sections; variance from prior year; fund balance analysis |
| `city-manager` | Transmittal letter, priority framing, council briefing | Manager transmittal letter; work session briefing framework |
| `councilmember` (optional) | Anticipate council questions and potential amendment scenarios | Q&A brief; potential amendment issue list |

### Skill lineup

| Skill | Used by | Purpose |
|---|---|---|
| `budget-variance-analysis` | Finance director agent | Year-over-year comparison, structural vs. one-time analysis |
| `revenue-forecast-scenario` | Finance director agent | Conservative/base/optimistic revenue scenarios for sensitivity |
| `kpi-dashboard-narrative` | City manager agent | Priority narrative connecting budget to council priorities |
| `council-meeting-brief` | City manager agent | Work session briefing structure |

### Workflow sequence

**Step 1 — Finance analysis first.** Run the finance director agent to produce the budget analytical narrative: revenue assumptions, expenditure drivers, fund balance impact, reserves position, and any structural imbalances. This is the factual foundation.

**Step 2 — Manager transmittal from finance output.** Attach the finance analysis to the city manager agent. Ask for a transmittal letter that: connects the budget to council-adopted strategic priorities, explains the key decisions made in the proposed budget, identifies the two or three items most likely to generate council discussion, and commits to the public hearing schedule.

**Step 3 — Anticipate council amendments (optional).** Run the councilmember agent against the proposed budget with the instruction: "You are a council member reviewing this proposed budget for the first time. What questions do you have? What are the two or three most likely amendment proposals?" This provides the City Manager and Finance Director with a preview of the council work session dynamic.

**Step 4 — Reconcile conflicts.** The most common conflict in this workflow: the finance director's transmittal is technically accurate but dry; the city manager wants a more accessible, priorities-focused narrative. The reconciliation step is: take the technical accuracy of the finance output and wrap it in the strategic framing of the manager output. Neither agent alone produces the best transmittal letter — the combination does.

Another common conflict: the finance analysis correctly identifies a structural imbalance (one-time money filling a recurring gap); the manager's transmittal downplays it to avoid a difficult council conversation. The right answer is to surface the imbalance clearly with a recommendation for how to address it — not to smooth it over. AI that is asked to "make the transmittal sound positive" will do so, and that is the wrong ask.

**Step 5 — Integrated budget package.** The final package includes: the manager transmittal letter (manager voice, reviewed by finance); the budget narrative (finance voice, reviewed by manager); the council work session briefing (manager voice, council-accessible); and the public hearing notice (clerk voice, legal requirements confirmed). Each section carries its authorship and review attribution.

### Key cautions for this example
- Verify all dollar figures against the actual budget document before any council distribution. AI will echo what you give it; if your input has a transposition error, the output will too.
- The manager transmittal letter is a political document as well as an administrative one. The AI can draft the structure and language; the City Manager must own the policy choices it reflects.
- Budget adoption is a council action by ordinance or resolution in most jurisdictions. The AI should not be used to characterize the adoption as complete until the formal vote has occurred and the clerk has attested the record.

---

## Example C: HR Investigation — HR, City Attorney, and Manager

### Scenario
A complaint has been filed against a mid-level department director alleging improper conduct toward a subordinate employee. The HR Director needs to open a formal investigation. The City Attorney needs to advise on legal exposure and process. The City Manager needs to know what operational decisions are required (paid leave, interim management, external investigator).

### Agent lineup

| Agent | Task | Output |
|---|---|---|
| `human-resources-risk-director` | Investigation intake, process structure, documentation requirements | Investigation plan; interview guide template; document checklist |
| `city-attorney` | Legal risk assessment, potential liability exposure, process adequacy | Legal risk memo; privilege considerations; settlement posture preliminary |
| `city-manager` | Operational decisions, interim management, communication with department | Decision brief; management action list; council notification assessment |

### Skill lineup

| Skill | Used by | Purpose |
|---|---|---|
| `investigation-intake` | HR director agent | Investigation intake structure, evidence preservation, witness list |
| `labor-employment-issue-scan` | City attorney agent | Employment law exposure, harassment framework, due process |
| `disciplinary-memo-builder` | HR director agent | Structure for documentation if findings lead to action |

### Workflow sequence

**Step 1 — DO NOT input personally identifying information.** Before engaging any AI tool, confirm your city's AI acceptable use policy covers personnel investigations. If it does not, do not use AI for this workflow until a policy is in place. Frame the scenario using role descriptions ("a department director" and "a subordinate employee"), not names, unless the policy specifically authorizes it.

**Step 2 — HR analysis first.** Run the HR director agent to produce an investigation intake: what process is required, what evidence must be preserved, what interviews must be conducted, and in what order. The HR agent also identifies whether this investigation should be conducted internally or by an external investigator.

**Step 3 — Legal risk assessment.** Attach the HR intake plan to the city attorney agent. Ask for: a legal risk memo on the city's exposure (harassment, hostile work environment, wrongful termination risk if action is taken); advice on whether attorney-client privilege covers the investigation; and whether an external investigator is advisable. The attorney's output should label clearly what is the city's legal exposure vs. what is the respondent employee's due process.

**Step 4 — Manager decision brief.** Attach the HR plan and legal assessment to the city manager agent. Ask for a decision brief covering: whether to place the respondent on paid administrative leave during the investigation; how to manage the department in the interim; whether the council should be notified (check charter obligations); and what the communication plan is for the department.

**Step 5 — Reconcile conflicts.** Common conflict in this workflow: HR recommends keeping the respondent in their role during the investigation to preserve normalcy; the city attorney advises that leaving them in place creates hostile work environment risk for the complainant. This is a genuine conflict requiring manager judgment. The AI cannot resolve it — it can only surface it clearly. The manager's decision should be documented.

Another common conflict: the HR agent recommends a specific disciplinary outcome framework; the city attorney flags that the recommended outcome could be challenged as disparate treatment if similarly situated employees were treated differently. This requires review of the actual personnel record — which the AI does not have.

**Step 6 — Preserve all work product.** Every output from this workflow is a litigation-sensitive document. The city attorney should advise on which documents are attorney-client privileged, which are work product, and which are subject to disclosure. Do not circulate this material beyond the attorney-client group without legal guidance.

### Key cautions for this example
- This is the workflow where AI misuse has the most serious consequences. Personnel litigation is expensive and can involve real harm to real people. The "human review required" standard is not optional here.
- The investigation findings must be made by a qualified investigator, not by an AI model. AI assists with structure and process; it does not determine credibility or fact.
- Do not generate a draft disciplinary letter until the investigation is complete and the findings have been reviewed by HR and legal.

---

## General principles for multi-agent workflows

**1. Each agent speaks in its lane.**
Resist the temptation to ask one agent to answer questions that belong to another role. If the planning director is analyzing a rezoning, do not also ask her to provide the legal findings. The discipline of role separation is what makes multi-agent outputs more reliable than single-agent outputs.

**2. The shared context document is the anchor.**
Every agent in a multi-agent workflow should start with the same situational context. This prevents agents from working from inconsistent understandings of the facts. Write the context document before running any agent.

**3. Conflicts are features, not bugs.**
When two agents give conflicting outputs, that is useful information. It means the issue is genuinely complex and the decision-maker needs to make a judgment call. Do not resolve conflicts by having the AI pick one answer — surface them clearly for the human reviewer.

**4. The integrator is a human.**
No AI agent should be asked to "integrate" the outputs of other agents into a final official document without a human assembling and reviewing the integration. The risk is that the integrating model will resolve conflicts silently in ways the human reviewer does not catch.

**5. Attribution matters.**
The final integrated document should note which section reflects which agent's contribution and who reviewed it. This is not bureaucratic overhead — it is the record of accountability that protects the city if the document is later challenged.

**6. One person owns the final output.**
In municipal government, every document has an owner: the staff report belongs to the Planning Director; the legal memo belongs to the City Attorney; the budget transmittal belongs to the City Manager. AI-assisted multi-agent workflows must still end with a named human owner who is responsible for the accuracy and appropriateness of the final product.
