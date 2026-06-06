# foundation-invariants-register — impl plan

Disjointness basis (search-established, D1 edit-site enumeration): the 4 units touch
pairwise-disjoint file sets — U1 {dev-notes/foundation-invariants/*}, U2
{development-process.md, CLAUDE.md}, U3 {hooks/commit-msg}, U4 {dev-notes/backlog/*}.

- U1 [FIRST] REGISTER (D2, D6) — create dev-notes/foundation-invariants/: README.md
  (membership rule = live-invariant ∧ external-anchor; anti-false-comfort residual in
  plain words; term definitions per F4/D6) + 5 INV-<n>-<slug>.md files (basis-rule,
  complete-state, verify-isolation, loopback-not-settled, exclusion-via-named-falsifier;
  each: invariant statement + kernel-home cite + external anchor) + archive/. Establishes
  the INV-* naming U2/U3 reference.
- U2 [after U1] VERIFY-WIRING (D3) — development-process.md §2 (add the
  foundation-invariant-check leg to the kernel-independent review, focusing not
  replacing operator soundness) + step-4 discharge template (add the check line) +
  CLAUDE.md:14-21 (terse third-leg mention, keep the development-process.md pointer).
- U3 [after U2] HOOK EXTENSION (D3b, D4) — hooks/commit-msg: (a) require the
  Foundation-invariant check line when staged diff touches kernel-source (mirror
  run-gate KERNEL_PATTERNS); (b) require Invariant-change-ratified marker when staged
  diff MODIFIES/DELETES dev-notes/foundation-invariants/INV-*.md (--diff-filter=MD;
  README/archive + Additions exempt). Local-only.
- U4 [PARALLEL with U1/U2/U3] BACKLOG (D5) — fold candidate-3 (different-model checker)
  into multivoter-verify-no-predicate-claims (relate-before-add); file candidate-2
  (scenario suite) toward anneal-empirical-validation-experiment; prep parent item for
  archive. File-disjoint (dev-notes/backlog/*) → parallel-eligible.

Run-level: U1 → U2 → U3 sequential (each references the prior's established
contract); U4 parallel throughout (disjoint).
