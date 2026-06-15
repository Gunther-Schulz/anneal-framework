# Cross-instance precedent discipline — no forcing-function to check sibling instances for prior art

**Status:** [DESIGN] (candidate — evaluate whether it earns a lens vs. "investigate harder").
Surfaced as a meta-observation during the `anneal-dev-model-tier-policy` run (2026-06-04,
session 7).

## The observation

When a run adds an **instance-level mechanism**, a sibling instance may have already
established the pattern — and that precedent is often load-bearing. In the model-tier run, the
**clippy** precedent (clippy already ships an instance-level dispatch-model config,
`clippy.config/models`, with "zero framework presence") was **load-bearing** for two decisions:
D2 (dispatch-model is instance-level, no framework touch) and D5 (bootstrap a 4th
operator-editable placeholder). Yet it was found only when the **convergence cycle's
new-surface requirement** forced continued searching (cycle 2) — **not** in the cycle-1
investigation. Nothing in anneal-dev's standardized lens set prompts *"has a sibling instance
already solved this?"*: `Fragmentation` fires only *within* one corpus, and sibling instances
are separate repos.

For a framework with 5+ instances sharing one method (clippy / daneel / campaign-craft /
bauleitplan / anneal-dev), cross-instance prior art is a recurring, easy-to-miss blind spot.
The convergence cycle caught it (working as designed) — but a cycle earlier, and more reliably,
if a discipline made it systematic.

## The candidate fix (to evaluate — practice 8 before shipping)

A standardized anneal-dev **lens** or an **investigation-pass discipline**: when a cycle adds or
changes an instance-level mechanism (a binding, a config artifact, a dispatch concretion),
search the **sibling instance specs/configs** for an existing instantiation of the same pattern;
cite it or cite its absence. Open question — does this earn a closed lens (the lens set is
closed; a new lens must be load-bearing and recurring), or is it adequately covered by
"investigate thoroughly + the convergence cycle backstop"? The n=1 here is a true-positive
(the precedent existed and mattered); watch for recurrence before committing a lens.

## Relates to
- `anneal-dev-model-tier-policy` run (the n=1; F6/F10 = the clippy precedent found late).
- `clippy-run-findings-dispatch-coupling.md` (the sibling precedent itself).
- The standardized lens set (`anneal-dev/spec/lens-set.md` — the home if it becomes a lens).
