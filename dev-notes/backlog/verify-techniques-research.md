# Verification techniques for anneal's independent-verify phase (research)

**Status:** RESEARCH RUN LAUNCHED 2026-06-03 (deep-research `wf_4f010d37-ae0`, background; task
`wk2gm2y4h`). Awaiting result.

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
