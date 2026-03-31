# Multi-Agent Orchestration Protocol

This document defines how to coordinate multiple MayorGPT agents on the same decision or deliverable.
It covers handoff format, output preservation, human review gates, and accountability tracing.

No equivalent published standard exists for municipal multi-agent AI work. This protocol is derived from
enterprise agentic AI architecture research and the specific governance requirements of local government.

---

## Why this protocol exists

When a single agent drafts a staff report, the source of every claim is visible — the agent, the attached
documents, and the human who runs the prompt. When multiple agents contribute (legal, financial, engineering,
managerial), accountability gaps open at the handoff points. If a city attorney's risk assessment is
summarized by the city manager agent before it reaches the council, the council sees only the synthesis,
not the original legal judgment. If that synthesis is wrong, the source of the error is invisible.

Municipal decisions affecting residents' property, employment, benefits, or safety require accountability
that survives a records request, a council inquiry, or a legal challenge. This protocol keeps that
accountability intact.

---

## Core principle

**Preserve specialist outputs before synthesis.**

Every agent in a multi-agent workflow should produce its output as a discrete, saved artifact. The
orchestrating agent synthesizes from those artifacts — it does not replace them. The stack produces
a bundle: specialist outputs plus synthesis, not synthesis alone.

---

## Roles

### Orchestrating agent
The agent that initiates the workflow, assigns work to specialists, and produces the final synthesis.
Typically the **City Manager**, **Mayor**, or **Chief of Staff** agent.

Responsibilities:
- Define the question or deliverable for each specialist
- Attach the relevant source material to each specialist prompt
- Preserve each specialist's output as a discrete document
- Synthesize across specialist outputs without burying dissenting views
- Insert human review gates at the points defined below
- Label the final synthesis clearly as a synthesis, not as the specialist's own conclusion

### Specialist agents
Agents contributing domain expertise: City Attorney, Finance Director, Planning Director, Department
Directors, External Advisors, etc.

Responsibilities:
- Produce output that clearly states its reasoning and sources
- Flag what it cannot assess given the materials attached
- Label conclusions as the specialist's assessment, not as organizational decisions

---

## Standard handoff format

When passing work from one agent to another, use this structure:

```
SPECIALIST CONSULTATION REQUEST
Role: [specialist agent name]
Question: [specific question for this specialist — one question per consultation]
Materials attached: [list every document attached to this prompt]
Prior work product: [attach any prior agent outputs relevant to this specialist's question]
Constraints: [any scope limits, e.g., "assess only the fiscal impact, not the policy merits"]
Output needed by: [deadline or review gate]
```

When receiving specialist output, store it with this label:

```
SPECIALIST OUTPUT — [role] — [date/session]
Question addressed: [restate the question]
Conclusion: [the specialist's finding in one or two sentences]
Basis: [the documents and reasoning behind the conclusion]
Cannot assess: [what the specialist flagged as outside its scope or requiring further information]
Review required: [any flagged items requiring human expert sign-off]
```

---

## Output bundle format

A completed multi-agent workflow should produce an output bundle containing:

1. **Synthesis document** — the orchestrating agent's integrated recommendation or draft, clearly labeled
   as a synthesis of specialist inputs
2. **Specialist outputs** — each specialist's discrete output, preserved in full, labeled as described above
3. **Disagreement log** — if specialist outputs conflict, the synthesis must name the conflict explicitly
   and state how it was resolved, rather than silently adopting one view
4. **Human review record** — a brief note of who reviewed each component, when, and what changes were made

This bundle, not just the synthesis, is what goes into the city's records.

---

## Human review gates

The following gates are mandatory. The workflow must stop at each gate until a qualified human has reviewed
and approved continuation.

### Gate 1: Specialist assignment review
**When:** Before any specialist prompt is run
**Reviewer:** The person responsible for the final decision (CM, Mayor, project lead)
**What to review:** Is the question framed correctly? Are the right specialists involved? Is the source
material complete?

### Gate 2: Specialist output review
**When:** Before any specialist output is passed to another agent or incorporated into synthesis
**Reviewer:** A human with sufficient expertise to evaluate the specialist's domain
**What to review:** Is the specialist's conclusion plausible? Does it flag the right risks? Is there
anything the specialist missed?

