# Measuring anneal's value — can we show a run is actually more sound/dependable?

**Status:** OPEN — exploratory, **operator-flagged next exploration** (2026-06-03).
Confirmed by the deep-research run (`wf_7dbc2c5e`, raw at
`dev-notes/research/anneal-placement-deep-research-2026-06-03.raw.json`) as the
**biggest real gap** — and the run gave it concrete material + a lead design (below).
Not yet designed; this is now the live thread of the placement research.

## The gap (CONFIRMED by the run)
anneal's whole claim — *it makes open-ended AI work sound and dependable* — is
**asserted, never measured.** No evidence that an anneal-driven run is *sounder* than the
same AI working unstructured. The run found this is not unique: the closest peer (APF,
arXiv 2602.19065) has the **exact same unmeasured-reliability gap** — it validates only via
qualitative "conceptual proof" and solicits partners for empirical validation. Closing the
gap would differentiate anneal *and* tell us which parts of the discipline carry the gains.

## ⭐ Lead design (the run's strongest finding): A/B-via-instances — the path APF can't walk
APF couldn't run empirical validation because it has **no testbed**. **anneal has instances**
(clippy / daneel / bauleitplan) — so an **ablation/A-B study is actually runnable here**:
anneal-disciplined runs vs an ungoverned baseline (same model + tool access), scored on a
domain benchmark, **before/after** — the same template the eval layer uses (VeriGuard,
ReliabilityBench). This is the most promising concrete path and the clearest differentiator.

**Lead with the TOKEN metric (operator insight, 2026-06-03).** Score the A/B *first* on
**tokens-to-correct-outcome**, not soundness. Tokens are **ground-truth-measurable** (just
count them) — unlike "epistemic soundness," which needs a proxy. The operator's experience is
that anneal (design-first) uses *fewer* tokens than act-first agents (shoot-first-fix-later);
that claim is currently **asserted-not-measured** (same status as the soundness claim) but is
the **cheapest to convert into evidence** and a compelling differentiator. Mechanism (why
design-first should be cheaper): an error caught at design time costs *design tokens*; the same
error caught post-implementation costs *re-implementation + tool re-runs + re-ingested context*,
and act-fix loops **compound** (tokens/iteration climb). External comparative token-cost
evidence to calibrate this comes from the dedicated ordering run →
`design-first-vs-act-first-research.md`. **Regime caveat:** the token win is expected in the
open-ended / expensive-late-verification regime, NOT where the env is a cheap instant oracle.

## Borrowable measurement methods (from the EVAL layer, NOT the methodology layer)
The run found measurement is borrowable — but with a **scope caveat that runs through all
of it** (see below). Three verified templates:
- **VeriGuard's metric-on-named-benchmark** (3-0): define a quantitative metric, run on a
  *named* benchmark, report before/after (it cut ASR 51.9%→0.0% on Agent Security Bench).
  Caveat: TSR *rose* on weaker backbones but **dropped on Claude-Sonnet-4** (89.0→85.1) —
  don't claim "maintains/raises completion."
- **AgentCompass's four-stage analytical pipeline** (3-0): error identification/categorization
  → thematic clustering → quantitative scoring → strategic summarization. A transposable
  *verification-stage scaffold*.
- **Trustworthy-agentic survey's outcome+PROCESS metrics** (3-0): constraint-violation rates,
  **trace completeness/coverage** + scenario-to-metric **release-gating** thresholds. The
  *process* metrics map most plausibly onto "was the discipline actually met."
- Surfaced but NOT 3-vote-verified (use with care): **ReliabilityBench** (2601.06112 —
  k-trial pass rates, Reliability Surface R(k,e,l), perturbation robustness), **Tau²-Bench
  pass^k**, "Beyond Benchmark Islands" (2603.14987).

## ⚠️ The scope caveat (the core of why this stays an *exploration*)
**Every borrowable template measures SAFETY (ASR), task COMPLETION (TSR), or post-hoc
debugging — NOT the epistemic soundness of open-ended work, which is anneal's actual claim.**
They transfer as measurement-methodology *templates* (define metric → name benchmark →
before/after), **not drop-in metrics.** Designing a metric for *"was every load-bearing claim
grounded"* / *"did state-coherence hold (nothing silently dropped)"* remains **anneal's own
unsolved problem.** Note the gap is NOT field-wide: agent *evaluation* does have quantitative
reliability measures (pass^k, ReliabilityBench) — which is *why* measurement is borrowable;
it's *methodology/framework* papers (APF, anneal) that lack it.

## Two metric families to separate (unchanged, still the right split)
- **Process metrics** (did the discipline fire?): loopback rate, false-[READY] rate (V-5),
  claim-groundedness, verify catch-rate. Easy; measures *adherence*, not *value*. ← the
  survey's process metrics (constraint-violation, trace completeness) are the borrowable kin.
- **Outcome metrics** (was the result sounder?): correctness vs unstructured baseline,
  shipped-defect rate, rework. Measures *value*; the hard ones — and what the A/B path targets.

## Third axis: grounding ratio (refine-vs-overthink) — operator distinction, 2026-06-03
The design-first run surfaced an *overthinking* counter-signal (more internal reasoning → worse
outcomes, cheap-oracle regime; Cuadron et al. 2502.08235). Operator's correct objection: that
metric measures *internal-reasoning displacing environmental-interaction* — and anneal is the
**architectural opposite** (the basis rule FORCES search/read; independent/executable verify
FORCES a check against reality). anneal *refines*, it doesn't *ruminate*. **But "we don't
overthink" is asserted-not-measured** (same status as the other claims) and is **regime-bound**
(in a cheap-oracle task even anneal's front-loaded design could be net-overthinking — fine, anneal
isn't *for* that regime). **The reframe: the overthinking score is an INSTRUMENT, not a threat.**
Score anneal on the internal-reasoning-vs-environmental-interaction ratio — if "refine not
overthink" is true, anneal should be **low overthinking AND high outcome**. Wrinkle: the metric
was built for act-in-environment agents (edit/run/test); anneal's interaction is *evidence-
gathering* (search/read/verify), so the operationalization must be **adapted to count
grounding-reads as interaction** — and doing so forces an operational definition of
refine-vs-overthink, which is itself the proof. → a 3rd measurement axis alongside outcome + tokens.

## Open questions (from the run — feed the design)
1. What metric captures epistemic soundness? Can the survey's process metrics be
   operationalized into an anneal-specific instrument — a **graded audit of whether basis-rule
   + state-coherence were met per work episode**?
2. Is the A/B-via-instances study (above) the right first build, and which instance is the
   cleanest testbed (clippy has the most runs + git-checkable outcomes)?
3. Spec-free analog of the **offline-verify / online-monitor split** — can a stable epistemic
   standard be "compiled once" into cheap per-step conformance checks? (Bridges to the verify
   thread.)

## Existing substrate to build on
`dev-notes/validation-watch.md` already logs design-uncertainty predictions + the
production-signal to watch — a partial, already-wired measurement surface. Could a
measurement story turn V-N "production signals" into tracked, scored outcomes?

## Relates to
- `anneal-placement-and-improvement-research.md` (the research origin; verdict recorded there).
- `dev-notes/validation-watch.md` (existing partial measurement substrate).
- Method-kernel-adjacent if it adds a measurement mechanism → anneal-dev + kernel-independent verify.
