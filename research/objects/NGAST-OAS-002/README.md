# OAS-002 — When evidence interpretation and decision composition diverge

**NGAST independent research · Bounded empirical findings · October 23, 2026**  
**Researcher:** Ryan Feller · [ORCID 0009-0000-7863-5792](https://orcid.org/0009-0000-7863-5792)  
**Research identity:** `NGAST-OAS-002` · **Public-page version:** `v0.1-review-candidate` · **Page prepared:** 2026-10-24  
**Study disposition:** `COMPLETE_WITHIN_FROZEN_PLAN / SOURCE_AND_RESCORE_PASS / BOUNDED_SEPARATION_ADVANTAGE / METHOD_QUALIFICATION_SEPARATE`  
**Publication disposition:** `DOCUMENTATION_REVIEW_CANDIDATE` — not a merged/admitted research release; no DOI, ORCID Work deposit, or Fork-core admission.  
**Primary evidence:** Retained separately; original execution ZIPs and raw model transcripts are **not distributed** through this page.

> **Core observation:** Under the declared synthetic decision rule, the same underlying evidence can be classified correctly at the component level and still yield an incorrect joint conclusion. A correct final label can also conceal incorrect component classifications.

[Read the aggregate results](#results) · [Failure modes](#what-failed) · [What a reader can and cannot verify](#verification-boundary) · [Architectural implications](#implications-for-evidence-systems) · [Machine-readable summary](results-summary.json)

## Research question

When an AI model classifies multiple evidentiary predicates and derives a joint decision, are **component interpretation** and **decision composition** separable sources of error?

The frozen study compared two paths against the same *declared synthetic* reference rule:

| Path | Decision procedure | Fully correct results |
| --- | --- | ---: |
| **C — Combined** | One model response classifies all three components and supplies the joint label. | **48 / 72 (66.7%)** |
| **E→J — Separated** | An evidence-classification stage supplies three components to a subsequent joint-decision stage. | **67 / 72 (93.1%)** |

These are **descriptive rates within this frozen design**, not estimates of general model accuracy or a causal estimate of the benefit of decomposition. The pathways differ in prompts, stage exposure, and composition opportunities; the experiment does not isolate a single causal factor.

## Design and examined material

- **Nine** synthetic base fixtures, each under **eight** systematic presentation conditions: 72 dependent presentations, **not** 72 independent semantic tasks.
- Variations included prompt style, short versus loaded evidence, and stage order.
- **Ten** separately preserved execution epochs were examined in their recorded historical order.
- **216** C/E/J request–response records, with the E→J handoff bound to the recorded response identity.
- The source audit of the supplied archives reported **10/10 ZIP CRC checks**, **894/894 manifest members**, **216/216 raw-response reconstructions**, and **72/72 complete three-stage case records** consistent with the declared synthetic rule.
- The recomputation was against the **supplied original archive bytes**. No independent attestation of model weights, server identity, capture times, external institutional authorization, or real-world action was provided.

## Results

| Observable predicate | Combined C | Separated E→J |
| --- | ---: | ---: |
| All three component labels correct | 63/72 | 67/72 (E stage) |
| Joint label correct against synthetic rule | 50/72 | 70/72 (J stage) |
| Joint label internally consistent with the component labels | 57/72 | 70/72 (J relative to E) |
| **Entire component-and-joint vector correct** | **48/72** | **67/72** |

**Paired full-vector outcomes:** 48 both correct; **19 separated-only correct**; zero combined-only correct; **five neither correct**. The unequal results remain descriptive, with shared base fixtures and dependent presentation variants.

The separation was observed in seven of nine base-fixture families; two families were ties. No family favored the combined pathway in these supplied records. In the 24 presentations with a reference joint state of `UNRESOLVED`, full-vector correctness was **7/24** for C and **20/24** for E→J. This subgroup contrast is a target for successor study, **not** a proven causal mechanism.

### Deterministic recomposition diagnostic

Applying the declared deterministic conjunction rule *after the fact* to the already recorded component outputs produced:

| Input to deterministic rule | Fully correct vectors |
| --- | ---: |
| C component labels, recomposed as D(C) | 63/72 |
| E component labels, recomposed as D(E) | 67/72 |

This diagnostic holds the component labels fixed while removing one model-produced joint-aggregation opportunity. It does **not** repair incorrect component interpretation, establish that deterministic composition is universally better, or replace an actual approved institutional decision rule.

## What failed

1. **Aggregation despite correct interpretation:** In **15** combined-pathway presentations, all component labels matched the synthetic reference but the combined joint conclusion did not.
2. **Failures shared by both paths:** **Five** presentations were not fully correct through either method. These are retained as adverse evidence, not discarded as exceptions.
3. **Joint-label accuracy masked component error:** Assessing only the final label would credit some presentations with incorrect underlying component vectors.
4. **Unresolved classifications were particularly fragile:** The `UNRESOLVED` subgroup displayed a large within-study separation; this is a descriptive observation with limited independent variation.
5. **No method-effect qualification:** The NGAST Lens Shift and Lens Removal methods were **not experimental arms** in OAS-002. Their use in the subsequent examination does not retrospectively prove method superiority.

The key distinction is:

```text
CORRECT COMPONENTS != CORRECT COMPOSITION
CORRECT JOINT LABEL != CORRECT COMPLETE STATE
SOURCE ARCHIVE HASH PASS != TRUSTED MODEL ORIGIN
SYNTHETIC RULE MATCH != ENTERPRISE AUTHORIZATION
```

## Implications for evidence systems

For an out-of-band, read-only evidence layer such as the research direction of **Fork**, a single success/failure field is inadequate to describe these observations. Distinct, version-bound fields should preserve:

1. The exact observed input and model-visible projection, including source and policy/context versions where supplied.
2. The model/tool serving profile and raw response, separated from parsing and scoring outcomes.
3. Each component-state claim and its warrant, without converting a missing component into an affirmative one.
4. The specified composition rule, computed joint state, and any contradiction between component and joint results.
5. Human review, **actual approval** (if any), proposed action, recorded execution, and independently observed effect as distinct events.
6. The reviewer-relative finding, unresolved conditions, and subsequent change in warranted standing.

This is an **architectural research implication**, not evidence that Fork already implements a production enterprise GRC connector or that any control owner has received or acted on a notification. An evidentiary exception may be represented and exported without making the evidence layer the authorization or enforcement authority.

## Verification boundary

**Already checked in the private source examination:** archive membership, supplied manifest hashes, request/response linkage, synthetic reference reconstruction, read-only rescoring, paired presentation counts, and prior epoch preservation.

**Verifiable from this public documentation alone:** arithmetic consistency of these reported aggregate counts, machine-readable summary structure, and the exact GitHub bytes of this documentary page. The original 10 ZIP archives, frozen input plan, individual model responses and the recomputation script are not attached. **A public reader cannot independently reproduce the underlying model experiment from this page.**

The reported archive checks do not authenticate the source, timing, model artifact, or correctness of the synthetic oracle. The page makes no claim that the reference synthetic policy is an independently validated institutional authorization rule.

**Release gates remaining:** release-object identity and rights review, disclosure screening of raw materials, separate technical review, public-source packaging and verification, and explicit publication/admission decision. The existing NGAST Research Records catalog and its separate DOI-bearing documentary publication remain unchanged by this page candidate.

## Successor experiments that could change the conclusion

- Held-out, matched-state A/B/C differentials under pinned serving profiles, fixed call/budget accounting, balanced order, and separately reviewed synthetic warrant rules.
- A public, independently recomputable disclosure package with source-to-summary receipts after the requisite rights and redaction review.
- Comparison against information-matched ordinary logs and prose to test whether a structured evidentiary boundary actually improves external reviewers' classification.
- A separately authorized integration study testing whether missing, stale, or contradictory evidence reaches the responsible external control and what action, if any, the authorized control takes.

**No execution, rollout, production suitability, safety certification, compliance determination, or legal/institutional authority follows from these proposed successors.**

## Citation and relationship to adjacent work

**Suggested temporary citation (no DOI):** Feller, R. (2026). *OAS-002: When evidence interpretation and decision composition diverge*. NGAST Research Records, `v0.1-review-candidate`, October 24, 2026. Cite the exact Git commit for any review of this candidate; do not describe it as a finalized research release.

**Related but separate:** OAS-001 SELECTIVITY-001 examined responsiveness to material authorization-evidence reversals, with **0/12** fully correct assessable reversal pairs in its 24/48 uniquely completed synthetic-case subset. Its negative result and missing halves belong to OAS-001, not the OAS-002 denominator. Other NGAST adaptive-harness failures likewise remain separate experiments.

The broader [Fork public evidence repository](https://github.com/RecomputableEvidence/fork-public-evidence) concerns bounded handoff/evidence preservation. Its [current standing](https://github.com/RecomputableEvidence/fork-public-evidence/blob/main/CURRENT_STANDING.md) is independent of this research candidate. **Relevance to Fork is not a Fork-core result, admission, certification, or authority transfer.**

[Return to NGAST Research Records](../../../README.md)
