# Verify's "re-open each citation" should be an explicit §4.3 leg for F-track disposition bases (not only D-track decision bases)

**Status:** OPEN — spawned 2026-06-05 by the `campaign3-enforcement-fidelity` run's cycle-3 intent-falsification pass (subagent `a0d22986f4dfa89c2`, finding F11, `[VERIFIED — surfaced]`). Filed, not folded into that run (the subagent's explicit "separate candidate, file rather than fold" disposition — it firms up MORE than D3.1). Framework-spec (method-kernel: `spec/core.md` §4.3) → anneal-dev + kernel-independent verify when pursued. Candidate ⑥ / a future de-pollution cycle (inherited surface, low urgency).

## The observation
`core.md` §3.2 (the basis rule, ~:187-190) mandates "Verifiers (§4.3) and convergence cycles re-open **each citation** to verify both the location AND the observable fact." This standing mandate is what makes a `[VERIFIED — <disposition>]` **finding** bind — verify re-opens the finding's disposition basis citation and an absent/false citation makes it malformed (§3.1) → the finding is short of [VERIFIED] → §4.3 forces [ISSUES FOUND].

But `core.md` §4.3's **four explicitly-enumerated verify legs** (planned-vs-actual, requirements-coverage, standardized-lenses, executing-the-verification) do **not** restate "re-open each F-track disposition basis citation" as an explicit leg. The obligation is real (it lives in §3.2 + §5.1 malformed-on-absence + the §4.3 finding-status ledger's "short of [VERIFIED]" malformedness) but it is **inherited/implicit**, not enumerated at the verify-leg surface where a reader looks for "what verify checks."

## Why it's load-bearing (and why it's only a watch, not urgent)
- **Load-bearing:** it is the hinge the `campaign3` D3.1 deferred-pending-authoring bind rests on — and, identically, the hinge under the EXISTING `surfaced` and `deferred (a)/(b)` dispositions. All of them bind only because verify re-opens the finding's disposition citation. If a future edit narrowed §4.3's legs to "only the enumerated four," every finding-disposition bind would silently weaken.
- **Not urgent (why surfaced, not fixed in `campaign3`):** the mandate IS present in §3.2 and the bind demonstrably holds today (the cycle-3 pass verified the chain end-to-end). This is an audit-trail / salience gap (the obligation isn't where a §4.3 reader expects it), not a live hole.

## Candidate fix (classifiable — structural, Pareto)
A one-clause cross-reference in `core.md` §4.3 making the §3.2 "re-open each citation" obligation an **explicit verify leg over F-track disposition bases** (a fifth enumerated leg, or a clause on the existing planned-vs-actual leg). Pareto: it firms `surfaced` + `deferred (a)/(b)` + the new `deferred-pending-authoring (c)` in one move (a single canonical home for the disposition-citation re-check). Behavior-preserving if framed as making-explicit-what-§3.2-already-mandates; non-behavior-preserving if it changes what verify is obligated to do — decide at design.

## Relates to
- `campaign3-enforcement-fidelity` run (D3.1, F11) — the origin; D3.1 ships independently (its bind holds on the inherited surface; this item firms the surface for ALL dispositions).
- `core-md-bloat-measure-then-cut` / a de-pollution cycle — natural co-home (both touch §4.3 / §5.1 / glossary disposition wiring).
- `intent-falsification-soundness-sweep` — same family (a bind resting on an implicit/inherited surface rather than an explicit enforced one).
