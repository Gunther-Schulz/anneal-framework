# Run: l1-convergence-pass-sequencing

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** L1 of `convergence-sequencing-enforcement` — encode the convergence cycle's
  intent→mechanical sequencing structurally (render the skill-craft v1.0.58 dispatch-dependency
  discipline into the anneal-dev kernel). Targets: `spec/core.md §4.1.4` + `spec/modules.md §3.3/§3.4`.
  (Parked sibling run: `move1-tail-honest-relabel`, IN-PROGRESS, different task — surfaced, left parked.)

## Requirements record (task-input; separated from the proposed solution)

- **Verbatim operator request:** "L1 we do now." (Following: fix the anneal-dev instance of the
  sequencing-enforcement gap that bit us — the convergence cycle's two passes run in parallel because
  the intent→mechanical dependency is prose-only.)
- **R1** — The intent→mechanical sequencing dependency is enforced by a **producer-independent, readable
  artifact**, not prose ordering: a mis-sequenced run (mechanical ran despite an intent-delta) is
  **detectable on return**, not silently identical to a correct run.
- **R2** — The mechanical pass's **input** includes the same-cycle intent-clean verdict; the mechanical
  dispatch **cannot be constructed without it** (renders skill-craft v1.0.58 "encode the dependency in the
  dependent step's input").
- **R3** — Pareto: reuse the **existing** coverage-check-on-return + the existing intent/mechanical
  artifacts; no new machinery. The mechanical artifact **cites** the intent-clean verdict; the
  coverage-check re-verifies that citation against the same-cycle intent artifact.
- **R4** — Consistent with live §4.1.4 semantics (intent-first; intent-delta → mechanical skipped+recorded;
  behavior-preserving re-trigger). The skip carve-out (`modules.md §3.4`) still holds and now **composes**
  with a new "mechanical-lines-present-in-an-intent-delta-cycle = malformed" check.
- **R5** (completeness) — every site stating/depending-on the sequencing reconciled; the phase-file
  render-follow queued (spec-only render-cadence policy), not dropped.

## F-track (findings)

- **F1** [PENDING] Undefined-shorthand/Fragmentation: "intent-clean verdict" must be **defined once** by
  reference to §3.4.1's clean criterion (intent artifact with **no** `mechanical-falsification-candidate`
  per-finding line / no D-track delta), not restated across D2/D3/D4. — basis: `modules.md`:396-397 (skip carve-out keys on "intent-falsification pass produced a D-track delta") + §3.4.1 route enum read this cycle.
- **F2** [PENDING] Missed-dependents: the mechanical-artifact shape (`modules.md §3.4`) is rendered into the
  phase file (`investigate-design.md` dispatch-brief (c) + coverage-check) and `tracker.md`'s artifact
  description; the closed-artifact State-summary (`modules.md`:51-52) cites the mechanical artifact. Adding
  the cited intent-clean field is a contract change → enumerate + queue the render-follow (D6). — basis: scope search this cycle (core.md/modules.md/phase-file hits); `modules.md`:51-52 read.

## D-track (design decisions)

- **D1** [VERIFIED] **Scope** = the sites encoding the intent→mechanical sequencing + the mechanical-pass
  input + the artifact + the coverage-check: {`core.md §4.1.4` sequencing prose (:410-419) + coverage-check
  (:460-481); `modules.md §3.3` dispatch-brief (c) convergence-falsification (:300-302) + `§3.4` artifact
  (:322-410, incl. skip carve-out :395-405)}. Render-follow (phase file `investigate-design.md` (c) +
  coverage-check) is in-scope-as-render, edited in the batch not this spec-only cycle. — basis (this cycle): scope greps for `sequenced|convergence cycle.s start|Coverage check|mechanical falsification` across core.md/modules.md/phase-file → the enumerated hits; no other site states the sequencing.
