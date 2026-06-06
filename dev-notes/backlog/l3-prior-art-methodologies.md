# L3 prior-art — verified-multi-step-agent methodologies (RAN 2026-06-06)

**Status:** RAN — one grounded web sweep (general-purpose subagent `ad7b5c242dd4083e3`, opus) +
operator-side verification of the headline (APF abstract fetched directly). The L3-method
investigation scoped in `platform-native-vs-anneal-delta.md`. Verdict + adoptables below.
Complementary to session-4's archived research (which checked academic *process literature* +
design-first-vs-act-first; this checks **agent-methodology prior art** specifically).

## Verdict — kill-switch OFF (no dominator, no strict superset)
Independently corroborates session-4's "no superior framework." The field **splits anneal's bundle
across two camps**; the two closest peers each miss a *different* load-bearing piece.

- **APF — Agentic Problem Frames** (arXiv **2602.19065**; abstract fetched + verified by the operator,
  not recalled — it postdates the Jan-2026 model cutoff). The **near-twin**: an Act-Verify-Refine (AVR)
  loop + Agentic Job Description (AJD) spec; grounds reasoning in "verified knowledge assets" (not "in a
  vacuum"); a verify/human gate; aims domain-general. **Missing: falsification** ("falsification" does
  not appear). **Validated by "a conceptual proof" / two case studies — the SAME unmeasured-reliability
  gap anneal has.** → cite APF as BOTH closest prior art AND as evidence that anneal's falsification
  cycle is the differentiator. (APF was also the peer session-4 found — now double-confirmed.)
- **Anthropic three-agent harness** (Planner→Generator→Evaluator; hard context resets; skeptic-calibrated
  Evaluator; human oversight for calibration). Strongest **fresh-context independent verify** —
  arguably better-engineered than anneal's. **Missing: basis rule / evidence-grounding, falsification;
  coding-specific.** ⚠ **Medium confidence** — sourced from InfoQ reporting (Apr 2026), NOT Anthropic's
  primary writeup. Deeper dive owes: find the primary source.

Everything else: reflection/critic techniques (Reflexion 2303.11366, Self-Refine 2303.17651, CRITIC
2305.11738) fail the *independent*-verify bar (self-critique); LATS (2310.04406) + the plan-then-execute
guide (2509.08646, a *security* impl guide) lack verify-as-discipline + grounding; agent frameworks
(LangGraph/DSPy/AutoGen/CrewAI/OpenAI SDK) are *libraries* (the construction kit, not the rulebook);
spec-driven dev (GitHub Spec Kit, Kiro, BMAD, SDD survey 2602.00180) grounds *code* not *claims* and has
no fresh-context re-derivation; Jackson "designation" is the pre-LLM RE ancestor of grounding.

## APF: closest on INGREDIENTS, different on STRATEGY (operator probe 2026-06-06 — sharpens "near-twin")
"Near-twin minus falsification" understated it. Two axes:
- **Ingredient axis — near-twin:** APF independently has evidence-grounding, a verify + human gate, the
  conceptual-proof gap. Closest parts-list out there.
- **Strategic/frame axis — genuinely different:** APF's frame is **control-systems + RE** (the name echoes
  Jackson's *Problem Frames*). My abstract-fetch: AVR *"functions as a closed-loop control system,"*
  *"anchoring stochastic AI within deterministic business processes"* — verification is **against the
  environment's objective feedback** (execution results; per the subagent's full-text read, callbacks/
  approvals). anneal's frame is **epistemic** (basis rule + fresh-context re-derivation of the *reasoning*)
  for the regime where the environment **can't cheaply adjudicate**.

→ **Falsification is a SYMPTOM, not the root:** anneal falsifies the *reasoning* because it can't lean on
environmental feedback; APF doesn't need it because it does. Different verification *substrate*.
→ **They partition the regime space, not compete:** APF owns the **deterministic-feedback** regime;
anneal owns the **no-cheap-oracle / expensive-late-verification** regime (exactly what anneal already
scopes its claims to). This makes the kill-switch verdict *even more clearly OFF* (different regime) AND
sharpens anneal's positioning (the methodology for the regime APF's control-loop can't serve).
**Confidence:** the control-loop framing = my abstract fetch (high); "substrate = environmental feedback"
= partly the subagent's full-text read (medium); "fundamentally different strategy" = a grounded
*inference* from the abstract framing, NOT a line-by-line read of all 18pp — a full APF read would
confirm/nuance the regime-partition.

## The empirical gift — anneal's core rules are now literature-backed
**Huang et al. "LLMs Cannot Self-Correct Reasoning Yet"** (2310.01798) + **Kamoi et al.** (2406.01297):
self-critique *without external feedback degrades* performance. This is the published empirical basis
for anneal's two most load-bearing rules — **fresh-context independent verify** and **AI confidence ≠
evidence**. They are not arbitrary; the alternative (self-critique) is shown to fail. → material for
`foundation.md` / the intent statement.

## anneal's defensible delta
The **bundle**: basis rule ∧ fresh-context independence ∧ **two-pass falsification (intent +
mechanical)** ∧ operator-irreducible gate ∧ domain-render. Sharpest single differentiator: the
**falsification cycle** — no surveyed peer frames verify as *active falsification*, let alone splits
intent from mechanical. (Honest caveat: each *ingredient* exists somewhere; the delta is the specific
assembly + the falsification cycle.)

