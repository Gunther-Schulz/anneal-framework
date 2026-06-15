# [READY] / fresh-session-implementability — orchestrator-self-attested verdict

**Status:** [DESIGN] — promoted 2026-06-05 from `intent-falsification-soundness-sweep`'s
"Unswept" register (where it was logged as a NEW target discovered by running the move-1
cycle). Standalone because it has its own scope, observed n=1, and anneal-dev cycle.
Sibling failure-class fix to `convergence-sequencing-enforcement` (L1 shipped today,
`f74b145`) — same class, different corner of the kernel.

## The gap
[READY]'s gates — fresh-session-implementability ("would a fresh session implement without
a new design decision?"), standardized-coverage-accounted-whole, the convergence-clean
judgment — are **orchestrator-self-attested**: the same context that wrote the design
judges it ready, with per-step citations but no fresh-context re-derivation of the
**readiness verdict itself**. The convergence cycle exists to catch design-vs-intent gaps,
but the [READY] machinery's own gates fire *upstream* of it.

## Observed instance (seed, 2026-06-05)
In `move1-s3.1-honest-relabel`, the fresh-session-implementability test self-attested
**PASSED at cycle 2** — yet the downstream fresh-context convergence cycle (cycle 3+)
caught two real design refinements (F-C "external terminus" under-defined; F-A
render-tracking), which a genuinely-implementable design would not have surfaced. The
implementability self-judgment under-detected; only the convergence cycle (a real
fresh-context pass) caught it.

Same "self-recorded verdict < fresh-context check" class as L1's parallel-dispatch trap,
at a different machinery point.

## Class membership (failure-class catalog from `intent-falsification-soundness-sweep`)
- **Class (i) — self-dischargeable enforcement:** the [READY] verdict is produced and
  judged in the same context; no independent tie.
- **Class (iv) — false-comfort artifact:** the per-step citations make the artifact READ
  as evidence-bearing, but the *readiness judgment itself* has no fresh-context check
  — comfort is generated before the convergence cycle's catch fires.

## Fix direction (design seed, not the locked design)
Two candidates:

1. **The convergence cycle IS the fresh-context re-derivation of the readiness verdict.**
   It already exists. The "fix" may be procedural — *don't present [READY] until the
   convergence cycle is observed clean*, with the implementability-test PASSED line
   produced at the convergence cycle's closing (fresh-context-produced), not at the
   cycle that proposes the design. Partly already the case (convergence cycle is
   required); the gap is the implementability line being produced earlier.
2. **A fresh-context dispatch for the implementability test itself** — a sibling to
   intent-falsification, dedicated to "fresh session implements without surfacing new
   design decision." Heavier; likely not Pareto over (1).

Prefer (1) (uses existing machinery; fewer new constructs).

## Disposition leaning (2026-06-05 — flagged during campaign ②; operator-raised)
**Likely close-as-substantially-covered-by-convergence — not new machinery.**
- The convergence cycle's fresh-context passes (intent + mechanical) ALREADY re-derive
  design-soundness independently. The residual is narrow: **fresh-session-implementability**
  (specification-completeness-for-impl — a distinct axis from soundness) is
  orchestrator-self-attested. But convergence **backstops** it: the n=1 seed itself shows the
  optimistic cycle-2 self-PASS was caught by the convergence cycle — no bad [READY] resulted.
- **Token-efficiency test (operator framing — "most token-efficient without sacrificing
  value/performance"):** fix-option 2 (a dedicated fresh-context implementability dispatch)
  adds a whole subagent dispatch for marginal value over convergence's existing catch — **not
  Pareto**. Fix-option 1 (anchor the implementability line at the convergence cycle's closing)
  is ~free and procedural.
- **Live dogfood (campaign ②, run `campaign2-completeness-rigor`, 2026-06-05):** the
  fresh-session-implementability PASSED line WAS produced in the convergence-clean block (already
  follows option 1); the convergence cycle's fresh-context passes caught **all 3 real D-deltas**
  (D2/D4/D5 re-forms), while the self-attested implementability line was secondary. Confirms
  convergence is the load-bearing gate; the readiness self-attestation rides on top harmlessly.
- **Leaning when ① runs:** close as covered, at most a one-line procedural note (option 1); do
  NOT add option-2 machinery. The self-attestation is acceptable *because* convergence backstops
  it — adding a check costs tokens without proportional value.

## Relates to
- `intent-falsification-soundness-sweep` — promoted out; sweep's Unswept register should
  cross-reference here.
- `convergence-sequencing-enforcement` — sibling failure-class fix shipped today.
- V-11 (per-step external evidence), V-16 (design-validity-at-ready) — adjacent watches;
  this is distinct (the *readiness verdict's* self-attestation, not the per-step evidence form).
- V-30 (`form-not-binding-class-recurrence`) — empirical watch on the broader class; this
  finding feeds it.
