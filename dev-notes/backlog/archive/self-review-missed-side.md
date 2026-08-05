# Self-review (missed-side) — unified design: Q3 novel-escape hunt + Q2 known-escape probe (+ the protocol-tension feeder)

**Status:** [DESIGN] — **consolidation (session 14, operator-confirmed 2026-06-08)** of
`post-run-review-failure-class-register` (absorbed → archived) + `surface-non-task-observations` **(b)
protocol-tension** (folded; the **(a)** work-observation half stays standalone). The **missed row** of
`self-improvement-signal-architecture` — i.e. what `post-run-review` *becomes* once its caught-side ambitions
are dropped (the `framework-gap-receipt` owns Q1/caught). Method-kernel (`modules.md` §4 post-run-review
minimum-shape + scope-narrowing) + corpus-evolution (`post-run-review.md` procedure) → anneal-dev +
kernel-independent verify.

## The frame
Self-review's entire value is the **missed row** — escapes the run's checks didn't catch, which the tracker
is structurally silent on (a converged tracker is a record of *success*). By the **lens-set-never-complete**
principle this is the *un-prunable* residual: the only escape-detection there is (the prune analysis in the
umbrella — it does NOT overlap the caught-side receipt). Two cells:
- **Q3 — novel-escape hunt (irreducible).** Open-ended; finds classes no check covers. Operator + production
  reality. The only source of NEW classes.
- **Q2 — known-escape probe.** A per-known-class probe against a maintained register: "did this run exhibit
  class X *without* catching it? — evidence or `clean`."

`post-run-review` (live, modules §4) currently muddles caught+missed+novel; **narrow it to this row** — a
Pareto *reduction* of a kernel mechanism.

## Q2 — the failure-class register (known-escape probe) [absorbs `post-run-review-failure-class-register`]
**The gap:** post-run-review's Q1 (Misses) is *reactive* — it lists defects the model spontaneously
recognizes. But the dominant failure shape ("saw the fact, didn't connect it to the decision") means a model
that missed an implication in-run **also misses flagging it in self-review** — the same reasoning-depth
ceiling in both passes. The clippy 6-bug retrospective (a manual cross-run review) caught classes the per-run
review didn't — evidence the self-review under-probes.

**The fix:** a maintained **failure-class register** the self-review probes per-run: for each catalogued
class, "did this run exhibit it? — cite evidence (quote/file:line) or `clean`." Artifact-forcing (per-class
evidence, not generic mush). **Additive**, not a replacement for the open-ended Q3.

**Consolidates the scattered catalogs** (Pareto — one probe-list vs N): V-30 form-not-binding classes;
`design-decision-implication-depth-gaps` (reasoning-depth classes); `framework-blindspot-class-analysis`
(proactively-enumerated classes — its output sink); `instance-domain-invariant-register` (instance-layer
classes). **Layered** (framework ∪ instance), mirroring the invariant registers: general classes at the
framework layer, domain classes at the instance layer. **A failure-class register is the *dual* of the
invariant registers** — invariants = what must hold (positive); failure-classes = what tends to break
(negative).

## Q3 — the novel-escape hunt (irreducible) [absorbs the design-quality probes + the protocol-tension feeder]
The open-ended interrogation that finds what no register covers. Two structured aids (**seed, not bound**):

