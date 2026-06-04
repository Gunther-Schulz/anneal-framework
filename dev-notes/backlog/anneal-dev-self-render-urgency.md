# anneal-dev self-render urgency — the render-cadence "stale-while-idle" rationale fails for the self-governing instance

**Status:** OPEN — surfaced as a meta-observation during the
`anneal-dev-model-tier-policy` run (2026-06-04, session 7). A render-cadence
policy gap, not a model-tier issue.

## The observation

The render-cadence policy (`instance-reinstantiation.md`) defers plugin renders
spec-only, justified by *"instances stay transiently stale — low-urgency per the
parked-while-idle convention (drift ~0 while an instance is unused)."* That
rationale is **structurally false for anneal-dev itself**: anneal-dev is *never*
idle — it is the single channel for all corpus-evolution. Every method-kernel edit
to anneal-dev's own spec (`anneal-dev/spec/*`, and the framework `spec/*` it renders
from) leaves the **running** anneal-dev plugin behind its own latest method until a
re-render + reinstall.

**Demonstrated live this run:** the convergence cycle relied on the
**intent-falsification pass** (session-6 spec) — which the *active* (cached 0.1.2)
plugin does **not** carry (its renders were deferred). The run only ran it because
the working context grounded in the live spec, not the stale loaded skill. F9 of
that run captured the per-rule symptom; this item is the generalized policy gap.

## The candidate fix (to evaluate)

A method-kernel edit whose render target is **anneal-dev's own plugin** should
re-render + reinstall anneal-dev **promptly** (its own render-tail), NOT batch it
into `instance-reinstantiation` with the idle instances — because the next
corpus-evolution run is conducted *by* anneal-dev, on whatever method the running
plugin carries. Other instances (clippy/daneel/…) keep the batched cadence (they
*are* idle between uses); anneal-dev is the exception because it is self-governing.

Shape to settle: is this a carve-out in the render-cadence policy ("self-render =
prompt; other-instance render = batched"), and does it warrant a forcing function
(e.g. a post-method-kernel-edit reminder/gate that anneal-dev's own plugin is now
stale)? Classify per practice 8 before shipping.

## Relates to
- `instance-reinstantiation.md` (the render-cadence policy this revises).
- `anneal-dev-model-tier-policy` run F9 (the per-rule symptom; archived run tracker).
- The activation step that resolves the immediate instance (re-render + reinstall,
  session 7).
