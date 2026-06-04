# anneal-dev self-render urgency — the render-cadence "stale-while-idle" rationale fails for the self-governing instance

**Status:** RESOLVED 2026-06-04 (session 7) — archived. Surfaced during the
`anneal-dev-model-tier-policy` run; a render-cadence policy gap, not a model-tier
issue.

**Resolution — the urgency dissolves; re-grounding is the rule, freshness is
hygiene.** The load-bearing mitigation all along was that anneal-dev runs
**re-ground in the live spec** — so the stale loaded plugin was never a
correctness risk, only an *invisible debt*. The fix is therefore not a prompt
self-render carve-out (expensive per-run render) nor a staleness detector — it
is to make the re-grounding the **explicit rule**: the project `CLAUDE.md`
"Self-hosting" clause now states that in this repo the **live co-located spec is
the source of truth** and the loaded anneal-dev plugin is a **build artifact**
that may lag (live spec governs on divergence). This works *only* because the
self-render problem is unique to the self-hosting repo (a downstream anneal-dev
has only its plugin → plugin IS its truth). With re-grounding explicit, plugin
freshness drops to **hygiene** — keep the batched cadence (no prompt-per-run
render, no detector hook); the urgency is gone. A project-instruction edit, not
a kernel edit or plugin render. (`instance-reinstantiation.md` render-cadence
note updated to match.)

**Immediate instance RESOLVED 2026-06-04 (session 7):** the
`anneal-dev-reinstantiation` run re-rendered the anneal-dev plugin from the live
spec (all 5 affected files; verify PASSED, render-fidelity battery clean) and
bumped `plugin.json` 0.1.2→0.1.3 — the verified render is in the working tree.
The running cache is **not yet** updated (R4 is github-release-coupled +
operator-gated — commit → push → plugin update). So the *stale-instance* symptom
is fixed pending the operator's reinstall; the **policy carve-out below remains
the open question.** D7 of that run committed to deferring it here (classify per
practice 8 before shipping).

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
