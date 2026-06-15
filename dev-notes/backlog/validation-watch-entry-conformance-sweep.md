# Validation-watch register — full per-entry conformance sweep

**Status:** [READY] — follow-on filed 2026-06-06 by the `v-entry-is-post-ship-only` run (its D6 / F7;
the run's spot-audit found the entries conformant but the FULL per-entry sweep is separable). Not
urgent. Touches `dev-notes/validation-watch/` entries only (no spec/kernel) → a mechanical audit,
not an anneal-dev kernel cycle (anneal-dev only if a finding implies a lifecycle-spec change).

## The task
The `v-entry-is-post-ship-only` run re-anchored the WATCHING state to "an already-shipped decision"
and added the post-ship/backlog exclusion, on a **spot-audit** (≈8 of 28 entries sampled across
cycles 4/6/8 — all conformant). This item is the **full per-entry pass** over all active entries
(`dev-notes/validation-watch/V-*.md`), confirming each is correctly classified under the clarified
lifecycle. Three checks per entry:

1. **Post-ship conformance.** Does the entry watch an **already-shipped** decision/choice/rule/fix
   — not park a not-yet-implemented consideration? (The latter → relocate to `dev-notes/backlog/`.)
   The spot-audit found none parking; confirm across all.
2. **Closing-rule vs transitions-table reconcile (folds F9).** The README transitions table models
   `WATCHING → FIX-SHIPPED → RESOLVED/INVALIDATED`, but some entries (e.g. V-30 class-recurrence,
   V-31 rule-residual) describe closing **WATCHING → RESOLVED/INVALIDATED directly**. Reconcile each
   entry's stated closing rule against the table; flag table-coverage gaps (does the lifecycle need
   a sanctioned WATCHING→RESOLVED path for choice/residual watches that never ship a remedial fix?).
   A confirmed gap → its own lifecycle-spec finding (would then be an anneal-dev cycle on
   `validation-watch/README.md`).
3. **Accepted-residual vs not-yet-built discriminator (folds F13).** V-16/V-17 (and V-25) fit the
   register via "accepted residual" (a shipped decision to accept a known limitation) — the
   *thinnest-fitting* shape. Apply the discriminator (`development-process.md` practice 8: genuine
   uncertainty about a shipped decision = watch; a classifiable not-yet-built fix = elsewhere) per
   entry; confirm each accepted-residual entry is genuinely a shipped-decision watch, not a parked gap.

## Relates to
- `v-entry-is-post-ship-only` (the run that filed this; archives when that run ships) — this is its
  bounded follow-on (D5/D6).
- `dev-notes/validation-watch/README.md` — the clarified lifecycle this sweep audits against; a
  check-2 finding could reopen it (lifecycle-coverage).
- `convergence-surfaced-finding-action-brake` — the run that spawned this also surfaced that brake
  finding; unrelated content, shared origin run.
- Origin: `v-entry-is-post-ship-only` run, cycles 1–9 (spot-audit) + F9/F13 (2026-06-06).
