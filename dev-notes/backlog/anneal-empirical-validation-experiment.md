# Empirical validation experiment — does design-first (anneal) beat act-first? (v0)

**Status:** ⏸ **PARKED 2026-06-06** — the controlled single-task A/B **structurally ties at
frontier capability** (opus). This is the proof-thread's *terminal verdict* (see VERDICT below),
not a TODO. The harness that feeds it is built + proven (`eval/`, `measurement-harness-mve.md`);
the *experiment* is parked, not the harness. (Prior: OPEN — experiment design v0, operator-requested
2026-06-03.) Origin: `design-first-vs-act-first-research.md` verdict — the literature supplies NO
such head-to-head, and anneal's instances are the testbed the field lacks.

## VERDICT (2026-06-06) — why the controlled A/B ties, and where value actually lives

**What we ran (cheap + decisive — not the 60-run study).** A frozen 10-task silent-failure pack +
one design-surface task (`config-resolver`), opus both arms, isolated `/tmp` workdirs, deterministic
held-out oracles (`eval/`). **7 act-first runs across 6 tasks — every one scored 1.0** (caught the
seeded defect / built the correct two-phase design). Clippy (full anneal) also 1.0, at **2.5–3.4×
the tokens** (~22k act-first vs 62–75k clippy) and ~3× wall-time. Plus a survey of the beat-the-books
production instance (34 real Clippy runs, 3,080 pre-Clippy commits, 833 pre-Clippy bug-fixes) for a
free control arm.

**The structural finding — the three-band model.** A bug is one of:
1. **Cheaply derivable from the code** → frontier opus catches it act-first; anneal adds only cost.
   (All our synthetic tasks, incl. the design-surface one — both arms independently found the
   merge-then-interpolate ordering + cycle detection.)
2. **Requires knowledge not in the evidence** (domain/operational facts learned by *running* the
   system) → *neither* arm catches it pre-ship; production does. (beat-the-books **W1**: the poller
   returned future-dated bets because "Azuro can't settle a bet before its game starts" — an
   incident-learned fact, not in the code. **State the fact → both arms fix it; omit it → both miss.**
   No gap either way.)
3. **Derivable, but only with careful reasoning act-first would skip** → anneal's genuine band.
   **Narrow at frontier capability, because opus reasons carefully even when acting fast.** We never
   landed a clean band-3 single-task; every task fell in band 1 or band 2.

**So a controlled *single-task* A/B ties** — not because anneal is worthless, but because its
discriminating band is thin at this model's strength, and tasks small enough to score cleanly fall in
band 1.

**Where anneal WOULD measurably win — and why we can't cheaply measure it.** At **scale**: across
many requirements, act-first's small per-item miss rate accumulates (drop ~1 of 20) while
design-first's forced enumeration catches more — a thin per-item edge becomes a visible *aggregate*
gap. But the many-requirement regime is large/messy and resists a clean deterministic oracle (the same
wall that sank the synthetic pack, from the other side). The regime where the gap is real is the regime
that can't be cheaply A/B'd.

**The beat-the-books arm is real but confounded.** 3,080 pre-Clippy commits are genuine non-disciplined
output and 833 bug-fixes are real shipped defects with ready-made oracles — but the pre-Clippy author
was an unknown/mixed process (not same-model opus act-first), so "Clippy finds bugs there" is
anneal-opus vs unknown-author (strawman risk), not the clean same-model A/B. Using a historical bug as
a *fresh task for both arms* removes the confound — but reintroduces the band-1/band-2 wall (per W1).

## The pivot (what replaces the controlled A/B)
Keep the **observational** evidence that's already accruing; don't manufacture a lab verdict that
structurally ties:
1. **Dogfooding catch-log** — anneal-dev's convergence/verify passes catch real defects in its own
   spec (session-10: F7 §3.1 over-attribution, F10 a mis-cite). Log these as they land; the rate is
   the in-regime value signal.
2. **The self-improvement loop** — beat-the-books' miss→root-cause→new-lens history
   (`design-decision-implication-depth-gaps`) + unit-16's 71/72-clean audit are documented value,
   misses included.
3. **Scale-only future option** (if ever worth the cost) — one large multi-requirement task where
   band-3 accumulates; accept judgment/messy scoring. Not cheap; not now.

## Methodology bankable for any future resumption (operator, 2026-06-06)
- **Act-first as the regime screen** ("run act-first until it fails"): escalate to the clippy arm
  only where act-first actually breaks — no compute where there's no gap. **Guard:** that's a *search*
  for the discriminating regime, NOT the scored set (scoring on act-first's misses is this doc's own
  selection-bias trap). Score a fresh, pre-registered set of the discovered class.
