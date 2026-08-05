# A re-render's change-set must be enumerated by source-delta diff, not an eyeball audit

**Status:** [READY] — anneal-dev (instance) method finding, surfaced 2026-06-03 during the
`anneal-dev-rerender` run (cycles 2 + 4 falsifications). An instance-mechanics sharpening,
NOT a kernel gap (the kernel's basis rule + convergence falsification already cover it).

## What happened
The re-render run's investigation pass (a dispatched "audit") declared the change-set
"light-touch — 5 citation re-points + 3 breadcrumb strips, no clause rewrites." It reached
that by **eyeballing the renders against the current spec**. Two independent convergence
falsifications then each found a real §4-content divergence it missed (the §5.3 [READY]
collapse; the two-vs-three-passes reconciliation) — both from one commit (`bf32f9c`, the §4
re-derivation the render predates). The audit's completeness *conclusion* was unreliable.

## Diagnosis (practice 1 — which level)
- **NOT anneal (kernel).** The basis rule already requires a completeness claim to carry a
  search-established basis, and "secondary sources aren't basis" (a sub-agent's cited facts
  are basis; its interpretation/conclusion is not). The convergence falsification is the
  structural backstop — it fired and caught the fault (twice). The kernel held. (A "re-render
  method" rule in `core.md` would over-prescribe the deliberately-ad-hoc investigation and
  Leak a rendering-domain concern into the harness-general kernel.)
- **Primary fault: adherence** (the orchestrator recorded the audit's completeness conclusion
  as a [VERIFIED] finding without the search-established basis the rule demands). A failure
  indicator recovered by the designed backstop — not a missing rule.
- **The worthwhile fix is anneal-dev (instance):** make the basis rule CONCRETE for re-renders.

## The sharpening (anneal-dev)
> A re-render's change-set is a **completeness claim**. Its basis is the **source-delta diff**
> — the spec commits the render predates, each change checked for render reflection — OR a
> **re-render-from-source** (regenerate the affected sections from the current spec and diff).
> Never an eyeball "looks faithful" audit.

anneal-dev ALREADY has the right primitive: the **`render-and-open-diff` extension re-renders
from the verified spec and diffs**. The audit's whole mistake was doing a manual divergence-hunt
*instead of* using that source-grounded approach. The fix points re-render investigations at the
primitive that already exists (and may extend it to cover a deliberate re-render task, not only
the post-spec-edit auto-fire).

## Where it lands
Likely `anneal-dev/spec` (a re-render binding/guidance) + possibly `phases/investigate-design`
guidance for the re-render task shape. Its own small anneal-dev run.

## Relates to
- `instance-reinstantiation.md` — governs ALL the re-renders; this is the METHOD they should use.
- `anneal-dev-extension-render-gate.md` — the `render-and-open-diff` extension (the right primitive).
- run tracker `.anneal-dev/runs/anneal-dev-rerender.md` (F7, cycles 2+4) — the surfacing.
- Sibling of `anneal-dev-impl-checkpoint-vs-discharge-hook.md` — both anneal-dev instance-mechanics
  findings the dogfooding surfaced (the kernel held in both).
