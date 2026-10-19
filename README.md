# NGAST Research Records

**Independent research catalog — metadata staging plus one published documentation-only report (2026-10-19).**

This repository indexes research objects concerning paired LLM encounters, responsive interaction, evidence-sensitive coordination, and historically versus currently warranted reliance. It distinguishes observed behavior, admissible interpretations, unresolved findings and execution status.

**This repository contains a catalog and bounded study descriptions, not the original event logs or executable model runners. One separately identified documentation-only report is published on Zenodo; its primary experimental evidence remains restricted.** Source archives are retained separately and will be considered for deposit only after individual release gates pass. Metadata SHA-256 digests identify candidate private archives; they are not publicly retrievable here.

## Study records

| Study | What the record establishes | Public evidence standing |
| --- | --- | --- |
| [Open-choice historical encounter](research/objects/NGAST-OPEN-CHOICE-HISTORICAL-001/) | Nine rounds; preserved inactivity and historical examiner framing | Metadata only; evidence not yet disclosed |
| [PAIR-OBS 001](research/objects/NGAST-PAIR-OBS-001/) | 13 fresh rounds, rejected actions, reciprocal drafting after authorization | Metadata only; evidence not yet disclosed |
| [Evidence-sensitive coordination pilot](research/objects/NGAST-EVIDENCE-COORDINATION-PILOT-001/) | Five-arm pilot, one unsupported explicit sandbox use, measurement limitations | Metadata only; evidence not yet disclosed |
| [Evidence-standing diagnostic](research/objects/NGAST-EVIDENCE-STANDING-DIAGNOSTIC-001/) | Strict-parser failure followed by separately versioned complete run; zero measured format benefit under a ceiling | [Zenodo documentation-only report](https://doi.org/10.5281/zenodo.23480962) published; original evidence restricted |

See the machine-readable [research catalog](research/catalog.json), [publication receipt](docs/PUBLIC_RELEASE_RECEIPT_20261019.md), [release gates](docs/RELEASE_GATES.md), [reproducibility boundaries](docs/VERIFICATION.md), and [research-line separation](docs/RELATIONS.md).

## Intended publication chain

Separate preserved object → object-specific disclosure and rights review → DOI-bearing research deposit if authorized → verified ORCID Work association → catalog update. One repository or an internal hash chain is not an independent assertion of truth, permission, software safety or scientific validity.

## Authorship and rights

The documentary report lists Ryan Feller as creator and is published under CC BY 4.0 **for that derivative only**. Model-generated transcripts, source runners, and other third-party material remain **unreleased** pending their separate rights review. That documentary license does not grant any public reuse rights for the restricted original evidence. See [rights and disclosure](docs/RIGHTS_AND_DISCLOSURE.md).

## Verify this repository's metadata

Run `python scripts/verify_catalog.py` (Python 3 standard library). This checks the staged metadata and checksum manifest only. It cannot verify archives withheld from this repository.

## Status and non-claims

- One version-specific Zenodo DOI is displayed for the [published documentation-only report](https://doi.org/10.5281/zenodo.23480962). Publication and public accessibility are supported by an owner-supplied unauthenticated browser screenshot. Independent resolver verification and downloaded-file hash comparison remain open.
- One ORCID Work is visibly listed on the creator’s public profile for the documentation-only diagnostic DOI. This is supported by an owner-provided unsigned-in-browser screenshot; independent ORCID API retrieval is not established. The three other NGAST studies have no ORCID Works confirmed here.
- No Fork-core research release or admission is implied.
- The 100-event historical encounter is **not** a predecessor participant-state record of the 152-event fresh PAIR-OBS lineage.
- This catalog does not establish free will, consciousness, real-world truth, generalized model tendencies, or a beneficial effect of structured handoffs.
