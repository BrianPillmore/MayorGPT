# Choosing a Model

MayorGPT works with any capable model, so the choice is yours. This checklist helps a city decide based on
what the work needs and what the city can govern, not on brand. It makes no rankings and no benchmark
claims; capabilities and terms change, so verify each item against the vendor's current documentation and
against your own tests.

## Start with the work

List the tasks you will actually run (agenda packets, budget analysis, constituent replies, ordinance drafts,
procurement review, public-facing writing). The more of these a model must do well, the more of the checklist
below matters.

## Capability checklist

Score each candidate Pass / Partial / Fail on your own test runs.

- [ ] **Instruction following**: keeps the role, tone, and required sections from the agent and prompt.
- [ ] **Context capacity**: fits your typical packet (agent + prompt + context pack + source documents) in one conversation, or you have a staged plan.
- [ ] **Document handling**: reads your real file types (PDF, Word, spreadsheet) correctly, including tables.
- [ ] **Numerical care**: arithmetic and budget tables check out against the source; flags uncertainty.
- [ ] **Citation behavior**: points to where in the source a claim came from, and says "not found" instead of inventing.
- [ ] **Structured output**: holds a requested format reliably (see `model-portability.md`).
- [ ] **Plain-language writing**: public-facing text at the target reading level.
- [ ] **Escalation behavior**: surfaces legal, fiscal, HR, and process review needs instead of smoothing them over.
- [ ] **Refusal behavior**: does not refuse ordinary municipal topics (code enforcement, public safety, personnel process) but declines inappropriate requests.
- [ ] **Consistency**: similar answers on repeated runs of the same task.
- [ ] **Accessibility**: usable with the staff's devices, assistive tools, and languages the city serves.

## Governance checklist

- [ ] Data handling terms fit your city's data classes (see `data-privacy-and-pii-handling.md`).
- [ ] Prompts and outputs can be retained, exported, and produced for public-records requests.
- [ ] Administrators can control accounts, sharing, and retention.
- [ ] The vendor states whether your content is used for training, and the setting can be fixed by contract or admin policy.
- [ ] The deployment option matches the sensitivity of the work (see `deployment-and-data-options.md`).
- [ ] The terms fit procurement rules and the vendor questions in `ai-procurement-and-records-retention.md`.

## Practical criteria

- **Cost model**: per-seat, usage-based, or self-hosted hardware; budget for pilot and steady state.
- **Staff fit**: does the tool work where staff already work (email, documents, chat)?
- **Support and continuity**: what happens if the vendor changes terms or retires a model? Because MayorGPT is portable Markdown, plan to be able to switch.
- **Local capability**: if you may need offline or on-premises use, check whether open-weight options meet your quality bar on your own tests.

## Decision process

1. Pick two or three candidates that pass the governance checklist for your data.
2. Run the same fictional scenarios on each (`cross-model-evaluation.md`).
3. Score with the rubrics in `../evals/`.
4. Choose per task if needed: one model may handle drafting while another or a local one handles sensitive material.
5. Document the decision, who approved it, and when you will re-test.

A smaller or cheaper model is acceptable for low-risk drafting if it passes your tests. Higher-risk work
(legal, personnel, public safety) always needs human review regardless of model.
