# purpose-mechanism-clause — cycle 1 standardized pass

In-scope lenses (cycle touched: an additive orientation clause to `spec/core.md` Purpose — a
domain-general file — committing design decision D1, which will render). One line per in-scope lens.

- **Bloat** — clean (conditioned). D1's added prose is Purpose-altitude *orientation*, parallel to
  the existing non-rule lines ("Human inspectability is a constraint"; "operate within the three
  contracts"); each sentence carries one of D1's four claims (stance / rationale / §3.1-pointer /
  operator-exception), bounded to ≈3-4 sentences. Basis: D1 (b)/(c). Residual guard → impl must not
  balloon into §3.1's weak/strong/gradient mechanics (re-checked at the impl write-time self-check).
- **Fragmentation** — clean. The mechanism is canonically stated in §3.1 (F2); D1 (b) requires the
  clause **cite** §3.1, not restate it → one canonical statement + a pointer, not a second copy that
  can drift. Basis: F2 + D1 (b).
- **Leakage** — clean. The clause's terms (AI, rule, operator, evidence-bearing artifact) are
  framework-general; no language/tool/path/problem-domain concretion in a domain-general file. Basis:
  D1 (b) (enumerated terms).
- **Missed-dependents** — clean (enumerated + handled). D1 amends Purpose; dependents = renders
  (`anneal-dev/.../foundations.md`, `README.md`, clippy/daneel) + cross-refs (`spec/README.md:107,
  148,152`; `instantiation-guide.md:77` "the two **values**"). None breaks: the clause is the *means*,
  not a third goal. Render-debt queued to all instances (D2). Basis: F3 + D2. Query:
  `grep -rln "Grounded claims"` + the cross-ref grep.
- **Unenforced-rule** — clean / N/A. D1 introduces NO new enforceable rule — it is orientation
  pointing to §3.1, where the enforcement already lives; nothing for the lens to force. Basis: D1 (c)
  ("no new enforceable rule introduced") + F2.
- **Undefined-shorthand** — clean. "structural, not willed" is a coined contrast defined inline by
  its rationale clause (rigor that does not depend on the AI *choosing* it). Defined-at-point-of-use,
  not floating. Basis: D1 (b).
- **Lossy-render** — clean (design-time). D1 commits no softening of a source "must" — it is
  additive orientation, not a render/paraphrase of an existing enforced clause. The render itself is
  checked at the batch render-fidelity (D2, deferred). Basis: D1 (b).
- **Over-claimed-verification** — clean. Cycle-1 "verified" claims (F1–F5) cite located reads + one
  observable fact, and the scope completeness claim (F3) cites the re-runnable grep query, not a
  recalled count. Basis: F1–F5 bases.

**Result: no load-bearing finding.** All in-scope lenses clean (Bloat/Fragmentation/Lossy carry a
named impl-time residual guard, not an open finding).
