# Investigation-pass lens priming — keep the legs pure (should the lens set prime the investigation pass at all?)

**Status:** SHIPPED 2026-06-15 (`7880be6`, run `convergence-machinery-batch`; batched with #2 as D2/D3'). V-32 instantiated at ship. Archived. — **REMOVAL DECIDED (operator, 2026-06-08, session 14).** Removed the lens-set priming of
the investigation pass (keep the legs pure); **ship-and-observe via daily use + the `framework-gap-receipt`
watch, NOT a controlled test** (see Decision below — consistent with the project's revealed-preference-over-
toy-tests finding). **Agreed + ungated → one convergence-machinery campaign with
`intent-falsification-coverage-binding`.** A **method-kernel edit** (`core.md` §4.1, the investigation pass)
→ anneal-dev + the kernel-independent verify (skill-craft form + operator soundness + foundation-invariant
register check) per CLAUDE.md "Method-kernel edits"; the verify **must confirm the implementation constraint
below**.

## The question
Today a cycle's **investigation pass** is primed by the lens set: "The standardized lens set is known
going in and **informs what the AI attends to** (not how it investigates)" (`core.md` §4.1, line ~345).
Does that priming **help** (raises coverage — the AI keeps known blind-spots in peripheral view while
following its natural lead) or **hurt** (anchors/narrows the natural search — the crowding effect)?
Operator is genuinely unsure; this item isolates it as a testable kernel question.

## The structural argument (why the lean is "priming is the suspicious part")
1. **The investigation pass has one irreplaceable job: open-ended, un-enumerable discovery** — catching
   what no lens and no mechanical check can name. That is its unique contribution; every other pass
   (standardized inspection, mechanical falsification) is *enumerable* coverage. Its value scales with
   **breadth** of attention.
2. **Priming with a fixed checklist is the one intervention that most directly threatens breadth** —
   attention is finite; a frame narrows search (functional fixedness / set effects). It taxes exactly
   the pass whose breadth is most valuable and least replaceable.
3. **The coverage priming buys is already backstopped elsewhere.** [READY] requires the *standardized
   lens set accounted for whole* (`core.md` §4.1.1) — every lens applied where its scope was touched, or
   cited out-of-scope, no lens silently absent. So lens coverage is guaranteed at the **run** level
   regardless of whether the investigation pass is primed. Priming only changes *when/whether* a concern
   surfaces during natural investigation vs. the inspection pass — i.e. it buys "early catch," not
   guaranteed coverage.

Net: priming spends the investigation pass's scarcest resource (open attention) to buy a largely
redundant "early catch," at the cost of the pass's one irreplaceable function (novel discovery).

## The clean resolution: keep the legs pure (DECIDED — see Decision below)
Run the **investigation pass unprimed** (maximize novel/un-enumerable discovery); apply the lens set
**only in the standardized inspection pass** (guaranteed enumerable coverage). Each pass stays true to
its side of the **enumerable / un-enumerable boundary** (the session-14 leg decomposition: investigation
= the un-enumerable discovery leg; the lens set = the enumerable coverage prosthetic). The only thing
lost is catching a lens-concern slightly earlier — cheap to lose.

## What removal must get right (load-bearing — the kernel verify must confirm this)
Removal is **sound iff the standardized inspection pass's lens-application is driven by the *work-product /
edit-set scope* — not by what the (now-unprimed) investigation happened to attend to.** The inspection pass
applies "each lens whose scope this cycle's investigation *touched*" (`core.md` §4.1), and [READY] requires
the lens set **accounted for whole** (every lens applied where its scope was touched, or cited out-of-scope;
no lens silently absent). **The risk:** if lens-application is gated on *investigation attention*, unprimed
investigation could leave a lens's scope untouched → the lens marked "out of scope" when priming would have
made investigation touch it and the lens fire. So the de-priming edit must ensure coverage is driven by the
**design's actual edit-set** (what the work touches), independent of attention — or carry a compensating
change. This is the concrete form of "unpriming is not pure upside," and **the one thing the anneal-dev
cycle + kernel-independent verify must get right.**

## Decision: REMOVE — ship-and-observe, no controlled test (operator, 2026-06-08)
Not gated on a controlled A/B. Rationale: the change is **reversible** (re-add priming if worse); the
structural argument (above) is strong; and a controlled toy test is exactly the instrument this project has
repeatedly found **fails to capture regime-dependent value** (`anneal-empirical-validation-experiment`:
"controlled toy tests indict the instrument, not the framework"; revealed-preference / daily use is the
more reliable signal here). The catcher is **observation, not a test:**
- **Daily-use signal** — does investigation run broader; do omission-class escapes drop.
- **`framework-gap-receipt` (Q1)** — passively detects whether omission/breadth-class misses *cluster* after
  the change. The receipt is now this change's **automatic watcher**, not a pre-test evidence source.

## Owed post-ship watch (instantiate a V-entry AT SHIP — not now; the change is still un-implemented)
A V-entry never holds an un-implemented change, so this is the *spec* of the watch, owed when de-priming ships:
- **watch-kind:** quality-watch (breadth ↔ omission-coverage trade-off).
- **claim:** unprimed investigation holds-or-improves omission-class coverage while raising novel-finding breadth.
- **catcher:** daily-use + the `framework-gap-receipt` omission-cluster signal.
- **closing rule:** omission-class escapes *rise* traceable to de-priming → re-add priming (or a lighter
  form); breadth improves / coverage holds across several runs → close confirmed.

## Why a distinct item (relate-before-add)
Sibling to `lens-crowding-vs-broad-search`, **not a fold** — both are faces of one recognition-economy
concern (finite, contested attention), but the locus and intervention differ:
- `lens-crowding` = does **lens count/stacking** in the falsification passes trade off against the broad
  sweep? Mitigation: **distribute lenses across fresh-context agents.**
- This item = should the lens set prime the **investigation pass at all?** The surgical, orthogonal case:
  the extreme "**zero lenses in this one pass**" of lens-crowding's "fewer-lenses-per-pass" corollary —
  and it stands *independent* of lens count/distribution (even one lens, even distributed, the
  prime-the-discovery-pass question remains). Cheaper test, cleaner basis (leg-purity). Pulling it out
  as its own next-up sharpens the backlog: a cheap, high-leverage kernel question rescued from a big
  paused experimental thread.

## Relates to
- `lens-crowding-vs-broad-search` — shared recognition-economy root; this is its surgical
  investigation-pass face (see "Why a distinct item"). The `lens-crowding` corollary "fewer lenses per
  pass / distribute across passes" is the general principle this item applies at the extreme to one pass.
- `anneal-empirical-validation-experiment` — the crowding anomaly (period omission 3/5 vanilla > 2/5
  adhoc) is the weak hint that lens salience can narrow the broad sweep; same mechanism, here at the
  investigation-pass-priming locus.
- `anneal-self-improvement-loop` — anti-accretion failure-mode 1; leg-purity is a structural guard
  against the enumerable contaminating the un-enumerable.
- Origin: session-14 (2026-06-08) thread — the leg decomposition (2 dynamic legs: iteration,
  independence + 1 static prosthetic: the lens set) and the enumerable/un-enumerable boundary. The
  same-session framework-gap-receipt work is the consumer that would *detect* whether breadth-class
  (omission) misses cluster — i.e. the receipt would surface the evidence this test isolates.
