# NGAST-LM — Independent Registration and Evidence Custody Review v0.1

**Standing:** `PUBLIC_PROTOCOL_PROPOSAL_ONLY / REVIEW_INVITED / ROLE_NOT_ACCEPTED / GRANT_UNISSUED / ATTEMPT_NOT_REGISTERED / EXECUTION_NOT_AUTHORIZED / CUSTODY_NOT_ESTABLISHED`  
**Date:** 2026-10-31  
**Scope:** Review of possible independent record retention for `NGAST-LM-IQ-OPEN-SLICE-001`; this document is not an executed custody arrangement or a technology evaluation.

## Purpose and boundaries

This is a proposed arrangement for an external actor to independently retain (1) an exact **pre-execution registration and acknowledgment**, and (2) a **post-execution evidence commitment before examiner disclosure**. The external actor would not thereby endorse a technology, certify test results, approve execution, or act as an independent downstream technical examiner. An independently retained receipt may demonstrate receipt and custody within its stated scope; it does not, by itself, demonstrate authentic execution or completeness of unobserved activity.

No original logs, model outputs, credentials, private paths, restricted artifacts, or examiner conclusions are published here. The public repository and draft PR are **review/coordination surfaces**, not independent custodians or blind compartments.

## Candidate experiment identity (provisional; not yet registered)

| Field | Candidate value |
| --- | --- |
| Experiment | `NGAST-LM-IQ-OPEN-SLICE-001` |
| Method | Reliance v0.2 |
| Proposed method SHA-256 | `402b9f90af22724e94e7923c64fab4329eca6a06eb5a969454de879c07346f27` |
| Subject | CQ-02 wire admission v0.1.2 |
| Proposed subject SHA-256 | `99e9716fc5c60ee6417c161d1b3159ae4a106a2dedffa068adba4e3911cb4775` |
| Track | Open demonstration; no controlled comparator required |
| Source of proposed values | Earlier private protocol design; **actual bytes and authority to disclose must be revalidated before binding** |

The hashes above are **candidate identifiers**, not a claim that any external person has seen the bytes or checked the hashes. Actual registration must bind an exact artifact manifest (filenames or content-addressed names, byte sizes, SHA-256 hashes), method/subject revisions, operator grant identity, budget policy revision, and attempt identity. If any component changes, create a separately identified version and registration. Do not silently amend a prior registered attempt.

## Proposed sequence and timing

1. **Review and role decision.** Prospective registrar/custodian examines this protocol, declares accepted scope, independence limitations and access arrangements, and separately accepts or declines. No role is assigned by this proposal.
2. **Operational grant (separate authorization).** Operator issues an attributable, time-bounded grant binding executor, permitted effects, exact source bytes and a versioned **enforceable numeric resource policy**; include stop conditions and the permitted attempt/retry envelope. This draft does not supply those required operational values.
3. **Pre-execution registration.** Before any authorized attempt starts, the registrar receives the full registration record, checks required fields against the agreed acceptance rule, stores the exact received bytes under independently controlled custody and issues an attributable acknowledgment containing a registrar-generated ID and receipt time in UTC. If no independently retained acknowledgment exists, the executor **must not launch** under this protocol.
4. **Authorized bounded execution.** Executor runs only under the separately issued grant, preserving attempt IDs, retries, null/adverse results, errors, resource use and original evidence bytes. Registrar's acknowledgment is not proof that the launch boundary was enforced; enforcement requires separate observable controls.
5. **Evidence commitment.** After execution and before disclosure of the original conclusions to the blind technical examiner, the separately controlled custodian receives and retains a signed/attributable commitment containing exact manifest and membership, attempt inventory and chronology. Issuing a receipt for a manifest does not imply possession or independent verification of every manifest-referenced byte. Record `MANIFEST_ONLY`, `BYTES_RECEIVED_UNVERIFIED`, or `BYTES_HASH_VERIFIED` explicitly.
6. **Independent blinded examination.** A differently qualified reviewer receives a restricted source/evidence view excluding operator conclusions and prior verdicts, commits a version-anchored examination receipt, then proceeds to reveal/reconciliation.
7. **Human disposition.** Operator separately evaluates registration, custody, examination, omissions, adverse evidence and disagreements. Neither registrar nor reviewer receipt automatically confers admission, integration or approval.

