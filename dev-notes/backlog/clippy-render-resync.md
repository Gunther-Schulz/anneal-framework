# Clippy — parked render-resync (c-safe + future T1/T2)

**Status:** **PARKED 2026-06-02** (operator: clippy not in active use; re-enter
when clippy work resumes — timing depends on other priorities). Render-debt is
tracked here so re-entry is a clean diff, not archaeology.

## Why parked (the batching decision)
With clippy idle, the drift cost of a lagging render is ~0, so the render-syncs
**batch**: finish the remaining framework-core de-pollution (T1/T2) without
interleaving clippy syncs, then do ONE clippy render pass covering everything
when clippy returns. (The a+b sync already shipped as clippy **v0.9.94** —
[[clippy-isolation-render-release]], archived — because clippy was current then;
from c-safe on, clippy went idle.)

## Render-debt owed (clippy lags the core by these cycles)
- **Cycle c-safe (§4.1.4 falsification)** — framework `5f4ed74`. Clippy's
  falsification render still carries the OLD vocab:
  - coupling shapes `target-shape`/`target-uses` → **`target-existence`/`target-dependents`**
  - predicate evidence ("result line" / glob / regex) → abstracted in core; clippy
    binds the concrete grep forms in its §3 binding (so clippy's render KEEPS the
    grep specifics, but as bindings, and adopts the abstracted framing)
  - **F3** (falsification covers [VERIFIED] only; [CONDITIONAL]/[AUTO-ACCEPTED]
    → verify) — confirm clippy's render states the handoff
  - sites (grep 2026-06-02): `plugin/skills/clippy/phases/investigate-design.md`,
    `references/tracker.md` carry the shape names; also check
    `references/lens-set.md` / `lenses.md`.
  - Behavior unchanged — vocabulary alignment, as the a+b sync was.
- **T1 / T2 tail leaks** — NOT YET DONE in the framework core
  ([[contract1-depollution-cluster]]). When they land, their clippy renders
  batch into this same pass.

## Re-entry procedure (when clippy returns to active use)
1. Diff clippy's render against the then-current framework core (c-safe + any
   T1/T2 landed) — one render-fidelity pass.
2. **Isolate the delicate falsification re-render** within the sync (the locked
   risk-isolation reason c-only was split from a+b).
3. Standard render cycle: skill-craft gate → re-render → separate-context
   render-fidelity → release (version-bump + marketplace pull + `claude plugin update`).
4. Check **daneel** too — [[daneel-cycle-b-sync]] (daneel's §5.2 already stale;
   daneel carries no falsification render, so c-safe likely adds no daneel debt —
   verify).

Relates to [[contract1-depollution-cluster]], [[clippy-isolation-render-release]]
(archived), [[daneel-cycle-b-sync]].
