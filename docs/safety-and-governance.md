# Safety, Review, and Governance

MayorGPT should help people work faster. It should **not** become a shortcut around public process,
legal review, procurement integrity, HR due process, or recordkeeping.

## Always use human review for
- ordinances and resolutions before formal action,
- contracts before execution,
- legal analysis and litigation matters,
- personnel discipline and investigations,
- budget adoption materials,
- emergency proclamations and public safety releases,
- election-related materials,
- public records responses,
- grant certifications and compliance statements.

## Review questions
1. Does this draft accurately reflect the city's authority?
2. Does it say what still requires review?
3. Does it preserve public trust if disclosed?
4. Could a resident understand it?
5. Could a clerk, lawyer, finance officer, or manager act on it without redoing the whole thing?

## Suggested AI governance controls
- Define approved tools and use cases.
- Require source attachment for official drafts.
- Require human sign-off for public release.
- Treat AI-generated drafts as city records when the applicable law or policy requires it.
- Keep version history when drafts influence official action.

---

## Highest-risk use cases and why

Some uses of AI in municipal government carry substantially higher risk than others. These warrant the most stringent review requirements.

### Personnel actions
Hiring, discipline, and termination decisions involve due process rights, employment law, potential discrimination claims, and union contract obligations. AI that influences a personnel outcome without adequate HR and legal review can expose the city to wrongful termination claims, civil rights liability, and grievance arbitrations. **Never use AI output to determine a personnel outcome.** Use it only to assist with structure, documentation templates, and general policy drafting — with named HR and legal review before any action is taken.

Note on religious expression in the personnel context: employee religious expression — displaying a religious symbol at a workstation, praying quietly, expressing a faith-informed view in conversation — is constitutionally protected personal expression under *Kennedy v. Bremerton School District* (2022) and Title VII. It is not a source of employer liability simply because it is visible to others or because a coworker is uncomfortable. The liability runs in the other direction: suppressing, penalizing, or requiring justification for protected religious expression creates First Amendment and Title VII exposure. HR review of a religious expression situation should begin by distinguishing protected expression (which requires no city action against the employee) from actual coercion (pressuring coworkers to adopt a faith, conditioning work relationships on religious participation, targeted harassment of a specific individual after they have asked it to stop) — which is the threshold that triggers adverse action. See the `skills/people/religious-accommodation-guide/` skill for the full framework.

### Legal conclusions in official documents
When a legal conclusion appears in an adopted ordinance, resolution, or finding — and that conclusion was AI-generated and not reviewed by the city attorney — the city has created a record of inadequate legal process. Opposing counsel will find it. Judges notice. **Every legal conclusion in an official document must be reviewed by the city attorney.** This is non-negotiable.

### Emergency declarations and proclamations
Emergency declarations trigger legal authorities under state and federal law and can affect liability, intergovernmental reimbursement, and civil liberties. An AI-drafted proclamation that misstates the legal authority or the triggering conditions can void the declaration. **The city attorney must review every emergency proclamation before the mayor signs it.**

### Election-related materials
Voter guides, election notices, and ballot language are subject to strict legal requirements and high public scrutiny. Errors can disenfranchise voters or invalidate elections. AI can assist with drafting, but every election-related document must be reviewed by the city attorney and the city clerk against applicable state election law.

### Financial representations to bond markets or federal agencies
Continuing disclosure documents, CAFR narratives, and grant compliance certifications that contain AI-generated content without adequate financial officer verification can create liability under federal securities law and grant regulations. **The Finance Director and city attorney must review any financial representation before it is released.**

### Public safety communications
Incorrect or premature public safety information during an emergency (wrong shelter location, incorrect injury count, unverified evacuation order) can directly harm residents. Public safety releases must be verified against field reports and cleared by the Emergency Manager and PIO before release.

---

## Public records and FOIA implications of AI drafts

AI-generated drafts that touch official city business are likely public records in most states. This has practical implications for how you create, store, and describe AI-assisted work.

### What is probably a public record
- An AI-generated draft staff report that was used to develop the final document
- An AI-generated risk memo that was shared with the city attorney
- An AI-generated constituent response letter that was sent
- Prompts you submitted to an AI tool that contained city government information