- **D2** [PENDING] **Input-dependency (renders "encode in input").** Amend `modules.md §3.3` (c)
  convergence-falsification dispatch scope: in addition to "the [VERIFIED] D-entry set at the convergence
  cycle's start," it carries the **same-cycle intent-clean verdict** (the §3.4.1 intent artifact showing no
  D-track delta); the mechanical dispatch is **constructed from** that clean verdict and cannot be issued
  without it. — basis: `modules.md`:300-302 (current (c)) read this cycle; F1 (clean def).
- **D3** [PENDING] **Artifact citation (renders "cite the prerequisite's result").** Amend `modules.md §3.4`:
  the mechanical falsification-pass artifact carries a **cited same-cycle intent-clean verdict** (intent
  artifact reference + "no mechanical-falsification-candidate finding"); a mechanical artifact without that
  citation is malformed. — basis: `modules.md`:330 (current line shape) + :392-405 (malformed-line + skip carve-out) read this cycle.
- **D4** [PENDING] **Coverage-check (renders "violation readable").** Amend `core.md §4.1.4` coverage-check
  (:460-481): add (v) — the orchestrator verifies the artifact's cited intent-clean verdict **against the
  same-cycle intent artifact**; mechanical lines present in a cycle whose intent artifact shows a D-delta
  (a `mechanical-falsification-candidate` finding), OR with an absent/unmatched intent-clean citation, is a
  **malformed return**. Composes with the existing skip carve-out (which covers the absence-of-lines case). — basis: `core.md`:460-481 (current coverage-check) + :415-418 (skip+clean semantics) read this cycle.
- **D5** [PENDING] **Prose reconcile.** Amend `core.md §4.1.4`:410-419 so the sequencing names its
  **structural enforcement** (the input-dependency D2 + citation D3 + coverage-check D4), not prose ordering
  alone — per §3.1 the bind is the producer-independent re-derivation (the coverage-check re-checks against
  the intent artifact), not the keyword. — basis: `core.md`:410-419 read this cycle; §3.1 bind/surface gradient (post-`819e84e`).
- **D6** [VERIFIED] **Render-follow queued, not done this cycle.** The phase-file render (`investigate-design.md`
  dispatch-brief (c) + coverage-check) + `tracker.md` artifact-description update queue to the render-debt
  batch (`instance-reinstantiation`), per the spec-only render-cadence policy. — basis: render-cadence policy (backlog README; framework runs ship spec-only); F2 dependents.

### Cycle 2 appends (design-completion — lock D2-D5, discharge F1/F2, fold F3)

- **F1** [VERIFIED — addressed] "intent-clean verdict" is defined once by reference to §3.4.1's criterion
  (intent artifact with no `mechanical-falsification-candidate` finding / no D-delta); D2/D3/D4 cite it, none
  restates. — basis: D2-D4 contracts (this cycle) reference §3.4.1; no second definition authored.
- **F2** [VERIFIED — addressed] Dependents enumerated: spec — none beyond the in-scope §3.4 (the State-summary
  `modules.md`:51-52 cites the artifact generically — unaffected by the added field); render — phase file
  (c)+coverage-check + `tracker.md` artifact desc, queued to D6. — basis: scope greps this cycle; `modules.md`:51-52 cites "mechanical falsification-pass artifact citation" (generic, no field-level dependency).
- **F3** [VERIFIED — addressed] **Behavior-preserving carry-forward case.** When a behavior-preserving mechanical
  fix means a later convergence cycle does NOT re-run the intent pass (`core.md`:419-423 — intent-clean carries
  forward), that cycle's mechanical pass has no *this-cycle* intent artifact; the governing intent-clean verdict
  is the **carried-forward** one. D2-D4 must cite "the **governing** intent-clean verdict (this cycle's intent
  artifact, OR — on a behavior-preserving carry-forward — the cited prior-cycle intent artifact it carries
  from)", making the carry-forward itself readable. Folded into D2-D4. — basis: `core.md`:419-423 (behavior-preserving re-trigger / carry-forward) read this cycle.
