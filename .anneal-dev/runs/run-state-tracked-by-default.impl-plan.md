# Impl plan — run-state-tracked-by-default (at [READY], 2026-06-06)

5 units, scope-disjoint (distinct files) → parallel-eligible (disjointness basis: distinct
file paths). Implemented in the **working context** (self-hosting + small kernel-doc edits;
and a bootstrapping note — D7 isn't live yet, so the formal dispatched-subagent in-place
integrity check would itself trip on the now-tracked tracker; in-context implementation
sidesteps it, the same `self-hosting-inplace-integrity-clean-precondition` friction). All edits
keep §5 + core.md §4.2 **domain-general** (F-leakage: the `allow-adhoc-kernel-edit` concretion
lives only in the anneal-dev binding).

- **U1 — `instantiation-guide.md` §5** (D1 + D2): rule 1 (`:364`), rule 3 (`:373`), Project-init
  (`:386-387`) → run-state TRACKED, only transient local override-flags gitignored; rewrite rule-1
  `:359-367` (the "runtime-state paths are gitignored / `git check-ignore`" marker sentence + the
  blur-contract rationale) so the observable marker is namespace/path (both tracked) + the
  don't-hand-edit convention; rule-3 "visible-vs-hidden maps to commit-vs-gitignore" →
  "operator-editable-vs-instance-written." **Domain-general** ("transient local override-flags").
- **U2 — `anneal-dev/spec/persistence.md`** (D1): Filesystem layout (`:102-105`) → run-state TRACKED
  (the accumulated history), not gitignored; only override-flags gitignored.
- **U3 — `anneal-dev/spec/bindings.md`** (D1 + D4): First-run bootstrap (`:295-296`) adds only the
  `allow-adhoc-kernel-edit` override-flag to `.gitignore` (run-state tracked); Operator-editable
  (`:282`) reword; Provisioning/Integration (`:187-199`) → work-product-vs-bookkeeping boundary,
  exclude run-state from integration (the separate-copy parallel to U4's in-place exclusion).
- **U4 — `spec/core.md` §4.2** (D7): in-place integrity (`:763-772`) — clean-before-dispatch +
  "no other modification" exclude **the run-state directory** (abstract, not `.anneal-dev/`); restore
  PRESERVES it. The work-product-vs-bookkeeping boundary, stated once canonically here.
- **U5 — `dev-notes/backlog/instance-reinstantiation`** (D5): file a render-debt row — the rendered
  anneal-dev plugin (SKILL.md:315 First-run bootstrap + foundations.md:469 + persistence + implement)
  re-renders the changed policy. Spec-only this run.

Post-impl: D1's `expected-match` flip — after U1-U3, `rg "runtime-state paths are gitignored|adds .anneal-dev/ to.*gitignore"` on the spec should be empty (the policy flipped). Verify (isolated): skill-craft form + cross-doc coherence (the policy consistent across §5 ↔ persistence ↔ bindings ↔ core §4.2; the work-product-vs-bookkeeping boundary stated symmetrically in-place + separate-copy) + the kernel-edit operator-soundness leg (already the [READY] gate).
