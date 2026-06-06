# Intent-falsification pass — cycle 3 (l1-convergence-pass-sequencing) [convergence cycle]

Fresh-context subagent (opus), criteria-first against R1-R5. Result: 2 findings → D-track delta
→ mechanical pass SKIPPED this cycle (intent-delta). Cycle NOT clean → NOT [READY].

## Per-R# attack lines
- {R1, refutation: core.md:410-419,460-481 + §3.1:139-153 — D4 makes the harmful case (mechanical lines in a cycle whose intent artifact shows a D-delta) detectable via clause (v) re-deriving clean from the intent artifact (re-checkable fact), outcome: SERVED}
- {R2, refutation: modules.md:300-302 + core.md:460-481 — "constructed from the verdict" (D2) is prose the orchestrator could ignore, BUT D3+D4 backstop the only harmful case (forged "clean" past a real D-delta is caught by re-derivation), consistent with §3.1 "bind comes from the checker's producer-independent re-derivability", outcome: SERVED}
- {R3, refutation: modules.md:330,392-405 + core.md:460-481 — clause (v) extends the existing §3.4 line + existing coverage-check; no new artifact/dispatch, outcome: SERVED}
- {R4, refutation: modules.md:395-405 + core.md:419-423 + behavior-preserving instance-defined/tracker-recorded — skip carve-out composes (absence vs presence of lines, disjoint); BUT carry-forward leaves a legitimacy hole, outcome: FINDING (FIND-1)}
- {R5, refutation: grep'd sequencing/artifact sites in core.md+modules.md — found core.md:564-568 ([READY] artifact composition: "...mechanical falsification pass artifact, or its recorded skip...") states the sequencing + names the mechanical artifact (shape changed by D3), NOT in D1's scope; D1's "no other site states the sequencing" basis is inaccurate, outcome: FINDING (FIND-2)}

## Per-finding lines
- {finding: FIND-1 — CARRY-FORWARD LEGITIMACY HOLE. On a behavior-preserving carry-forward cycle (core.md:419-423) the mechanical artifact cites a PRIOR cycle's intent-clean verdict. D4 clause (v) verifies the cited verdict exists + shows no-D-delta + citation matches — but NOT that the carry is legitimate (that every intervening mechanical fix since the cited clean was behavior-preserving). Behavior-preserving is instance-defined / tracker-recorded — orchestrator say-so, not producer-independent. So a mechanical run that carried a clean verdict across an intervening NON-behavior-preserving fix passes the check: the harmful case (mechanical ran on a design whose character changed since the cited clean) is undetectable on return. criterion-attacked: R4/R1, refutation: core.md:419-423 + behavior-preserving say-so + D4 contract (no behavior-preserving-chain check), route: mechanical-falsification-candidate}
- {finding: FIND-2 — R5 SCOPE MISS. core.md:564-568 (the [READY]-artifact-composition sentence) states the sequencing ("or its recorded skip") AND names the mechanical artifact whose shape D3 changes; D1's scope (:410-419 + :460-481) omitted it and asserted "no other site states the sequencing" — inaccurate. Likely field-agnostic like modules.md:51-52 (generic citation) but never surfaced for that judgment → R5 completeness unmet. criterion-attacked: R5, refutation: core.md:564-568 vs D1 scope vs :51-52 parallel, route: surfaced}

## Disposition (orchestrator)
- **mechanical skipped: intent-delta this cycle** (FIND-1 routed mechanical-falsification-candidate = D-track delta).
- FIND-1 → reopens D2/D3/D4 (the carry-forward clauses) [INVALIDATED]→[PENDING].
- FIND-2 → reopens D1 (scope basis inaccurate) [INVALIDATED]→[PENDING].
- D5 (prose reconcile, depends on D2-D4) reopens [PENDING] (broken-basis).
- Resolution carried to next cycle: **D7 [CONDITIONAL] — remove the intent-pass carry-forward optimization**
  (intent-falsification runs every convergence cycle; mechanical's governing intent-clean verdict is always
  THIS cycle's), which fully closes FIND-1 + moots F3 + simplifies the spec. Considered alternative: keep the
  optimization + make the carry chain readable + file the behavior-preserving say-so as a separate "bind
  behavior-preserving classification" item (inherits the residual). **Surfaced to operator — shipped-semantics fork.**