- **D2** [VERIFIED] **Input-dependency** — realization-ready. Contract: `modules.md §3.3` (c)
  convergence-falsification scope additionally carries **the governing intent-clean verdict** (this cycle's
  §3.4.1 intent artifact showing no `mechanical-falsification-candidate` finding, or the cited carried-forward
  one per F3); the orchestrator constructs the mechanical dispatch **from** it and cannot issue it without it.
  Realization wording at impl. — basis: `modules.md`:300-302 + F1 + F3 (this cycle).
- **D3** [VERIFIED] **Artifact citation** — realization-ready. Contract: the `modules.md §3.4` mechanical
  artifact carries a **cited governing intent-clean verdict** (intent-artifact reference + "no
  mechanical-falsification-candidate finding"); absence = malformed line. Realization at impl. — basis: `modules.md`:330/:392-405 + F1 + F3 (this cycle).
- **D4** [VERIFIED] **Coverage-check** — realization-ready. Contract: `core.md §4.1.4` coverage-check gains
  clause (v) — the orchestrator re-derives clean from the **cited** governing intent artifact and verifies the
  citation; mechanical lines present in a cycle whose governing intent artifact shows a D-delta, OR with an
  absent/unmatched intent-clean citation, = malformed return. Composes with the existing absence-of-lines skip
  carve-out. Realization at impl. — basis: `core.md`:460-481 + :415-423 + F3 (this cycle).
- **D5** [VERIFIED] **Prose reconcile** — realization-ready. Contract: `core.md §4.1.4`:410-419 names the
  structural enforcement (D2 input-dependency + D3 citation + D4 coverage-check) as what binds the sequencing
  — per §3.1 the bind is the producer-independent re-derivation against the intent artifact, not the keyword;
  drop reliance on prose ordering alone. Realization at impl. — basis: `core.md`:410-419 + §3.1 gradient (this cycle).

### Cycle 3 appends (CONVERGENCE cycle — intent-falsification pass, sequenced first; produced delta → mechanical SKIPPED)

- **mechanical skipped: intent-delta this cycle** (FIND-1 routed mechanical-falsification-candidate). Convergence
  cycle NOT clean → NOT [READY]. Intent artifact: `.anneal-dev/runs/l1-convergence-pass-sequencing.cycle-3.intent-falsification.md`.
- **F4** [PENDING] **Carry-forward legitimacy hole** (FIND-1, route mechanical-falsification-candidate). D4's
  coverage-check verifies a carried-forward intent-clean verdict exists/matches but NOT that the carry is
  legitimate (intervening fixes all behavior-preserving) — and behavior-preserving is orchestrator say-so
  (`core.md`:419-423, instance-defined/tracker-recorded), not producer-independent. A mechanical run that carried
  a clean across a non-behavior-preserving fix passes → undetectable harmful mis-sequencing. — basis: `core.md`:419-423 + D4 contract (no behavior-preserving-chain check), fresh-context intent pass cycle-3.
- **F5** [PENDING] **D1 scope miss** (FIND-2, route surfaced). `core.md`:564-568 ([READY]-artifact-composition:
  "...mechanical falsification pass artifact, or its recorded skip...") states the sequencing + names the
  mechanical artifact (shape changed by D3); D1's "no other site states the sequencing" basis is inaccurate. — basis: `core.md`:564-568 vs D1 scope, intent pass cycle-3.
- **D1** [INVALIDATED]→[PENDING] scope basis inaccurate (F5) — must add `core.md`:419-423 (carry-forward, if removed per D7) + :564-568 (F5) and re-establish the completeness basis.
- **D2** [INVALIDATED]→[PENDING] · **D3** [INVALIDATED]→[PENDING] · **D4** [INVALIDATED]→[PENDING] (carry-forward
  clauses reopened by F4) · **D5** [INVALIDATED]→[PENDING] (broken-basis, depends on D2-D4).
- **D7** [CONDITIONAL] **Remove the intent-pass carry-forward optimization** — the intent-falsification pass runs
  **every** convergence cycle; the mechanical pass's governing intent-clean verdict is **always this cycle's**
  (no carry-forward). Fully closes F4, **moots F3** (no carry-forward to make readable), and simplifies D2/D3/D4
  back to "this-cycle intent artifact"; reconciles `core.md`:419-423 (removes the carry-forward paragraph; the
  §3.4 skip for *this-cycle* intent-delta stays). **Assumption (operator-resolvable):** the extra intent dispatch
  per convergence cycle is acceptable vs keeping the optimization — a shipped-semantics change.
  considered: keep optimization + make the carry chain readable + file behavior-preserving say-so as a separate
  "bind-behavior-preserving-classification" item (rejected: inherits the say-so residual; FIND-1 only *contained*,
  not closed; more spec complexity, not less). — basis: F4 + `core.md`:419-423 read this cycle; thorough-fix + Pareto (removes a special case + a say-so dependency).

### Cycle 4 appends (re-design — operator approved D7; re-lock simplified)

- **D7** [VERIFIED] (operator-resolved 2026-06-05) **Remove the intent-pass carry-forward optimization.** Amend
  `core.md §4.1.4`: the intent-falsification pass runs **every** convergence cycle; remove the carry-forward
  paragraph (:419-423). The mechanical pass's governing intent-clean verdict is always **this cycle's**. The
  §3.4 skip (this-cycle intent-delta → mechanical skipped) is **retained**. Touches ONLY :419-423; the
  behavior-preserving *definition* (`core.md`:890) stays (verify §4.3 uses it independently). — basis: references-search this cycle — `carries forward|re-open the intent` → sole convergence-site `core.md`:419-423; `:890` is the behavior-preserving def (verify-side, untouched); `modules.md`:514 unrelated.
- **F3** [INVALIDATED] **mooted by D7** — no carry-forward exists, so "make the carry-forward readable" has no
  referent; D2-D4 collapse to the this-cycle case. — basis: D7 removes the carry-forward construct F3 addressed.
- **F4** [VERIFIED — addressed] carry-forward legitimacy hole **closed** by D7 (no carry-forward → no
  carry-legitimacy question; the cited intent-clean verdict is always re-derivable from THIS cycle's intent
  artifact). — basis: D7 (this cycle).
- **F5** [VERIFIED — addressed] `core.md`:564-568 enumerated in D1 scope; it's a **generic** mechanical-artifact
  reference (field-agnostic, parallel to `modules.md`:51-52) + a "recorded skip" mention consistent with the
  retained skip → **no edit needed**. — basis: `core.md`:560-570 read this cycle (artifact named generically, no internal-field dependency).
- **D1** [VERIFIED] (re-locked) **Scope** = {`core.md §4.1.4`: sequencing prose :410-419 + carry-forward para
  :419-423 (removed, D7) + coverage-check :460-481 + [READY]-composition :564-568 (F5, no-edit); `modules.md
  §3.3` (c) :300-302 + `§3.4` artifact :322-410}. — basis (this cycle): references-search `carries forward|re-open the intent|sequenced|Coverage check` → the enumerated set; :419-423 sole carry-forward site, :564-568 the only additional [READY]-composition mention; no other.
- **D2** [VERIFIED] (re-locked, simplified) `modules.md §3.3` (c) convergence-falsification scope carries
  **this cycle's** intent-clean verdict (the §3.4.1 intent artifact this cycle with no
  `mechanical-falsification-candidate` finding); mechanical dispatch constructed from it. (Carry-forward clause
  dropped per D7.) — basis: `modules.md`:300-302 + D7 (this cycle).
