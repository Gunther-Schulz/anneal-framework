## V-30 Form-not-binding / silent-correctness — class recurrence

**Status:** WATCHING — opened 2026-06-05 after L3 (skill-craft v1.0.58, authoring discipline)
and L1 (`convergence-sequencing-enforcement` / `f74b145`, kernel-level instance) shipped.
Watches whether the failure class **recurs** at any level despite the fixes.

**Watch-kind:** quality-watch (correctness-class recurrence; not a single rule's mitigation).

**Catcher:** any future bug whose shape matches one of the four classes catalogued in
`intent-falsification-soundness-sweep`:
- **class (i)** — self-dischargeable enforcement (gate checks an artifact the AI itself
  produces; no independent tie)
- **class (ii)** — overclaimed gate (sold as binding; actually bypassable friction or
  prose-only)
- **class (iii)** — operator-detection-dependent (silently requires operator detection;
  malformed per `foundations.md` Operator-expected-action-bound)
- **class (iv)** — false-comfort artifact (caveat placed where it is not read at the
  moment comfort is generated)

**Empirical base (n=2 at open):**

1. **Kernel level — convergence cycle's intent→mechanical sequencing (this session,
   2026-06-05).** The dependency was prose-only ("the intent pass runs first; only when
   clean does the mechanical run") in `core.md §4.1.4`. Two passes independently
   dispatchable, identical-artifacts-on-the-clean-path. AI parallel-dispatched both;
   operator caught it. Fixed at L1 by encoding the dependency in the mechanical pass's
   input + the artifact citing the verdict + coverage-check clause (v) re-deriving
   against the same-cycle intent artifact. Class (i) + (iv) shape.

2. **Instance work-product level — clippy's investigation sweeps (other session,
   2026-06-05; carried into anneal-framework via the operator).** Clippy's per-unit
   falsification verified each unit's basis correctly; cross-unit intent was unmet.
   Four bugs found:
   - replay verified green but no score producer existed (tests supplied fixture scores)
   - freshness gate's attribute-match selected wrong market for `team_total`
   - `signal_id` lossy when `team_total` dimension was added
   - alert dedup checked `autobet_bets` but later unit wrote to `autobet_paper_bets`
   Each unit was correct on its own terms; the cross-unit invariant was never locked.
   Class (i) + (iv) at the work-product layer. **Not fixed by L1** — different shape;
   addressed by the filed `instance-domain-invariant-register`.

**Watch question:** do the fixes — L1 (kernel-level structural sequencing) + L3 v1.0.58
(authoring-time dispatch-dependency discipline + scope-precedes-default principle) +
sweep Moves 2-5 + scope-item-2 + `ready-machinery-self-attestation` +
`instance-domain-invariant-register` — actually reduce recurrence of this class? Or do
new instances surface in shapes none of the fixes cover?

**Closing rule (opportunity-exercised — per `dev-notes/validation-watch/README.md`):**
closes when **(a)** every listed audit/fix has landed (the opportunity to find class
instances has been exercised), AND **(b)** the next major framework-or-instance edit
cycle does NOT surface a new class-i-iv instance. **Pure non-occurrence does NOT close**
— the opportunity must have arisen and been handled.

**Re-fire trigger:** any new bug fitting class (i)-(iv) — log here as a recurrence
datapoint, classify shape, and route to the appropriate audit.
