# EVIDENCE-STANDING-DIAGNOSTIC-001 — Format Repair 001

## Evidence of the failure

The original diagnostic v0.1 halted during the first historical paired case: C07, actor A, one Perplexity Agent response. The raw response was a complete JSON object enclosed in a Markdown `json` code fence. The original strict `json.loads(raw)` parser raised `JSONDecodeError`. The record ended with `response_invalid` and `batch_halted`, **7 events, 1 request, 0 completed paired cases, 0 scored observations**. The preceding failed run remains historical evidence, never rewritten, reclassified, or merged into a completed case.

Prior halted evidence tip: `023f7a8f2b7bf3852cfbcf6f2f7a07aaf87b35c8d8de2abc215f6803a66b48fa`.

## Authorized repair scope and caveat

This is a *post-observation*, explicitly labeled instrumentation repair. It changes how the runner accepts a response envelope: raw JSON objects remain accepted; exactly one complete ` ```json ` code block is also accepted after unwrapping. The raw model output is preserved. Fences with extra text, other languages, malformed JSON, or schema violations are rejected. A new hash-chained `response_envelope` event records the wrapper type and raw-byte digest and is recomputed by the verifier.

The diagnostic's participant instruction bytes, seven scenario fixtures, historical/current meanings, answer schema, format conditions, seeded schedule, model IDs, request limit, $2 cumulative local guard and cost estimates remain unchanged. The original participant instruction still requests bare JSON; this repair tolerates one syntactic variation rather than changing what is asked of the model.

Because the repair was motivated by observed behavior, **the new run is a disclosed repaired feasibility run, not an untouched execution of the original frozen operational criterion**. It is unsuitable for pooling as a pre-registered replicate without acknowledging this procedural change.

Do not resume or modify the halted v0.1 run. Unzip this package to a **new** folder, and give its new run a different name. The new run's initialization binds the original failed tip and the repair ID. No previous model calls are reused, so paid requests in the new run are a separate $2 maximum local authorization.

## Tests

Checks include acceptance of a single complete fenced JSON object, strict rejection of prose/other languages/extra blocks, full 56-response synthetic run with one fenced response and raw evidence preservation, and verification of the untouched historical failure if the original log is available. No live requests were made during this repair.