### What may be exempt from disclosure
- Attorney-client privileged communications (the city attorney's legal advice, including AI-assisted drafts prepared for legal advice purposes)
- Deliberative process documents in states that recognize that exemption
- Personnel records in most states
- Active law enforcement investigative material

### Practical rules
1. **Create with disclosure in mind.** Every AI-assisted document should be written as if it could be requested and disclosed. Do not use AI to create a less-permanent record of a decision — that approach is legally and ethically problematic.
2. **Retain consistently with your records retention schedule.** AI drafts that became the basis for official action should be retained under the same schedule as the official records they supported.
3. **Do not train AI tools on city data without legal review.** Some AI platforms use submitted content to train future models. This may create public records complications or confidentiality risks. Confirm the data practices of any tool you use before submitting city documents.
4. **Consult your city attorney on your state's specific law.** Records exemption doctrine varies significantly by state.

---

## Religious expression by officials and employees — post-Kennedy posture

The legal framework for religious expression in municipal government changed materially with *Kennedy v. Bremerton School District* (2022, SCOTUS). Governance policies, HR protocols, and legal guidance should reflect current law, not the pre-2022 Lemon-test framework.

**The current legal baseline:**
- *Kennedy* (2022) abandoned the Lemon test. Courts now apply a historical-practices-and-understandings framework. A government employee's personal, voluntary religious expression does not become an Establishment Clause violation simply because it occurs in a government setting or is visible to others.
- *Town of Greece v. Galloway* (2014) expressly permits legislative prayer at public body meetings. A city council or board opening its session with prayer is constitutionally permissible.
- The Establishment Clause requires neutrality between religion and non-religion — not hostility toward religion. Treating religious expression as more suspect than equivalent secular expression is viewpoint discrimination against religion, not constitutional neutrality.

**Where the legal risk actually lies:**
The risk that warrants active management is coercion — requiring others to participate in religious activity, conditioning city services on religious compliance, or using government power to compel adherence to a specific religion. The risk does not lie in the expression itself. A governance policy, HR protocol, or legal memo that treats protected religious expression as a primary source of city liability is applying the wrong standard and may itself create legal exposure.

**Practical governance implications:**
- AI-assisted drafts on religious expression topics — guidance memos, accommodation responses, policy language — should be reviewed against the post-Kennedy framework, not against Lemon-era endorsement reasoning.
- HR protocols that single out religious expression for heightened review or restriction, while permitting equivalent secular expression, should be corrected.
- The city attorney is the appropriate reviewer when a specific, factual coercion concern arises. Routine religious expression by employees or officials in the workplace or public settings does not require legal review before it occurs.
- The city's AI governance policy should not treat religious expression guidance as a uniquely high-risk category. Apply the same review discipline you would apply to any other employment or First Amendment question.

---

## What to tell residents if they ask whether AI was used

Transparency is the right posture. The following guidance covers the most common scenarios.

### In a public document or response
Include a brief disclosure when appropriate: *"This document was prepared with AI assistance and reviewed by [title/department] before release."* This is accurate, honest, and increasingly expected by informed residents.

### When asked directly in a public meeting
Respond directly: "Yes, AI tools were used to help draft [X]. The final document was reviewed and approved by [name/title]." Do not be defensive — this is a reasonable question and a straightforward answer builds more trust than hedging.

### When asked about a specific decision
Clarify the distinction between AI as a drafting tool and AI as a decision-maker: "AI assisted with drafting and analysis, but the decision was made by [council / staff / named official] based on [criteria / process]." This is almost always accurate and important to say clearly.

### What not to say
- Do not say "the AI decided" or frame the outcome as AI-driven even colloquially. This confuses residents about who is accountable.
- Do not say AI was not used if it was. If the disclosure is challenged and proven false, the credibility damage is far worse than the original disclosure.

---

## Sample AI governance policy checklist

The following checklist is a starting point for a city adopting a formal AI governance policy. It is not a complete policy — it is a structured list of decisions a city must make. See `skills/people/ai-acceptable-use-policy/` for a full policy drafting workflow.

### Scope and authorization
- [ ] Which AI tools are approved for city use? (List by name or category)
- [ ] Which staff roles are authorized to use AI tools for official city work?
- [ ] What categories of city business are excluded from AI use (e.g., personnel investigations, active litigation)?

### Review and accountability
- [ ] What is the named reviewer for each category of AI-assisted document? (legal: city attorney; fiscal: finance director; public communications: PIO; etc.)
- [ ] What does "reviewed" mean operationally? (Read and approved; verified against source data; redlined and revised?)
- [ ] Is there a sign-off requirement before AI-assisted documents are released or filed?

### Data and privacy
- [ ] What city data may be input into AI tools? (What categories are prohibited — personnel records, active litigation, law enforcement data?)
- [ ] Have you reviewed the data retention and training practices of each approved tool?
- [ ] Does your use of AI comply with applicable state privacy law?

### Public records
- [ ] Are AI-generated drafts that informed official action being retained consistently with your records retention schedule?
- [ ] Has the city attorney opined on the records status of AI-generated working documents in your state?

### Disclosure
- [ ] What is the city's standard disclosure language for AI-assisted documents?
- [ ] Are staff and elected officials trained on how to respond if asked about AI use?

### Training and culture
- [ ] Have key staff (City Manager, City Clerk, City Attorney, Finance Director, PIO) been briefed on AI capabilities, limitations, and the city's use policy?
- [ ] Is there a process for staff to flag AI errors they discover after a document has been released?
- [ ] Is there a process for updating the policy as AI tools and law evolve?

### Review and update
- [ ] When will this policy be reviewed for adequacy? (Recommend annual review at minimum)
- [ ] Who is responsible for monitoring changes in state law and AI technology that affect the policy?
