# Deployment and Data Options

Where a model runs decides where your data goes. This guide compares the four common deployment options
for city use and lists implications for records retention, public records, and sensitive data. It is
general guidance, not legal advice; have your city attorney and records officer review local rules.
Product features and terms change, so check each vendor's current documentation.

## The four options

### 1. Consumer chat (free or personal accounts)
- Account controlled by the individual, not the city.
- Retention, sharing, and any use of content for training follow consumer terms that the city did not negotiate.
- The city cannot reliably retrieve conversations, apply a hold, or enforce policy.
- **Use for**: public information only, if at all. Do not use personal accounts for government work.

### 2. Enterprise or business tenant
- Account purchased and administered by the city, with admin controls over users, sharing, and retention settings.
- Contract terms can address training use, confidentiality, and data location. Verify them in writing.
- Conversation history may be exportable by administrators, which supports records requests.
- **Use for**: most routine drafting and analysis with non-restricted data, under a written city AI policy.

### 3. Government cloud or government-designated offerings
- Some vendors and cloud providers offer environments built for government compliance programs.
- Availability, scope, and certifications vary by vendor and change over time; confirm with the vendor and your counsel what is actually covered and for which services.
- **Use for**: work needing stronger compliance commitments, after your attorney and security lead agree the offering fits the data class.

### 4. Self-hosted or local models
- Open-weight models run on city-controlled or contracted infrastructure, or on a staff device.
- Data stays within your environment, but the city owns security, patching, access control, logging, and backup.
- Quality and context length depend on model size and hardware; test on your own tasks (`cross-model-evaluation.md`). See `../integrations/local-models/README.md`.
- **Use for**: the most sensitive material when no hosted option is acceptable, if you can operate it safely.

## Records retention and public records

- Prompts, attached documents, and outputs related to city business may be public records or subject to retention schedules, depending on state law and content. Ask your records officer and attorney.
- Decide where official copies live (your records system, not only a vendor's chat history) and who saves them.
- Check whether history can be exported, how long it is kept, whether deletion by users can be prevented, and whether a legal hold can be applied.
- Keep a record of which model and version produced which final work product, as your policy requires.
- Staff should know that a conversation may be requested; write prompts accordingly.

See `ai-procurement-and-records-retention.md` for details.

## Sensitive data

- **PII** (residents, employees): follow `data-privacy-and-pii-handling.md`. Redact or avoid it unless the deployment and contract clearly allow it.
- **CJIS and law-enforcement data**: criminal justice information carries specific handling and agreement requirements. Do not put it into any tool unless your law enforcement agency's CJIS security officer and counsel have confirmed that tool is approved for it.
- **Personnel, privileged, and closed-session material**: keep out of tools that have not been cleared for it.
- **Security-sensitive infrastructure information**: apply your existing handling rules.

Matching data class to deployment option:

| Data class | Consumer | Enterprise tenant | Government cloud | Self-hosted |
|---|---|---|---|---|
| Public information | Not recommended for city use | Generally fine | Fine | Fine |
| Internal drafts | No | Per policy | Per policy | Per policy |
| PII, personnel, privileged | No | Only if terms and policy allow | Only if cleared by counsel | Possible with strong controls |
| CJIS data | No | Only if approved | Only if approved | Only if approved by CJIS authority |

"Per policy" and "if approved" mean your written policy and the responsible officials decide, not the user.

## Vendor question checklist

- [ ] Is customer content used to train models, by default or optionally? Can this be fixed by contract?
- [ ] Where is data stored and processed? Can location be specified?
- [ ] What is the retention period for prompts, files, and outputs? Can the city set or export it?
- [ ] Can administrators export all conversations for records requests and legal holds?
- [ ] Who at the vendor can access content, and under what conditions?
- [ ] What security attestations and audits exist? Provide current reports.
- [ ] Are law enforcement or CJIS-related terms available if needed?
- [ ] How are subcontractors and sub-processors handled and disclosed?
- [ ] What happens to data when the contract ends?
- [ ] How are model changes and retirements communicated?
- [ ] What incident notification commitments exist?
- [ ] Do terms fit public-sector procurement requirements, including public records obligations on the vendor's side?

## Practical path

Start with a city-administered enterprise tenant for non-sensitive work, write the AI policy, train staff,
and add stricter options only for the data classes that need them. Because MayorGPT is portable, you can
use different deployment options for different tasks.