- **D3** [VERIFIED] (re-locked, simplified) `modules.md §3.4` mechanical artifact cites **this cycle's**
  intent-clean verdict; absence = malformed line. — basis: `modules.md`:330/:392-405 + D7 (this cycle).
- **D4** [VERIFIED] (re-locked, simplified) `core.md §4.1.4` coverage-check clause (v): orchestrator re-derives
  clean from **this cycle's** intent artifact + verifies the citation; mechanical lines present when this-cycle
  intent shows a D-delta, or with absent/unmatched citation, = malformed return. Composes with the absence-of-lines
  skip carve-out. — basis: `core.md`:460-481 + :415-418 + D7 (this cycle).
- **D5** [VERIFIED] (re-locked) `core.md §4.1.4`:410-419 names the structural enforcement (D2+D3+D4) as the bind
  (§3.1 producer-independent re-derivation, not the keyword); coordinated with D7's removal of :419-423. — basis: `core.md`:410-423 + §3.1 gradient (this cycle).

### Cycle 5 appends (CONVERGENCE cycle — intent-falsification first, clean-dispositioned; mechanical NOT skipped)

- **F-a** [VERIFIED — surfaced] (cycle-5 intent pass) `glossary.md` states the sequencing at :151-159, :200-209,
  :279-281 — D1's "no other site" basis was an overclaim. Read each: all definitional glosses cross-referencing
  `core.md §4.1.4`, describing intent-first order + this-cycle skip (both retained), **none asserts the removed
  carry-forward**, none carries the enforcement mechanism → **consistent, no edit** (parallel to F5/:564-568).
  Operator-reviewable residual: the no-edit judgment. — basis: `glossary.md`:151-159/:200-209/:279-281 read this cycle (each ends "Specified in `core.md` §4.1.4" / cross-refs it; order+skip only).
  - **D1 basis strengthened (cycle 5):** completeness search now covers `glossary.md` (:151-159/:200-209/:279-281,
    consistent-no-edit) in addition to core.md/modules.md; edit-set resolution UNCHANGED → basis-only refinement,
    not amendment, no D-track delta.
