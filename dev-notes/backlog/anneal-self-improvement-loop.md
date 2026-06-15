# anneal self-improvement loop — harness-as-oracle, tiered (unattended Tier-A + operator-gated Tier-B)

**Status:** [GATED] — exploratory, operator-raised 2026-06-06. **GATE REFRAMED (session-11): the loop is
gated on a REGRESSION NET + the tiered mechanical gate — NOT on a methodology-proof / "positive A/B
verdict."** The proof (does anneal's compounding value beat act-first?) turned out **unprovable cheaply**
(session-11 — controlled one-shot tests tie; the value is compounding + regime-dependent) AND — the key
realization — **was never operationally required**: a regression net is a *safety guardrail*, not a
proxy-to-maximize, so it doesn't carry the "validate the proxy first" burden the proof was meant to
satisfy. So the loop is **blocked on building the regression net, not on an impossible proof** (see "The
gate is the regression net" below) → **near-term-unblockable**, which is the point given the operator's
"backlog keeps growing / getting difficult." Origin: operator's "rising run-count / backlog keeps growing"
+ "could anneal auto-improve itself using the harness + auto-review + tests for known failures."

## The concept
Compose a **regression net** (objective per-known-failure oracles) + the **self-review** machinery +
**tests devised for known failures** into a loop that improves anneal **unattended** (Tier A), with the
operator gating only the irreducible-judgment changes (Tier B) — anneal drains its own backlog instead of
the operator driving every run. (No methodology-proof prerequisite — see the gate reframe below.)

## Verdict: real merit — and it's anneal's OWN architecture applied recursively
NOT a new paradigm. anneal's core move is *bind the measurable, surface the irreducible-judgment to the
operator* (the intent-falsification pass's operator-independence boundary + gated-kernel cadence).
Pointed at anneal-improving-anneal, with the **harness as the external oracle**, it yields a **tiered
loop**:

- **Tier A — unattended:** regression-guard improvement on **known failures with objective, blind
  oracles.** Real production failure (a clippy Unit-N finding) → seeded-defect test capturing it →
  anneal-dev run fixes the spec → re-run the test + the full regression net → ship if green + no
  regression. = `canonical-scenario-regression-suite` + the harness + auto-fix + auto-review-on-the-
  measurable-axis. Unattended-SAFE exactly where the oracle binds. **Drains the bulk of the rising
  run-count** (production-failure-driven items are most of it).
- **Tier B — operator-gated (IRREDUCIBLE):** soundness, intent-fidelity, novel blind-spots,
  foundation-invariant changes, cross-run drift/coherence. Stays with the operator — but **bounded**
  (invariants are a small set; novel blind-spots rare; coherence-audit periodic). Operator load drops
  from *per-run* → *set-direction + adjudicate-soundness*.

## Why it dissolves the "never finish" worry
Runs spawn runs (rising count) — but if most are Tier-A unattended, the count stops being the
operator's bottleneck. anneal becomes a **self-maintaining system in steady state, not a project with
a finish line.** Consistent with V1: the unattended loop is the **engine** driving toward the
"tolerable residual" asymptote; the operator's residual involvement is bounded, not zero. *Maintained
at tolerable residual* was always the goal, not *finished*.

## Where it breaks — design against these (the bound is anneal's operator-irreducibility)
The harness replaces operator judgment **only on the measurable axis** (the foundation; the
`purpose-mechanism-clause` mechanism clause). Three failure modes:
1. **Goodhart / proxy-drift** — loop optimizes the oracle (catch-rate) and drifts on the unmeasured
   (soundness/coherence/intent) — the proxy-vs-full-claim gap (APF discussion) weaponized by
   automation. Mitigation: Tier-B gate + the regression net guards *known-good* (not just the target)
   + periodic coherence-audit.
2. **Test-authoring circularity** — anneal writing its own tests + fixes + grading → overfit/strawman.
   Mitigation: tests from **real production failures** (external/grounded — clippy findings), NOT
   self-imagined (Gödel: can't enumerate own blind spots — `framework-blindspot` needs external
   lenses) + blind objective oracles + operator audits new *test-classes*.
3. **Self-certification recursion** — self-review is loaded-but-inert / self-correction-degrades
   (2310.01798) recursively. Escape: the **harness is the external binding check** (§3.1
   separate-checker); self-review stays a *surfacer*, never the bind.

All designable-against — but Tier B must be **mechanically enforced** (a hook halts the loop for
operator soundness when a change touches a foundation invariant or lacks an objective oracle — the
convergence-gate-as-hook pattern, `convergence-cycle-mechanical-enforcement`).

## The gate is the regression net, NOT the proof (session-11 reframe — the key unblock)
The original framing (and prereq #1) made a **positive A/B verdict the gate** — "don't automate on an
unvalidated proxy." Session-11 dissolved that on two counts:
- **The proof is unprovable cheaply** — compounding, regime-dependent value; controlled one-shot tests tie
  (`anneal-empirical-validation-experiment` Addendum 2). A proof-gate is therefore unsatisfiable → the loop
  stays blocked forever *while the backlog grows*. Unacceptable.
- **The proof was never operationally required.** The Goodhart fear ("validate the proxy first") applies to
  *optimizing* a metric. The loop does NOT optimize catch-rate — it **gates on no-regression** (a safety
  guardrail) and leaves *value/soundness judgment to the operator* (Tier B). Guardrail + operator-judgment
  is safe *without* proving the metric tracks value, because **the operator IS the value-check; the net just
  stops breakage.**

So the **real gate** = (a) a regression net of real known-failures + (b) the Tier-A/B mechanical boundary
(hook) + (c) periodic coherence-audit. **The loop is blocked on building the regression net — tractable,
and it accumulates from the real failures you already hit — not on an impossible proof.** That is the
direct answer to the backlog-growth pain: build the net → Tier-A drains the bulk unattended → operator
handles only Tier-B.

**Residual honesty:** the Goodhart risk is *reduced, not zero* (Tier-B + coherence-audit are the live
mitigations); building the net is real, incremental work; and the "Tier-A drains the bulk" split should be
checked empirically. The operator's **lived evidence that the framework compounds** (act-first < monolithic
< modern, daily use) is the standing justification that the shipped changes are worth it — the regression
net just keeps them *safe*.

## Empirical inputs (session-11 validation arc — anecdotal, n=5)
The real-codebase A/B (`anneal-empirical-validation-experiment` Addendum) produced lessons that bear
directly on this loop's design — several **confirm the failure modes above empirically**:
- **The gate has weak-positive evidence:** dose-response act-first 2.6 → vanilla 3.4 → adhoc 4.4
  bugs/run. Nudges, doesn't clear (anecdotal, single-pass — which *understates* anneal).
- **Confirms failure-mode 3 (self-certification recursion) — and sharpens prereq #2:** at n=1 the
  methodology question was *unanswerable*; a single self-run flipped the verdict **twice**. → the loop
  MUST evaluate every change it makes by **rate over multiple runs (k≥several)**, never a single
  self-judged run. A one-shot self-assessment of "did this improvement help?" will mislead the loop.
- **Confirms failure-mode 1 / anti-accretion — adds a concrete brake:** focused lenses help only on
  their *matched* bug-class (provenance lens 2/5→5/5); one candidate (completeness) added nothing; and a
  faint hint that piling on lenses can *trade off* against the broad pass (period 3/5 vanilla > 2/5
  adhoc — likely noise, possibly real "crowding"). → the loop must **prune / measure each lens's
  marginal value, not just add** (the additive-reflex anti-pattern weaponized by automation), and the
  regression net MUST include **broad / omission-class** scenarios so a lens-add that *degrades* general
  coverage is caught — not only the targeted bug.
- **Tier-A scope refinement:** improvements split into (a) *general-discipline* gains (broad,
  transferable — most of the value; the act-first→vanilla step) and (b) *matched-lens* gains
  (class-specific, only when the class is present; the vanilla→adhoc step). Bank (a) broadly; gate (b)
  on "is this class actually present, and does it regress the broad pass?"
- **Worked instance:** the arc *is* a manual Tier-A step (real clippy-domain failure → provenance bug
  class → a concrete lens identified — `provenance-at-handoff-lens`), minus the automation. Evidence the
  value-step is real, not hypothetical.

## Prerequisites (ordered — session-11 reframe: the A/B verdict is NOT one)
1. **The regression net** (`canonical-scenario-regression-suite`) — real known-failure scenarios with
   known-good outcomes; the Tier-A oracle. **The actual gate + the actual blocker** (build this and go).
2. **Objective, blind, un-gameable oracles** per scenario (the honest-hard-part — `measurement-harness-mve`
   task-pack methodology; the committed `eval/` harness is the machinery pattern).
3. **The Tier-A/B boundary as a mechanical gate** (a hook — `convergence-cycle-mechanical-enforcement`
   family); Tier B (soundness / invariants / novel blind-spots) stays with the operator.
4. **Periodic coherence-audit** — the cross-run drift guard on the unmeasured axis.
- **NOT a prerequisite (decoupled, session-11):** a "positive A/B verdict" / methodology-proof. Unprovable
  cheaply AND not operationally required (gate-not-optimize; operator is the value-check). The operator's
  lived evidence is the value-justification; the net is the safety gate. `anneal-empirical-validation-experiment`
  is now a *separate, optional* thread, not this loop's gate.

## Relates to
- `anneal-empirical-validation-experiment` / `measurement-harness-mve` — the harness (machinery pattern) +
  the now-DECOUPLED proof thread (no longer this loop's gate, session-11).
- `canonical-scenario-regression-suite` — the Tier-A regression net (this loop is what *uses* it).
- `framework-intent-vision-statement` / V1 — the loop is the engine to the tolerable-residual asymptote.
- `convergence-cycle-mechanical-enforcement` — the hook pattern that enforces the Tier-A/B boundary.
- `framework-blindspot-class-analysis` / `post-run-review-failure-class-register` — external sourcing of
  the known-failure tests (don't let anneal self-imagine its blind spots).
- `auto-battle-cadence-mode` — the cadence kin (auto-cycle affordance); this is its unattended-loop cousin.
- The operator-irreducibility foundation (`dev-notes/foundation-invariants/`) — the hard bound.
- Origin: operator, 2026-06-06.
