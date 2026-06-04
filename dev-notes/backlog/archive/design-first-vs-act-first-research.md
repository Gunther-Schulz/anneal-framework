# Design-first vs act-first ordering — is anneal's ordering valid, or is post-analysis better? (research)

**Status:** RESEARCH RUN DONE (clean solo re-run `wf_ee31a53c-5a0`, task `wnzx09e30`,
2026-06-03; first attempt failed in a 3-concurrent-run overload). 21 sources, 98 claims, top-25
adversarially verified (20 confirmed / 5 killed). Raw at
`dev-notes/research/design-first-vs-act-first-deep-research-2026-06-03.raw.json`. Verdict below.
Validity test with a kill-switch — **kill-switch NOT triggered, but design-first NOT proven.**

## VERDICT (2026-06-03)
**No equal-or-superior design-first framework found → don't stop anneal. But design-first is
UNREFUTED *and* UNPROVEN — the deciding experiment has never been run by anyone.**

- **Spectrum: nearly everything in the agent space is act-first / loose-plan-then-iterate.**
  ReAct, Reflexion/ReflAct, Self-Refine, Plan-and-Solve, ADaPT (decompose-on-failure), DOVA — all
  act-first. **APF itself is act-first** (Act-Verify-Refine; execution precedes verification;
  "Dynamic Specification" concretized just before execution) — this *sharpens* the placement run:
  even the closest peer is act-first on the ordering axis.
- **anneal's distinguishing feature appears genuinely unmatched.** The only design-first PEERS
  (CARE; the TEACh plan-verifier) are WEAKER: their pre-commit review is by the **authoring
  parties** (CARE = joint SME+developer self-review), NOT separate-context INDEPENDENT design
  verification. No equal-or-superior framework with outperformance evidence → kill-switch off.
- **The core comparative question is UNANSWERED.** No rigorous design-first-vs-act-first
  head-to-head on OPEN-ENDED work measuring correctness AND token cost exists. APF/CARE/TEACh
  supply zero comparative ordering evidence (APF & CARE both end soliciting partners).
- **The one plan-first-wins number** (Plan-and-Solve +~5pp over Zero-shot-CoT) is entirely in the
  **cheap-oracle arithmetic regime** the brief warned against — and is "more-plan vs less-plan,"
  not plan-vs-no-plan. Can't generalize.
- **Real counter-signal (anti-rose, honest):** the *overthinking* study (Cuadron et al.,
  arXiv 2502.08235; SWE-bench Verified) — MORE internal deliberation correlates with WORSE
  outcomes; picking lowest-overthinking trajectories gained ~30% perf / cut ~43% compute. **This
  is act-first winning where the oracle is cheap/instant.** Properly scoped to that regime — NOT
  evidence for design-first, and a caution against a *blanket* deliberate-always policy.
- **Token-cost hypothesis (operator's "fewer tokens") UNTESTED.** No source measures it; DOVA's
  40–60% savings come from an adaptive thinking-budget, NOT design-first ordering — does not
  corroborate.
- **(a)-vs-(b) discriminator:** evidence is CONSISTENT with (a) neglected-but-better (act-first
  dominates because flagship benchmarks — SWE-bench/GSM8K/ALFWorld — are cheap-oracle /
  act-first-friendly *by construction*: a benchmark-incentive artifact) but does NOT establish it;
  (b) not supported either. **The comparative evidence base for the precise question does not exist
  yet — that absence is the key finding.**

## What this means / next
- **anneal's instances (clippy) are the testbed the literature lacks** — the expensive-regime
  design-first-vs-act-first head-to-head (correctness AND tokens) that NO ONE has run. This is both
  the validation path AND a potential contribution. → drives `anneal-reliability-measurement.md`
  (token A/B in the expensive-verification regime, not the cheap-oracle regime).
- Open: does the overthinking counter-signal survive OUTSIDE the cheap-oracle regime, or is it an
  artifact of free trial-and-error? (Determines whether it's a real threat or just confirms regime
  discipline.)
- **Refine-vs-overthink (operator, 2026-06-03):** the overthinking metric measures
  *internal-reasoning displacing environmental-interaction* — anneal is the architectural opposite
  (basis rule + executable verify FORCE grounding), so it shouldn't map. But that's
  asserted-not-measured + regime-bound. **The metric is an INSTRUMENT, not a threat** — adapted to
  count evidence-gathering (search/read/verify) as interaction, it operationalizes "refine ≠
  overthink" and becomes a 3rd measurement axis. → folded into `anneal-reliability-measurement.md`.

## The discriminator the run resolved (kept for context)

## The goal (operator, 2026-06-03)
Verify whether anneal's **design-first** ordering (investigate → design + converge to soundness
via INDEPENDENT verification BEFORE implementing → implement → verify) is actually valid, OR
whether the prevailing **act-first** ordering (shoot-first, verify/fix-later) is better for
open-ended work. The operator can't find anyone doing anneal's strong design-first and finds the
*absence* suspicious — not because it's novel (it isn't; it's mature-SE discipline) but because
it seems obvious. **If a clearly superior framework is found, the operator will stop developing
anneal.** Empirical anchor so far: only anneal (specifically clippy) has outperformed everything
else the operator has tried — but that's small-n / own-experience.

## The discriminator the run must resolve
Two opposite explanations for "no one does it":
- **(a) Neglected-but-better** — design-first wins for open-ended / expensive-late-verification
  work, but the field skips it: benchmarks reward act-first + cheap auto-verify; base models are
  RL'd to act; act-first demos better; design-soundness-without-execution is the hard problem
  everyone punts to the environment; tokens were treated as cheap.
- **(b) Neglected-because-not-better** — the absence is signal; act-first/post-analysis is
  genuinely superior and the operator's positive experience is biased / lucky.
The run discriminates (a) from (b) with comparative evidence, split by verification-cost regime.

## Why this run is distinct (not covered by the other research)
- Placement run (`anneal-placement-and-improvement-research.md`, done) — framed around anneal's
  four *disciplines*; **never optimized for the design-before-act ordering axis**, so its "no
  superior found" is under-tested on exactly this axis. This run closes that.
- `process-literature-for-anneal-research.md` (launched) — mines *mature SE/RE* for disciplines
  + the SE *economics* of ordering (Boehm). This run is the *current agent-space* ordering
  superior-check + head-to-head comparative evidence.

## The brief (as fired — full args in git history / run script)
Anti-rose (hypothesis to refute = "design-first is better"); maps the spectrum
(ReAct / Reflexion / Self-Refine / Plan-and-Solve / Plan-and-Execute / ADaPT / LLMCompiler /
ToT / LLM+P / spec-first coding agents / APF) on a design-first↔act-first axis; demands
head-to-head evidence on OPEN-ENDED tasks measuring **correctness AND token/compute cost**;
splits all results by verification-cost regime (cheap-oracle → act-first plausibly wins;
expensive/late-verification → design-first's case).

## On result
- A named equal/superior framework → operator's kill-switch answer (evaluate adopt-instead).
- No superior + evidence design-first wins in the expensive-verification regime → (a) confirmed;
  feeds positioning + the measurement A/B.
- Evidence act-first wins even in anneal's regime → (b); reconsider the approach honestly.
- Token-cost evidence either way → calibrates `anneal-reliability-measurement.md` (token A/B).

## Relates to
- `anneal-placement-and-improvement-research.md` (the axis it under-covered).
- `process-literature-for-anneal-research.md` (the SE-economics side of the same question).
- `anneal-reliability-measurement.md` (token-cost evidence → the measurable A/B).