- **Intent pass clean-dispositioned** (F-a terminal at [VERIFIED — surfaced]; no `mechanical-falsification-candidate`
  finding → no intent-delta) → mechanical falsification pass runs this cycle (sequenced after intent).
- **Mechanical falsification pass: ALL HOLD** (D1-D7, aggregate holds). Artifact:
  `.anneal-dev/runs/l1-convergence-pass-sequencing.cycle-5.falsification.md`. No [VERIFIED] entry falsified.
- **F-b** [VERIFIED — surfaced] Realization note: tracker line numbers drifted slightly vs live (§4.1.4 para opens
  :406; carry-forward :419-423 exact; coverage-check :460-481 exact; [READY]-composition :564-569) — **impl
  re-anchors to live line numbers**. D7 independence strengthened: `anneal-dev/spec/bindings.md`:112-119 ties
  behavior-preserving to §4.3 only. — basis: cycle-5 mechanical pass reads (live-line verification).
- **CONVERGENCE CLEAN — [READY].** Convergence cycle (5) ran investigation (new surfaces: glossary + fresh
  falsification searches) + standardized (clean) + intent-falsification (clean-dispositioned, F-a basis-refinement)
  + mechanical falsification (all hold); **zero D-track deltas**.
- **Fresh-session implementability: PASSED** — per-implementer-step external evidence:
  - D4 step: edit `core.md §4.1.4` coverage-check — target exists, live :460-481 (clauses (i)-(iv) located, observable).
  - D5+D7 step: edit/remove `core.md §4.1.4`:406-423 — sequencing prose (:410-419, ordering-only, observable) + carry-forward para (:419-423, located).
  - D2 step: edit `modules.md §3.3`(c) — live :300-302 ("[VERIFIED] D-entry set at the convergence cycle's start", located).
  - D3 step: edit `modules.md §3.4` — live :330 line shape + :392-405 malformed/skip (located).
  - Each step's realization wording derivable from the locked contract + the cited source; no new design decision.

> **Phase status:** investigate-design COMPLETE at [READY]. Awaiting operator `next phase` to enter implement
> (impl plan: `.anneal-dev/runs/l1-convergence-pass-sequencing.impl-plan.md`). Method-kernel edit — verify will
> add the kernel-independent legs (skill-craft form + operator soundness). F-a/F-b [VERIFIED — surfaced] are
> operator-review residuals (no edit).

### Implement complete → verify

