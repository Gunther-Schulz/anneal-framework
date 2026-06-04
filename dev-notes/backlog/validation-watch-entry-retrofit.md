# Retrofit the active validation-watch entries to the new lifecycle (watch-kind + catcher)

**Status:** OPEN — follow-on from the `validation-watch-lifecycle-fix` run (shipped 2026-06-04, release
`78be6e8`/`0aa04e3`). **Low priority, lazy.** The new lifecycle (opportunity-exercised closing; the
correctness-watch/quality-watch split; name-your-catcher / opportunity-test) **applies going forward**;
the **26 active entries** still carry the old framing and have not been retrofitted.

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
