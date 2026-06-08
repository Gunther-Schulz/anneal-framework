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

## Candidate mitigation (gated on the hypothesis): distributed lens-agents (operator idea, 2026-06-07)
If crowding is real, distribute lenses across **agents**, not prompt-lines:
- **Main / investigative agent(s): NO lenses loaded** → the broad falsify-every-kind sweep stays
  uncrowded (preserves omission-catching).
- **One fresh-context lens-agent per focus** → focused depth on its target class, on its own attention budget.
- **Merge** broad + focused findings (dedup) at convergence.

Two benefits in one move: lens-focus-without-crowding **and** the fresh-context *independence* the verify
arm is about (an agent that didn't form the original belief). Fits anneal's existing shape — the
convergence/verify pass is already a separate fresh-context agent; lens-agents extend it. The clean form
of the corollary above (distribute across passes → distribute across **agents**).
- **Gating:** value is conditional on crowding being real (unproven) — if it's noise, this is just cost.
  Build only **after** the test below confirms crowding; don't build speculatively.
- **Cost is bounded:** parallelizable; spawn a lens-agent only for *present/relevant* bug-classes (not all,
  always); and if crowding is real the cost *recovers* value stacking loses — not pure overhead.

## The test that would settle it — AND test the mitigation (queued; runs paused)
Controlled ablation, more reps (k≥10), arms: **only-provenance** · **only-generic-falsify** · **stacked**
(both in one agent = current adhoc) · **distributed** (broad-main lens-free + a fresh-context
provenance-agent, findings merged). Measure BOTH the *omission* rate (period) and the *provenance* rate.
- stacked < only-falsify on omissions (beyond noise) → **crowding is real.**
- distributed ≥ only-falsify on omissions AND ≥ stacked on provenance → **distribution mitigates it**
  (recovers broad coverage while keeping focused depth) — confirms the operator's mitigation.
One design tests both. Pair with a **directive-count gradient** (1 / few / many in one agent) vs omission
rate. (Runs paused per operator; queued next experiment if resumed.)

## Post-ship watch — the first KERNEL basis-rule instance (provenance shipped 2026-06-07, `cd2fd2c`)
The provenance form shipped into the **framework basis rule** (`core.md §3.2.1`, run
`provenance-basis-naming`) — not a clippy lens-prompt but a salient directive in the kernel every
instance renders. This is the **first instance of the crowding question at the basis-rule level**:
INT-A (the provenance falsifier is recognition-gated) and this hypothesis are two faces of one
**recognition-economy** concern — recognition is finite and contested. The run's own soundness verdict
was explicitly scoped: provenance raises recognition **on the provenance class** (validated 5/5-vs-2/5),
but whether adding it to the basis rule's salience **trades off against the broad sweep** (esp. the
*omission* class, where the same A/B showed the focused arm at 2/5 < vanilla's 3/5) is **unproven**.
Choosing (b)-as-one-form-in-the-kernel over a discrete-lens-pile was the deliberate containment.
- **watch-kind:** quality-watch (net-recognition trade-off, not a correctness regression).
- **catcher:** a future eval / A/B where the basis rule's broad recognition (omission-class catch-rate)
  is measured and shows degradation traceable to the added provenance (or other) salience — vs the
  pre-provenance baseline. The settling test above (only-falsify / stacked / distributed × omission-rate)
  is the instrument; this run is its first kernel datapoint.
- **closing rule:** the controlled crowding test runs and either confirms (→ prune/distribute the
  kernel's salient forms) or refutes (→ the basis-rule salience is free) the trade-off, per
  `v-entry-is-post-ship-only`. Until then: do not pile further salient forms into the basis rule
  reflexively (additive-reflex at the attention level).

## Relates to
- `investigation-pass-lens-priming` — the **surgical sibling**: should the lens set prime the
  *investigation* pass at all? The extreme "zero lenses in one pass" of this item's "fewer-per-pass /
  distribute" corollary, isolated as a distinct, cheaper test (priming on/off for one pass, vs this
  item's count/distribution arms). Same recognition-economy root.
- `anneal-empirical-validation-experiment` — the source A/B + the per-bug mechanism (3-arm ×5 data).
- `provenance-at-handoff-lens` (**archived — shipped** as the (b)-direction at `core.md §3.2.1`, `cd2fd2c`)
  — the focused form whose attention-pull is the suspected cause; now the live kernel datapoint above.
- `anneal-self-improvement-loop` — the anti-accretion failure-mode this would empirically ground.
- skill-craft **additive-reflex** anti-pattern — the doctrine this extends from "clarity/Pareto" to "attention."
- (earlier in-session) the retracted n=1 "clippy lenses narrow attention" claim — same hypothesis, first appearance.