- Operator selected `next phase` (n) at [READY]. Implement: single combined unit (core.md §4.1.4 + modules.md
  §3.3/§3.4), dispatched to a subagent, in-place under the Integrity check (tree clean pre-dispatch, HEAD
  `ab6a231` snapshot; post-return only the two in-scope files advanced — Integrity PASS). Subagent self-check
  clean (4 write-time lenses + change-set-vs-scope); no loopback.
- **Persistence reference:** `66331c0` (anneal-checkpoint, anneal-framework container; discharge gate skips it).
- **Phase → verify** (isolated subagent; method-kernel edit → kernel-independent legs: skill-craft form +
  operator step-4 soundness, aimed by the foundation-invariant register check).

### Verify result (isolated subagent)

```
Verify result: [PASSED] (isolated)
Finding ledger:
  F-V1 [VERIFIED — deferred]
```
- All four checks accounted for: planned-vs-actual D2-D7 hold; requirements R1-R5 covered (+ verbatim leg clean);
  standardized lenses clean; battery (a) render-fidelity N/A (spec-only, no `plugin/skills/*` in `66331c0`),
  (b) coherence HOLDS (cross-file intent-clean criterion identical at the 3 sites; carry-forward removal leaves no
  spec-side dangle; grep-confirmed), (c) skill-quality N/A (no skill files). No spec-side defect, no softened
  must/closed-set, clause (v) ↔ skip carve-out compose without contradiction.
- **F-V1** [VERIFIED — deferred] the rendered plugin phase file `investigate-design.md`:203-207 still carries the
  carry-forward semantics D7 removed — a **lagging rendered-clause dependent**, tracked render-debt (D6/F2 → queued
  to `instance-reinstantiation`), NOT a spec defect / untracked dangle. Deferred under the **operator-ratified
  spec-only render-cadence policy** (CLAUDE.md self-hosting; backlog render-cadence policy 2026-06-04) — the standing
  operator pull; re-fire trigger = the render-follow batch lands / `instance-reinstantiation` runs. (Surfaced to the
  operator at step-4 for explicit ratification, per the method-kernel discipline.)

### Foundation-invariant register check (focusing artifact — aims the operator's soundness pass; NOT a verdict)

- **INV-3 (verify-isolation — verifier ≠ actor)** — [TOUCHED · HOLDS/STRENGTHENED]. The edit moves the
  intent→mechanical sequencing from an **orchestrator self-asserted ordering** (parallel-dispatchable, self-checked)
  to a **producer-independent re-derivation**: the coverage-check re-derives intent-clean from THIS cycle's
  §3.4.1 intent artifact (produced by the fresh-context intent subagent, separate from the mechanical subagent and
  the actor) and rejects a mismatch. This IS INV-3's principle (don't trust the producer's self-check; tie to a
  separate context). **Anchor** (Panickssery et al. — self-verifier unreliable; independence > self-checking):
  satisfied/strengthened. **Operator focus:** confirm the coverage-check's re-derivation genuinely terminates at
  the separately-produced intent artifact, not a new orchestrator self-check.
- **INV-5 (exclusion via a named, runnable falsifier — the soundness keystone)** — [TOUCHED · HOLDS]. The
  named-runnable-falsifier mechanism is intact (every [VERIFIED] decision still gets its candidate falsifier, run +
  cited). The edit gates the mechanical pass's *timing* (intent-clean precondition) and **removes** the carry-forward
  say-so (D7) — tightening, not weakening, the exclusion regime (intent now attacks every convergence cycle → more
  falsification coverage, not less). **Anchor** (Platt exclusion / WRSPM completion-insufficient): satisfied.
  **Operator focus:** confirm removing the carry-forward doesn't reduce falsifier coverage (it increases it).
- **No new invariant.** The edit APPLIES the bind/surface producer-independence principle (INV-3); it does not add a
  novel kernel invariant (consistent with move-1's D5 — the bind/surface distinction did not earn its own slot).
- **Register-clean ≠ sound** (anti-false-comfort residual): this ledger names INV-3/INV-5 holding against their
  anchors; it does NOT certify soundness. The operator's step-4 soundness verdict is irreducible (+ the kernel-
  independent skill-craft form leg, pending).
