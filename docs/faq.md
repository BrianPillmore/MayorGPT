# Frequently Asked Questions

Practical answers to the questions city staff, elected officials, and consultants most commonly ask about using AI in municipal work.

---

## 1. What can AI actually do well in a city government context?

AI is strongest at tasks that are structurally complex but text-based and procedurally defined. It excels at:

- drafting staff reports, memos, ordinances, and resolutions from source materials you attach,
- organizing a complex situation into decision-ready buckets: facts, options, risks, recommended next steps,
- surfacing criteria, checklist items, and process steps that humans under deadline pressure sometimes miss,
- translating dense technical or legal content into plain language for elected officials or the public,
- building first drafts under time pressure that give a reviewer a structured starting point rather than a blank page,
- running consistency checks (does this ordinance conflict with a charter provision? does this budget line match the adopted figure?),
- synthesizing a large volume of public comments or survey responses into themes and patterns.

AI is not good at: knowing your local political context, confirming facts it was not given, applying state law it does not have access to, signing certifications, replacing licensed professional judgment, or knowing what it does not know (without being prompted to say so explicitly).

---

## 2. What should AI never do in municipal work?

Certain categories of work should not be delegated to AI output without specific, named human review:

- **Legal conclusions.** AI can identify issues and frame analysis, but it cannot practice law. Every AI-assisted legal memo requires attorney review before it is used to advise elected officials or staff.
- **Budget certifications and financial representations.** AI can help build variance analysis and scenario tables, but the Finance Director must verify every number against the general ledger before it is shared with council or the public.
- **Personnel decisions.** Hiring, discipline, and termination have due process and employment law dimensions that require HR and legal oversight. AI can help structure documentation — it should not determine outcomes.
- **Official proclamations and emergency declarations.** These trigger legal authorities under state law. Template assistance is appropriate; the city attorney must review the signed document.
- **Grant compliance certifications.** Federal grant certifications are signed by an authorized official who is personally attesting to compliance. AI cannot certify and humans should not certify based solely on AI output.
- **Public records responses.** Whether a specific document is or is not subject to disclosure requires a legal determination in your jurisdiction. AI can help triage volume, but the records officer and legal counsel make the disclosure decision.

---

## 3. Are AI-generated drafts public records?

Possibly, and the answer depends on your state's open records law and how the drafts were used.

**The general principle:** If an AI-generated draft was used to inform, develop, or produce an official city document or decision, it is likely a public record subject to disclosure under most state public records laws. "Pre-decisional" or "deliberative process" exemptions may apply in some states, but those exemptions have limits and litigation risk.

**Practical guidance:**
- Treat every AI-generated draft that touches an official city matter as a potential public record.
- If the draft influenced a final document, keep a version history.
- Do not use AI drafts to avoid creating a paper trail on a controversial decision. That approach is likely to backfire legally and politically.
- Consult your city attorney on your state's specific law before establishing an AI records policy.
- When in doubt, retain rather than delete. Destruction of public records, including electronic records, can carry serious legal consequences.

---

## 4. What should we tell residents if they ask whether AI was used?

Be straightforward. The default posture should be: AI was used to assist with drafting, and the final product was reviewed and approved by [named staff or official].

A sample disclosure: *"This document was prepared with AI assistance and reviewed by [title] before release."*

Most residents who ask are asking because they want to know if a human being was responsible for the content. The honest answer — yes, a human reviewed and approved it — is both accurate and satisfying. Transparency about AI use builds more trust than silence, especially as AI use in government becomes more widely known.

What residents are more likely to object to is AI being used to make decisions without meaningful human review. Make sure your workflow includes real review, and your disclosure can honestly reflect that.

---

## 5. How do we handle AI errors in official documents?

If an error from an AI draft makes it into an official document that was adopted or released:

1. **Do not silently correct.** Document the error and the correction through your normal amendment, errata, or correction process.
2. **Assess the materiality.** A typographical error in a staff report title is different from an incorrect legal citation in an adopted ordinance. The correction process should match the severity.
3. **For adopted ordinances or resolutions:** Corrections typically require a correcting ordinance or resolution unless the error is purely scrivener's error (a purely ministerial correction of an obvious clerical mistake). The city attorney and city clerk should advise on your jurisdiction's practice.
4. **Preserve the original.** Do not overwrite the original document. The record of what was adopted — error and all — should be preserved.
5. **Brief the City Manager and city attorney.** They need to know. If the error affected a legal right, contract, or budget figure, there may be downstream obligations.

