# Framework-gap receipt — cross-run falsification-pattern tally → lens / framework / neither routing

**▶ SHIPPED + ARCHIVED 2026-06-15 — `6673e29` (main, pushed).** Built via anneal-dev (run
`framework-gap-receipt`, auto-battle, opus). Shipped as **practice 13 "Periodic framework-gap receipt"**
in `development-process.md` (+ the intro machinery-enumeration in both homes: development-process.md +
README.md). The convergence cycles caught 8 design seams fixed before [READY] (overloaded-flip confound,
SG4 internal contradiction, pass-type-vs-landed-type, auto-battle binder gap, README missed-dependent);
verify [PASSED] isolated. 2 irreducible residuals stated in the practice (weak class-label; lens/framework
fits-both). Run records: `.anneal-dev/runs/framework-gap-receipt.*`.

**Status:** SHIPPED (was [READY]) — operator-raised 2026-06-08 (session 14), **NEXT-UP #1** (ahead of
`investigation-pass-lens-priming`). **Additive machinery OUTSIDE the per-run kernel** — a *periodic,
post-hoc reader* of existing run records, not a new per-run obligation. The low-risk first cut (it
*tells you* whether kernel questions like investigation-pass priming are real, before you touch the
kernel). Implementation is dev-process / corpus-evolution machinery → anneal-dev when built; but its
defining property is that it does **not** touch `core.md` cycle machinery — it reads what the cycles
already persist.

## The gap (grounded in the Unit-31 beat-the-books run-record analysis, session 14)
Clippy's run records (`.clippy/runs/*.md` + `*.passes.md`) are **100% object-level**: they record what
falsification caught about *the design*, and every finding **self-heals within the run** (the design
reaches [READY]; the D-entries re-lock). The **meta-signal** — what the *pattern* of falsifications says
about the **framework's own** adequacy — is implicit and never extracted. (Grep of the 64KB Unit-31 run
record: the *only* framework-level mention is one inline `"Not a framework gap"` — a bare dismissal.
There's a latent instinct to ask "is this a clippy gap?" but no channel and no receipt.)

Concrete instance the receipt would surface: across Unit-31's 9 convergence cycles, the **same class**
(enumeration / co-producer completeness) was falsified **twice, both post-[VERIFIED]** (cycle 3: D2
scoped its grep to `src/`, missed `tests/`; cycle 5: missed the arb co-producer at `:2899`). That
repetition is a framework signal — invisible in the per-run record, visible only by tallying across
cycles.

## The mechanism
A **periodic, post-hoc, fresh-context** pass over the run records (`.passes.md` and equivalents across
instances): tally falsification findings **by class**, detect **recurrence**, route each recurring class
via the boundary discriminator. A *reader* of existing artifacts; runs at the operator's framework-review
cadence ("which we periodically implement"), not per run.

**The routing discriminator (the boundary applied to the machinery itself):**
> Names a **new thing to look *for*** (enumerable, general, currently uncovered) → **lens**. Changes
> **how the looking is *structured*** (cycle count, convergence criterion, independence, **sequencing**)
> → **framework**. Otherwise → **neither** (one-off: domain-specific, non-recurring, or "falsification
> caught it as designed; system working") — the **default**.

**Split the tally by pass-type — the split *is* the router:**
- A recurring **mechanical**-falsification class = enumerable → **lens-or-sequencing** question (Unit-31:
  the Consumer-enumeration lens *exists and fired* → the gap is it caught *late* → **re-sequence**
  (force it at design-lock), **not** add a lens).
- A recurring **intent**-falsification class = judgment → a much stronger **framework-gap** signal (the
  forming context keeps mis-serving intent), and almost never a lens candidate (you cannot compress an
  intent-fidelity check into a checklist item).

**Scope of this router — caught-side only.** The pass-type split routes only what falsification *caught*
(this is a Q1 mechanism). **Escapes have no pass-type** — no pass caught them — so the *missed* side routes
by self-review (`self-review-missed-side`, Q2/Q3), **not** by this split. This is also *why* the receipt and
self-review don't merge (the umbrella's prune analysis): the router is pass-type-based, and pass-type exists
only for caught findings.

