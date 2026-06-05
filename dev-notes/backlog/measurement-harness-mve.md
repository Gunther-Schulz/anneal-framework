# Measurement harness — wiring skill-creator's runner to the anneal MVE

**Status:** OPEN — plan ready, not yet built (2026-06-05). The **HOW** for the
measurement gap: operationalizes `anneal-reliability-measurement.md` (the
why/what — 3 metric axes) and `anneal-empirical-validation-experiment.md` (the
A/B/C protocol — pre-registered, seeded-defect) by borrowing Anthropic
skill-creator's eval harness as the execution runner instead of building runner
plumbing. Operational home: `eval/` (see `eval/README.md`).

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
