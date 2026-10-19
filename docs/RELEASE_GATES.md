# Object-specific release gates

Publication status for all four research objects is **metadata_staging_only**. Passing the following checks must be recorded per object before issuing or associating a DOI:

1. **Object identity:** exact immutable research object, version, provenance and source membership selected.
2. **Integrity:** every file byte length and SHA-256 checked against authoritative sources; event-chain and audit code examined. Preserve negative predecessors.
3. **Execution standing:** separate model outputs, applied actions, aborted actions, repaired software, offline tests, and experimenter decisions.
4. **Rights:** explicit authorized publication rights for researcher code, model-generated outputs, third-party text, datasets and gateway terms; named license selection.
5. **Disclosure:** manual review of identities, Windows paths, private information, provider metadata, secrets and nested ZIP contents; separately named redaction derivative if needed.
6. **Review:** second-person technical and disclosure review, with reviewer scope and limitations.
7. **Identifier duplicate check:** existing Zenodo, DataCite, GitHub release and ORCID Work lookup for exact research objects.
8. **Deposit:** draft-first, object-specific Zenodo uploads after explicit approval; compare downloaded published bytes to approved hashes.
9. **Attribution:** register the DOI-bearing object in ORCID; independently confirm visibility and identifier relation.
10. **Catalog:** update immutable version details and evidence-backed publication status only after confirmation.

A reproducible checksum is not provider provenance or validated semantic support. There is no aggregate scientific certification or release authorization here.
