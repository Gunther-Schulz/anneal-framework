# Standardized-pass — cycle 3 (convergence cycle)

New surfaces investigated this cycle (convergence-cycle new-surface requirement):
- Surface A — `sed -n '462,678p' spec/core.md | grep '(below|above)'`: the 9 intra-§4.2 cross-refs are sub-topic references (convert to §4.2.x anchors), no rule split across a seam — D2 behavior-preserving confirmed.
- Surface B — `grep -rln 'any-match|expected-match' <instance>/plugin`: the falsification format lives in instance renders at both `phases/investigate-design.md` and `references/tracker.md` (anneal-dev, clippy) — D3 de-dup is render-safe (daneel carries neither: a lighter pre-existing render, [CONDITIONAL] under D1).

Lenses:
- **Missed-dependents** — **FINDINGS (F7, F8)**. The falsification pass (this cycle's third pass) surfaced two dependent-enumeration defects: F7 — D1/D2's §4.2 cite enumeration missed 3 sentence-final cites (raw token=23 vs basis regex=20); F8 — D3's predicate-closed-set home enumeration missed the glossary definitional home (3rd home). Both reopen their decisions. Basis: the cycle-3 falsification artifact + verification greps.
- **Over-claimed-verification** — **FINDINGS (F7, F8)**. D1/D2's "20 cites" and D3's "2 homes" were [VERIFIED] completeness claims that over-claimed — the true units are 23 cites and 3 homes. The boundary regex `§4\.2([^.0-9]|$)` is the silent-substitution vector (a narrowed search dressed as a complete one). Basis: F7, F8.
- **Fragmentation** — CLEAN (re-confirmed). F8's glossary home is the README-sanctioned definitions-only layer (`Glossary is definitions-only / Closed sets are enumerated`, README:77–81), not a duplication to collapse; D3's de-dup stays core↔modules with glossary retained. Basis: F8, README:77–81.
- **Bloat / Leakage / Unenforced-rule / Lossy-render / Undefined-shorthand** — no new rule-text added this cycle (investigation + falsification only); out of scope.

Outcome: the convergence cycle is NOT clean — F7/F8 reopen D1/D2/D3. Loop continues to cycle 4 (re-form with corrected bases).
