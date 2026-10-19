# Release Gate Examination 001 — Evidence Standing Diagnostic 001

Exam date: 2026-10-19. **Decision: TECHNICAL INTAKE PASS; PUBLIC RIGHTS/DEPOSIT HOLD.**

## Technical tests (PASS)

- Original 89,306-byte study archive SHA-256 independently matches recorded digest.
- All 11 contained study files match internal SHA-256 manifest.
- Seven-event strict-parser predecessor verifies and ends `batch_halted`; it is NOT counted as an experimental comparison.
- 283-event post-observation format-repair successor verifies and ends `batch_completed`.
- Repaired software ZIP passes CRC and the extracted offline `unittest discover -s tests` suite returns 16/16 PASS. Tests do not reproduce live-model choices.
- Automated aggregate fields independently counted: 3 conditions × 14 judgments × 5 fields = 210/210 exact matches; no format advantage observed.
- Heuristic filename+byte scan including recursively nested source ZIPs found no matched email addresses, Windows user-home paths, PEM private-key blocks, or common API-key signatures. **Scan does not prove absence of sensitive content or complete disclosure fitness.**

## Open gates — NOT PASSED

1. **G-RIGHTS:** Confirm original source code and research text disclosure rights, including human-authored versus assistant-generated components; assess model/provider terms as applicable. Perplexity API Terms §2.3.1 state customer owns output as between Perplexity and customer, to extent allowed; §2.6 additionally applies third-party model terms. This is relevant but not a comprehensive rights clearance.
2. **G-LICENSE:** Select explicit software license and text/data license(s). The original Fork repository's license, and Zenodo's default CC BY, must not be inherited silently.
3. **G-DISCLOSURE:** Reviewer approve public release of raw model transcripts and provider response IDs (none included in public derivative candidate), or a separately named redaction regime, with disclosure of any loss of recomputability.
4. **G-METADATA:** Confirm creator/ORCID attribution, contribution roles, intended version, title, repository record type and funding/affiliation details if any; do not invent collaborators.
5. **G-IDENTIFIERS:** Search existing DOI/Zenodo deposits for exact duplicate research object, and confirm new identifier only after clear-rights draft review.
6. **G-INDEPENDENCE:** Mark verifier as local examiner recomputation of copies; provider response identifiers and self-consistent hashes do not authenticate model identity or source provenance.

## Item classifications

- **Retain unchanged, controlled copy:** original event ledgers, reports with individual model text, source ZIPs, original manifests, provider metadata; never re-seal or silently rewrite.
- **Draft public derivative candidate (not yet licensed/published):** examiner-produced bounded README, preregistration, repair note, original digests, derived aggregate verification; no raw event strings or executable code.
- **Future reproducibility deposit:** original complete artifact only after rights and disclosure clearance, or named partial derivative with an explicit dependency to controlled original bytes.

## Exact bounded scientific claim

Both model endpoints matched all five assigned synthetic classification fields in all 42 second-stage judgments in a post-observation format-repaired run. No performance difference was observed among three presentation conditions, with ceiling effects and explicitly directed reasoning. Not evidence of actual downstream authorization reliability or improvement by structured handoffs.

## Decision rule

No public full-evidence GitHub commit, Zenodo publish, DOI status, license statement, or ORCID-work confirmation follows from this technical PASS alone. A new examiner approval and exact license/rights decision are prerequisites.
