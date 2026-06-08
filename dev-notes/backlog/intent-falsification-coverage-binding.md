# Intent-falsification sharpenings — bind requirement-coverage completeness at convergence (+ criteria from verbatim)

**Status:** OPEN — operator-raised **and agreed** 2026-06-08 (session 14). **NEXT-UP #2** (after
`framework-gap-receipt`; ahead of `investigation-pass-lens-priming` — this is *agreed + ungated*, priming
is *test-first + gated on the receipt*). **Method-kernel edit** (`core.md` §4.1.4 / §3.4.1 + `modules.md`
§3.4.1) → anneal-dev + kernel-independent verify (skill-craft form + operator soundness + foundation-
invariant register check) per CLAUDE.md. Likely **one campaign** with `investigation-pass-lens-priming`
(both touch the convergence machinery).

Both sharpenings share one shape: **pull the *enumerable* parts of intent-coverage upstream — from verify
(§4.3, post-implement) to bind at convergence (pre-implement)** — cheaper, and forces explicit disposition
before [READY]. The "front-loading / catch-earlier" probe (`post-run-review-failure-class-register` §
design-quality probes) applied to the intent pass. Neither raises the *ceiling* (intent never stated stays
the operator's irreducible residue — `core.md` §4.1.4 "not a soundness certificate"); they raise the floor.

## Sharpening 1 (primary) — bind requirement-coverage *completeness*
**Current:** the intent pass's bind route fires only when a finding "reduces to a §3.4 coupling-shape
falsification of a [VERIFIED] D-entry's basis" (`core.md` §4.1.4, ~:616). A requirement with **no serving
decision** (the Unit-31 "decline half unserved" / R5 case) has no entry to falsify — the problem is
*absence* — so it routes to `[VERIFIED — surfaced]` (~:623), dispositionable away; the real coverage
backstop is **verify §4.3**, which is *post-implement* (an expensive loopback through implement).

**The sharpening:** "is every R# served by ≥1 decision" is **enumerable** (a coverage matrix with no empty
rows) → by the enumerable/un-enumerable boundary it should **bind**. Make the **R#→D# coverage matrix** an
explicit artifact; an **empty row holds the phase** and forces an explicit disposition (serve / descope /
reject-the-requirement). The *quality* of each mapping stays judgment (surfaced); only the *completeness*
(no empty row) binds.

**Why it's Pareto / consolidation, not addition:** coverage is *already* checked — informally in the per-R#
attack lines, formally at verify §4.3. One explicit matrix read by *both* = a single source of truth,
caught at the **cheapest (pre-implement)** point, reducing late verify→implement loopbacks. Surfaced by
applying the session-14 boundary discriminator to the pass's *own* routing — the bind-route covers
"coupling-shape basis falsification" but misses "coverage completeness," equally enumerable.

## Sharpening 2 (secondary, weaker) — criteria-first re-derived from the *verbatim* request
**Current:** criteria-first derives success criteria from "the requirements record" (`core.md` ~:599),
which holds *both* the R# enumeration *and* the operator's verbatim request (`core.md` §4.1, ~:396). If the
fresh context derives from the pre-chewed **enumeration**, it inherits any mis-capture the working context
made (the acknowledged never-captured residual, ~:609 — "reduced by verify's requirements-coverage check,
not eliminated").

**The sharpening:** derive criteria from the **verbatim** request, and attack "does the R# enumeration
faithfully capture the verbatim?" — catching enumeration-*capture* errors at convergence instead of at
verify. **Honest bound:** a requirement in *neither* verbatim *nor* enumeration (a genuinely unspoken
assumption) stays invisible — this shrinks the *capture-error* residual, not the *unstated-intent* one. And
for terse requests there's little verbatim to re-derive from → uneven value. The weaker of the two.

## Relates to
- `post-run-review-failure-class-register` — the **sibling intent-pass enrichment** (its §design-quality
  probes propose adding *judgment* attack-criteria — workaround-vs-principle, proportionality, … — to the
  intent pass). This item adds an *enumerable completeness* bind. **Orthogonal axes; likely co-designed**
  in the same convergence-machinery cycle.
- `V-28-never-captured-requirement` (validation-watch) — the residual sharpening 2 reduces (not eliminates).
- verify §4.3 requirements-coverage (`core.md`) — the *downstream, post-implement* backstop these pull
  upstream to bind pre-implement.
- `investigation-pass-lens-priming` — sibling `core.md` §4.1 convergence-machinery kernel edit; likely one
  anneal-dev campaign.
- Conceptual spine: the **enumerable/un-enumerable boundary** (session 14) — sharpening 1 *is* that boundary
  applied to the intent pass's routing.
- Origin: operator, 2026-06-08 (session 14), agreed in-thread.
