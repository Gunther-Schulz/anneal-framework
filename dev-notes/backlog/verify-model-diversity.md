# Verify model-diversity — should the checker run on a different model than the actor?

**Status:** OPEN (narrowed + renamed 2026-06-04, was `multivoter-verify-no-predicate-claims` —
the old name implied multi-voting, which is dead; see below). Two of this item's three threads
are CLOSED, leaving ONE live residual:

- **Multi-voting / quorum — DROPPED.** The verify-techniques research deflated it ("model
  diversity > vote-count; quorum gains marginal/task-dependent, sometimes worse"). Dead; do not
  revive.
- **The intent-falsification pass — SHIPPED** (session 6, run `intent-falsification-convergence-pass`;
  live in `core.md` §4.1.4 + the `[VERIFIED — surfaced]` disposition). This item was its
  prospective wiring; now realized. The judgment-class sibling of the mechanical falsification pass.
  - **Conformant-success track record (practice 1):** **n=1** — the foundation-invariants run
    (caught 2 BLOCKING soundness flaws the mechanical convergence-falsification passed clean past).
    **n=2** — the `anneal-dev-model-tier-policy` run (2026-06-04 session 7): caught the
    *absent-by-default floor* (Finding 2) that all **8 standardized lenses + the mechanical pass
    missed** → drove the D5 bootstrap flip. Both are real flaws the mechanical/lens passes
    structurally could not see (the "does it serve its intent?" question). True-positives, not
    false-accept measurements — the pass keeps earning its keep; n accumulates.
- **LIVE residual — model-diversity for verify.** anneal's verify-independence today rests on
  *fresh-context* isolation only, NOT a *different model*. INV-3's anchor (Panickssery et al.)
  says a verifier sharing the actor's base model inherits self-preference bias, so a
  different-model checker is the stronger form. **Open question:** should anneal's verify run on
  a model distinct from the actor's — and how does that reconcile with the **model-tier floor**
  (shipped session 7 via `anneal-dev-model-tier-policy`), which now pins author AND verifier to
  the same top tier (F8)? Options: carve verify out of the floor, seek diversity *within* the top
  tier, or accept the trade. (Operator accepted the trade for now — this item holds the option open.)
  - **2026-06-05 (campaign ②, fork ε):** operator **re-confirmed accept-the-trade**; this item is
    **dropped from the ② cycle** (its live residual is a held decision, not a design). Stays OPEN
    holding the option — revisit only if the model-tier floor is reopened (then carve-out vs
    within-tier-diversity is the live fork). Not method-kernel work until then.

**(History below — the reframe + the shipped intent-falsification design — kept as context.)**

## The observation (unchanged)
anneal's falsification step (`core.md` §4.1.4) is a **deterministic predicate over a
re-runnable search/read** (any-match / any-outside-scope / expected-match) — the orchestrator
computes holds/falsified, no judgment. Epistemically strong, but it only bites on claims with
a **mechanical handle** (existence, dependents, scope). Claims with **no** mechanical predicate
(is this design *sound*? does it serve its *intent*? the right abstraction?) cannot be
statically discharged — today anneal routes them to a single independent verifier, and the
SOUNDNESS half rests entirely on the operator.

## The candidate (REFRAMED → single intent-falsification)
A **single, criteria-first, adversarial intent-falsification**: state the design's intent
INDEPENDENTLY, then a default-skeptical attack on whether the design *serves* it. NOT a
multi-voter quorum. The vote-count machinery is overkill — deflated by the verify-techniques
run ("model diversity > vote count; quorum gains marginal/task-dependent, sometimes worse")
AND by the n=1 below (a single check caught blocking flaws). Drop the quorum; keep the
judgment-class *attack*.

## n=1 demonstration (foundation-invariants-register run, 2026-06-04) — STRONG signal
Run ad-hoc (operator-requested experiment), grounded in dev-process practice 11 + operator.
- **Round 1** found 2 **BLOCKING** soundness flaws the mechanical convergence-falsification
  confirmed clean past: the new machinery's own enforcement was self-dischargeable (AI writes
  the string the hook checks) and its protection marker was overclaimed-as-binding.
- **Round 2** (on the corrected design) found a **notable consistency defect** (the
  operator-detection honesty applied to one mechanism but not its sibling).
