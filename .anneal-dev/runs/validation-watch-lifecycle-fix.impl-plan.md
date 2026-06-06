# Impl plan — validation-watch-lifecycle-fix

Units from the locked design (D1–D8). **One container** (anneal-framework). Two units, **sequential**
(U2's Q7 "defer to the README" depends on U1's README carrying the canonical lifecycle).

- **U1 — README lifecycle + V-13** (dev-notes; NOT rule-corpus → no skill-craft gate, still dispatched).
  `dev-notes/validation-watch/README.md`: rewrite the **Entry lifecycle** + **Vocabulary** to carry —
  D2 the opportunity-exercised closing rule (opportunity must arise + handled; pure non-occurrence never
  closes; two evidence shapes caught/produced-clean), D5 the split (correctness-watch / quality-watch),
  D4 name-your-catcher / opportunity-test + correct-by-construction-is-not-a-watch, D8 the archive-check
  (scan archive before a new entry; match-or-adjacent → reopen INVALIDATED; the regression-net framing),
  D3 keep n=1 (now justified by D2). New Vocabulary terms: correctness-watch, quality-watch, catcher
  (**disambiguated** from post-run-review's generic "primary catcher" per the D5 sub-annotation),
  opportunity-test. Then `dev-notes/validation-watch/V-13-minimal-verbatim-scope.md`: add a
  `Kind: quality-watch` marker + reconcile disjunct-a to produced-clean-under-opportunity (D6). **First.**
- **U2 — post-run-review.md Q7** (rule-corpus → **skill-craft gate**). After U1. `post-run-review.md:173-191`
  Q7 FIX-SHIPPED walk → restate per D2 (caught / produced-clean / not-exercised / evaded, per kind) AND
  **defer to the README** lifecycle rather than re-stating the closing rule (D7, closes the F2 fragmentation);
  the new-entry/outcomes-land path notes the archive-check (D8). Scope: `post-run-review.md` only.

**Disjointness:** none — sequential, single container, U2 depends on U1.

**Method-kernel note:** U2 touches `post-run-review.md` (rule-corpus per the commit-msg hook + anneal-dev's
own process machinery) → verify adds the kernel-independent review (skill-craft form + operator soundness).
U2 invokes skill-craft before its edit.

**Spec-only:** the clippy/daneel instance post-run-review Q7 render DEFERS to the batch re-render
(`instance-reinstantiation` Render-debt queue).
