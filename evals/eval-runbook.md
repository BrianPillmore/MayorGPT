# Eval Runbook: Running Side-by-Side Comparisons

A lightweight method for checking whether a prompt, skill, agent, or model produces better municipal output. No special tooling is needed; a spreadsheet and two reviewers are enough.

## When to run an eval
- Before merging a new or substantially revised skill, prompt, or agent
- When switching AI tools or models (see `docs/model-portability.md`)
- After a governance or policy change
- Periodically on your most-used workflows

## Step 1: Pick a test case
- Use a realistic but fictional or fully redacted scenario. The `examples/` folders have usable inputs.
- Do not use real resident, employee, or confidential data in an unapproved tool (see `docs/data-privacy-and-pii-handling.md`).
- Choose cases of varying difficulty, including one with a trap (a missing attachment, an ambiguous legal question, an unconfirmed fact).

## Step 2: Define the comparison
Pick one variable to change at a time:
- Baseline (a plain request with no MayorGPT files) versus MayorGPT agent/skill
- Version A versus Version B of a skill
- Model X versus Model Y with identical inputs

Keep constant: source attachments, user request wording, and any settings you can control.

## Step 3: Generate outputs
- Run each variant from a fresh session with the same inputs.
- Save each output as a separate file named `case-variant-date`.
- Record the tool, model name or version if shown, and any settings.
- Run each variant at least twice if you can; outputs vary.

## Step 4: Blind the comparison
Remove labels that reveal which variant produced which output. Have the reviewer score outputs labeled only "A" and "B" in random order.

## Step 5: Score with the right rubric
- General: `municipal-output-rubric.md`
- Plus the domain rubric: financial, legal, HR, agenda packet, emergency brief, public-facing writing, procurement and grants, planning and land use, or constituent communications and accessibility.
- Score each criterion 1-5 and write one sentence of evidence per score.
- Apply automatic fail conditions where a rubric lists them.
- Use two reviewers when stakes are high: one domain expert (for example, a finance officer for a financial output) and one generalist. Average scores or discuss differences greater than one point.

## Step 6: Record results
Use a table like this:

| Case | Variant | Reviewer | Criterion scores | Fails | Pass? | Notes |
|---|---|---|---|---|---|---|

Add a short written summary: what improved, what regressed, and any hallucination, invented citation, or role-boundary violation.

## Step 7: Decide
- Prefer the variant that passes with no fail conditions, then the higher scores on the highest-stakes criteria, not the highest average.
- A single hallucinated legal citation or invented figure is a blocking issue regardless of overall score.
- Document the decision, the date, and who made it. Keep the evaluation record per your retention schedule.

## Pitfalls
- **Reviewer bias toward length or confident tone**: Score evidence, not polish.
- **Testing only the happy path**: Include missing-information cases and see whether the output asks for the missing material.
- **Treating a pass as clearance**: A passing score means a safe starting point for human review, never approval for official use.
- **Small samples**: Treat results from one or two cases as indicative only.

## Optional: lightweight regression set
Keep three to five test cases per high-use workflow in a shared folder with their last passing outputs. Rerun them when a skill or model changes and compare scores.
