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

**Relates to:** `auto-battle-cadence-mode` (sibling ⑦ mode-mechanic — cadence vs
weight; distinct concerns) · the framework's existing behavior-preserving
classification (verify already uses delta-vs-fresh re-verify — extend that
*forward* to right-size the whole cycle) · D7 carry-forward removal (the negative
precedent).

**Next action:** none until campaign ⑦ is un-deferred. When it is: settle the
"who certifies light, non-circularly" fork WITH the operator (decide-ahead),
then run anneal-dev.

**Filed:** 2026-06-05 (session-strategy campaign map — captured the
proportional-weight idea raised during the rate re-assessment so it isn't lost;
no-silent-deferral).
