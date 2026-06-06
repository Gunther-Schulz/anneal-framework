# Impl plan — l1-convergence-pass-sequencing

2 dispatch units, **parallel-eligible**. Disjointness basis: the units edit **different files**
(`spec/core.md` vs `spec/modules.md`) with no shared edit region — confirmed by D1's scope enumeration
(core.md sites :406-423 + :460-481; modules.md sites §3.3(c):300-302 + §3.4:322-410). Both honor the
locked D2-D5/D7 contracts; the cross-file coherence (D4's coverage-check (v) ↔ D3's cited field ↔ D2's
input) is held by both rendering the same §3.4.1 "intent-clean" criterion (no `mechanical-falsification-candidate`
finding). **Realization re-anchors to LIVE line numbers** (per F-b drift note), not the tracker's.

- **Unit 1 — `spec/core.md` §4.1.4** (first; parallel with Unit 2): D4 coverage-check clause (v) [live :460-481]
  + D5 prose reconcile [live :406-419, name the structural enforcement, not keyword] + D7 remove the carry-forward
  paragraph [live :419-423]; the §3.4 this-cycle-intent-delta skip stays; behavior-preserving def (:890) untouched.
- **Unit 2 — `spec/modules.md` §3.3/§3.4** (first; parallel with Unit 1): D2 add the this-cycle intent-clean
  verdict to the convergence-falsification dispatch scope (c) [live :300-302] + D3 add the cited this-cycle
  intent-clean verdict field to the mechanical artifact + malformed-if-absent [live :330/:392-405].

**Not in this run (D6, render-follow, queued to the batch):** the phase file `investigate-design.md` (dispatch-brief
(c) + coverage-check + the carry-forward prose at :203-207) + `tracker.md` artifact-description → re-rendered from
the verified spec in the `instance-reinstantiation` batch (spec-only render-cadence policy).

Each unit: invoke skill-craft before edit; self-check against the locked design with the write-time lenses
(Lossy-render, Missed-dependents, Undefined-shorthand, Over-claimed-verification) + change-set-vs-scope.