Prevention is cheaper than correction. Establish a named reviewer for every AI-assisted document before it leaves the building.

---

## 6. How do we handle personnel matters with AI?

Personnel matters require special care for three reasons: due process, employment law, and privacy.

**Do not input personally identifying employee information into AI tools** unless your city has an adopted AI use policy that specifically authorizes it, you have assessed the privacy implications under applicable law, and you understand whether the tool stores or trains on input data.

**What AI can appropriately assist with in HR:**
- Drafting general policy language (handbook sections, performance review frameworks, position descriptions)
- Structuring an investigation intake template without case-specific names or details
- Summarizing general legal frameworks (progressive discipline, FLSA, ADA reasonable accommodation)
- Building a disciplinary memo template from general facts, with placeholders for specific findings

**What AI should not do in HR:**
- Make disciplinary or termination recommendations based on case-specific facts
- Draft a specific adverse action letter that names an employee and describes their conduct without attorney and HR review
- Summarize investigation findings in a way that could be disclosed in litigation without privilege review

Every AI-assisted HR document should be reviewed by HR staff and, in anything involving discipline or termination, by the city attorney.

---

## 7. Can AI keep up with changes in state law and local code?

No. AI models have knowledge cutoffs. They do not automatically update when your state legislature amends the open meetings act, your council adopts a new ordinance, or your city charter is amended by voter referendum.

**Practical rule:** Always attach the current, authoritative text of the legal provision you need the AI to apply. Do not ask AI to "know" state law — ask it to analyze the text you have attached.

