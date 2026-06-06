# Lens crowding vs broad search — do focused directives trade off against open-ended falsification?

**Status:** OPEN — **hypothesis / open question**, anecdotal (n=5, a single observation). Surfaced
session-11 (2026-06-06) in the real-codebase A/B. **NOT claimed** — flagged for a future controlled
test. Operator-flagged twice as "the single most interesting thing to test next."

## The hypothesis
A salient set of **focused directives / lenses** ("trace each value to its producer," "follow each
field to its consumers," …) may **pull attention toward what it names** — and *away* from the broad,
open-ended "falsify every kind" sweep that catches the bugs **no lens names** (especially *omissions*).
I.e. focused lenses and broad search can **trade off**; adding directives isn't free — it can
*redirect* attention rather than purely *add* to it. ("A salient checklist crowds out open-ended search.")

## The empirical hint (weak)
3-arm ×5 A/B (`anneal-empirical-validation-experiment`), the *omission* bug (period) catch-rate:
- act-first (no discipline): **0/5**
- vanilla-anneal (generic: ground / investigate / verify-each-kind / falsify): **3/5**
- adhoc (generic **+** focused trace/completeness lenses): **2/5** ← *fewer* than vanilla, despite "more"

Meanwhile adhoc crushed the *provenance* bugs its focused trace lens targets (**5/5** vs vanilla's 2/5).
So adhoc spent attention where its directives pointed (provenance) and **underperformed vanilla on the
omission** — exactly the shape the crowding hypothesis predicts.

## Two readings (honest)
1. **Most likely noise.** At n=5, 3-vs-2 is well within sampling error (CIs overlap heavily). One observation.
2. **Possibly a real crowding effect.** This is the **same hypothesis floated and retracted earlier this
   session** (then on n=1 — clippy's lens-set "narrowing"); a faint *independent* hint here keeps it
   alive. Recurrence ≠ proof, but it's twice now.

## Why it matters (if real)
- **Lens-set design:** piling on lenses could *degrade* the general pass → a lens-set should be
  **pruned/measured, not accreted**. Empirical backing for the **additive-reflex** anti-pattern at the
  *attention* level (beyond the usual Pareto/clarity level).
- **Self-improvement loop:** an auto-loop that only *adds* lenses each run could make anneal *worse* at
  the omission class over time → the loop must measure each lens's marginal value **and** guard the
  broad classes in its regression net (`anneal-self-improvement-loop` failure-mode 1 / anti-accretion).
- **Clippy / instance lens-sets:** argues for a **lean lens-set backed by the general disciplines**, not
  a maximal one.

## If real, it ARGUES FOR the multi-pass process (reconciles with "the additions compound")
Crowding (if real) is about a **single attention-limited pass** being somewhat *zero-sum on focus*: a
focused directive buys depth on what it names by spending attention it can't also give the broad sweep.
That does **not** contradict the operator's lived "the anneal additions compound / help" — it **explains a
mechanism by which the *process* layer earns its keep:** if one pass can't hold focused-depth + broad
breadth at once, the way to get both is **multiple passes / fresh contexts with different focuses**
(convergence, fresh-context verify). So "lenses divert attention *within a pass*" is an argument **for**
the cycles, not against them — the process buys back the breadth a single focused pass sacrifices.
- **Corollary:** the value isn't "more lenses in one prompt" (where crowding bites) — it's **fewer lenses
  per pass, more passes / fresh contexts** (lean-per-pass + iterate). Ties to the prompt-vs-process reframe
  (`anneal-empirical-validation-experiment` Addendum 2): single-pass prompt-stacking is the *weak* form;
  the process is the *strong* form.
- **Reframes the self-improvement anti-accretion rule:** don't only prune lenses globally — **distribute**
  them across passes (a fresh-context pass per focus) rather than piling them into one.

## The test that would settle it (queued; runs paused 2026-06-06)
Controlled ablation, more reps (k≥10): adhoc with **only** the provenance lens vs **only** generic-
falsify vs **both** — measure the *omission*-class rate (period) across them. If "both" < "only-falsify"
on omissions beyond noise → crowding is real. Pair with a **directive-count gradient** (1 lens / few /
many) vs omission-catch rate. (Runs paused per operator; this is the queued next experiment if resumed.)

## Relates to
- `anneal-empirical-validation-experiment` — the source A/B + the per-bug mechanism (3-arm ×5 data).
- `provenance-at-handoff-lens` — the focused lens whose attention-pull is the suspected cause.
- `anneal-self-improvement-loop` — the anti-accretion failure-mode this would empirically ground.
- skill-craft **additive-reflex** anti-pattern — the doctrine this extends from "clarity/Pareto" to "attention."
- (earlier in-session) the retracted n=1 "clippy lenses narrow attention" claim — same hypothesis, first appearance.
