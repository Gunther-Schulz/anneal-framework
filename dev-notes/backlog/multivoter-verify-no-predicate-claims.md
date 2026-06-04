# Intent-falsification verify for no-mechanical-predicate (judgment) claims

**Status:** OPEN — **reframed 2026-06-04** from "multi-voter adversarial quorum" to **single
criteria-first intent-falsification**, after a live n=1 demonstration in the
`foundation-invariants-register` run. The judgment-class sibling of anneal's mechanical
falsification. **PURSUE via its own decide-ahead + anneal-dev run** (method-kernel edit to
core anneal). No longer gated on multi-vote measurement — the vote-count apparatus is dropped
(below). (Filename kept for backlink stability; the item is the intent-falsification candidate.)

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
