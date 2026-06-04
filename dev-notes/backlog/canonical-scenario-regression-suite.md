# Canonical-scenario regression suite — "executable verification" for the method itself

**Status:** OPEN — filed 2026-06-04 from the `foundation-invariants-register` run (candidate
(2) of the foundation-self-certification machinery, split out per the locked decision D5).
The stronger complement to the foundation-invariants register; heavier, gated. Pursue via
its own decide-ahead + run.

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
- `anneal-empirical-validation-experiment.md` — the cousin (the falsifiable A/B); decide
  shared scaffolding vs distinct at design.
- `multivoter-verify-no-predicate-claims.md` — the judgment-class verify sibling (intent
  falsification); the scenario suite is the outcome-regression sibling. Both are
  "verify the method itself" candidates.
- Origin: `foundation-self-certification-machinery` (archived) / the
  `foundation-invariants-register` run (D5).
