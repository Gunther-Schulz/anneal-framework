# Debt accrual: shift from trailing detection (Clippy) to leading prevention

**Status:** OPEN — operator strategic insight 2026-06-07 (beat-the-books debt investigation, after the F29 run).
Framework/-dev + clippy. The deeper frame behind several existing items — files the **root** + cross-references.

## The insight (operator)
Clippy was **unavoidable** (it caught 4 ship-blockers that would otherwise be production debugging cycles) — but it
is a **trailing detector, not a leading preventer**. The root gap is **per-unit locality**: Clippy/the framework
verifies each change correct+complete against *its own* design; nothing owns the codebase's **cumulative coherence**.
Debt accrues in the **seams between units** — every unit ships green, the whole degrades anyway. Structural, not a bug
(it's a per-change conductor by design).

**The compounding loop (the load-bearing point):** debt accrues → Clippy's per-unit convergence does *more* work
(more surfaces, more co-producers, longer convergence; the F29 run's threading fragmentation directly inflated its
convergence + caused F29) → runs get more expensive as the app grows. **So prevention isn't hygiene — it directly
bounds Clippy's future cost.** (Compounds with `proportional-cycle-weight` / the ~68k-for-one-lens cost datapoint.)

## Three specific holes
1. **No subtraction-forcing-function.** The basis rule forces the **add** side of a replacement (enumerate
   references/dependents of what you change) but NOT the **subtract** side when a successor is staged across units:
   a unit can ship a new engine/field/mechanism with no obligation to retire the predecessor or register the orphan
   with a cutover trigger → ghost fields, legacy remnants. *(This is the canonical referent of
   `deferred-removal-cross-run-obligation-ledger`.)*
2. **Residuals die in the gitignored per-run tracker.** `[VERIFIED — surfaced]`/`[VERIFIED — deferred]` residuals
   live in `.clippy/runs/<run>.md` (gitignored, never read by the next unit) → debt invisible across runs,
   re-discovered ad hoc. No persistent, burn-down-able register feeds sequencing.
3. **No mechanism-proliferation check at design time.** Target-locality fires on "new *file*", not "new *way of
   doing X*" — adding the 2nd/3rd threading store never tripped a "you're duplicating an existing mechanism" wire.

## The fixes (so it doesn't just re-accrue)
- **A checked-in debt register** (e.g. `docs/DEBT.md`): the instance reads it at investigation (a unit knows the debt
  in its neighborhood) + writes deferred/surfaced residuals to it at run-end. Cumulative-visible, burn-down-able.
  (Fixes hole 2; the persistent half of `deferred-removal-cross-run-obligation-ledger`.)
- **A supersession obligation at [READY]:** introduce a successor → retire the predecessor in-unit OR register a debt
  entry with an explicit cutover trigger; can't reach [READY] with an un-dispositioned supersession. The
  **subtraction-side mirror** of the existing add-side completeness rule (§3.2.2). (Fixes hole 1.)
- **A mechanism-proliferation lens** (generalize Target-locality from new-file to new-way-of-doing-X). (Fixes hole 3;
  a clippy lens, relate to `bidirectional-lens-coverage-tenet` — both generalize an existing lens.)

## Honest caveat (operator) — not all of this is Clippy's job
Cross-corpus **coherence** is a genuinely different mode from per-change verification, and this project already has the
right tools — **`coherence-audit`** + **`architecture-audit`** — they're just **not run on a cadence**. The cheapest
durable move is **process**: run a coherence/architecture audit at each roadmap "Next up" rollover (or every N units).
Clippy's three fixes keep awareness cheap; the periodic audit is the actual cross-corpus sweep.

## Home split (decide in the cycle)
- **Framework/-dev:** the subtraction-forcing-function / supersession-obligation-at-[READY] (basis-rule §3.2.2
  add-vs-subtract asymmetry) + the cross-run residual-visibility (debt register vs gitignored tracker) → anneal-dev
  kernel + each instance's persistence binding.
- **Clippy instance:** the mechanism-proliferation lens.
- **Process:** the coherence/architecture-audit cadence (a dev-process discipline, not a spec mechanism).
Apply additive-reflex per facet (is each a new mechanism, or the existing completeness/true-unit discipline applied to
*subtraction* / *cross-run* / *mechanism-identity*?).

## Relates to
- `deferred-removal-cross-run-obligation-ledger` (holes 1+2 — the canonical removal/ledger item; this is its strategic frame)
- `bidirectional-lens-coverage-tenet` + Target-locality (hole 3 — lens generalization)
- `proportional-cycle-weight` (the compounding-cost loop — prevention bounds Clippy's per-run cost)
- `coherence-audit` / `architecture-audit` (the cross-corpus cadence) · `surface-non-task-observations` (residual-surfacing)
- Origin: operator strategic step-back, beat-the-books debt investigation, 2026-06-07.
