# Impl plan — provenance-basis-naming

1 dispatch unit (single edit; sequential in-place under the integrity check). Spec-only release;
renders (anneal-dev/plugin self-render + clippy fire-point) → render-debt (instance-reinstantiation).

## Unit 1 — core.md §3.2.1 basis-naming bullet (D2+D3)
Files: `spec/core.md` only.
- Extend the embedded-claims enumeration at `core.md:219-221` (currently "...implicit premises in
  target-naming decisions, cited rules or prior decisions, completeness counts asserted as facts")
  with a FOURTH form: **a name or label asserting an artifact's MEANING or PROVENANCE** (its source,
  identity, perspective, unit, or value-domain), whose basis is a **located read at the artifact's
  PRODUCER/SOURCE (where it is set/produced), NOT its use-site label** — distrust the surface
  assertion, ground at the source. Reuses §3.2(b)'s located-read (`core.md:185-187`).
- CRITICAL (INT-B watch-point): the **producer-not-use-site** redirection must survive into the
  rule-text — without it the form collapses toward §3.2(b)'s generic located-read and loses the
  distinctness that justifies the #2-sharpen. Keep tight (one clause, domain-general; coding
  concretions → clippy render). Define inline (no new glossary term).
- Briefed: load foundations/tracker/implement.md; invoke skill-craft before the edit; write-time
  self-check (Lossy-render / Missed-dependents / Undefined-shorthand / Over-claimed + change-set-vs-scope).
