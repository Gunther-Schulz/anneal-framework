# Self-improvement signal architecture — the caught/missed × known/novel map (umbrella)

**Status:** [PARTIAL] — organizing **umbrella**, operator-raised 2026-06-08 (session 14). Frames a cluster of
existing items as one coherent design so they stop fragmenting (the "backlog is a corpus too" discipline at
cluster scale). Carries the **prune analysis** the operator asked for (does receipt/tracker overlap
self-review?) and the consolidation it licenses. The spec-touching part (narrowing `post-run-review`'s
scope, `modules.md` §4) → anneal-dev + kernel-independent verify; the backlog item-merges are a flat
restructure (operator-confirmed). **▶ Item-merge EXECUTED 2026-06-08** — `self-review-missed-side` created;
`post-run-review-failure-class-register` archived; `surface-non-task-observations` (b) folded. The
post-run-review **scope-narrowing** (modules §4) remains the owed spec cycle (anneal-dev).

## The frame: every framework-improvement signal is one cell of a 2×2

| | **Known class** | **Novel class** |
|---|---|---|
| **Caught** (in the tracker) | **Q1** — `framework-gap-receipt`: tally the caught falsification pattern; recurrence (esp. post-[VERIFIED]) → re-sequence. *In-tracker, automatable.* | **Q4** — *empty by construction* (a check that catches it encodes the class → it's known). |
| **Missed** (escaped all checks) | **Q2** — a per-known-class probe: "did this run exhibit class X *without* catching it? — evidence or clean." | **Q3** — open-ended self-review + operator live-probing + production reality. *Un-enumerable; the only source of NEW classes.* |

**The learning loop** (the cells feed forward): **Q3** discovers a novel escape → it enters the shared
**failure-class register** (the vocabulary all cells read) → **Q2** now probes for it as known → once it
recurs and proves enumerable, **Q1**'s receipt routes it to lens/sequencing → it becomes **caught**.
Novel → known → caught. That *is* the self-improvement loop, organized.

## The prune analysis (operator's question: does receipt/tracker overlap self-review → can we prune self-review?)

**Answer: NO — not in a way that licenses pruning self-review against the receipt.** They are *opposite
rows* of the 2×2:
- The **tracker is a record of a converged run — i.e. a record of SUCCESS.** Everything in it was caught and
  resolved. It is **structurally silent on escapes** (a defect that escaped left no finding). So the
  **receipt** (which reads the tracker) can only ever surface *how we succeed* (caught-pattern → re-sequence).
  It is **blind to escapes by construction** — the Gödel/blind-spot wall.
- **Self-review is the entire MISSED row** — the only signal for escapes (Q2) and novel classes (Q3).
- **Decisive (the operator's own principle):** *the lens set can never be complete.* The tracker holds only
  what the **incomplete** checks caught. Pruning self-review against the receipt would assume the checks are
  complete — which they provably aren't — and would **delete the only escape-detection there is.** The
  irreducible Q3 (operator + production reality) is exactly the un-enumerable residue that nothing automatable
  can reach.

**So the prune instinct is half-right — but the redundancy is WITHIN self-review, not between self-review and
the receipt.** The three "self-review items" are not independent; they are **components of one missed-side
design**, fragmented:
- `post-run-review` (live, `modules.md` §4) — the operator-invoked missed-side review. Currently attempts
  Q1+Q2+Q3 muddled.
- `post-run-review-failure-class-register` — is **Q2** (the per-known-class probe) + the **shared vocabulary**.
- `surface-non-task-observations` **(b) protocol-tension** — is a **Q3 feeder** (a framework-gap noticed at
  runtime). *(Its (a) work-observation half is NOT in this cluster — that's an operator-awareness channel for
  work-product issues; leave it separate. Do not over-merge.)*

## The consolidation this licenses (the real Pareto reduction)
1. **Merge the missed-side into one self-review design — ✅ DONE (2026-06-08):** `self-review-missed-side`
   created; `post-run-review-failure-class-register` absorbed → archived; `surface-non-task-observations` (b)
   folded (its (a) half kept standalone). **3 items → 1 design.**
2. **Narrow `post-run-review`'s scope to the missed-side** (drop its caught-side ambitions — the receipt owns
   Q1). A Pareto *reduction* of the live mechanism. Spec change (`modules.md` §4) → anneal-dev.
3. **Keep separate, do NOT merge:** `framework-gap-receipt` (Q1, the caught-side mechanism — opposite row);
   `surface-non-task-observations` (a) (operator work-observation channel); the irreducible Q3 (operator +
   production reality — un-prunable).

**Correction this forces to an earlier claim:** the receipt was called "the Tier-A sourcing mechanism" for
`anneal-self-improvement-loop`. With the 2×2 that's only half — the receipt sources the **caught** side
(re-sequencing); the regression net's *known-failures-with-oracles* come from **Q3 escapes promoted through
Q2** (self-review is the **escape-side** sourcing). Both feed the loop, opposite sides; neither supersedes
the other.

## Relates to (the cluster members + their cells)
- `framework-gap-receipt` — **Q1** (caught×known). Separate mechanism; opposite row from self-review.
- `self-review-missed-side` — the **unified missed-side design** (Q2+Q3); absorbed
  `post-run-review-failure-class-register` (→ archived) + `surface-non-task-observations` (b).
- `surface-non-task-observations` — **(a)** stays standalone (work-observation); its **(b)** folded into
  `self-review-missed-side`.
- `post-run-review.md` / `modules.md` §4 (live mechanism) — *proposed: scope-narrow to the missed-side* → anneal-dev.
- `anneal-self-improvement-loop` — the loop this organizes the SIGNAL for (receipt = caught-side sourcing;
  self-review = escape-side sourcing).
- `framework-blindspot-class-analysis` — the *proactive* Q3 populator (imagined-ahead classes), complement to
  the receipt's empirical caught-side.
- Conceptual spine: the **enumerable/un-enumerable boundary** + **2+1 leg model** (session 14). The caught/known
  cells are enumerable/automatable; the missed/novel cell is the un-enumerable, operator-irreducible core.
- Origin: operator, 2026-06-08 (session 14).
