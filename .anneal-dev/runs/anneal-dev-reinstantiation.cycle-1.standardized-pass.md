# Standardized-pass artifact — anneal-dev-reinstantiation, cycle 1

Lens set: core (8) ∪ project supplement. Project supplement
`anneal-dev.config/lenses.md` checked: placeholder/empty (no project lenses)
→ runtime set = core 8. Each line cites this-cycle basis.

- **Lossy-render** [in scope] — CLEAN at design: no design decision (D2–D6)
  commits to a softened render; each commits to *carrying* the source clause
  with its enforcement (R2, faithful-render requirement). The realized
  artifact's fidelity is the verify render-fidelity battery's job (lens-vs-
  battery split, `references/lenses.md`); the dominant risk is the large
  §4.1.4 intent-falsification render (D2, ~90 source lines) — flagged for the
  battery, not a design-time softening. basis: D2–D6 bodies (carry-clause
  commitments) + R2.
- **Missed-dependents** [in scope] — FINDING F7: D2 renames the rendered term
  "falsification pass" → "mechanical falsification pass", an amendment of an
  existing rendered contract; its dependent set across the plugin must be
  enumerated. basis: `grep -rniE 'falsification' anneal-dev/plugin/skills/anneal-dev/`
  → SKILL.md (1: L186), investigate-design.md (22 lines incl L38/168/179/260
  template), tracker.md (12 lines incl L129 §-heading/L201 file-path). The
  rename's true-unit basis is this enumeration.
- **Over-claimed-verification** [in scope] — CLEAN: F1–F6's [VERIFIED —
  non-issue] claims each re-open to a search-established basis (F1 diff-stat
  query, F2/F4 empty greps, F3 located read L1-11, F5 diff file-list, F6
  bindings.md located read); none asserts more than its cited basis. basis:
  F1–F6 basis fields (this cycle).
- **Fragmentation** [in scope] — CLEAN: D5 renders the model-tier floor in ONE
  home (`SKILL.md` dispatch-wide rule) + the config-slot listing in
  `foundations.md`; no second copy of the floor principle. The blanket-over-all-
  dispatch-kinds property (F6) is what lets one rendered rule cover impl/verify/
  falsification without per-phase-file duplication. basis: D5 + F6.
- **Bloat** [in scope] — FINDING F9 (watch): the render is additive across
  SKILL.md (model-tier rule + bootstrap 4th placeholder + closed-artifact
  citations) and investigate-design.md (the two-pass convergence cycle); the
  realized files must stay faithful-not-expanded, and SKILL.md's size is
  skill-craft-budgeted. Watch at impl/verify (skill-craft review + Bloat lens
  on realized text), not a design-time bloat. basis: D2/D5/D6 (additive
  targets) + SKILL.md current 332 lines (`wc -l`).
- **Undefined-shorthand** [in scope] — FINDING F8: the render introduces terms
  new to the plugin — "intent-falsification pass", "[VERIFIED — surfaced]",
  "mechanically-confirmable / pure-judgment", "requirements record",
  "requirements-coverage check", "mechanical falsification pass". Each must have
  a defining home in the rendered plugin (used-with-definition, not used-bare),
  citing the framework glossary where the plugin defers. basis: `grep -rniE
  'requirements|model[- ]tier|surfaced'` (F4 + token grep) → the terms are
  absent today, so the render must define them at first use, not assume them.
- **Unenforced-rule** [in scope] — CLEAN at design: D2/D5 commit to carrying
  each rendered rule's enforcement artifact — the model-tier floor's observable
  model-param ("a downgraded dispatch is visible on the dispatch itself"), the
  intent-falsification artifact's malformed-line rules, the requirements-coverage
  finding-producer. Realized enforcement checked at verify. basis: D2/D5 bodies
  + bindings.md "Enforcement" clause.
- **Leakage** [OUT of scope] — cited reason: the render target is the
  *instance* level (anneal-dev plugin); the Leakage lens fires on domain-general
  files (framework spec, skill-craft canonical), per `references/lenses.md`
  Scope. Instance-level domain concretions are correct, not leakage. basis:
  `references/lenses.md` Leakage Scope ("domain-general").
