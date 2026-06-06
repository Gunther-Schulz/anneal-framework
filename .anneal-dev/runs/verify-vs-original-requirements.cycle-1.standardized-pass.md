# Cycle 1 — standardized inspection pass

Cycle 1 committed no rule-text (design decisions are [VERIFIED] scope / [OUTLINED] direction); lenses
keyed to *added/amended rule-text* are therefore out of scope this cycle, cited below. The change
amends an existing rule (verify §4.3), so Missed-dependents is in-scope now.

- **Missed-dependents** — IN SCOPE (D2 amends the verify rule). Dependent set enumerated: `core.md`
  §4.3 + `anneal-dev`/`clippy`/`daneel` `phases/verify.md` (Planned-vs-actual) + `glossary.md:138` /
  `modules.md:282` + clippy/daneel `post-run-review.md` — basis: F3 corpus-wide searches (`grep -rn
  'locked design'`, `grep -rniE 'design-completeness|Planned vs actual'`). No dependent class
  unsearched (cross-ref, paraphrase-restatement, rendered clause all covered by the two token
  searches). Clean for cycle 1; re-runs as D2's amendment basis when D2 concretizes.
- **Fragmentation** — cited-clean: no existing requirements-coverage principle to duplicate — basis:
  F2 search (`grep -rni 'requirement' spec/ …` empty of any requirements-check sense).
- **Bloat** — out of scope this cycle: no rule-text added/amended yet (D2 [OUTLINED]). Re-fires when D2 commits prose (cycle 2).
- **Leakage** — out of scope this cycle: no edit to a domain-general file yet. Cycle-2 concern: "what counts as a requirement" must be the instance slot, not a code-domain concretion in core (D2's practice-9(f) delegation).
- **Unenforced-rule** — IN SCOPE-pending: D2's check MUST be evidence-bearing (verify produces a coverage finding from a tracked requirements artifact) — flagged as a cycle-2 design obligation, not yet concrete.
- **Undefined-shorthand** — IN SCOPE-pending: D2 introduces "requirements artifact" / "requirements-coverage" — needs a `glossary.md` entry (practice 10) when the term locks (cycle 2).
- **Lossy-render / Over-claimed-verification** — out of scope this cycle: no render committed; no verification claim recorded beyond the search-grounded scope (D1).