- **The harness is reusable** (`eval/`): frozen pack + oracles + well-formedness gate + arm briefs
  (`eval/arms/`). Token + grounding-ratio capture works from the foreground subagent `<usage>` block.
- **Real-bug task source** if scale-resumption: the 833 beat-the-books pre-Clippy fixes (each fix =
  a real defect + a ready oracle); run *both arms fresh* on the reconstructed task to stay same-model.

## Addendum — the real-codebase A/B actually run (session 11, 2026-06-06)
We then *did* run the clone-at-a-commit version on **beat-the-books** (real 250-file codebase, a
real pre-fix commit, both arms fresh opus, neutral "review the replay settlement pipeline" task; the
period-drop bug as the band-3 target). Arms: act-first, clippy (full skill), adhoc-anneal (the core
disciplines as a by-hand checklist, no skill). **Result reinforces the verdict and corrects an
overclaim:**
- **Three arms × 5 each — a clean monotonic dose-response (the de-confounded result):**
  | bug | act-first (none) | vanilla-anneal (generic disc.) | adhoc (+ focused lenses) |
  |---|---|---|---|
  | handicap | 5/5 | 5/5 | 5/5 |
  | team_qualifier crash | 4/5 | 5/5 | 5/5 |
  | market_id (provenance) | 2/5 | 2/5 | **5/5** |
  | closing_lines (provenance) | 2/5 | 2/5 | **5/5** |
  | period drop (omission) | **0/5** | **3/5** | 2/5 |
  | mean bugs/run | **2.6** | **3.4** | **4.4** |
- **The anneal discipline measurably helps — de-confounded.** *Vanilla* anneal (generic disciplines only:
  ground / investigate / verify-each-kind / falsify — the focused trace + completeness mechanisms
  **removed**) still beats act-first 2.6→3.4 and catches **period 0/5→3/5**. So the gain is the *general
  method*, not merely the lenses (resolves the "the focused lenses did all the work" worry).
- **Period is caught by generic thoroughness, NOT the completeness lens** (corrects an earlier note):
  vanilla *lacks* the "notice a dropped field" mechanism yet catches period *more* than adhoc (3/5 vs 2/5).
  → that candidate (dimension-completeness) lens is **redundant with plain thoroughness**.
- **The provenance lens is where focused checks add real value:** market_id + closing_lines sit at 2/5 for
  *both* act-first and vanilla, and jump to 5/5 only under adhoc's explicit "trace each value to its
  producer." Generic discipline does **not** catch that class → `provenance-at-handoff-lens` is the
  stronger of the two candidate lenses.
- **The zigzag (meta-lesson):** n=1-each → looked like an edge; act-first×5 vs adhoc×**1** → looked like
  *no* gap (unequal-n error); proper ×5-each → clean ladder. **At n=1 the methodology question is
  unanswerable; the *rate* is the signal.** (Supersedes an earlier "no demonstrated capability gap" note.)
- **Honest bounds:** n=5 → wide per-bug CIs (per-bug numbers noisy; the *monotonic aggregate* is the robust
  signal). All **single-pass**, which *understates* anneal (multi-pass cycles compound) → 3.4/4.4 are
  conservative floors. The **clippy (heavy-machinery) arm was run single-pass / same-context** → undersold
  (its fresh-context convergence cycles never engaged); so **lightweight-vs-heavy is untested**, not answered.
- **Bugs were real** (market_id / handicap / team_qualifier / closing_lines, all traced + corroborated
  by the project's own Unit-27 fix for handicap+team_qualifier; market_id + closing_lines real-latent,
  unfixed). Confirms the *regime* is genuine — just that frontier act-first reaches it too, given enough
  draws.
- **Spawned a concrete improvement:** `provenance-at-handoff-lens.md` (4 of the 5 bugs share one
  class: a value's assumed semantics ≠ its producer's). Honest framing: the lens buys *reliability*
  (raise a ~40%-found class toward ~100%), not new capability. **What caught it was the root basis-rule
  / trace-to-producer discipline** (an adhoc by-hand pass), not clippy machinery and not anneal-dev —
  a root-framework property. The "clippy's lenses narrowed attention" idea was an n=1 overreach,
  retracted; lenses remain *additive to scope* (prior position holds).

Net: the real-codebase run **did not** overturn "controlled single-task A/B ties" — it sharpened it.
The honest value remains observational + the self-improvement loop (this run *is* an instance: a real
review surfaced a real latent bug-class and a concrete lens to close it).

---

## Goal (original v0 design — retained below the verdict for the resumption case)
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
