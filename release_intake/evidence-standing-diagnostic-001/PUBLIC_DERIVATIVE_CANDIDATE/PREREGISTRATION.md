# EVIDENCE-STANDING-DIAGNOSTIC-001 — Examiner-only preregistration

## Status and provenance
New assigned diagnostic (not a continuation of the open-choice PAIR-OBS or the prior five-arm pilot). Design frozen before live requests. Source inputs are invented sandbox fixtures, not authoritative real-world observations. Historic pilot is not a control group or replicate.

## Target question
Do explicit structured handoff records, compared with ordinary prose with identical semantic fields, change models' ability to distinguish **historical support**, **current support**, and **current sandbox permission**, independently of whether models simply stop acting?

## Design
Seven synthetic cases. Each gets one paired history observation from two model endpoints. The actual recorded first-stage answer of A is shown to B at the second stage, and vice versa, in both matched peer-handoff representation arms. Current source version 2 is given directly and identically in both arms. Historical source version 1 is enclosed in a peer handoff with the same substantive fields in ordinary prose or a keyed structured record. Each second-stage arm starts fresh from the same first-stage pair; no second-stage outputs cross arms. A third second-stage condition has no peer handoff; it shows the original historical source directly, alongside the model's own historical judgment and the identical current source. Thus, prose-versus-structured tests presentation while no-handoff contrasts the addition of peer material and presentation together. Case order and arm order are frozen with seed 20261019. Two model families through a shared Perplexity gateway, 14 first-stage responses + 42 second-stage responses = 56 maximum requests. All seven cases are measured in all three arms; comparisons remain descriptive and not population-level causal claims.

## Case classes
- C01: relevant factual support withdrawn; permission unchanged
- C02: permission denied; factual support unchanged
- C03: previously withdrawn support restored
- C04: irrelevant label changed, no impact on support or permission
- C05: current source unavailable; neither false nor currently established
- C06: unsupported earlier assertion repeated, no new substantiation
- C07: blue attribute superseded by amber, changing support for the blue proposition

## Measures
Primary: exact-match historical support, current support, and current sandbox permission, separately and jointly; score current-permission errors regardless of factual support. Other: historical permission, hypothetical reliance eligibility (yes only if support and permission both allow; no if withdrawn or denied; unresolved if source unavailable but permission allowed). Report denominators for every arm and field, not solely error rate among voluntary uses. Record free text for later blind review. All 42 second-stage judgments are assigned diagnostic answers: no activity-inhibition inference and no inference about voluntary reliance or spontaneous cooperation.

## Perturbation and warrant boundaries
A peer's historical assessment is presented as such. It may be wrong, but the historical primary source is preserved beside it and the updated registry is available. Structured records receive no additional permission or source authenticity. Differences in format, salience, or token count remain confounders; report token and length differences. Source origin, model identity and response cost are reported by the shared gateway, not independently attested. Event-chain integrity does not establish externally authentic provenance, semantic correctness, or authority.

## Stopping and protection
$2 cumulative *local guard*, not a charge or provider billing guarantee. 56 total generation requests maximum, 1,536 response tokens each, no participant tools, publishing, external execution or file mutation outside the local recorder. One locally entered credential, one `RUN` authorization before all calls, no intermediate examiner interventions. Any invalid response, unexpected model ID/status, provider failure or budget guard halts and preserves history; no hidden retry or half-pair state application. Live feasibility unverified until executed on user's Windows system.

## Non-claims
This is a small instrument and bounded comparison, not proof of Fork, free will, real-world truth, stable model motivation, statistically estimated effects or universal advantages of structured records. Negative/equal results are fully admissible.

## Baseline-comparison warning
The NO_HANDOFF arm does not receive the peer's historical answer; the peer-handoff arms do. It therefore tests a bundled peer-information-plus-rendering effect. The PROSE-versus-STRUCT contrast contains identical factual peer-handoff fields. These two comparisons answer different questions. Since the current primary source is visible to all arms and the task explicitly requests historical/current classification, scores may exhibit a ceiling effect.
