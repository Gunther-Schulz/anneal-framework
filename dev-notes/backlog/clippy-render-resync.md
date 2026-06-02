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

**This batching holds only for vocab-debt.** The drift cost is ~0 *because the
de-pollution so far is vocabulary-alignment, behavior unchanged* — mechanical to
batch and re-verify in one pass. A **semantic** framework change (one that alters
instance behavior, not just naming — e.g. finalizing the framework-dev instance,
or `verified-integrity-consolidation`) is partly *validated by being rendered
into an instance*: deferring its render loses the per-change feedback loop and
turns the eventual sync into risky archaeology rather than a clean diff. So
vocab-debt batches freely into this parked pass; a **semantic** change should
pull a render-validation forward to near when it lands, not into this batch.

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
- **T1 (`file:line` → "a located read of the source") — framework DONE**
  (`f9fd5b4`). Clippy's render uses `file:line` directly — which is clippy's
  **legitimate binding** of the framework's "located read," so the c-only sync
  likely needs little/no change here; verify clippy presents `file:line` as its
  binding, not as the framework concept.
- **T2 / T3 tail leaks — framework DONE** (`c634ebf`): T2 `code`/`fixtures` →
  "the work product"; T3 `grep` → "search". Clippy binds code/grep — likely
  minimal render change (verify at the sync).
- **Coherence-audit fix — framework DONE** (`8bfa20b`): the **spawn-fallback**
  name is now unified across implement/falsification/verify (§4.2/§4.1.4/§4.3).
  Clippy's degraded-path renders should adopt the single unified name. (The §3.1
  "for code" illustration marker adds NO clippy debt — clippy IS the code instance.)
- **Contract-surface discriminator (R1) — framework DONE** (this cycle, 2026-06-02):
  the `Contract surface` definition abstracted from code-shaped "observable from
  outside" → coupling-based "what a dependent would break if it silently changed"
  (`core.md` §5.2(b) + glossary Contract surface + target-existence). Clippy
  renders §5.2 body-shape (already in the Cycle-b debt above) + uses contract-surface
  in `tracker.md`; the discriminator change folds into the same §5.2 render-sync —
  a marked `for code:` gloss is likely clippy's legitimate binding. See
  [[anneal-dev-framework-flowback]] R1.

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
