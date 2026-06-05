## V-23. Glossary partition trigger — does the ~50-entry cardinality threshold hold?

**Status: WATCHING.**

**Kind: quality-watch.** The fix is a form-change (partition into category sub-files, or intra-file category headings) with no catcher — so it closes on a *produced-clean* instance: a run where the new structure resolves a "where does X live" navigability friction the old single-file form would have hit (see README closing rule).

**Decision (`spec/glossary.md` cardinality at audit time ~22
entries; cycle D.1 audit F11 observation).** Glossary remains a
single file ~400 lines mixing vocabulary categories
(operational primitives, analytic descriptors, lifecycle-
extension semantics, watch-entry-state vocabulary). F11
observed that granularity is fine at current cardinality, but
flagged the corpus-wide observation that further growth may
require partitioning.

**Why uncertain.** ~50 entries is a heuristic threshold for
when single-file glossary stops being navigable. The actual
breakpoint depends on cardinality, conceptual diversity, and
cross-reference density — none of which are predictable
in advance. Too-early partitioning fragments a coherent
vocabulary; too-late retains a navigability problem.

**Production signal to watch.** Either of two shapes, observed
at n=1:
- **Navigability signal.** Glossary cardinality reaches ~50
  entries AND the operator/AI starts experiencing "where does
  X live" friction (multiple grep queries needed to find the
  right entry; cross-reference drift accumulates).
- **Conceptual-mix signal.** A new entry's category doesn't
  cleanly fit any of the four implicit categories (operational
  / analytic / lifecycle / watch-state) AND adding it requires
  expanding the conceptual frame mid-file.

Closing criterion (WATCHING → FIX-SHIPPED): observed n=1 of
either signal; partition into category sub-files (e.g.,
`glossary-operational.md` + `glossary-analytic.md` + ...) OR
introduce intra-file section headings by category. FIX-SHIPPED
→ RESOLVED on first subsequent run where the new structure
catches a navigability issue that would have been worse pre-
partition.

Per `development-process.md` practice 8, this V-N is
legitimate: the fix-shape (partition or section-header
structuring) is classifiable, but the trigger condition is
empirically unmeasured — cardinality threshold is genuinely
uncertain.

---

