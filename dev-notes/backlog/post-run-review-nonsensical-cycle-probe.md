# Post-run review should catch ANY nonsensical / wasteful cycle — not only protocol-forced grind, not a fixed catalog

**Status:** OPEN — operator-clarified 2026-06-06 (during the `v-entry-is-post-ship-only` run:
"when I said post review should catch such nonsensical cycles I meant it should catch **any**
nonsensical cycles"). Framework: `post-run-review.md` Q3 (corpus-evolution) + possibly
`spec/modules.md` §4 post-run-review minimum-shape (**method-kernel**) → anneal-dev +
kernel-independent verify. NOT urgent; a sharpening with a clear edit site.

## The gap
The post-run review's **Q3 (Grind — cost)** asks: *"where did effort go… repeated work… identify
any work **the protocol forced** but the run didn't need."* Its lens is **protocol-forced
overhead** (ceremony, attestation, repeated passes). It does **not** catch
**orchestrator-discretionary** nonsensical cycles — work the run chose to do that produced no
requirement-serving value: circular work (produce a clause, then revert it), net-zero cycles,
cycles that didn't advance the design toward the requirements. The protocol didn't *force* those;
the orchestrator's own (mis)judgment did. So Q3, as written, slips them.

**n=1 (this run).** Cycles 7–8 of `v-entry-is-post-ship-only`: cycle 7 *added* a discriminator
clause (gold-plating, beyond the requirements); cycle 8 spent a fresh opus dispatch attacking it;
the clause was then *removed*. Net contribution to the shipped design: zero. Two cycles + two
dispatches of self-inflicted, non-protocol-forced waste. Q3's "work the protocol forced" framing
would not flag this — the protocol didn't force it.

## What the operator's "any" requires (two edges)
1. **Source-agnostic.** Catch a nonsensical cycle whether the *protocol* forced it (Q3 today) OR
   the *orchestrator* inflicted it (the gap). The test is outcome-based: did the cycle's work
   advance the design toward a requirement, or was it circular / reverted / net-zero?
2. **Open-ended, not a catalog.** "Any" — not "did this run exhibit known-wasteful-shape X?". A
   fixed catalog of wasteful-cycle shapes becomes blinders (the same lens-narrowness the
   `post-run-review-failure-class-register` item warns about). The probe asks the general question
   and lets the model surface novel shapes; confirmed shapes can inform a brake, but the probe
   itself stays general.

## Fix shape (sketch)
Broaden Q3 (or add a sibling probe) so its artifact-forcing question covers **any cycle whose work
did not advance the design toward the requirements record** — circular / reverted / net-zero —
**regardless of source** (protocol-forced *or* orchestrator-discretionary). Keep Q3's existing
artifact-forcing discipline (quote the cycle's tracker lines / pass artifacts; specific examples,
not impressions). The evidence already exists in the tracker (a D-entry [VERIFIED]→[INVALIDATED]→
reverted, or a cycle that added then removed prose) — so the probe is artifact-checkable.

## Sharpening — diagnose convergence-failure causes, not just flag waste (operator note 2026-06-06)
"Catch any nonsensical cycle" has a high-value special case: **a convergence cycle that
*failed to converge*** (produced a D-delta → forced another cycle). The probe should, for each
such non-convergence, **classify the cause**: a *legitimate* defect-catch (the cycle correctly
reopened the design — e.g. this run's cycles 4/6 caught the over-narrow axis + the collision) vs
a *nonsensical* one (chased an addition the requirements didn't need — cycles 7/8's gold-plating).
The diagnosis is what separates "the convergence cycle earning its keep" from "the convergence
loop amplifying churn" — and names the cause (gold-plating, unbounded requirement, mis-scoped
design, …) so it routes to the right fix (`convergence-surfaced-finding-action-brake`,
`proportional-cycle-weight`). This is the per-cycle granularity of the general probe, aimed at the
convergence loop specifically.

## The two-axis map (why this is its own cell, not a fold)
|              | known/specific shape           | any/open-ended                                  |
|--------------|--------------------------------|-------------------------------------------------|
| **preventive (in-run gate)** | `convergence-surfaced-finding-action-brake` (the action-time brake, one shape) | — (a general in-run brake is hard; that's why the detective net matters) |
| **detective (post-run)**     | `post-run-review-failure-class-register` (output-defect *classes*) | **THIS ITEM** (process-level nonsensical *cycles*, any source, open-ended) |

The register item catches **output-defect classes** (defects that could ship); this catches
**process-level wasted cycles** (no defect ships, but effort burned + a method weakness signalled).
Different objects → different cell.

## Relates to
- `convergence-surfaced-finding-action-brake` — the **preventive, single-shape** counterpart; this
  is the **detective, general** net behind it (the brake stops the known shape; the probe catches
  whatever the brake doesn't, including novel shapes). Two sides of "wasteful cycles."
- `post-run-review-failure-class-register` — sibling post-run-review probe; **distinct object**
  (output-defect classes vs process-level nonsensical cycles) — share the *additive / not-blinders /
  open-ended* discipline; sequence/compose them when either is worked (likely the same `modules.md`
  §4 + `post-run-review.md` edit pass).
- `anneal-reliability-measurement` — the cost/token-metric thread; a wasted-cycle probe composes
  with cost telemetry (Q3's cost-data discipline).
- `post-run-review.md` Q3 (Grind) — the edit site; `spec/modules.md` §4 — the kernel minimum-shape.
- Origin: `v-entry-is-post-ship-only` run, operator clarification 2026-06-06.
