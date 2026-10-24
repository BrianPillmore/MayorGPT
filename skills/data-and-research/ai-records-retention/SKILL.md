---
name: ai-records-retention
description: Identify when AI prompts and outputs are public records, apply the correct retention schedule to AI-generated content, and produce a records retention map covering every AI use case in the city.
argument-hint: [list of AI use cases or department]
---

## Purpose
Map each city use of AI tools to the records it creates, the retention rule that applies, where the record lives, and how it would be produced in response to a public records request or litigation hold. The governing principle: retention follows the content and function of the record, not the tool that produced it.

## Required inputs
- List of AI tools and use cases by department, including free-tier, personal, and embedded features (for example copilots inside office suites).
- The state general records retention schedule and the city's local schedule, and records officer/clerk contact.
- Vendor contracts and terms of service: data retention, ownership, deletion, export, and records-production provisions.
- Active litigation holds, open records requests, audits, and grant records obligations.
- Existing AI use policy and training.

## Workflow
1. Inventory each use case: who uses it, with what data, and what is produced (prompt, conversation log, output, edited final).
2. Categorize the record type produced: administrative correspondence; official drafts leading to final action (staff reports, ordinances, notices); legal analysis (privileged); financial records; personnel records; enforcement records; research and policy synthesis; meeting records; transitory or convenience copies.
3. Apply the existing schedule series for that category. A staff report drafted with AI has the same retention as one drafted by hand. Distinguish final records from drafts: many schedules treat transitory drafts as short-retention, but drafts that document decision-making or are subject to a request or hold must be kept.
4. Public-record status of prompts and logs: in many states, prompts and outputs that relate to the conduct of government are public records (Washington State Archives issued guidance on this in 2024; confirm the current text and your own state's position). Flag prompts that reference a specific city matter, resident, employee, or pending decision, contain city data, or were used to develop an official product.
5. Litigation and individual-rights matters: enforcement, discipline, procurement evaluation, and benefit determinations may need AI inputs and outputs preserved as part of the record; apply holds before normal disposition.
6. Vendor access: for each tool, determine whether the vendor retains logs, for how long, whether the city can export them, whether the contract obliges production for public records, and whether employees can retrieve their own history. Check enterprise retention settings in the city's tenant.
7. Personal accounts: official work in personal AI accounts creates records the city cannot control or retrieve; require city-managed accounts.
8. Produce the retention map and gaps list; recommend schedule amendments, contract changes, configuration settings, and training; coordinate with the city attorney and the state archives for ambiguous categories.

## Output structure
| Use case | Tool | Record type | Schedule series | Retention & trigger | Custody (city/vendor) | Retrieval method | Gap |
Add: vendor access table (tool, log retention, contract term, gap), hold/exception list, and action list with owners.

## Red flags / escalate
- Vendor holds logs and the city cannot retrieve them.
- Personal or free-tier accounts used for official work.
- Prompts containing confidential personnel, legal, or CJIS-type data in tools not cleared for that data.
- Uses not covered by any schedule series.
- Active hold or open records request.
- Grant records with longer federal retention than the state schedule (commonly three years from final report or longer under 2 CFR 200.334; verify the award).

## Common mistakes
- Assuming AI output is exempt or "not a record."
- Deleting chat histories on vendor default settings without a records decision.
- Treating the AI summary as the official record.
- Ignoring embedded AI features.

## State-law variance
Public records law, archives guidance on AI, and retention schedules differ by state. Where there is no specific AI guidance, apply general records law by function and consult the city attorney and state archives.
