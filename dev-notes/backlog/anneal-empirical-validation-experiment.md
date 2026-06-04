# Empirical validation experiment — does design-first (anneal) beat act-first? (v0)

**Status:** OPEN — experiment design **v0** (operator-requested 2026-06-03). **To be sharpened
after** the two in-flight research runs land (they inform specific parts — see bottom). This is
the operationalization of the measurement gap: the falsifiable test that can prove anneal **right
OR wrong**. Origin: `design-first-vs-act-first-research.md` verdict — the literature supplies NO
such head-to-head, and anneal's instances are the testbed the field lacks.

## Goal
A pre-registered, falsifiable A/B(/C) test of: *anneal (design-first, evidence-grounded, cyclic)
produces sounder outcomes at equal-or-lower token cost than act-first (edit/run/test), in the
expensive-verification regime.* Must be capable of refuting anneal, not just confirming it.

## Predictions (each can fail independently)
- **P1 (soundness):** in the expensive-verification regime, anneal > act-first on **hidden-oracle**
  correctness.
- **P2 (cost):** anneal reaches that outcome at **≤ tokens** vs act-first (the operator's
  "fewer tokens" claim).
- **P3 (mechanism):** anneal scores **low** on the grounding ratio (refine, not ruminate) AND that
  low score correlates with the P1 win.

**Refutation conditions (the honest part):**
- act-first matches anneal correctness at ≤ tokens → value proposition collapses *in-regime*.
- anneal wins correctness only by spending MORE tokens → "sounder but pricier," not "cheaper."
- anneal wins but scores HIGH on grounding-ratio → it works for a reason other than design-first.

## Design
- **Regime (load-bearing):** ONLY where verification is expensive/late, so the cheap oracle
  (compiles? quick test passes?) gives *misleading* signal. Canonical class: **silent-failure
  tasks** — runs/compiles/passes-naive-tests but wrong on a comprehensive hidden check (the
  scientific-sim example from the run; the azuro F18 inheritance-break is a clippy-domain instance).
  Cheap-oracle tasks are explicitly OUT (act-first owns that regime; the overthinking study too).
- **Arms (same base model + same tools throughout — no strawman):**
  - **A — clippy** (full anneal).
  - **B — act-first baseline:** same model, plain edit/run/test loop, *same weak/partial oracle*
    available (real conditions). Good-faith ReAct-style agent, not crippled.
  - **C — ablation:** clippy *minus independent verification* (self-verify) OR *minus design-first*
    (tracker but act-first). Isolates whether the ORDERING/INDEPENDENCE carries the gain vs just
    "more scaffolding." Without C you prove "anneal helps," not "design-first is why."
- **Tasks & scoring (gameable-resistant):** ~10–20 regime tasks, each with (a) a *weak* oracle
  during the run + (b) a **held-out comprehensive oracle or seeded subtle defect** for scoring.
  Seeded-defect catch-rate is objective + hard to game (better than LLM-judge). k=3–5 runs/task/arm
  (stochasticity); report distributions (pass^k), not point estimates.
- **Metrics (the 3 axes):** hidden-oracle correctness · total tokens (every arm, every loop) ·
  grounding ratio (adapted overthinking metric — counts evidence-gathering search/read/verify as
  interaction).
- **Pre-registration:** fix task set + regime criterion + metrics + P1–P3 BEFORE running; grader
  blind to arm. This is what makes it "proven right or wrong," not post-hoc.

## Threats to validity (kept explicit so the result is credible)
- Confound "anneal = more scaffolding" not "design-first" → arm C isolates it.
- Strawman baseline → fair same-model act-first agent + same tools.
- Selection bias → pre-registered regime criterion, tasks chosen before seeing results.
- Over-generalization → results bind to the tested regime ONLY.
- Study cost → start with the MVE (below).
- Grader leakage → hidden oracle / seeded defects resist gaming better than LLM-judge.

## Minimal Viable Experiment (start here)
clippy · ONE regime (silent-failure code) · ~10 seeded-defect tasks · arms A vs B · k=3 · the 3
metrics · pre-registered P1–P3. Effect shows → scale (add arm C, more domains/instances). Act-first
matches/beats A → refutation, taken honestly.

## Sharpenings from the completed runs (2026-06-03)
Both literature runs landed — concrete refinements to fold into the protocol:
- **Verify-arm design** (verify-techniques run): the verify arm + arm-C should use **criteria-first**
  verification (rubric fixed BEFORE seeing the output — counters agreement bias, which compute does
  NOT fix), on a **different base model** than the actor (counters correlated self-confirmation), and
  **decompose judgment claims into falsifiable sub-questions** rather than holistic verdicts.
- **Arm C (independence isolation)** should test **different-model vs same-model-fresh-context** — no
  source has A/B'd that, so the experiment closes a real open question (not just self-validation).
- **Cost curve (P2):** Boehm's 1:10:100 did NOT verify (process-literature run) — do NOT cite it as
  the predicted shape; state the cost prediction as anneal's own hypothesis, not borrowed fact.
- **Grounding ratio (P3):** the adapted overthinking metric (evidence-interaction vs internal
  rumination), per `anneal-reliability-measurement.md`.
- **The unique contribution:** NONE of the borrowed verify techniques were measured on **text-only
  judgment claims** (design-soundness/synthesis-accuracy) — anneal's exact class — so this experiment
  closes a gap the literature explicitly leaves open.
- **Possible 4th arm:** carry **multiple working hypotheses** at investigate-design (does it improve
  outcomes?) → `multiple-working-hypotheses-investigate-design.md`.

## Relates to
- `anneal-reliability-measurement.md` (the why/what — this is the how; the 3 metrics live there too).
- `design-first-vs-act-first-research.md` (the verdict that motivates it: no head-to-head exists).
- `verify-model-diversity.md` (arm C's independent-verify variants).