**Intended order:** registrar acknowledgment < execution start < evidence checkpoint < pre-disclosure custody receipt < examiner disclosure < blind-exam receipt < reveal. Where exact order cannot be independently supported, mark `CHRONOLOGY_UNESTABLISHED`. Clock timestamps are recorded claims unless supported by an agreed time authority; timestamps alone do not prove ordering.

## What the registrar/custodian would and would not attest

**In scope if actually performed:** exact bytes received (or manifest identity, distinguished from evidence bytes); attributable sender and receiver record; the receiver's observed receipt time and precision; retained record ID and digests; control of retained copies; retrieval capability; amendments, access changes and exceptions.

**Not in scope without a separate examination:** authorization sufficiency; truth or provenance of the underlying observation; actual execution of all registered attempts; absence of omitted attempts; completeness of all events; effectiveness/correctness/safety of Reliance, CQ-02 or any technology; scientific independence of the technical reviewer; endorsement, publication approval or integration admission.

The registrar may refuse, qualify, or withdraw prospectively, with an attributable record. Previously received records must not silently change.

## Retention, access and independence terms for negotiation

- **Proposed duration:** at least 12 months from the final disposition, subject to written mutual acceptance and any overriding legal/security constraints. No obligation begins until agreement.
- **Storage:** independently administered location under custodian control, separate from the executor's unilateral edit/delete authority. Permission logs, restore/retrieval tests, backup/encryption and breach procedures to be agreed before accepting live evidence.
- **Disclosure:** no public release of restricted evidence; allow reviewable manifest/receipt redaction derivatives only under an explicit disclosure decision, preserving linkage to sealed originals.
- **Changes:** corrections are append-only, preserving originals, supersession links and times; a later corrected record cannot manufacture a pre-execution acknowledgment.
- **Prior collaboration:** disclose the prospective custodian's prior technical feedback/exchanges and any relationships relevant to the particular experiment. Evaluate independence for **custody/control** separately from independence of experimental design, technical assessment, outcome selection and funding. Neither friendship nor prior feedback is automatic disqualification; neither may be hidden or equated with blind technical independence.
- **Separation:** a custodian who previously saw conclusions cannot be counted as a blinded examiner of those conclusions. If the same actor is both registrar and custodian, disclose the concentration of roles and test the relevant controls; do not label it two independent actors.

## Example A: pre-execution registration — illustrative only, NOT ISSUED

```json
{
  "record_type": "PRE_EXECUTION_REGISTRATION",
  "status": "ILLUSTRATIVE_ONLY_NOT_ISSUED",
  "experiment_id": "NGAST-LM-IQ-OPEN-SLICE-001",
  "attempt_id": "<EXACT_ATTEMPT_ID>",
  "method": {"name": "Reliance", "version": "0.2", "sha256": "<REVALIDATED_METHOD_HASH>"},
  "subject": {"name": "CQ-02 wire admission", "version": "0.1.2", "sha256": "<REVALIDATED_SUBJECT_HASH>"},
  "artifact_manifest_sha256": "<MANIFEST_HASH>",
  "operational_grant_id": "<ISSUED_GRANT_ID>",
  "resource_policy_id": "<VERSIONED_ENFORCEABLE_POLICY_ID>",
  "allowed_execution_window_utc": "<START_AND_END>",
  "executor_identity": "<AUTHENTICATED_EXECUTOR>",
  "registrar_identity": "<SEPARATELY_CONTROLLED_REGISTRAR>",
  "created_utc": "<ATTRIBUTABLE_ISSUE_TIME>",
  "retention_terms_id": "<ACCEPTED_TERMS_ID>"
}
```

