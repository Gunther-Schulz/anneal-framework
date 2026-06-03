# Measuring anneal's value — can we show a run is actually more sound/dependable?

**Status:** OPEN — exploratory, **operator-flagged as a next exploration target** (2026-06-03).
Surfaced by `anneal-placement-and-improvement-research.md` as the **biggest real gap**: the field
has eval/benchmarks for agent reliability; **anneal has none.**

## The gap
anneal's whole claim — *it makes open-ended AI work sound and dependable* — is **asserted, never
measured.** There's no evidence that an anneal-driven run produces a *better/sounder* outcome (or
fewer shipped errors) than the same AI working unstructured. Everything rests on the *plausibility*
of the discipline, not on a measured effect. That's the weakest point in the whole story, and the one
most worth closing (it would both *validate* anneal and tell us *which parts* of the discipline carry
the gains).

## What to explore (not yet designed)
- **What to measure — separate two kinds:**
  - *Process metrics* (did the discipline fire?): loopback rate, false-[READY] rate (V-5), claim-
    groundedness, verify catch-rate (did verify catch real issues a separate context found?). Easy to
    capture, but they measure *adherence*, not *value*.
  - *Outcome metrics* (was the result actually sounder?): outcome-correctness vs an unstructured
    baseline, shipped-defect rate, rework needed. These measure *value* — and are the hard ones.
- **How — candidate designs:** A/B (same task ± anneal); a small **reliability benchmark** (a task
  set; anneal-run vs unstructured-run; score correctness/defects) — borrowing from the agent-eval
  literature (AgentBench-style, the eval surveys in the placement note); or longitudinal (track
  production signals over real runs).
- **The hard part (why it's an *exploration*, not a quick fix):** anneal's domains are *open-ended*
  (corpus-evolution, design, debugging) — there's often **no ground-truth "correct" answer** to score
  against. So outcome-measurement needs proxies: operator-judged soundness, did-a-loopback-prevent-a-
  real-error, regressions-avoided. Defining a *credible* proxy is the core of the exploration.
- **Existing substrate to build on:** `dev-notes/validation-watch.md` already logs design-uncertainty
  predictions + the production-signal to watch — a partial, already-wired measurement surface. Could a
  measurement story extend it (turn V-N "production signals" into tracked, scored outcomes)?

## Why it matters beyond validation
A measurement story would also let anneal *improve empirically* (which parts of the discipline earn
their cost?) — and would be the honest answer to "is anneal actually better, or just plausible?"

## Relates to
- `anneal-placement-and-improvement-research.md` (lead #3 — the research origin; + the rigorous
  deep-research run will surface reliability-benchmark methods to borrow).
- `dev-notes/validation-watch.md` (the existing partial measurement substrate).
- Method-kernel-adjacent if it adds a measurement mechanism to the framework → anneal-dev + kernel-independent verify.