For jurisdictional questions (what does our state's OMA actually require?), provide the statute. For local questions (what does our code say about RM-2 approval criteria?), attach the code section. AI that has the text in front of it is far more reliable than AI working from memory.

---

## 8. What is a "walking quorum" and how does AI help with open meetings compliance?

A walking quorum is a sequence of individual contacts among a majority of a governing body that collectively constitute deliberation on public business outside of a posted public meeting. Many states' open meetings laws prohibit this even when no single contact involves a quorum.

AI can help by:
- Running a proposed communication scenario through the `open-meeting-risk-check` skill to identify whether the pattern triggers quorum concerns,
- Drafting a council communications policy to prevent future violations,
- Helping the city attorney frame the risk analysis when a complaint has been filed.

AI cannot advise definitively on whether a specific set of communications violated your state's law. That requires a licensed attorney with access to state case law and AG opinions.

---

## 9. How do we manage AI use across multiple staff members?

Without coordination, different staff members will use different tools, different system prompts, and different levels of review discipline. The risks are inconsistent quality, disclosure of sensitive information to third-party AI services, and unclear accountability for errors.

**Minimum governance steps:**
1. Adopt an AI acceptable use policy that defines approved tools, prohibited use cases, and review requirements. The `skills/people/ai-acceptable-use-policy/` skill can help draft one.
2. Designate a named reviewer for each category of AI-assisted document (legal: city attorney; budget: finance director; public communications: PIO or City Manager).
3. Establish a disclosure standard — what gets disclosed on documents, in what form.
4. Train staff on the review expectations, not just the tools. The tool is only as good as the human who reviews the output.

See `docs/safety-and-governance.md` for a more detailed governance checklist.

---

## 10. Can AI be used in a council meeting — for example, to draft a motion on the fly?

It can be used to support preparation, but real-time use during a public meeting requires judgment and caution.

**Appropriate pre-meeting uses:**
- Drafting motion language for review before the meeting
- Building a Q&A brief for the mayor or presiding officer
- Preparing agenda packet summaries and staff report supporting materials

**Real-time meeting use risks:**
- AI output has not been reviewed by counsel, the clerk, or the city manager before it is read into the record
- Motion language that is legally imprecise can create enforcement problems after adoption
- If an AI tool is used and this fact is later disclosed, questions about transparency and process may arise

Best practice: use AI to prepare before the meeting; use reviewed, staff-approved language during the meeting. The city clerk should never use unreviewed AI output to record official motion language in the minutes.

---

## 11. Does using AI change our liability exposure?

Using AI responsibly — as a drafting and analysis tool, with named human reviewers and a real review process — is unlikely to increase liability beyond the baseline of human error. The key is that a human with appropriate authority reviewed and approved the output.

**Where AI can increase exposure:**
- If AI output replaces rather than assists professional judgment (e.g., a legal conclusion is adopted without attorney review)
- If AI is used to create a false appearance of analysis when a real decision was made on other grounds
- If AI-generated errors in adopted documents cause harm and the city cannot show an adequate review process existed

**Where AI can reduce exposure:**
- Structured AI analysis that surfaces checklist items and process steps can prevent procedural errors that create legal vulnerability
- A well-built AI draft that was reviewed by counsel and Finance is a stronger record of due diligence than a rushed human draft that skipped those steps

Document your review process. If an AI-assisted document is later challenged, you want to be able to show exactly who reviewed it, when, and what they confirmed.

---

## 12. How do we know when an AI output is good enough to use?

An AI output is ready for use when:

1. A qualified person who understands the subject matter has read it carefully, not just skimmed it.
2. All factual claims have been verified against primary sources.
3. Legal conclusions have been reviewed by the city attorney.
4. Fiscal figures have been verified against the general ledger or budget documents.
5. Any item labeled "assumption," "pending," or "unconfirmed" in the AI output has been resolved or explicitly flagged in the final document.
6. The document would survive the "newspaper test" — if a journalist obtained it under a public records request, nothing in it would embarrass the city or misrepresent the facts.

The most useful question to ask before releasing an AI-assisted document: *"If someone asked who is responsible for this, could I name that person?"* If yes, the review process is adequate. If the answer is "the AI wrote it," it is not ready.

---

## 13. Can city officials and employees express personal religious beliefs in their official roles?

Yes. Personal religious expression by government employees and elected officials is constitutionally protected, and the legal framework governing this area is affirmatively protective of that expression — not merely tolerant of it.

**The governing cases:**

*Kennedy v. Bremerton School District* (2022, SCOTUS, 6-3) is the controlling framework. The Court expressly abandoned the Lemon test (the three-part analysis from Lemon v. Kurtzman, 1971) for Establishment Clause questions. Courts now apply a historical-practices-and-understandings test. The practical consequence: a government employee's personal, voluntary religious expression does not become an unconstitutional establishment of religion simply because it occurs in a public setting, is visible to others, or happens in the context of official duties. The government cannot suppress private religious expression merely to avoid the appearance of endorsement. As the Court's majority stated, the Constitution "neither mandates nor permits the government to act in a manner that is hostile to religious observance."

*Town of Greece v. Galloway* (2014, SCOTUS, 5-4), building on *Marsh v. Chambers* (1983), holds that opening a public body's meetings with legislative prayer is constitutionally permissible. The practice has a historical tradition extending to the founding of the republic. A mayor or council member opening a city council meeting with prayer is on solid constitutional ground.

**What this means for elected officials:**
A mayor or council member may express personal religious conviction in public remarks and speeches, pray publicly, invoke faith in policy framing, open meetings with a prayer, and participate in community religious events in an official capacity. None of these are Establishment Clause violations under the current Supreme Court framework. The city attorney should advise accordingly — counseling toward how to exercise these rights lawfully, not defaulting to suppression as the "safe" answer.

**What this means for city employees:**
An employee who displays a small religious symbol at their workstation, prays quietly, or expresses a faith-informed view in conversation is exercising constitutionally protected expression. HR policy should not treat this as a liability source or require it to be managed into invisibility. The liability runs in the other direction: suppressing or penalizing protected religious expression creates First Amendment and Title VII exposure for the city.

**The symmetry principle:**
The Establishment Clause requires neutrality between religion and non-religion — not hostility toward religion. A secular philosophy, political conviction, environmental value, or social worldview that informs an official's or employee's public work is on equal constitutional footing with a religious conviction. Any policy that applies heightened scrutiny or special justification requirements to religious expression while accepting equivalent secular expression without question is viewpoint discrimination against religion, not constitutional neutrality.

**Where the actual line is:**
The constraint is coercion — requiring others to participate in religious activity, conditioning city services on religious compliance, or using government power to compel adherence to a specific religion. That is the constitutional line the city must not cross. Personal expression by officials and employees — including visible, public, faith-informed expression — is on the protected side of that line.

**Practical guidance:**
- Opening a city council meeting with a prayer: constitutionally permissible under *Town of Greece*.
- A mayor referencing faith in a public speech or policy statement: protected personal expression under *Kennedy*.
- An employee displaying a religious symbol at their desk or praying before a meeting: protected expression; not an HR matter unless accompanied by actual coercion of coworkers.
- A coworker complaint that a colleague's religious expression makes them uncomfortable: explain the distinction between protected expression and actionable harassment (coercion, conditioning work relationships on religious participation, targeted repeated harassment) — not grounds for disciplining the employee who expressed their faith.
- Consult the city attorney when there is a specific, factual basis for a coercion concern — not simply because religious expression is visible or has generated a complaint.