## What's already free vs. what needs building
- **Coarse routing is free** — already in the artifacts. Each falsification finding is tagged by pass
  (`Intent-falsification` vs `Mechanical falsification`) and route (`mechanical-falsification-candidate`
  vs `[VERIFIED — surfaced]`, `modules.md` §3.4/§3.4.1). That pass/route tag *is* the enumerable-vs-
  judgment split; mechanical-recurrence vs intent-recurrence is tallyable from what's persisted.
- **Fine class-recurrence needs the post-hoc pass** — the *specific* class (consumer-enum vs branch-
  coverage vs …) lives in the finding prose, not a tagged field. A fresh context assigns the class and
  tallies. The Unit-31 descriptions are rich enough to classify post-hoc (verified, session 14).

## Load-bearing safeguards (state all, or it Goodharts / accretes)
1. **A falsification firing is NOT a framework failure** — usually it's the framework *succeeding*
   (catching the class is the point of the loop). The signal is narrower: the *same class recurring
   within one run, post-[VERIFIED]* = the forming discipline isn't internalizing what falsification keeps
   teaching → re-sequence. A single catch = system working.
2. **Mechanical detection of the pattern; human judgment on the interpretation.** The operator *binds*
   lens/framework/neither (calibrating, not per-finding) — the RLHF shape: operator as reward-model
   *calibrator*, not per-case adjudicator. Auto-promoting "recurring class → new lens" walks straight
   into `lens-crowding` (piling lenses trades off against broad search).
3. **Recurrence usually → re-sequence/strengthen EXISTING structure, not new lens.** Recurrence is
   evidence for *re-sequencing*; only *novelty + generality* is evidence for a *new* lens. The receipt
   forces that justification every time (guards the additive-reflex anti-pattern).
4. **Outside the kernel.** A reader of existing run records, not a per-run tracker field — keeps the
   kernel lean, and gives the classification its own fresh-context independence.

## Relates to
- `post-run-review-failure-class-register` — **composes, distinct.** Shares the failure-*class*
  vocabulary, but: that = a register the *per-run self-review* probes for *defects the run produced*
  (object-level, modules §4 method-kernel, raises self-review recall); this = a *cross-run* reader of the
  *falsification pattern* (meta-level, outside-kernel) that *routes framework edits*. The receipt is one
  **producer** that feeds recurring classes *into* the register (per its "novel classes feed back / it
  grows" rule).
- `framework-blindspot-class-analysis` — the *proactive-enumeration* populator; the receipt is its
  *empirical / falsification-derived* complement (classes found by what the loop actually caught,
  recurrently, vs classes imagined ahead).
- `surface-non-task-observations` — the (b) protocol-tension channel (runtime-surface → dev-time-resolve);
  the receipt is the systematic, falsification-pattern-grounded version of that dev-time signal.
- `anneal-self-improvement-loop` — the receipt is a **Tier-A sourcing mechanism**: it produces grounded,
  real known-failure classes (from production runs, not self-imagined — failure-mode 2) that seed the
  regression net.
- `investigation-pass-lens-priming` — the receipt is the **consumer** that would detect whether
  breadth/omission-class misses cluster, i.e. it produces the evidence that item's priming-on/off test
  isolates. (Build the receipt first → it tells you whether the priming kernel-edit is worth running.)
- Conceptual spine (session 14): the **2+1 leg model** (2 dynamic legs — iteration, independence — + 1
  static prosthetic, the lens set) and the **enumerable/un-enumerable boundary**; the routing
  discriminator *is* that boundary applied to the machinery.
- Origin: operator, 2026-06-08 (session 14), grounded in the Unit-31 `.passes.md` analysis.
