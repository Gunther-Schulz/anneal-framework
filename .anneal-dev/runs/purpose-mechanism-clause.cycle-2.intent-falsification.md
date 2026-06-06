# purpose-mechanism-clause — cycle 2 intent-falsification pass

Fresh-context subagent (opus tier), criteria-first (criteria derived from R1–R5 before reading the
design). Attacks whether the locked design (D1) serves its intent.

## Per-R# attack lines

- `{R1, refutation: read core.md:10-28 — securing relation absent from Purpose surface; read clause S1 "These goals are secured by … structural enforcement" — relation now on surface, outcome: served}`
- `{R2, refutation: read clause S1+S4 for totalizing "all rigor structural" vs the operator carve-out; S1 = direction-of-shift not "all", S4 carves "one irreducible exception … deliberately-willed gate, not a gap to close"; cross-check core.md:156-157, outcome: served (wording-drift F2 noted)}`
- `{R3, refutation: grep "satisfic" spec/ foundation.md → 0; clause predicates failure on the rule's dependency ("depends on the AI choosing rigor leaks: loads but does not fire"), not a property-of-AI assertion, outcome: served}`
- `{R4, refutation: read §3.1 (core.md:109-169), verified each §3.1-attributed claim; evidence-bearing-artifact + separate-non-producing re-derivation CONFIRMED, operator-irreducible-terminus CONFIRMED, but "AI cannot certify its own foundation" NOT in §3.1, outcome: finding (F1)}`
- `{R5, refutation: grep "asymptot|hoped.for|rigor-enforced|leaning on" spec/ foundation.md → 0; clause stops at "not a gap to close" (the R2 accuracy carve), no trajectory content, outcome: served}`

## Per-finding lines

- `{F1: clause S4 tags "the AI cannot certify its own foundation" as (§3.1), but §3.1 does not carry that reason — it lives in CLAUDE.md:20-21 (dev-process), not run-spec §3.1; criterion-attacked: R4; refutation: grep -niE "certif|own foundation" scoped core.md:111-169 → 0 matches (only 425/613 elsewhere, unrelated); route: mechanical-falsification-candidate, shape=target-existence, predicate=expected-match:certif over §3.1 range → FALSIFIED}`
- `{F2: clause S4 "genuinely-human judgment" vs canon "genuinely-irreducible judgment" (core.md:157) — reattributes terminus from irreducibility to humanness; criterion-attacked: R2/R4; refutation: grep -rniE "genuinely-(human|irreducible)" spec/ foundation.md → only "genuinely-irreducible" @core.md:157, "genuinely-human" nowhere; route: mechanical-falsification-candidate, shape=target-existence, predicate=expected-match:genuinely-human over §3.1 range → FALSIFIED}`
- `{F3: clause S1 "secured by" echoes Purpose opener "exists to secure" (core.md:12) — tightness nick; criterion-attacked: intent (tight/coherent-with-neighbors); refutation: read core.md:12 vs clause S1; route: [VERIFIED — surfaced]}`

## Orchestrator verdict (holds-or-falsified computed by applying predicates to results)
- F1 → **falsified** (§3.1 range lacks "certif"). → D-track delta: amend D1.
- F2 → **falsified** (§3.1 uses "irreducible", not "human"). → folded into D1's realization (D1's surface already says "irreducible"; the draft drifted).
- F3 → `[VERIFIED — surfaced]`, terminal, non-blocking.

**Intent pass NOT clean → produced a D-track delta (F1 amends D1).** Per the convergence sequencing
rule (`investigate-design.md`), the **mechanical falsification pass is SKIPPED this cycle**
(intent-delta — the design is about to change). Loop to cycle 3.

Holistic: the design's *substance* serves intent (operator = irreducible willed terminus is
canonically true); the defect is citation-accuracy in the realization/surface — a clause whose job
is "cite §3.1, don't restate" must cite §3.1 *accurately*. Fix is surgical (recast the
operator-exception to §3.1's actual ground; drop the mis-attributed self-certification phrase).
