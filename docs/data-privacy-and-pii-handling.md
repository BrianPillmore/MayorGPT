# Data Privacy, PII, and CJIS Handling with AI

This guide helps cities decide what information may and may not be entered into an AI tool. It is a practical starting point, not legal advice. Privacy, public records, and criminal justice information rules vary by state and by agreement; your City Attorney and IT or security lead decide what applies in your city.

Related: `safety-and-governance.md`, `small-city-guide.md`, `ai-procurement-and-records-retention.md`, and the skill `skills/people/ai-acceptable-use-policy/SKILL.md`.

---

## 1. The core rule

Do not put information into an AI tool unless your city has approved that tool for that category of information. Approval depends on the tool's contract terms (data use, retention, security), not on how helpful the tool is. When in doubt, use fictional or redacted data, or do not use AI for that step.

## 2. Data categories and default handling

| Category | Examples | Default for unapproved or consumer tools | Default for city-approved enterprise tools |
|---|---|---|---|
| Public | Adopted budgets, posted agendas, published reports | Allowed | Allowed |
| Internal, not sensitive | Draft staff memos without personal data, internal schedules | Redact first; prefer approved tool | Allowed with review |
| Personally identifiable information (PII) | Names with addresses, phone numbers, account numbers, birthdates, ID numbers, case numbers tied to a person | Do not enter | Only if the contract and your policy allow; minimize and redact |
| Sensitive personal information | Medical, immigration, disability, financial hardship, student records | Do not enter | Only with explicit legal review and policy authorization |
| Personnel records | Discipline, investigations, evaluations, medical leave | Do not enter | Use position-level descriptions or fictionalized facts; HR and City Attorney authorize anything else |
| Privileged or confidential legal material | Attorney-client communications, litigation strategy, settlement positions | Do not enter | Only with City Attorney approval and a contract that protects confidentiality |
| Criminal justice information (including CJIS-governed data) | Criminal history, certain database returns, driver or vehicle data obtained through law enforcement systems | Never enter | Never enter unless the Police Chief, the CJIS Systems Officer (or equivalent), and the vendor confirm in writing that the tool meets applicable security requirements |
| Security-sensitive | Passwords, network diagrams, critical infrastructure vulnerabilities, emergency plan details that are exempt from disclosure | Never enter | Never enter unless IT security approves |
| Procurement in progress | Sealed bids, evaluator notes | Do not enter | Only with Procurement Administrator authorization |
| Minors' information | Youth program rosters, juvenile case data | Do not enter | Do not enter without legal review |

## 3. CJIS and law enforcement information

Criminal justice information is governed by the FBI Criminal Justice Information Services Security Policy and by your state's CJIS agency and policies. Obligations include access control, personnel screening, security requirements for any system that stores or processes the data, and agreements with vendors who touch it. Do not assume a general-purpose AI tool meets those obligations. Treat the following as default-prohibited:

- Entering CJI, including criminal history, query returns, or case narratives containing identifiable CJI, into an AI tool.
- Using AI to summarize call-for-service or report data that contains CJI unless the system has been formally approved by your CJIS Systems Officer or state CJIS agency.

Permitted uses are typically limited to non-CJI tasks, such as drafting a general community newsletter, building a training outline, or analyzing aggregate and de-identified statistics. Confirm with your state CJIS agency and Police Chief. State and local policies may be stricter than the federal policy.

## 4. Other regimes that may apply

These regimes often apply to part of city operations. Whether they apply to you depends on your functions and your state; this list is not complete.

- Health information (for example, programs or clinics that are covered entities, or EMS billing).
- Education records (for example, youth programs run with schools).
- Payment card data (utility and recreation payments).
- Driver and vehicle record protections.
- State privacy and breach-notification laws, and state public records exemptions for personnel, security, and law enforcement records.
- Library patron confidentiality statutes in many states.
- Tax and utility account confidentiality.

Flag these to the City Attorney and map each to an AI do-not-enter rule in your acceptable use policy.

## 5. Minimize, redact, and fictionalize

1. **Minimize**: Provide only what the task needs.
2. **Redact**: Replace names, addresses, and identifiers with role labels or placeholders (Resident A, Parcel 1). Keep a separate key outside the AI tool if you must reattach details.
3. **Aggregate**: Use counts and ranges instead of individual records.
4. **Fictionalize**: For skill testing and training, use scenarios like those in `../examples/`.
5. **Check re-identification risk**: Small cities and rare facts can identify a person even when the name is removed.

## 6. Account and tool rules

- Use city-managed accounts. Avoid personal or free-tier accounts for city work.
- Turn on available enterprise protections (no training on city data, administrative controls, audit logs) and verify them in the contract, not just the marketing page.
- Do not upload files from shared drives that contain mixed-sensitivity folders; select documents deliberately.
- Disable or avoid tools that record meetings or capture screens unless the legal basis, notice, and retention are settled.

## 7. If something goes wrong

If sensitive data is entered into an unapproved tool:
1. Stop and screenshot or record what was entered, where, and when (do not paste it elsewhere).
2. Notify the supervisor, IT or security lead, and City Attorney promptly.
3. Follow your incident response and any breach-notification process; notification timelines and triggers vary by state and by the data involved.
4. Request deletion from the vendor if possible, and document the request.
5. Update training and controls.

## 8. Public records and AI

Prompts and outputs about city business may be public records. See `ai-procurement-and-records-retention.md`. Do not assume a prompt is private because it was typed into a chat window.

## 9. Quick staff card

- If it names a person, it probably should not go in.
- If it came from a police system, it never goes in without written approval.
- If it is a personnel or legal matter, ask first.
- If you are unsure, redact or ask.
