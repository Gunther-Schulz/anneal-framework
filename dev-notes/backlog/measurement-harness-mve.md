# Measurement harness — wiring skill-creator's runner to the anneal MVE

**Status:** [PARKED] ⏸ **HARNESS BUILT + PROVEN; the A/B it feeds is PARKED** (negative/structural verdict —
see `anneal-empirical-validation-experiment.md` VERDICT 2026-06-06). The harness works end-to-end
(frozen pack + oracles + well-formedness gate + arm briefs `eval/arms/`; opus both arms; token +
grounding capture from the foreground subagent `<usage>`). What it *measured* is the point: **7
act-first runs across 6 tasks all scored 1.0** — frontier opus one-shots tractable tasks, so the
controlled single-task A/B ties (clippy same outcome, 2.5–3.4× cost). The three-band model + the
pivot to observational evidence live in the experiment item. The harness is **retained, reusable** for
a scale-resumption (the only regime where a gap would show). The **HOW** for the
measurement gap: operationalizes `anneal-reliability-measurement.md` (the
why/what — 3 metric axes) and `anneal-empirical-validation-experiment.md` (the
A/B/C protocol — pre-registered, seeded-defect) by borrowing Anthropic
skill-creator's eval harness as the execution runner instead of building runner
plumbing. Operational home: `eval/` (see `eval/README.md`).

## Progress
- **Step 0 — done (2026-06-05, `abcb0af`).** Seam proven end-to-end: two live arms
  (clippy-discipline vs act-first) → deterministic oracle → `grading.json` → vendored
  `aggregate_benchmark.py` → `benchmark.json` (dynamic arm names + variance + delta).
  Scaffold at `eval/{vendor,oracle,tasks}/`; `eval/runs/` gitignored.
  **Plumbing-only result:** both arms caught the defect (catch-rate Δ0); the discipline arm
  cost +1065 tokens — the cheap-oracle null this thread already predicts. The task is the
  lesson: too easy / wrong regime.
- **Step 1 — task pack done + FROZEN (2026-06-06).** The full silent-failure pack: **10 tasks**,
  each with `tasks/<slug>/{prompt.md,solution.py}` (seeded-defect starter) + a deterministic
  held-out `oracle/<slug>_oracle.py` (built on the new shared `oracle/_harness.py`). Diverse
  defect classes (mutation, lost-ordering, missing-tiebreak, delimiter-escaping, non-idempotency,
  case-folding, empty-input, forgotten-bound, wrong-rounding-rule, dropped-partial-page) so a
  measured effect isn't a single-bug artifact. Reference correct fixes live gate-only in
  `oracle/fixtures/` (arm never sees them). **`eval/wellformedness.py` gates all 10 GREEN** (weak
  check green on the defect; held-out < 1.0 on the defect; correct fix == 1.0). Pre-registration
  manifest = `eval/PACK.md` (frozen by rubric, NOT by performance — selection-bias guard).
  `discount-floor` is documented-excluded (the criterion-4 null). merge-config defect re-scores
  0.5 under the migrated harness (behavior preserved).
  - **Next (Phase 2, operator-gated):** build the arm briefs + dispatch A/B at k=3 (~10×2×3 ≈ 60
    runs); the arm-fairness / anti-strawman design is decided with the operator before compute spend.

## Task-pack rubric (the load-bearing design — added 2026-06-06)
Step 0's `discount-floor` (floor division) gave a null because it failed criterion **4**: a
floor-division bug is requirement-*trivia* (one extra test case catches it), not requirement-
*space-gated*. A task is in the silent-failure regime iff:
1. **Fair** — the full requirement is stated in the prompt prose. The info needed to catch the
   defect is available to *both* arms (no hidden-intent gotcha).
2. **Weak-oracle-green** — the seeded defect passes the visible/quick check the prompt advertises
   (mechanically checkable: run the weak check on the starter).
3. **Held-out-detectable** — a deterministic script (no LLM, no arm-awareness) catches it, and a
   correct fix scores 1.0 (the oracle is neither blind nor over-strict).
4. **Requirement-space-gated** — catching it requires *enumerating a requirement the visible check
   never exercises* (the design-first mechanism under test), not domain-trivia or an extra random
   test. ← the criterion `discount-floor` failed.
5. **Plausible** — the defect looks like a natural first implementation, not an obvious blunder.

**Pre-register by rubric, NOT by performance.** Each task is argued in-regime from this rubric;
the pack is frozen *before* any scored run. We do **not** filter tasks by running arm B and keeping
its misses — that is the experiment doc's own **selection-bias** threat (tuning the set toward
arm-B failure rigs the comparison toward clippy). Consequence taken honestly: if arm B catches a
rubric-conformant task, that is a legitimate *measured* result (toward refutation), not a harness
artifact. The Step-0 fix is therefore a **better rubric**, not a difficulty-filter.