## Adoptables — TRIAGED (2026-06-06, anneal's own additive-reflex/iterative-narrowing discipline applied)
Subtract what anneal already covers; only the residual is a real adoptable. Most collapse to
**CONFIRMATION** — anneal independently arrived at what the harness/APF engineer (reassuring, cite as
external validation). Real residual ≈ **1.5 items**.

1. **Calibrated-skeptic verifier rubric** (Anthropic harness) → **mostly CONFIRMATION.** anneal already
   does *criteria-first verify* (rubric before output — `verify-vs-original-requirements` + intent-pass
   criteria-first). New bit (few-shot calibration *set*) risks domain-leak in a domain-agnostic method →
   instance-level at most. **Low.**
2. **Tool-grounded claim-checking as the basis-rule MECHANISM** (CRITIC 2305.11738) → anneal has the
   *gate* (cite-or-assumption) + re-open-each-citation verify leg; CRITIC adds a generative *procedure*
   (extract claims → retrieve per claim → cite). anneal leaves investigation ad-hoc → **instance-level
   investigate technique, not a framework rule** (framework-wide = over-prescription). **Medium, instance.**
3. **Structured-handoff-artifact schema** (Anthropic harness) → **CONFIRMATION.** anneal has it (tracker +
   falsification/verify dispatch-brief template). **Low.**
4. **AJD acceptance/boundary spec** (APF) → **CONFIRMATION.** anneal has the requirements record (R1..Rn)
   + per-decision acceptance criteria (tracker body-shape (c)) + scope (the foundational completeness
   claim). **Low.**
5. **Active/selective verification** → **the genuinely novel one — and the most tensioned.** Serves the
   "≤ tokens" claim (spend verify budget on uncertain cases) BUT "judge which cases are uncertain"
   reintroduces the **willed judgment anneal exists to remove** (the cost-gradient trap —
   `convergence-cycle-mechanical-enforcement`). **anneal already has a STRUCTURAL version:** mechanical
   falsification routes by **status/artifact-strength** (textual falsification for `[VERIFIED]`;
   runtime-exercise-by-verify for `[CONDITIONAL]`/`[AUTO-ACCEPTED]`; weak vs strong, §3.1) — selection by
   *mechanical* signal, never AI confidence. Residual adoptable = make that token-allocation **explicit +
   measured** (driven only by the mechanical signal). **Folds into the measurement thread.**
   (Source cited by the subagent was GLEAN/2603.02798 — **unverified by the operator**; the mechanism
   stands on anneal's own §3.1, not on that cite.)

**The honest sting (#5):** this run is live evidence — ~4 convergence cycles + ~5 opus subagents to
verify a **3-sentence clause.** anneal's thoroughness is in genuine tension with its "≤ tokens" claim;
if verification overhead is high, the cheaper-than-act-first claim is *at risk*. The measurement thread
tests it; selective-verification-by-mechanical-signal is the principled lever if the token metric comes
back unfavorable. **→ this is a live input to `anneal-empirical-validation-experiment` / the token metric,
not a bolt-on.**

## The shared gap — is it closeable? (elaboration 2026-06-06)
anneal's core claim (sounder + cheaper) is **asserted, never measured** — validated only by conceptual
proof (coherent design + literature-endorsed parts). Coherence ≠ value; the gap is the leap to
*demonstrably better outcomes.* APF sits in the identical spot. **Closeable?** Not the *universal* claim
(no general soundness oracle; over-generalization; reasoning-ceiling) — that stays conceptual. But the
*bounded* claim IS provable AND refutable: sounder (seeded-defect catch-rate proxy) at ≤ tokens, in the
silent-failure regime, pre-registered tasks. The mitigation (the proof thread) converts "unproven" →
"bounded-validated-in-regime + scoped residual" = exactly the V1 definition. **Kicker:** APF is stuck
because it has *no testbed*; anneal *has instances* → it can run the A/B APF can't → closing this gap is
anneal's single most differentiating move. (Mitigation is planned + prioritized: the proof-first order.)

## Confidence + gaps
- APF core: **triple-grounded** (session-4 + this sweep + operator abstract-fetch). High.
- "No dominator": a broad-sweep **negative** — a longer-tail effort could exist (RE / formal-methods-for-LLM
  venues, ICLR/NeurIPS agent tracks, primary BMAD/Tessl docs not fully swept).
- Anthropic harness: **medium** (single secondary source, InfoQ). Adoptable #1/#3 inherit that.
- "APF lacks falsification": confirmed in abstract + AVR sections; NOT a line-by-line read of the full 18pp.
- Framework-library classifications: from comparative surveys (adequate for the negative, not primary reads).

## Relates to
- `platform-native-vs-anneal-delta` — L3 was scoped there; this is the RUN. Confirms "L3 = anneal's
  genuine core" with prior-art grounding.
- `framework-intent-vision-statement` — the delta (the bundle + falsification) sharpens the intent; the
  self-correction papers (2310.01798, 2406.01297) ground the basis/independence rules empirically.
- `anneal-empirical-validation-experiment` — APF's conceptual-proof gap is EXACTLY what anneal's proof
  thread would close; running it is how anneal escapes the gap APF/anneal share. Cite APF there.
- The 5 adoptables — candidate inputs to verify-side / investigate-side cycles (not yet filed as items).
- Origin: operator "can we do this now", 2026-06-06.
