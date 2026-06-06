# Standardized-pass — cycle 1

Lenses in scope this cycle: the cycle produced findings F1–F6 (observations of
existing §4 structure) + scope decision D1 ([VERIFIED]) + re-derivation decisions
D2–D6 ([OUTLINED] — committed directions; no rule-text added yet, realization
output deferred to impl per `tracker.md` brevity discipline).

- **Missed-dependents** — CLEAN. D2–D6 change/amend existing §4 rules → in scope. The dependent set is enumerated in D1, search-established: `grep -rnE '§4\.2([^.0-9]|$)' …` → 20 bare-§4.2 spec sites + render-side (anneal-dev 2 / clippy 1 / bauleitplan 1); `§5.3` → 6; `§4.1.4` → 20 (anchor unchanged by S2). Basis: D1.
- **Over-claimed-verification** — CLEAN. D1's scope is a completeness claim → in scope. Its basis is the re-runnable queries re-run THIS cycle (actual output), not the Explore subagent's summarized counts ("113+ files", "38+ files") — those were rejected per `core.md §3.2.3` secondary-sources and re-grounded to 20/20/6/26. Basis: D1, this-cycle searches.
- **Fragmentation** — CLEAN. D3 (S2 de-dup) and D4 (S4 consolidate) REDUCE existing duplication (F2 falsification triplication, F3 [READY] fragmentation); the cycle commits no second copy of any principle. Basis: F2, F3, D3, D4.
- **Lossy-render** — CLEAN. D2–D6 target framework-spec sections that render into plugins; decisions are behavior-preserving (S1 sub-numbering, S2 de-dup-with-cite, S4 consolidate, S6 strip) except F4's two-vs-three-passes reconciliation, which sharpens an existing contradiction (does not soften a "must"). Enforcement strength preserved. Basis: D2–D6, F4.
- **Bloat** — OUT OF SCOPE this cycle. Fires on rule-text the cycle adds/amends; this cycle adds no rule-text (D2–D6 [OUTLINED]; realization output produced at impl). The re-derivation's direction is bloat-reducing.
- **Leakage** — OUT OF SCOPE this cycle. No rule-text added to a domain-general file; no domain concretion introduced.
- **Unenforced-rule** — OUT OF SCOPE this cycle. No new load-bearing rule stated; structural decisions preserve existing enforcement.
- **Undefined-shorthand** — OUT OF SCOPE this cycle. No new coined term introduced (`§4.2.x` are section labels, not defined shorthand).
