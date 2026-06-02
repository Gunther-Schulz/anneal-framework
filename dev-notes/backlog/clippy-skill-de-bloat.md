# clippy: de-bloat SKILL.md (+ candidate 2nd anneal-dev dogfood)

**Status:** OPEN — not pressing (clippy idle). Named in the
[[framework-dev-as-anneal]] locked decision as a known corpus mess ("the bloated
`SKILL.md`") and a step-5 dogfood candidate; filed as its own item rather than left
as a loose mention (no-defer discipline, 2026-06-02).

## The mess
clippy `plugin/skills/clippy/SKILL.md` is ~372 lines / ~2400 words — over
skill-craft's 1500–2000-word ideal (under the 5000 max). Same density shape flagged
on anneal-dev's `SKILL.md` (step-5 finding N1): orchestrator detail + dispatch
mechanics that partly restate the phase files. Candidate consolidation: compress the
dispatch-mechanics overlap, keep the closed-artifact form (load-bearing at routine
use). Confirm the actual over-budget extent at investigation — don't assume.

## Two ways to do it
- **As a 2nd anneal-dev dogfood** — drive the de-bloat through anneal-dev. More
  self-hosting validation, and a *larger* change than `daneel-cycle-b-sync`, so a
  better V-27 datapoint (the n=1 seed was too small to stress the ceremony-cost
  ceiling). **Caveat:** re-activates clippy → un-parks [[clippy-render-resync]] (the
  batched vocab render-debt); bundle them.
- **As a plain clippy render cycle** — if anneal-dev dogfooding isn't the goal.

Either way: instance render work (fix lands in clippy's `SKILL.md`), separate-context
skill-quality + render-fidelity review, release.

Relates to [[framework-dev-as-anneal]] (named there; 2nd-dogfood candidate),
[[clippy-render-resync]] (bundles if clippy re-activates).
