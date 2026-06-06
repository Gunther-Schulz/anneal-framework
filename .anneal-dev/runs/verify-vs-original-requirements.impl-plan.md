# Impl plan — verify-vs-original-requirements

Units derived from the locked design (D1-D6; D8/D5 per operator resolution at [READY]).

**RE-SHAPED to spec-only at implement (operator-directed 2026-06-04, render-cadence policy).** This run
ships **U1 only** (the kernel spec edit). The render units **U2/U3/U4 are DEFERRED** to the batch
re-render, queued in `dev-notes/backlog/instance-reinstantiation.md` (Render-debt queue). D1's scope
(the change renders into all 3 instances) is **preserved as tracked debt** — only the render *cadence*
moves; no [VERIFIED] decision is invalidated. Verify (this run) checks U1's spec rule-text against the
locked design; render-fidelity is the batch run's concern (the framework's decoupled-render model —
`render-and-open-diff` is post-verify). The active impl plan is therefore a **one-unit plan (U1)**.

- **U1 — framework source (spec).** `core.md` §4.1 (add the requirements-record capture rule + D8
  verbatim-request capture) + §4.3 (add the design-coverage-of-requirements check) + `glossary.md`
  (D6: "requirements record" + "requirements-coverage check" entries) + any modules touch.
  **First / sole unit this run.** Sequential, in-place (single-unit Integrity-check path).
  Scope: `core.md` §4.1/§4.3, `glossary.md`. Contract: the new requirements-record artifact + the verify check.
  **✅ COMPLETED** — change-set `spec/core.md` + `spec/glossary.md` (modules.md untouched — D3 home expressed by cross-reference, not a header field); self-check 4 lenses clean; integrity check passed (change-set within scope); checkpoint ref recorded in tracker.

**— DEFERRED to the batch re-render (instance-reinstantiation Render-debt queue) —**
- **U2 — anneal-dev render** (DEFERRED). `anneal-dev/plugin/skills/anneal-dev/phases/investigate-design.md` + `phases/verify.md`.
- **U3 — clippy render** (DEFERRED). `../coding-clippy/plugin/skills/clippy/phases/investigate-design.md` + `verify.md`.
- **U4 — daneel render** (DEFERRED). `../daneel/plugin/skills/daneel/phases/investigate-design.md` + `verify.md`.

**Disjointness basis (parallel-eligibility) — corrected at implement entry (resumed session):** the
parallel-safety rests on **file-scope disjointness**, not repo-separateness. Container map (verified via
`git -C <dir> rev-parse --show-toplevel`): U2's files live in the **anneal-framework** repo
(`anneal-dev/` is a subdirectory, *not* a separate repo — the same `ls */phases` imprecision cycle-4
flagged on D1); U3 → separate `coding-clippy` repo; U4 → separate `daneel` repo. Each of the three
parallel units therefore touches a **distinct container** (U2→anneal-framework, U3→coding-clippy,
U4→daneel) with disjoint file-scopes, so concurrent in-place dispatch cannot clash. U2 shares the
anneal-framework container with U1 but runs **after** U1 (renders derive from the source) and edits
disjoint files (`anneal-dev/plugin/skills/…` vs U1's `spec/…`). U1 is sequential-first. Conclusion
(U2/U3/U4 parallel-eligible, U1 first) unchanged from the [READY] plan; only the basis is corrected.

**Method-kernel note:** U1 edits the kernel → verify adds the kernel-independent review (skill-craft
self-review + operator soundness), recorded at release-loop step 4. Each unit invokes skill-craft
before its rule-corpus edit (the pre-edit gate).
