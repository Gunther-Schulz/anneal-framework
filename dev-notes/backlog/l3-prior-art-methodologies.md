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

## Adoptables (candidate inputs; source each)
1. **Calibrated-skeptic verifier rubric** (Anthropic harness) — give the fresh-context verifier an
   explicit calibration set + scoring criteria, not just "re-derive."
2. **Tool-grounded claim-checking as the basis-rule MECHANISM** (CRITIC 2305.11738) — draft → extract
   checkable claims → retrieve evidence per claim → revise + cite.
3. **Structured-handoff-artifact schema for context resets** (Anthropic harness) — specify the exact
   state the fresh verifier needs to "execute cold."
4. **AJD-style acceptance/boundary spec** (APF) — a pre-registered "what correct looks like" contract
   sharpening investigate-design's output.
5. **Active/selective verification** — spend verify budget on uncertain cases — directly serves anneal's
   "≤ token cost in the expensive-verification regime" claim. (Verify the source cited — GLEAN/2603.02798
   was the subagent's; unverified by the operator.)

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