**(i) Design-quality probe-templates** — a fresh adversarial interrogation of each load-bearing decision's
*shape/quality* (not "did defect X recur"): workaround-vs-principle · proportionality (additive-reflex) ·
default-justification · altitude/scope · front-loading/simplicity · precedent-linking. Surfaced empirically —
across a long 2026-06-06 session these operator "proving-questions" repeatedly found gaps the framework's own
checks (basis, missed-dependents, lenses, intent-falsification) passed clean. **Dual home:**
*design-time-cheapest* in the convergence **intent-falsification pass** (add as judgment attack-criteria — the
sibling `intent-falsification-coverage-binding`) AND a *post-review backstop* here ("did the run lean on the
operator's live probing to find gaps the framework should have caught?").
  - *Empirical base (2026-06-06):* workaround-probe pressure-tested the integrity-check fix; proportionality
    caught the v-entry gold-plating (→ `convergence-surfaced-finding-action-brake`); default-justification
    flipped runs-data off→on; altitude reframed runs-data scope; front-loading simplified archive→track-in-
    place; precedent-linking surfaced `design-decision-implication-depth-gaps`.
  - *Empirical base (2026-06-15, `convergence-machinery-batch`):* operator proving-questions on the
    aggressive-batching workflow — each building on a process-aside the AI surfaced ad-hoc — produced 3
    filed gaps the run's own checks passed clean on: "does coherence warrant more batching?" → coherence-batch
    economics + the batch-size ceiling (`proportional-cycle-weight`); "should the F9 fix be re-verified?" →
    isolation-is-not-a-proportional-lever (a delta-verify must stay isolated, INV-3); "is the convergence-cluster
    miss a protocol phenomenon?" → `backlog-status-queryability`. **Two-step composition:** the AI's ad-hoc
    process-surfacing (the (ii) feeder) *seeded* the operator's probing (this (i)) — neither alone would have
    filed them, and the surfacing was **willed** (parentheticals), so an un-probed aside would have dropped
    (the `surface-non-task-observations` capture gap). A datapoint that the (i)×(ii) channel is recurrent +
    productive but its AI-surfacing half is un-structured.

**(ii) Protocol-tension feeder** [from `surface-non-task-observations` (b)] — two protocol rules that clash
*only at runtime* (seed: single-unit impl in working-context vs a configured `impl: sonnet` — the agent
silently picked working-context; the operator had to poke it). **Key insight:** an *interaction* conflict
(rules that don't textually contradict, only clash in a runtime situation) is **structurally invisible to a
dev-time text review** — the protocol twin of static-blind-to-behavioral-coupling. Runtime is the only place
it reliably surfaces (the situation is *real*, not simulated): **runtime-surface → dev-time-resolve**, not
either/or (the dev-time-only version is largely the coherence-audit). **Hard part:** runtime detection is
judgment-heavy (no clean mechanical trigger) → risks naked-judgment. Tractable hardening: flag *known*
interaction-points with a runtime surface ("if I won't apply here, surface why") — though those tend to get
*resolved* instead of flagged. Consumer: the framework maintainer (feeds sharpening / coherence-audit).

## Load-bearing disciplines (state all, or it oversells)
1. **Additive, not blinders.** A fixed register/probe-list becomes blinders if it *replaces* the open-ended
   Q3. It MUST compose with "no existing check covers this class" (the novel surfacer), and **novel classes
   feed BACK into the register** (it grows — the institutional memory of failure modes; this is the learning
   loop's novel→known promotion).
2. **Floor, not ceiling.** A register-probe / self-asked adversarial question raises the floor but cannot
   replace the operator: a self-asked question can be **vacuously satisfied** (the intent-pass's own
   acknowledged weakness). A fresh *human* adversary is harder to fool. The reasoning-depth ceiling is
   *reducible, not eliminable* by process.
3. **Seed, not bound.** The probe-lists seed the interrogation; they must not become a checklist the AI
   runs-and-stops (skill-craft "Checklist as ceiling"). Trace each lead beyond the list.

## Implementation vector + open design questions
- **modules §4** post-run-review minimum-shape: the Q2 per-class probe + the Q3 design-quality probes (a new
  Q or a Q1 extension); the per-class evidence/`clean` artifact; **scope-narrowing** to the missed-side.
  *(method-kernel → anneal-dev + kernel-independent verify.)*
- **post-run-review.md** procedure (the Q-set + state-aware walk).
- Register **home + layering** (framework vs instance; one file or a slot like the invariant registers).
- The **feed-back loop** (novel class → register entry — who adds, when).
- Composition with V-30 (its 4-class catalog made first-class) + `framework-blindspot-class-analysis` (the populator).
- **Subagent pre-evaluator for surfaced candidates** (operator-load-reducer; operator-raised 2026-06-15). A
  subagent that **triages** the (ii)-feeder's surfaced improvement-candidates *before* the operator: **relate-
  before-add dedup** ("already tracked?" — a backlog search, **retrieval not ceiling-bound** → pure load-
  reduction), **classification/routing** (which cell Q2/Q3, which existing item it feeds, which failure-class),
  and a **first-pass severity** — producing a structured first-judge list the operator **second-judges**.
  **NOT a new mechanism-class:** it's the existing intent-falsification (subagent force-fixes the checkable,
  surfaces the residual; operator judges) + **practice-11** (subagent detects → AI first-judge → operator
  second-judge) pattern applied to the self-improvement channel. **Bounding caveats (or it oversells):**
  (1) **shared reasoning-depth ceiling** (the INV-3 / `verify-model-diversity` logic) — a subagent of the
  surfacer's model inherits its blind spots, so it **cannot be the gate** (operator-irreducible per discipline
  #2); mitigate with **fresh-context + ideally model-diversity**. (2) **signal-threshold / flooding**
  (`surface-non-task-observations`'s hard Q) — a mis-calibrated evaluator **shifts** load (operator wades
  through over-flags) instead of reducing it; the **dedup/retrieval** leg is pure win, the **triage** leg carries
  the risk. Needs a practice-9 design surface. **Positive datapoint (2026-06-15):** a 5-subagent (sonnet) grounding
sweep of the 70-item backlog ran exactly this triage shape (dedup/classify/state-tag — the retrieval leg)
and caught every shipped-stale item + the archive conflict with compact output. The *sound* leg works in
practice; cheap-model (sonnet) sufficed for retrieval/classification. Origin: operator, 2026-06-15 (this run's Q3 datapoint, below).

## Relates to
- `self-improvement-signal-architecture` — the umbrella; this is its **missed row** (Q2+Q3).
- `framework-gap-receipt` — the **caught row** (Q1), the *opposite* mechanism; NOT redundant with this (the umbrella's prune analysis).
- `framework-blindspot-class-analysis` — proactive Q3 populator (imagined-ahead classes) feeding the register.
- `intent-falsification-coverage-binding` — the design-quality probes' *design-time* home (intent-pass enrichment); this item is their *post-review backstop*.
- `design-decision-implication-depth-gaps`, `instance-domain-invariant-register`, V-30 — source catalogs + the reasoning-depth ceiling.
- `surface-non-task-observations` — its **(a)** work-observation half (stays standalone; this absorbed its **(b)**).
- `foundation-invariant register` (`dev-notes/foundation-invariants/`) — the architectural dual (invariants positive ↔ failure-classes negative).
- Origin: consolidation of `post-run-review-failure-class-register` + `surface-non-task-observations` (b), operator-confirmed 2026-06-08 (session 14).
