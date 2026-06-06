# Proportional cycle weight — right-size anneal-dev ceremony to the change

**What it is:** a candidate method-kernel discipline — run a *light* anneal-dev
cycle (single investigation pass, no convergence cycle, one verify) for changes
that are small / cosmetic / behavior-preserving / grab-bag, reserving full
ceremony (convergence + intent+mechanical falsification + isolated verify) for
method-kernel + load-bearing semantic edits.

**Status / stage:** DEFERRED — campaign ⑦ (rate machinery). **Practice now,
formalize only if proven.** The *practice* is already available: the operator
calls cycle-weight per item in-loop when draining a campaign. This item is the
*formalization* (a spec change making the light path a documented default) — run
it as its own anneal-dev cycle only after the practice has earned it.

**The soundness hazard (why it's not a free win):** this is the cousin of the
**carry-forward optimization removed by D7** (`f74b145`, the sweep's L1) — that
one was the WRONG simplification because it let a pass skip re-verification on
its own say-so. Proportional weight is only sound with a **non-circular certifier
of "light"**: the operator (or a non-producing checker) classifies the change's
weight, NOT the same pass that wants to skip ceremony. If the AI self-certifies
"behavior-preserving" to drop falsification, that's the exact circularity D7
closed. Encode the classifier as operator-in-loop (or an external check), never
self-attested.

**Empirical evidence (n=1, 2026-06-06 — the "proven" the deferred status waited for):**
the `v-entry-is-post-ship-only` run — a **non-method-kernel, small doc-clarification**
(re-word one state def + one exclusion sentence + a Vocab pointer) — got the **full**
ceremony: **3 convergence intent-falsification dispatches** (cycles 4/6/8) + an isolated
verify, across **10 cycles** for a ~3-edit change. Two findings:
1. **The cost was the convergence ceremony, not verify** — 3 opus dispatches vs verify's 1.
   A *light* cycle (no convergence, one verify) would have cut ~3 dispatches and kept the
   irreducible independent check. (The operator's instinct "skip verify?" aimed at the wrong
   target — verify stays; convergence is the lever.)
2. **The heavy ceremony GENERATED churn, not just cost** — each convergence cycle invited
   additive over-fixing (the gold-plating in `convergence-surfaced-finding-action-brake`);
   cycles 6–8 chased an unbounded "unambiguous" requirement's tail. A light cycle would have
   *avoided* the churn by never opening the convergence loop. So proportional weight is not
   only a cost win — for a small/non-kernel change it removes a churn *source*.
   The operator flagged the disproportion **twice** in-run (overthinking in convergence; verify
   weight) — the signal the light path was warranted and not taken.

**Relates to:** `auto-battle-cadence-mode` (sibling ⑦ mode-mechanic — cadence vs
weight; distinct concerns) · `convergence-surfaced-finding-action-brake` (complementary:
the brake prevents gold-plating *within* a convergence cycle; proportional-weight *avoids*
the convergence cycle for a light change — two levers on the same 2026-06-06 churn) · the
framework's existing behavior-preserving classification (verify already uses delta-vs-fresh
re-verify — extend that *forward* to right-size the whole cycle) · D7 carry-forward removal
(the negative precedent; the soundness hazard above is its cousin).

**Next action:** none until campaign ⑦ is un-deferred. When it is: settle the
"who certifies light, non-circularly" fork WITH the operator (decide-ahead),
then run anneal-dev.

**Filed:** 2026-06-05 (session-strategy campaign map — captured the
proportional-weight idea raised during the rate re-assessment so it isn't lost;
no-silent-deferral).
