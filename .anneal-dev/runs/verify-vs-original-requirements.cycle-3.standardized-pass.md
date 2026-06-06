# Cycle 3 — standardized inspection pass

Cycle 3 locked the design (D1 re-searched, D3/D4/D6 [VERIFIED], D8 [CONDITIONAL], F1/F4/F5 resolved).
Decisions commit to additions; realization prose is produced at impl (`tracker.md` body shape).

- **Bloat** — cited: the additions (requirements record + coverage check) carry a namable load-bearing function — they close the audit-confirmed F1 gap (a dropped requirement otherwise escapes verify). Not bloat.
- **Fragmentation** — cited-clean: no existing requirements-coverage principle to duplicate — basis: F2 empty search.
- **Leakage** — cited-clean: "what counts as a requirement / how elicited" delegated to the instance slot (D3), not concreted in domain-general core.
- **Missed-dependents** — cited: D1 scope re-searched this cycle (grew to §4.1); dependents = 3 instance `investigate-design.md` + `verify.md` + foundations/glossary/modules — basis: the cycle-3 re-search.
- **Unenforced-rule** — cited: D4's check is evidence-bearing (uncovered requirement → a finding, mirroring the design-completeness audit); D3's requirements record is the artifact the isolated verify reads. Following-the-rule produces the coverage map; not-following produces an uncovered-finding.
- **Undefined-shorthand** — cited: D6 adds glossary entries for the two new terms (practice 10), discharged at impl.
- **Lossy-render** — cited (design-time): D3/D4 specify the rule's enforcement strength (a "must" coverage check); the rendered artifacts are clause-checked at verify (render-fidelity battery).
- **Over-claimed-verification** — cited: each [VERIFIED] decision's basis is a re-checkable read/search (core.md §5/§5.1, :694-697, :708-720, :80; the scope searches); no claim exceeds its cited basis. F5 records the one honest residual rather than over-claiming closure.

No load-bearing finding open. F5 is a recorded residual (deferred), not an open gap.

## Fresh-session implementability — PASSED
A fresh session with only the tracker implements the locked design without surfacing a new design decision:
- D3 → add the requirements-record capture rule at `core.md` §4.1 — basis form: located read `core.md:285-294` (the Scope decision is the established "capture-first at investigate-design" pattern the requirements record parallels).
- D4 → add the coverage check at `core.md` §4.3 — basis form: located read `core.md:708-720` (the design-completeness audit is the structural template to mirror).
- D6 → add 2 glossary entries — basis form: located read `glossary.md` entry shape (definition + spec citation), per practice 10.
- render → 3 instance `investigate-design.md` + `verify.md` — basis form: search `ls */phases/{investigate-design,verify}.md` (all present, cycle-1/cycle-3 searches).
- D8 [CONDITIONAL] as-recommended (capture verbatim request; defer the soft record-vs-request check) is implementable; the deferred soft check is explicitly out of this run's scope (F5/D8 — soft-judgment-verification dependency).
