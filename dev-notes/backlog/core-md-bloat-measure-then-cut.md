# core.md bloat — measure-then-cut (core↔modules convergence dedup)

**Status:** OPEN (DOWNGRADED — measured 2026-06-15) — ⚠ **the 2026-06-04 premise is largely STALE.** Re-measure
(core.md now **1304ln**, §4.1.4 now `:475-702`, not the cited `:408-429`): **D-point-2 already-addressed** — the
glossary entries (Self-check/Integrity-check/Spawn-fallback/Status-tag) already **index** core bodies with `§`
pointers, not restate them (intervening work tightened them). **D-point-1 down to a minor delicate trim** — §4.1.4
↔ `modules.md §3.4` already cross-ref heavily; only §4.1.4's coverage-check (i)-(v) re-enumerates a few artifact
fields modules owns. **Per measure-then-cut / NO-blind-rewrite: minor residual or close** — do NOT run a full
gated-kernel cycle for a few-line reword (proportional-cycle-weight). — split off 2026-06-04 from
`kernel-consolidation-glossary-hygiene` (its **D-point-1**),
to keep the glossary/dev-process-home consolidation run (`kernel-consolidation-batch`) coherent. The
delicate **core/modules structural** half. Framework-spec edit → **anneal-dev + kernel-independent
verify**. Tier-2 F3 (or F-prefix consolidation), **after** `kernel-consolidation-batch`.

## Scope
From the coherence-audit (`ac39b6ab6d5d929cd`): `core.md` = 976 ln, §4 (phase specs) = ~510 ln / **52%**.
Operator's standing constraint: **measure-then-cut, NO blind rewrite** — only concrete, measured movable
points move.

**The two measured movable points (both D-points — both touch `core.md` bodies, so both land here):**
- **D-point-1:** `core.md §4.1.4` convergence mechanics (`:408-429`) **duplicate** `modules.md §3.4`
  (`:312-390`) — both carry the full line-form / predicate mechanics. Fix: `core.md` states the
  convergence *requirement* + cross-refs the mechanics to `modules.md §3.4`; modules stays the single
  mechanics home. Behavior-preserving consolidation, not a rewrite.
- **D-point-2:** glossary entries restate `core.md` bodies instead of indexing them — `glossary.md`
  Integrity-check / Spawn-fallback / Self-check (`:208-235`) ↔ `core.md §4.2.3`; glossary Status-tag
  (`:306-319`) ↔ `core.md §5.2`. Fix: those glossary entries index the `core.md` body, not restate it.
  (Same "glossary indexes, doesn't restate" principle as the sibling run's A — but these entries index
  *core* bodies, so confirming the trim needs the `core.md` reads, which pairs them with this core run.
  Re-scoped here from `kernel-consolidation-batch` 2026-06-04 so that run touches no `core.md`.)

## Why split (not done in the batch)
- It's the backlog item's own named "second tightly-coupled (core/modules consolidation)" half.
- Most delicate: core surgery + its own render implications; deserves a focused cycle, not bundled into
  the glossary-home cluster.
- Thematically core/modules-structural, not glossary/dev-process-home.

## Method
Per `anneal-dev-rerender-changeset-by-source-delta` discipline if any render reflection is needed; but the
dedup is behavior-preserving (mechanics already in modules), so likely a delta-verify. Spec-only; instance
renders (if §4.1.4 renders) defer to the batch re-render.

## Relates to
- `kernel-consolidation-glossary-hygiene` — the parent cluster (this is its D-point-1, split out).
- `kernel-consolidation-batch` run — the sibling run carrying A/B/C/D-point-2 + validation-watch folder.
- coherence-audit handoff `ac39b6ab6d5d929cd` (2026-06-04).
