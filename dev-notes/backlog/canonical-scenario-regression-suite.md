# Canonical-scenario regression suite — "executable verification" for the method itself

**Status:** OPEN — filed 2026-06-04 from the `foundation-invariants-register` run (candidate
(2) of the foundation-self-certification machinery, split out per the locked decision D5).
The stronger complement to the foundation-invariants register; heavier, gated. Pursue via
its own decide-ahead + run. **Promoted from tier 6 → tier 4 on 2026-06-05** (per skill-craft
v1.0.61's evaluation framing + V-30 closing rule): per-edit cadence + Tier-2-shaped
behaviour-delta signature measurement at the method level. Sibling to
`anneal-dev-evaluation-discipline` (which renders Tier 1/2 at the plugin level).

## The idea
A frozen set of corpus-evolution scenarios with **operator-ratified expected outcomes** —
"executable verification" *for the method itself*. Catches soundness flaws that violate
**no stated invariant** but DO break a known-correct outcome — which the static
foundation-invariants register (breaks-against-named-invariants only) misses.

## Why it sits atop the register, not beside it
The register checks an edit against *named invariants*; the scenario suite checks it against
*known-correct outcomes*. The suite is a real lift: authoring + operator-ratifying a frozen
scenario set. It is a **lightweight cousin of `anneal-empirical-validation-experiment`** (the
parent item's own framing) — relate the two at decide-ahead so they don't duplicate.

## Relates to
- **skill-craft v1.0.61 evaluation discipline** — this item *renders* Tier-2 (behaviour-delta
  signature, un-fakeable artifact) into the anneal method itself: the frozen scenario set
  is the with/without measurement substrate at the method level.
- **`anneal-dev-evaluation-discipline`** — sibling at the **plugin** level (renders Tier 1/2
  into anneal-dev-the-skill); this item renders Tier 2 into anneal-the-method. The two
  compose: the plugin-level eval measures whether anneal-dev fires its discipline; the
  method-level scenario suite measures whether the discipline produces correct outcomes.
- **V-30 `form-not-binding-class-recurrence`** — the scenario suite provides the empirical
  per-edit input V-30's closing rule depends on. A spec change that silently breaks a
  known-correct outcome surfaces as a regression failure → recurrence data point for V-30.
- `anneal-empirical-validation-experiment.md` (tier 6, proof thread) — the cousin (the
  one-shot falsifiable A/B); decide shared scaffolding vs distinct at design. Different
  cadence — A/B is one-shot framework-level validation; this is per-edit method-level
  regression.
- `verify-model-diversity.md` — the judgment-class verify sibling (intent falsification);
  the scenario suite is the outcome-regression sibling. Both are "verify the method itself"
  candidates.
- Origin: `foundation-self-certification-machinery` (archived) / the
  `foundation-invariants-register` run (D5).
