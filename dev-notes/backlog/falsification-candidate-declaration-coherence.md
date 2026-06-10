# Falsification candidate declaration-coherence — predicate/scope can mis-declare against the basis it attacks

**Status:** OPEN — operator-raised 2026-06-10, surfaced by two clippy runs in one
beat-the-books session (`2026-06-10-unit-35-claim-notify-idempotency`,
`2026-06-10-unit-36-ev-announce-market-mislabel`; both auto-battle, falsification
subagents on opus). **Spec-root** by the in-run triage: faithful following of the
dispatch brief still produced **3 mechanically-malformed candidate lines across 4
mechanical/intent dispatches**, same failure family each time. Method-kernel
(falsification pass: the dispatch-brief template + the closed predicate set —
`core.md` §4.1.4 region; rendered into instances as
`phases/investigate-design.md` §Falsification dispatch-brief template +
`references/tracker.md` §The mechanical falsification-pass artifact; ground the
exact spec section at pickup) → re-render to all instances if pursued.

## The failure family (3 instances, 2 runs)

A candidate's **declared predicate or scope is incoherent with the basis it
attacks** — applied mechanically, the line computes `falsified` against evidence
that actually *confirms* the basis. The orchestrator's coverage-check caught all
three; each cost a re-dispatch round-trip (~85k subagent tokens + an
orchestrator turn).

1. **Dependents-scope excludes benign textual mentions** (U35/D4): subagent
   declared `any-outside-scope:{settlement.py}` for a symbol grep whose own
   result contained a *comment line* in a file that was in the unit's locked
   edit scope — mechanical falsification on a non-caller.
2. **Same shape** (U36/D5): `any-outside-scope:<dir>` for a producer-enumeration
   grep whose result contained a docstring mention and a comment outside the
   dir — neither a producer. Accepted correction: a **call-shaped pattern**
   (`symbol(`) + scope = the exact call-site file set, with each match
   classified (call-site / def / re-export / mention) in the result field.
3. **`expected-match` aimed at an absence claim** (U36/D3): the basis's
   pre-state is "field NOT present on the class"; the subagent could only bend
   `expected-match` (shape-mandated for target-existence) at the absent
   construct — mechanically `falsified` by the very absence the basis claims.
   Accepted correction: `expected-match` on the **receiving construct's
   presence** (the class def line), with the field-enumeration absence evidence
   carried in the result field.

Both runs converged clean after correction; **no [VERIFIED] entry was actually
falsified** — all three were declaration-form errors, not real basis breaks.

## Why spec-root, not model-root

- The closed predicate set has **no native form for absence claims**
  (target-existence/behavior are locked to `expected-match`, which is
  presence-shaped), so an absence pre-state forces the subagent to improvise.
- Nothing in the dispatch-brief template tells the subagent that a
  dependents-scope must be **coherent with the claim-unit** — enclosing (or
  pattern-excluding) known-benign non-code matches (docstrings, comments,
  re-exports) when the basis enumerates callers/producers.
- The same model (opus) performed soundly on every other artifact leg in both
  runs; the errors cluster exactly where the spec under-specifies.

## Proposed fix (smallest first)

1. **Two sentences in the dispatch-brief template** (return-state expectations
   (d), or the per-dispatch (c) scope text):
   - *Dependents coherence:* a `target-dependents` candidate must either use a
     match-pattern that cannot hit textual mentions (call-shaped, def-shaped),
     or declare its scope as the exact known match-file set with non-code
     matches classified in the result field; a scope narrower than the unit's
     own locked edit-target set for the searched symbol is malformed.
   - *Absence rendering:* a basis whose claimed pre-state is the ABSENCE of a
     construct renders its candidate as `expected-match` on the **receiving
     construct's presence**, carrying the enumeration that evidences the
     absence in the result field — never `expected-match` targeting the absent
     construct itself.
2. **(Heavier, only if 1 proves insufficient)** extend the closed predicate
   enum with `absent-match:<pattern>` (result CONTAINING the pattern is
   falsifying), shape-coherent for target-existence/behavior absence
   pre-states. Weigh against keeping the enum minimal; option 1 alone would
   have prevented all three observed instances.

## Cross-references

- `basis-recorded-query-fidelity.md` — nearest neighbor, different object:
  there the *basis's recorded query* may not reproduce its conclusion; here the
  *falsification candidate's declaration* mis-computes against a true basis.
  Both are declaration-vs-reality fidelity gaps on opposite sides of the
  attack.
- `convergence-mechanical-pass-value.md` — the coverage-check's catch record
  here is evidence FOR the mechanical pass earning its cost (its
  orchestrator-computed verdict is what exposed the malformed declarations).
- Evidence trail: the two run trackers + `.passes.md` artifacts in
  beat-the-books `.clippy/runs/`, and the orchestrator re-dispatch corrections
  accepted verbatim (session 2026-06-10).
