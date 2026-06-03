# Multi-voter adversarial verify for no-mechanical-predicate claims

**Status:** OPEN — candidate verify-mechanism, surfaced 2026-06-03 from the deep-research
adversarial-verify mechanics + the APF deep-read. **Validate-before-adopt** (its payoff is
itself unmeasured → depends on `anneal-reliability-measurement`).

## The observation
anneal's falsification step (`core.md` §4.1.4) is a **deterministic predicate over a
re-runnable search/read** (any-match / any-outside-scope / expected-match). Epistemically
strong — but it only bites on claims with a **mechanical handle** (code coupling, references,
scope). Claims with **no** mechanical predicate (is this design sound? the right abstraction?
is this synthesis accurate?) can't be statically discharged — §4.1.4 routes them
[CONDITIONAL]→verify, where anneal leans on a **single** independent (separate-context)
verifier. One checker, no quorum.

## The candidate
Borrow the deep-research / APF pattern for *exactly that claim-class*: a **multi-voter
adversarial quorum** — N independent skeptics, each prompted to **refute** (default-skeptical),
majority-to-kill (deep-research uses 3 votes, 2/3 to kill; APF uses a separate critic that
"does not approve their own work"). Rationale: independent voters **de-correlate errors** —
directly attacking the "closed loop of correlated errors when the verifier shares the actor's
base model" that the self-correction literature flagged (TACL; trustworthy-agentic survey
2605.23989; see placement research).

## Scope discipline (why this is NOT a blanket change)
anneal's single-independent-context verify is **deliberate minimalism**; a quorum is real cost
(N× verify spend). This is a candidate for the **no-mechanical-predicate claim class only** —
NOT for claims a falsification predicate already discharges deterministically (there, one
mechanical check beats any LLM vote). Additive-reflex risk if applied broadly.

## Validate before adopting
Whether 3 votes actually catch more than 1 independent context is itself an **unmeasured**
claim — adopting blind would violate anneal's own basis discipline. Gate on
`anneal-reliability-measurement` (an A/B: 1-context verify vs N-vote quorum on a claim set with
known-planted soft errors).

## Relates to
- `anneal-reliability-measurement.md` (the validate-before-adopt gate; A/B testbed).
- `anneal-placement-and-improvement-research.md` (origin: deep-research adversarial-verify +
  the self-correction "closed loop" evidence + APF's separate-critic).
- `clippy-run-findings-dispatch-coupling.md` §4.1.4 ([CONDITIONAL]→verify = the claim-class
  boundary this targets).
- `verify-vs-original-requirements.md` (sibling verify-discipline finding).