## Example B: independent registration acknowledgment — illustrative only, NOT ISSUED

```json
{
  "record_type": "REGISTRATION_ACKNOWLEDGMENT",
  "status": "ILLUSTRATIVE_ONLY_NOT_ISSUED",
  "registrar_generated_receipt_id": "<REGISTRAR_RECEIPT_ID>",
  "registration_record_sha256": "<EXACT_RECEIVED_REGISTRATION_BYTES_HASH>",
  "attempt_id": "<EXACT_ATTEMPT_ID>",
  "observed_received_at_utc": "<UTC_WITH_DECLARED_PRECISION>",
  "clock_basis": "<CLOCK_SOURCE_AND_LIMITATIONS>",
  "identity_and_authentication_basis": "<SENDER_AND_REGISTRAR_CHECKS>",
  "independent_retention_location_reference": "<NONPUBLIC_RETRIEVAL_REFERENCE>",
  "accepted_scope": "EXACT_RECORD_RECEIPT_AND_RETENTION_ONLY",
  "acknowledger_attestation": "<ATTRIBUTABLE_SIGNATURE_OR_EQUIVALENT>"
}
```

## Example C: post-execution evidence commitment and receipt — illustrative only, NOT ISSUED

```json
{
  "record_type": "EVIDENCE_COMMITMENT_AND_CUSTODY_RECEIPT",
  "status": "ILLUSTRATIVE_ONLY_NOT_ISSUED",
  "linked_registration_receipt_id": "<REGISTRAR_RECEIPT_ID>",
  "attempt_inventory": ["<ATTEMPT_IDS_INCLUDING_FAILED_OR_UNRESOLVED>"],
  "checkpoint_manifest_sha256": "<COMPLETE_MANIFEST_HASH>",
  "checkpoint_membership": [
    {"path_or_id": "<EVIDENCE_OBJECT_ID>", "size_bytes": "<EXACT_INTEGER>", "sha256": "<HASH>"}
  ],
  "scope_of_actual_custody": "MANIFEST_ONLY | BYTES_RECEIVED_UNVERIFIED | BYTES_HASH_VERIFIED",
  "custodian_received_at_utc": "<UTC_WITH_DECLARED_PRECISION>",
  "examiner_first_disclosure_at_utc": "<INDEPENDENTLY_OBSERVED_OR_UNESTABLISHED>",
  "observed_exceptions": ["<OMISSIONS_OR_UNRESOLVED_CASES>"],
  "custodian_attestation": "<ATTRIBUTABLE_SIGNATURE_OR_EQUIVALENT>"
}
```

These are **templates, not genuine receipts, registration records, or attestations**. No IDs, timestamps or hash placeholders are to be filled with invented values.

## Proposed review questions

1. Does the timing and evidence model prove only what is actually observed?
2. What minimum independent controls are needed to make receipt retention non-substitutable by the executor?
3. Which record kinds must be kept as original bytes versus a signed/hashed manifest?
4. What retention duration and authenticated retrieval procedures are feasible?
5. Do prior technical interactions compromise independence for **custody**, or only for selected evaluation roles? What disclosure is required?
6. What failure cases would force `REGISTRATION_UNESTABLISHED`, `CUSTODY_UNQUALIFIED`, `BLINDNESS_UNESTABLISHED`, or `CHRONOLOGY_UNESTABLISHED`?

## Standing and next step

Invite a review of **this proposal only**. A GitHub star, comment, draft PR review or protocol endorsement does **not** appoint a registrar, create custody, issue a grant or authorize execution. Formal independent custody requires separately accepted role terms, authenticated identities, storage/control verification, source-byte revalidation and an actual pre-execution acknowledgment.

**Desired disposition:** `PROTOCOL_REVIEW_ONLY / INDEPENDENCE_ASSESSMENT_PENDING / CUSTODY_NOT_ESTABLISHED / NO_EXECUTION`.
