---
name: public-comment-summarizer
description: Synthesize hearing or meeting comments into themes, misconceptions, unanswered questions, and response options.
argument-hint: [meeting-topic]
---

# Public Comment Summarizer

**Purpose:** Convert raw comments into an honest, usable summary for decision makers, while preserving the official record. A summary never replaces the underlying comments, which must stay in the record.

## Required inputs
- All comment sources: oral testimony (recordings/minutes), emails, web forms, letters, petitions, survey responses, social comments if included
- The question the body is deciding and the adopted criteria (if quasi-judicial)
- Comment period dates; identifying fields (address, ward, role) if collected

## Workflow
1. **Inventory and de-duplicate.** Count unique commenters, form letters, and petitions separately. Record the timing of each comment against the deadline.
2. **Code each comment** by position (support / oppose / mixed / question) and by theme (traffic, cost, safety, equity, environment, process, property values, design, and others emerging). Allow multi-coding.
3. **Report counts with caution.** Public comment is self-selected and not a poll. State this, avoid percentages implying representativeness, and show who is and is not heard (renters, non-English speakers, young people); compare commenter geography to affected area where possible.
4. **Extract substance**: specific facts, data, alternatives, and conditions proposed. For quasi-judicial matters, separate comments relevant to the adopted criteria from comments about general preference; tell the decision maker which are record evidence.
5. **Flag misconceptions** with the correct, sourced fact and a suggested neutral response (feeds `faq-builder`).
6. **List unanswered questions** and owner/answer-by date.
7. **Present representative quotes** (short, accurate, attributed per policy; avoid exposing private details).
8. **Offer response options**: modify the proposal, add a condition, extend the comment period, hold a second session, publish a response memo, or no change with reasons.
9. **Document** how comments were considered; keep the raw set and the summary together under records retention.

## Output structure
- Method and counts, with caveats
- Top themes ranked by frequency and by consequence
- Position map by area/group
- Misconceptions and answers
- Unanswered questions
- Recommended responses

## Example
> Theme: "Traffic safety on Elm" (41 of 128 comments; 9 offered specific data). Misconception: "The plan removes all parking" - the plan removes 12 of 140 spaces (staff report p.6).

## Red flags / escalate to the city attorney
- Comments containing threats, personal data, or claims against the city
- Late comments in a closed-record quasi-judicial hearing
- Potential evidence of bias or ex parte communication by a decision maker

## Common mistakes
- Treating volume as consensus
- Omitting minority views
- Dropping comments that criticize staff or officials (viewpoint neutrality)

*Not legal advice.*
