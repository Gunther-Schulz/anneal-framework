# Verification techniques for anneal's independent-verify phase (research)

**Status:** RESEARCH RUN DONE (clean solo re-run `wf_93a152ec-4da`, task `w7abv8l2k`, 2026-06-03;
first concurrent attempt `wk2gm2y4h` broke in the 3-run overload). 20 sources, 93 claims, top-25
adversarially verified (22 confirmed / 3 killed). Raw at
`dev-notes/research/verify-techniques-deep-research-2026-06-03.raw.json`. Verdict below.

## VERDICT (2026-06-03)
**Standout adoptable: criteria-first verification.** Borrowable for anneal's verify on
no-mechanical-handle judgment claims, in priority order:
1. **Criteria-first / self-grounded verify (THE standout)** — verifier elicits/fixes its success
   criteria BEFORE seeing the work product, then judges against them. Peer-reviewed (SGV, ICLR 2026,
   arXiv 2507.11662). Targets **"agreement bias"** — the verifier over-validating the actor and
   rationalizing its flaws (exactly anneal's independent-verifier risk on soft claims). **KEY:
   agreement bias is NOT fixed by more compute** (failure-detection 44% baseline → 48% CoT+majority
   → 55% reasoning+extended-thinking — all far below ideal); only the criteria-first *restructuring*
   fixes it. So a bigger/longer verifier is NOT the answer — reorder it.
2. **Different-MODEL verifier (not just different-context).** Same-base-model judge over-rates its
   own outputs (self-preference bias; NeurIPS 2024 oral 2404.13076; self-recognition linearly
   predicts self-preference). anneal mandates separate-*context*; evidence says separate-*model*
   breaks correlated self-confirmation more. Candidate upgrade. (Open: model vs context share of the
   gain — no source A/B'd it → experiment.)
3. **Decompose judgment claims into small falsifiable sub-questions** — beats holistic agent-as-judge
   (holistic judges MISS judgment-class errors, catch only obvious failures; decomposition F1
   +12–48pp, preprint 2601.15808, single small subset). **Converges with the process-literature run**
   (Platt falsifiability-gate + Gunter exclusion-obligation): two independent runs, same conclusion —
   extend anneal's falsification-predicate to judgment claims by decomposing them into
   exclusion-oriented sub-questions with criteria fixed first.
4. **Swap-and-recheck** for pairwise judging (position bias flips ~30% of GPT-4 verdicts). Narrow.

**Multi-voter quorum** (answers `multivoter-verify-no-predicate-claims` validate-before-adopt):
**MARGINAL, not a multiplier — and the lever is MODEL DIVERSITY, not vote count.** Disjoint-model
panel > single large judge (less bias, 7× cheaper) but non-uniformly; debate > majority voting by
only ~1.25–4.08pp (3/4 within CI noise) and sometimes worse; the amplification proof collapses when
voters share biases. → prefer a disjoint-model panel over same-model N-vote.

**Number correction:** the "~+20pt failure-detection" lead was a **conflation** — SGV's
failure-detection gain is **+25pp** (+14pp accuracy); the +20pp is a *downstream task-completion*
SOTA number. Cite +25pp.

**Biggest caveat (domain-transfer gap):** NONE of this was measured on **text-only judgment claims**
(design-soundness/right-abstraction/synthesis-accuracy) — anneal's exact target. Measured on agent
trajectories, visual-math, pairwise preference. **Mechanisms transfer as principles; effect sizes do
NOT.** Precisely the gap anneal's own experiment could close.

## Origin
Two latent research seeds from this session that the placement run didn't close:
- The **self-grounded-verification** lead (placement-research lead #1, claimed ~+20pt
  failure-detection) **fell below the placement run's top-25 verification cut** → still
  unverified; flagged "re-probe if pursued."
- The **multi-voter adversarial quorum** candidate (`multivoter-verify-no-predicate-claims.md`)
  is **validate-before-adopt** — its core claim ("N votes beat 1 verifier") is unmeasured.
This run resolves both + surveys what anneal's verify phase could adopt for the
**no-mechanical-predicate claim class** (soundness/quality judgments, where the falsification
predicate doesn't bite and anneal leans on a single separate-context verifier).

## Sharpened deep-research question (as fired)
> Survey + adversarially verify verification/self-evaluation techniques an agent can apply to its
> OWN work before shipping, for strengthening an INDEPENDENT-verify phase: (1) **self-grounded
> verification** — elicit criteria in isolation BEFORE verifying; VERIFY/REFUTE the ~+20pt claim
> + find its primary source; (2) **LLM-as-judge** reliability + known biases (self-preference,
> position, verbosity) + when trustworthy; (3) **multi-agent/debate/multi-vote** — does an
> N-voter quorum beat a single verifier, by how much (evidence)?; (4) **verifier–actor
> independence** — does separate-context / different-model measurably cut correlated
> self-confirmation errors?; (5) **criteria-first vs output-anchored** judging. Asserted-vs-
> measured for each; cite primary; flag peer-reviewed vs preprint.

## On result — feeds these items
- `multivoter-verify-no-predicate-claims.md` — supplies the validate-before-adopt evidence (does
  the quorum earn its cost?).
- `verify-vs-original-requirements.md` — criteria-first / self-grounded verification bears on the
  fact-vs-intent (Callback/Confirm) verify obligation.
- `anneal-reliability-measurement.md` — the verifier-independence + quorum questions are A/B-able.

## Relates to
- `anneal-placement-and-improvement-research.md` (self-grounded-verification lead origin + the
  self-correction "closed loop / correlated errors" evidence).
- `process-literature-for-anneal-research.md` (Fagan/Cleanroom inspection = the *SE-process* side;
  this run is the *LLM-technique* side — disjoint by design).
