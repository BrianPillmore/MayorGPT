---
name: records-retention-mapper
description: Map city record series to required retention periods, custody locations, sensitivity classifications, and disposition steps — using the state retention schedule, local policy, and any applicable litigation-hold or audit-hold constraints.
argument-hint: [record-series or department]
---

## Purpose
Build or update a department's records inventory and retention map so records are kept as long as the law requires, no longer, and can be found and produced. The state retention schedule governs; a local policy can lengthen but usually cannot shorten required periods.

## Required inputs
- Department record series inventory (name, description, format, system, volume, date range, owner).
- Current state general retention schedule and any department-specific or local schedule; the records officer/clerk.
- Active litigation holds, audits, open public records requests, and grant/contract retention clauses.
- IT systems of record, backup practices, cloud vendors, and email/messaging/text policies.

## Workflow
1. Define each record series by function and content, not by file name or software. Identify duplicates and convenience copies.
2. Match each series to a schedule item. Record the item number, retention period, trigger event (end of fiscal year, contract expiration, case closure, separation, superseded date), and disposition (destroy, transfer to archives, permanent).
3. Identify longer-of rules: federal grant records (generally at least three years after the final financial report under 2 CFR 200.334, longer if audit or litigation is open), bond and debt records, tax records, personnel and medical records (separate files and statutory periods), construction records (statutes of repose), and contract records (statute of limitations).
4. Classify sensitivity: public, confidential by statute (personnel, medical, criminal justice information, attorney-client, certain security plans), or mixed requiring redaction. Record the legal basis for confidentiality and who may access.
5. Custody and format: where the official copy is held, the system of record, whether electronic records are preserved in a usable format over the retention period, and who maintains permanent records (migration plan).
6. Holds and suspensions: list any hold that suspends disposition, scope, and the person who can release it. Disposition requires hold check.
7. Disposition process: approval by department head and records officer, documentation of destruction (certificate/log), secure destruction methods, and the transfer to state archives for permanent items.
8. Identify gaps: series not on the schedule, inconsistent practices, shadow systems, unmanaged email or messaging, and legacy storage. Recommend schedule requests, policy fixes, and training.

## Output structure
| Series | Description | Schedule item | Retention & trigger | Disposition | Custodian/system | Sensitivity | Hold? | Gap |
Add: disposition-ready list for the period, items needing attorney or state archives input, and an action plan. See retention-map-template.md.

## Red flags / escalate
- Destruction in progress while a hold, audit, or public records request is open.
- Series with no schedule item.
- Records in personal accounts or unmanaged systems.
- Confidential data in broadly accessible storage.
- Shortened retention in a local policy that conflicts with state law.
- Loss or unauthorized destruction: city attorney and state archives notification as required.

## Common mistakes
- Treating all email as one series.
- Counting from creation when the trigger is a later event.
- Destroying paper while the electronic version is the official copy (or vice versa) without a decision.
- Not documenting destruction.

## State-law variance
Retention schedules, destruction approval, and confidentiality rules are state-specific; use your state's official schedule.