- Lesson: **mechanical and judgment checks have non-overlapping blind spots** — the mechanical
  pass was *right* that all bases held; it structurally could not see the question that
  mattered. Also: the same-model agreement-bias worry took a hit (the model refuted its own
  design, hard). Caveat: this is a **true-positive demonstration, not a false-accept
  measurement** — enough to build on, not enough to stop watching.

## The kernel-integration problem (the hard part — must be solved in the decide-ahead)
The reliability we got in the experiment came from **dev-process** machinery (practice 11 =
AI-first-judge / operator-second-judge) — which is **NOT core anneal**. Porting it to the
kernel collides with two kernel constraints:
1. **Core anneal keeps judgment OUT of the falsification pass** — the orchestrator computes
   holds/falsified from a predicate; the subagent does not judge. Intent-falsification
   *reintroduces* judgment.
2. **`foundations.md` forbids operator-detection-dependence** — enforcement requiring the
   operator to detect/inspect is malformed; AI-discipline or a fresh-context checker must
   carry it. So "operator second-judges" — the thing that made the experiment reliable — is
   **not available** as the kernel mechanism.

The naive port ("add a judgment pass, operator backstops it") is malformed at the kernel level.

## Promising integration sketch (NOT a locked design)
Core anneal already solved *operator-resolvable judgment without depending on the operator*:
**`[CONDITIONAL] → [AUTO-ACCEPTED]`** + **fresh-context isolation**.
- Run the intent-falsification in a **fresh context** (like verify-isolation already does) —
  this removes the "defend-my-design" bias from the kernel mechanism. At the kernel level this
  is **REQUIRED, not overkill** (dev-process used the operator as the bias-backstop; the kernel
  can't, so fresh-context separation must carry it).
- Split its findings: **mechanically-confirmable** ("this discharge line is an AI-written
  string" — verifiable by reading the hook) → a hard finding → loopback (same as today);
  **pure-judgment** ("this doesn't serve the intent") → recorded `[CONDITIONAL]`, surfaced
  `[AUTO-ACCEPTED]` for *optional* override — the kernel-native way to hold an irreducible
  judgment without detection-dependence.

## Open design questions (for the decide-ahead)
- Who dispositions the findings without being the actor (fresh-context first-judge)?
- How does the judgment verdict avoid **both** self-certification **and**
  operator-detection-dependence?
- **Iterate, don't single-pass** — round 2 found what round 1 missed; the leg must
  loopback-until-a-pass-is-clean (bounded by diminishing returns), not fire once.
- **Criteria-independence** — elicit success criteria from the *problem* before reading the
  design, so the attack isn't anchored to the design's self-justification (the SGV lever).

**Recursive dogfooding (operator-directed 2026-06-04):** the integration run itself applies
**ad-hoc intent-falsification to its own design** — the check must prove its value on the work
that adopts it. Catching flaws there is continued n-evidence; failing to survive its own
integration is a deep signal. (Ad-hoc is correct: the kernel mechanism need not be finished to
use the check — exactly how the foundation-invariants run used it.)

## Relates to
- `intent-falsification-soundness-sweep.md` — the **retrospective** sibling (audit shipped
  enforcement for the blind spot this check exposes); this item is the **prospective** wiring.
- `foundation-self-certification-machinery` / the `foundation-invariants-register` run — origin
  (B1/B2/F15 = the demonstration; tracker in `.anneal-dev/runs/`).
- `verify-techniques-research.md` (criteria-first / SGV / the vote-count deflation),
  `verify-vs-original-requirements.md` (sibling verify-discipline, already shipped).
- `anneal-reliability-measurement.md` — only relevant if multi-vote is ever revisited (the
  reframe makes that unlikely); the single intent-falsification's n=1 is "pursue," not "gate."
- `anneal-dev-model-tier-policy` — **conflict to resolve if model-diversity-for-verify is pursued
  here.** anneal-dev's blanket top-tier pin runs verify on the **same tier as the actor**, foreclosing
  the cross-tier model-diversity lever (verify-techniques' "model diversity > vote count"). Pursuing
  model-diversity for anneal-dev's verify collides with the model-tier floor — the conflict must be
  resolved (e.g. diversity *within* the top tier, or an explicit floor carve-out for verify), not
  assumed away.
