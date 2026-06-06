# Standardized-pass — cycle 3 (convergence cycle)

New surfaces investigated this cycle (convergence new-surface requirement):
- Surface A — glossary "Basis and evidence" section read (glossary.md:47-113): the
  insertion home for "evidence-bearing-artifact rule"; re-confirms the firewall
  (entries carry `core.md §`-pointers internally, e.g. :53-54, :89-90).
- Surface B — glossary "Triage and review classifications" (glossary.md:423-458):
  "post-run review" is USED here (:426) but undefined as a headword → insertion home.
- Surface C — instantiation-guide "The skill content is rendered, not authored"
  (instantiation-guide.md:424-458): the render relationship; the citation rule's home
  is the §3 (Binding) area, near this section.
- Surface D — new-angle search `rg "(core|modules|glossary)\.md\b" <instance> | rg -v §`:
  the target citation style ALREADY exists in-corpus — instances cite
  `anneal-framework/spec/glossary.md Coupling shape` (term, no §) at clippy
  tracker.md:226/239, anneal-dev investigate-design.md:196/221/294. Strengthens D2.
- Surface E (falsification) — `modules.md §3.2` "standardized-pass findings artifact".

Lenses:
- **Missed-dependents** — **FINDING (F8)**. The cycle-3 falsification pass surfaced a
  dependent D3's interface-completeness enumeration missed: the §3.2 "standardized-pass
  findings artifact" is a §-cited method-concept (clippy/spec/bindings.md:48,
  anneal-dev/spec/persistence.md:6, daneel/spec/bindings.md) with NO glossary headword,
  unlike its §3.3/§3.4 siblings. D3's "exactly 2" undercounted by 1. D3 reopens. —
  basis: cycle-3 falsification artifact (D3 target-dependents, positive) + orchestrator
  greps (glossary headword absent; siblings at :152/:343).
- **Over-claimed-verification** — **FINDING (informs F8)**. Cycle 2's "spot-verified
  gap = 2" (F6) was an incomplete enumeration: it checked Model/post-run/evidence-bearing
  + 4 binding terms, but did NOT iterate the full §-cited-concept set against the
  glossary — so it missed §3.2. The completeness claim "exactly 2 gaps" rested on a
  sampled subset, not the whole §-cited set (the silent-substitution shape). Corrected
  by the falsification pass's full iteration. — basis: F6 vs cycle-3 falsification.
- **Bloat / Fragmentation / Leakage / Unenforced-rule / Undefined-shorthand** —
  re-attested CLEAN on D1/D2/D4/D5 (unchanged this cycle; convergence re-attestation).
  basis: cycle-3 falsification (D1/D2/D4/D5 all hold).

Convergence cycle 3 is NOT clean — one D-delta (D3 falsified→reopened). Re-formation
in cycle 4; fresh convergence in cycle 5.
