# Verification boundaries

The private archival packet was assembled with exact copied input files and internal event-chain checks. Four individual study packets and their SHA-256 digests are recorded in each `research/objects/*/metadata.json`; these ZIP files are not distributed here.

What `scripts/verify_catalog.py` establishes:

- exact bytes of this release's included public files versus its checksum list;
- well-formed object identities, references, and internally consistent selected event totals and chain tips;
- no accidental DOI, ORCID Work, license selection or Fork-core admission in the three metadata-only candidate objects; the documentary diagnostic has an explicitly bounded public DOI and observed ORCID association.

It does **not** verify public access to withheld archives, independent provider origin, model identity, experimental causality, source authenticity, privacy/rights clearance, or semantic warrant. Recomputing an already recorded event chain differs from reproducing model responses in fresh runs. The original diagnostic's seven-event format failure and separately repaired 283-event record both remain listed.
