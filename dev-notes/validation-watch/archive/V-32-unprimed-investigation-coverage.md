# V-32 — Unprimed investigation: breadth ↔ omission-coverage trade-off

**watch-kind:** quality-watch (breadth ↔ omission-coverage trade-off).

**Origin:** `investigation-pass-lens-priming` shipped 2026-06-15 (`7880be6`, run
`convergence-machinery-batch`) — removed the lens-set priming of the investigation pass (keep the
discovery leg pure) + re-anchored the standardized inspection pass's lens-application to the **edit-set**
(attention-independent). Ship-and-observe, NOT a controlled test (per the project's
revealed-preference-over-toy-tests finding, `anneal-empirical-validation-experiment`).

**Claim under watch:** unprimed investigation **holds-or-improves** omission-class coverage while
**raising** novel-finding breadth. The removed priming bought "early catch" of lens-concerns *during*
investigation; the design's bet is that the edit-set-driven standardized inspection pass guarantees lens
coverage regardless (the 8 lens Scopes are edit-set-defined), so de-priming loses only early-catch, not coverage.

**Catcher (observation, not a test):**
- **Daily-use signal** — does investigation run broader; do omission-class escapes drop.
- **`framework-gap-receipt` (Q1)** — passively detects whether omission/breadth-class misses *cluster*
  after the change. The receipt is this change's automatic watcher.

**Closing rule:**
- **Re-add (refute):** omission-class escapes *rise* traceable to de-priming → re-add priming (or a lighter form).
- **Close (confirm):** breadth improves / coverage holds across several runs → close confirmed.

**Filed:** 2026-06-15 (owed-at-ship, per the shipped item's "Owed post-ship watch"; the V-entry the
de-priming ship owed but the run omitted — caught in the 2026-06-15 grounding/hygiene pass).
