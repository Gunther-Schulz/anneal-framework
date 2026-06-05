# Retrofit the active validation-watch entries to the new lifecycle (watch-kind + catcher)

**Status:** CLOSED 2026-06-05 (session 8 quick-win — done as a single sweep). All active entries retrofitted
with the watch-kind + catcher/opportunity-test field (modeled on the V-13 exemplar). Classification was
fanned out to 3 subagents (read+classify each batch against the README lifecycle + the current spec), then
reconciled and applied. **Outcome:**
- **25 entries gained a `**Kind:**` line** (V-13 already had one): **19 correctness-watch** (fix is a
  catcher) + **7 quality-watch** (fix is a form-change). V-21 noted as a borderline fit (a cadence
  *calibration* — neither a pure catcher nor an output-form change; quality-watch is the better of the two).
- **Staleness review (the companion pass) surfaced + ACTED ON** (operator: "prefer cleaning rigor over
  cautious keeping"):
  - **V-24 / V-28 / V-29 → flipped WATCHING → FIX-SHIPPED** — their cited fixes had shipped but the Status
    line was stale (V-24 commit `e2c0776`, also backfilled in the Decision line; V-28 `1d93e58`; V-29
    `35cc329`).
  - **V-26 → ARCHIVED, correct-by-construction** — the coupling-shape/predicate enums are deliberately
    closed (`modules.md` §3.4 / `glossary.md`), so a "missing 4th shape" is a future framework-amendment
    trigger, not an in-spec failure → not a watch entry.
  - **V-15 → ARCHIVED, overtaken-by-construction** — its measured noise (out-of-scope + re-attest lens-lines)
    is structurally eliminated by `modules.md` §3.2; the small residual (trivially-clean touched-scope lines)
    is re-fileable via the README archive-check.
- Active set after the sweep: **26 entries** (all carry a Kind line); archive now holds V-5, V-15, V-26.

Was: follow-on from the `validation-watch-lifecycle-fix` run (shipped 2026-06-04, release `78be6e8`/`0aa04e3`).

## The work
For each active `dev-notes/validation-watch/V-N-*.md` entry (the ~4 FIX-SHIPPED + ~22 WATCHING; V-13 was
already done in the fix run):
- mark its **watch kind** (`Kind: correctness-watch` / `Kind: quality-watch`);
- name its **catcher** (correctness — the check/lens/phase that catches its failure) or **opportunity-test**
  (quality — what a run looks like where the old form would have produced the bad artifact);
- where an entry is found **correct-by-construction** (the failure can't be expressed under the current
  spec), it's not a watch at all → archive or drop with a note.

## Why lazy, not now
The rule binds new entries + the post-run-review Q7 walk from now on. Existing entries only NEED the
retrofit when they're next walked (a post-run-review touches them) — so retrofit **opportunistically**
(when an entry is exercised) or in a **single sweep** if/when the active set wants tidying. No urgency:
an un-retrofitted entry still has its Status + Production-signal; it just lacks the new kind/catcher fields.

## Pairs with
- `validation-watch-entry-archival` (shipped — the folder) + the lifecycle-fix run (shipped — the rule).
  This is the data-migration tail of those two.
- The **staleness review** idea (read the WATCHING entries against the current spec — are they still live?)
  noted during the 2026-06-04 FIX-SHIPPED sweep — a natural companion pass; do them together.
