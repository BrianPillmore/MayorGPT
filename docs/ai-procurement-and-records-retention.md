# Procuring AI Tools and Retaining Prompts and Outputs

Guidance for cities buying or approving AI tools, and for handling the records they create. This is practical guidance, not legal advice. Procurement law, public records law, and retention schedules vary by state and by city; the City Attorney and Clerk control the answers.

Related: `data-privacy-and-pii-handling.md`, `safety-and-governance.md`, `../skills/data-and-research/ai-records-retention/SKILL.md`, `../skills/people/ai-acceptable-use-policy/SKILL.md`, and `../skills/data-and-research/vendor-proposal-scorecard/SKILL.md`.

---

## Part 1: Procurement of AI

### Before you buy
1. Define the problem and the workflows, not the technology.
2. Inventory existing tools already licensed (productivity suites often include AI features).
3. Decide who owns the tool: IT, department, or Clerk.
4. Confirm the procurement path required for the cost and type of purchase under your city code and state law. Cooperative purchasing may be available, but confirm its terms and your authority to use it.
5. Run the conflict-of-interest check before any AI-assisted evaluation (see `../stacks/ORCHESTRATION_PROTOCOL.md`).

### Vendor questions
Ask every vendor in writing and keep the answers with the procurement file.

**Data and privacy**
- Is city data used to train or improve models, now or later? Can that be contractually prohibited?
- Where is data stored and processed? Are subprocessors used? Can we get a list and notice of changes?
- What is the retention period for prompts, outputs, uploaded files, and logs? Can the city set or reduce it? Can the city delete on demand?
- Is data encrypted in transit and at rest? What access controls and audit logs exist?
- What happens to data at contract end? Describe return and certified deletion.
- Does the product meet any criminal justice information requirements, if relevant? Will the vendor sign the agreements your state CJIS agency requires?

**Public records and legal**
- Can the city export all prompts, outputs, and metadata in a usable format for public records requests and litigation holds?
- Can the vendor suspend deletion on a litigation hold instruction?
- How does the vendor respond to subpoenas or government requests for city data? Will it notify the city first where lawful?
- Indemnification for intellectual property claims arising from outputs? Limits of liability?
- Does the vendor accept your state's required contract terms (public records, non-appropriation, governing law)?

**Security and accountability**
- Independent security attestations or audit reports available (describe which ones)?
- Incident notification timeline and process?
- Model change notice: how will the vendor notify us of material model or feature changes?
- Human oversight: what features support review, logging, and disabling?

**Accessibility and language**
- Accessibility conformance documentation for the interface and generated content?
- Language support and known limitations?

**Performance and bias**
- Known limitations, documented evaluation results, and hallucination controls?
- Any use in decisions about people (benefits, enforcement, hiring)? If so, what bias testing and appeal mechanisms exist? Many cities prohibit automated decision-making without human review.

**Commercial**
- Total cost of ownership, usage-based charges, and renewal escalators?
- Exit terms, data portability, and no lock-in?

### Contract terms to request
Data ownership by the city; no training on city data; deletion and return; records export; litigation hold support; breach notice; subprocessor controls; audit rights; accessibility obligations; non-appropriation clause; termination for convenience. The City Attorney finalizes language.

### Evaluation
Use `../evals/eval-runbook.md` to pilot candidate tools on fictional or redacted test cases before purchase.

### Governance after purchase
- Name an owner and a review cycle.
- Train users on the acceptable use policy.
- Review use annually (`../prompts/annual/ai-governance-refresh.md`).

---

## Part 2: Records retention of prompts and outputs

### Principles
1. **Retention follows content and function, not the tool.** A staff report drafted with AI has the same retention as one drafted by hand. Apply your retention schedule to the record's content.
2. **Prompts and outputs may themselves be public records.** Guidance from state archives varies; some treat prompts and outputs relating to government business as records. Ask your state archives or records agency and the City Attorney. Do not assume a chat history is exempt.
3. **Final versions and drafts.** Many cities retain final, official versions and treat transitory drafts under existing transitory-record rules. Whether AI prompts and intermediate outputs are transitory depends on your state schedule. Document your city's rule.
4. **Litigation holds and open records requests override normal disposition.** If a hold applies, preserve AI prompts, outputs, and logs for the matter.
5. **Vendor-held records remain city records** if they relate to city business. The contract must give the city access.

### What to capture
For AI use that contributes to an official record or decision:
- The final output used
- The prompt or instruction and the source materials attached, or a reference to them
- Tool name and approximate date
- Reviewer name and changes made (see the accountability trace in `../stacks/ORCHESTRATION_PROTOCOL.md`)

### Practical setup
- Prefer tools with exportable history and administrative retention controls.
- Save the final output in your official records system; do not rely on the chat window as the record.
- Establish a naming convention (matter, date, version).
- Include AI in your retention schedule mapping (use `ai-records-retention` and `records-retention-mapper` skills).
- Train staff not to delete chat history on personal initiative when it relates to open matters.
- Review how your public records request process searches AI tool data.

### Disclosure notes
Some states and cities require disclosure when AI is used in certain public communications or decisions. Check your state and local requirements and your own policy. Do not invent a disclosure rule; ask the City Attorney.

### Checklist
- [ ] AI tool inventory exists
- [ ] Each tool mapped to a retention category
- [ ] Contract allows export and hold
- [ ] Staff know where to save final records
- [ ] Records request process includes AI sources
- [ ] Annual review scheduled