### Gate 3: Synthesis review
**When:** Before the synthesis document is used for any official purpose
**Reviewer:** The responsible official (CM, Mayor, or Council member, depending on the action)
**What to review:** Does the synthesis accurately represent each specialist's input? Are disagreements
named, not buried? Does the synthesis stay within what the source materials support?

### Gate 4: Official use sign-off
**When:** Before any multi-agent output becomes an official record, public communication, legal document,
or basis for an adverse decision
**Reviewer:** Varies by output type — see `docs/safety-and-governance.md`
**What to review:** Has every required domain expert (attorney, finance officer, etc.) actually reviewed
the relevant section, not just the synthesis?

**Rule:** No multi-agent synthesis may substitute for a specialist's direct review when the relevant
subject matter requires professional sign-off. A synthesis of the city attorney's risk assessment is
not the same as the city attorney reviewing the final document.

---

## Accountability trace

For any multi-agent workflow that produces an official record, maintain this trace:

```
ACCOUNTABILITY TRACE
Decision or deliverable: [description]
Date: [date]
Orchestrating agent: [agent name]
Specialist agents used: [list]
Source documents attached: [list each document, version/date]
Specialist outputs preserved: [yes/no — file location]
Human review — Gate 1: [reviewer name, date]
Human review — Gate 2: [reviewer name(s), date, any revisions]
Human review — Gate 3: [reviewer name, date, any revisions]
Human review — Gate 4: [reviewer name, date, sign-off]
Final output location: [file path or record system reference]
```

This trace is a public record. It should be retained according to the same schedule as the deliverable
it supports.

---

## Handling disagreements between specialists

When specialist outputs conflict — for example, the City Attorney flags legal risk on an action the
Finance Director recommends for fiscal reasons — the synthesis must:

1. **Name the conflict explicitly.** Do not average, minimize, or select one view without acknowledgment.
2. **Present both positions in full.** Each specialist's reasoning should appear in the synthesis, not
   just the conclusion adopted.
3. **Frame the decision for the human.** The synthesis should state clearly: "This is a judgment call
   that requires human decision-making. The legal risk is X. The fiscal case is Y. The decision is
   yours, not the AI's."
4. **Escalate as needed.** If the conflict is between legal risk and operational need, the city attorney
   and city manager should confer directly — not through the AI synthesis.

---

## Highest-risk configurations

### Legal synthesis without direct attorney review
**Risk:** The city attorney agent's output is a drafting aid, not legal advice. Synthesizing it through
a city manager agent before the council sees it can obscure legal risk or give the impression of legal
clearance where none exists.
**Mitigation:** Gate 4 requires the city attorney — the person, not the agent — to review any legal
section in the final document.

### Procurement evaluation with AI assistance
**Risk:** Specialist agents evaluating vendor proposals may encode bias toward particular approaches,
and the AI tool itself may have commercial relationships with vendors being evaluated.
**Mitigation:** The procurement-bid-evaluator skill governs this workflow. The conflict-of-interest
check must be run before any AI-assisted evaluation begins.

### Personnel and disciplinary matters
**Risk:** Multi-agent synthesis of HR and legal agent outputs can produce a disciplinary document that
appears authoritative but was never actually reviewed at the claim level by HR and legal.
**Mitigation:** The disciplinary-memo-builder skill governs this workflow. Gate 4 requires HR director
and city attorney review of the final document against original incident documentation, not just the
AI synthesis.

### Emergency operations
**Risk:** Under time pressure, review gates get skipped. The orchestrating agent's synthesis of an
emergency incident brief can become a public statement before anyone has verified the underlying facts.
**Mitigation:** Even under pressure, Gate 4 for public communications requires PIO sign-off on every
factual claim. Confirmed facts and preliminary reports must remain labeled separately throughout the
workflow — never merged.

---

## Worked examples

See `docs/multi-agent-guide.md` for three fully worked multi-agent examples:
- Complex rezoning (legal + planning + engineering)
- Budget adoption (finance + manager + council)
- HR investigation (HR + attorney + manager)

Each example follows this protocol.

---

## Relationship to stacks

Each stack in `stacks/` defines which agents to combine and in what sequence. This protocol defines
how those agents should hand off work, preserve outputs, and route through human review. The stack
tells you who; the protocol tells you how.

When building a new stack or adapting an existing one, check that:
- Every specialist in the stack has a defined question and output format
- Every Gate applies to the workflow
- The accountability trace is included in the stack's sequence
