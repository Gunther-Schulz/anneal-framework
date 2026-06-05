## V-29. Register focus-payoff — does the foundation-invariants register SHRINK the operator's soundness pass, or add net artifacts?

**Status: FIX-SHIPPED (2026-06-04, commit 35cc329).**

**Kind: quality-watch.** The fix is a form-change (the foundation-invariants register produces a focusing holds/violates ledger that aims the operator's soundness pass) with no catcher — so it closes on a *produced-clean* instance: a method-kernel edit where the focusing artifact narrows the pass to the named touched invariants plus a small scoped residual, where the old open-ended "is this sound?" would have been the whole pass, counterfactual shown (see README closing rule).

**Decision (`dev-notes/foundation-invariants/` register + the method-kernel-edit
verify wiring at `development-process.md` §2 / step-4 / `hooks/commit-msg`; run
`foundation-invariants-register`, 2026-06-04).** The register pairs each
load-bearing kernel invariant with a genuine external anchor; a method-kernel edit
produces a per-touched-invariant holds/violates-against-anchor ledger that is the
**focusing input** to the operator's soundness pass — naming which invariants the
edit touches and which anchors to satisfy, so the operator's review is *aimed*
rather than open-ended ("is this sound?").

**Why uncertain (intent-falsification round-1 finding N2, this run).** The headline
claim — the register *shrinks and focuses* the operator's soundness work — is
**unproven**. The empirical grounding cited at design time (3 foundation edits
shipped via anneal-dev, each closed by an operator "ship it") does **not** establish
that the operator's cost was re-deriving the **known** invariants (which the register
shrinks) versus judging **novelty** (which the register structurally cannot touch —
the anti-false-comfort residual). If the binding cost was the novel judgment, the
register adds artifacts (5 entries + README + a discharge line + a hook marker) and
removes nothing from the half that actually costs. Whether the focus-payoff is real —
vs. net artifact-addition — is not judgeable ahead of operation. (The anchor-grounding
value holds regardless; this watch is only about the *focus/shrink* claim.)

**Production signal to watch (n≥1).** A real method-kernel edit where the register's
focusing artifact demonstrably **narrows** the operator's soundness pass — the
operator's review reduces to "do these named invariants still hold against their
anchors?" plus a small, scoped novel residual, where the *old* open-ended "is this
sound?" would have been the whole pass (the counterfactual shown). That is the
**quality-watch produced-clean** evidence the focus-payoff is real. Conversely, a
stretch of method-kernel edits where the operator's effort is dominated by novel
judgment the register could not touch — the register having added its artifacts
without shrinking the pass — is evidence the payoff is marginal and the register's
standing cost warrants reconsidering (or that its value is the anchor-grounding alone,
not the focus claim).

Per `development-process.md` practice 8, this V-N is legitimate: genuine uncertainty
about a shipped design choice's **payoff**, to settle empirically — not deferral of a
classifiable fix (no fix is in hand; whether the register focuses the pass is an
empirical question about operation, not a mechanism the run withheld).

---

**n≥1 observation (`anneal-dev-model-tier-policy` run, 2026-06-04 session 7) — MIXED, leans
produced-clean on the SCOPE claim.** The focusing artifact named INV-3 as the sole touched
invariant (holds on context-isolation; F8 the surfaced residual) and INV-1/2/4/5 untouched.
The operator's soundness pass was demonstrably **aimed** — it reduced to "does INV-3 hold, and
is the F8 verify-cross-tier-diversity trade acceptable?" rather than open-ended "is this
sound?". That is real **scope-shrink** evidence (the counterfactual open-ended pass would have
re-derived all five invariants). **But** the register did NOT make the residual *judgeable* on
its own: the operator initially accepted ("sound-as-is"), then asked for a plain-language
unpacking of F8 before genuinely rendering the verdict — i.e. the focus named the right thing,
the judgment still cost. Consistent with the anti-false-comfort residual above: the register
shrinks WHAT to judge (the known-invariant scope), not the cost of judging the novel/irreducible
part. One data point, true-positive on focus, not a false-accept measurement; keep WATCHING.
