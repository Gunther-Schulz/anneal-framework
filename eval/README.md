# eval/ — anneal measurement harness

The validation layer over the methodology: does an anneal-disciplined run
(clippy, daneel, …) produce **sounder outcomes at equal-or-lower token cost**
than an act-first agent, in the regime anneal is for — expensive/late
verification, i.e. silent-failure tasks?

**Status:** spec only — not yet built. This README is the build plan; the
decision and rationale live in `dev-notes/backlog/measurement-harness-mve.md`.
The designs it implements: `dev-notes/backlog/anneal-reliability-measurement.md`
(metrics) and `dev-notes/backlog/anneal-empirical-validation-experiment.md`
(A/B/C protocol).

## Approach: borrow the runner, keep our design
We do **not** build a runner. Anthropic's `skill-creator`
(`~/dev/reference/skills/skills/skill-creator/`) ships the execution +
aggregation scaffold; anneal already out-designs it at the *what-to-measure*
layer. So we vendor its scripts as the runner and supply our own arms, oracle,
metrics, and tasks.

## The seam
`aggregate_benchmark.py` reads a `grading.json` per run → `benchmark.json`
(mean ± σ + delta). It discovers config-dir names dynamically, so arms are just
directory names (`arm_A_clippy`, `arm_B_actfirst`). **Reuse the aggregation;
replace the scorer** — `summary.pass_rate` becomes seeded-defect catch-rate.

## Proposed layout
```
eval/
├── README.md                 # this file
├── vendor/                   # copied from anthropics/skills (provenance noted)
│   ├── aggregate_benchmark.py
│   └── schemas.md
├── arms/
│   └── actfirst_runner.md    # arm-B agent brief                      (build)
├── oracle/
│   └── <task>_oracle.py      # deterministic seeded-defect scorer →
│                             #   grading.json                          (build)
├── tasks/
│   └── <task>/               # prompt + weak oracle + held-out oracle  (build,
│                             #   pre-registered)
└── runs/
    └── <bench>/<task>/<arm>/run-K/{grading.json,timing.json}
```

## Components
**Reuse (skill-creator, vendored):** `scripts/aggregate_benchmark.py`; the
`grading.json` / `timing.json` / `benchmark.json` schemas
(`references/schemas.md`); `eval-viewer/generate_review.py`; optional
`agents/comparator.md` for a blind qualitative second signal.

**Build (anneal):**
- `arms/actfirst_runner.md` — fair act-first agent (same model + tools as the
  instance under test; plain edit/run/test; same weak oracle available).
- `oracle/*.py` — deterministic seeded-defect scorer; writes `grading.json` with
  `summary.pass_rate` = caught? 1:0. Objective, blind by construction.
- grounding-ratio extractor — from `tool_calls` composition in `metrics.json`.
- `tasks/` — ~10 silent-failure code tasks, pre-registered (frozen + committed
  before any run).

## Metrics (3 axes)
1. **Outcome** — seeded-defect catch-rate (hidden oracle).
2. **Cost** — tokens-to-correct-outcome (from `timing.json`). *Lead here:
   cheapest, ground-truth-measurable.*
3. **Grounding ratio** — evidence-gathering vs internal rumination (from
   tool-call composition) — refine, not ruminate.

## Run Step 0 (prove the seam end-to-end)
1. Pick ONE task with ONE seeded defect.
2. Dispatch arm A (clippy) and arm B (act-first) on it (k=1).
3. The oracle writes each run's `grading.json`; capture each subagent's
   `total_tokens` / `duration_ms` into `timing.json` as the notification arrives.
4. `python vendor/aggregate_benchmark.py runs/step0 --skill-name clippy`
5. Read `benchmark.json` — confirm a delta on catch-rate + tokens, end-to-end.

Then scale to k=3 / ~10 tasks (Step 1) and add arm C — clippy minus independent
verify — to isolate that design-first ordering carries the gain (Step 2).

## The honest hard part
Not the plumbing (a day of glue) — the **task pack + seeded-defect oracles** for
the silent-failure regime. The MVE sidesteps the unsolved general
epistemic-soundness metric by using seeded-defect catch-rate as a concrete,
scriptable proxy. Runnable now.