**Well-formedness gate (every task, before freeze):** the 3-way check run on `merge-config` —
(a) weak check passes on the seeded defect, (b) held-out oracle scores < 1.0 on the defect,
(c) held-out oracle scores 1.0 on a correct fix.

## The decision
Don't build a runner. skill-creator (`anthropics/skills`, cloned at
`~/dev/reference/skills`) already ships the execution + aggregation scaffold,
and anneal already out-designs it at the *what-to-measure* layer (process vs
outcome metrics, ablation arms, seeded-defect scoring). So: **borrow the
runner, keep our design.** The runner is theirs; the experiment is ours.

## The seam
The harness pivots on one file: `aggregate_benchmark.py` reads a `grading.json`
per run and emits `benchmark.json` (mean ± stddev + delta per configuration). It
**discovers config-dir names dynamically** — not hardcoded to with/without — so
arms can be named `arm_A_clippy` / `arm_B_actfirst`. Layout:
`<bench>/<task>/<arm>/run-K/grading.json`. Whatever writes `grading.json` in its
schema drives aggregation, so we **reuse the aggregation and replace the
scorer**: `summary.pass_rate` becomes seeded-defect catch-rate.

## Reuse vs build
Reuse from skill-creator (as-is):
- `scripts/aggregate_benchmark.py` — variance/delta, dynamic arm names.
- `timing.json` capture (tokens + duration from the task-completion
  notification) → the token metric (P2) for free.
- `eval-viewer/generate_review.py` — human eyeball of arm outputs + transcripts.
- `agents/comparator.md` (optional) — blind qualitative A/B as a second signal.

Build (anneal-specific, small):
1. **Arm-B runner** — a fair act-first agent (same model + tools as the instance
   under test, plain edit/run/test, same weak oracle). The one real harness piece.
2. **Seeded-defect oracle** — a deterministic per-task script that checks the
   held-out defect and writes `grading.json` (`summary.pass_rate` = caught? 1:0).
   Replaces the LLM grader → objective, un-gameable, blind by construction. The
   un-fakeable-artifact principle applied to the experiment itself.
3. **Grounding-ratio extractor** — from `tool_calls` composition (already in
   `metrics.json`): evidence-gathering reads/searches/verifies vs total → P3.
4. **Task pack** — ~10 silent-failure code tasks, each with a weak oracle during
   the run + a held-out comprehensive oracle. Pre-registered (frozen + committed
   before running).

## Lead with the token result
`anneal-reliability-measurement.md` flags tokens-to-correct-outcome as the
cheapest, ground-truth-measurable metric. The plumbing yields it the moment it
is wired (tokens/run, mean ± σ, delta). First publishable result — *does clippy
reach correct outcomes at fewer tokens than act-first in the silent-failure
regime* — lands before the general soundness metric is solved.

## Sequence (de-risked)
- **Step 0 — prove the seam.** ONE task, ONE seeded defect, arm A vs arm B,
  k=1. Dispatch both → oracle writes `grading.json`, notifications write
  `timing.json` → run `aggregate_benchmark.py` → get a `benchmark.json` with a
  delta. End-to-end before investing in 10 tasks.
- **Step 1 — the MVE.** k=3, 5–10 tasks, add the grounding-ratio extractor,
  pre-register P1–P3. Run, aggregate, view.
- **Step 2 — read honestly, then isolate.** Check against the refutation
  conditions in `anneal-empirical-validation-experiment.md` (act-first matches
  at ≤ tokens → value collapses in-regime — take it). Effect shows → add arm C
  (clippy minus independent verify) to isolate that the design-first ordering
  carries the gain, not just "more scaffolding."

## The honest hard part
Not the plumbing (a day of glue) — the **task pack + seeded-defect oracles** for
the silent-failure regime. The MVE sidesteps the unsolved general
epistemic-soundness metric by using seeded-defect catch-rate as a concrete,
scriptable proxy: "did it catch the planted defect the cheap oracle misses."
Runnable now.

## Relates to
- `anneal-reliability-measurement.md` — the why/what (3 metric axes; this is the how).
- `anneal-empirical-validation-experiment.md` — the experiment design this wires a runner to.
- `eval/README.md` — the operational home + layout + step-0 recipe.
- skill-creator harness: `~/dev/reference/skills/skills/skill-creator/` (`scripts/`, `agents/`, `references/schemas.md`).
