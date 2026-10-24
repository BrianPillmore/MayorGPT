# Cross-Model Evaluation

How to run the same municipal task on two or more models and compare the results fairly using the rubrics in
`../evals/`. This builds on `../evals/eval-runbook.md`. Use fictional scenarios only; never test with real
resident, personnel, or CJIS data.

## What you need

- Two or more candidate models or deployment options.
- A small set of fictional scenarios drawn from the repo's `../examples/`, covering low-risk and high-risk work.
- The matching agent and prompt files, and a context pack (the sample pack works).
- The relevant rubrics in `../evals/` (for example agenda packet, financial analysis, legal analysis, public-facing writing).
- Two or three reviewers who know the work, ideally from different roles (clerk, finance, communications).

## Step 1: Fix the inputs

For each scenario, freeze the exact agent text, prompt text, context pack, and attachments. Every model
receives identical content. If a model needs a format change (for example no system field), make the
smallest change that is needed and note it.

## Step 2: Run

- Start a fresh conversation per scenario per model.
- Use default settings unless you are testing settings deliberately; record any you change.
- Run each scenario at least twice per model to see consistency.
- Save raw outputs with the model name, plan or deployment, date, and settings in a log kept outside the outputs.

## Step 3: Blind the outputs

1. A coordinator who will not score removes all model names, product references, and formatting that reveals the source.
2. Assign each output a random code (A, B, C...) per scenario, shuffle order, and keep the key sealed.
3. If style makes a source obvious, note it; do not guess aloud.

## Step 4: Score

Each reviewer scores independently with the rubric for that task, before any discussion. Score:
- accuracy against the source (check every number and citation),
- process and review gates surfaced (legal, fiscal, HR, procurement, public process),
- completeness, including the missing-information list,
- tone and plain-language quality,
- format adherence.

Record any hard failure separately (fabricated citation, wrong figure, missed required referral). A hard
failure on a high-risk task should weigh more than any average.

## Step 5: Unblind and compare

- Combine scores per model and per task type; look at the spread between reviewers.
- Review disagreements together using the blinded text.
- Open the key and tabulate. Compare consistency across repeat runs.
- Add non-quality factors: cost, speed, ease of use, and the governance checklist in `choosing-a-model.md`.

## Step 6: Decide and document

Record which models are approved for which task types, the evidence, the reviewers, the date, and when you
will re-test (at least when the model, plan, or version changes). A model can be approved for low-risk
drafting and not for high-risk work. Human review still applies to every official output.

## Tips

- Keep the sample small and the scenarios realistic; five good scenarios beat twenty vague ones.
- Do not tune the prompt for one model during the comparison; if you must, rerun all models.
- Include at least one trap scenario with missing information to see whether the model says so or guesses.
- Report results as observations on your tasks, not as general claims about a vendor.
