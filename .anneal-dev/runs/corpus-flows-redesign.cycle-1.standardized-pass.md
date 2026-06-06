# corpus-flows-redesign — cycle 1 standardized inspection pass

Cycle 1 produced findings + design decisions over framework-dev routing
prose; it wrote NO rule-text and committed NO render/paraphrase. Lens
scope is assessed against that.

## In scope this cycle

- **Fragmentation — FINDING (F9).** The "run through anneal-dev" routing
  principle is stated independently in `development-process.md`,
  `instantiation-guide.md` §6, and `spec/README.md` :50 — three copies that
  can drift. The redesign (D3) must canonicalize to one statement +
  cross-refs, not add a fourth. — basis: this-cycle search (`re.render` +
  `corpus.evolution` tokens) hitting all three files; F9.
- **Unenforced-rule — FINDING (F3 → D4).** Path-3 re-render routing is
  prose-mandate only; the pre-edit hook enforces skill-craft-invocation,
  not anneal-dev routing. Named in D4 as the gap to close structurally.
  — basis: F3 (hook scans `Skill skill-craft`, not anneal-dev) + D4.
- **Missed-dependents — FORWARD NOTE (clean this cycle; flagged for impl).**
  No rule changed yet, but D1 names `spec/glossary.md` + `spec/modules.md`
  as the re-render METHOD-DEFINITION dependents any re-render-routing edit
  must audit. — basis: this-cycle search `rg -ln 're.render'` returning
  glossary.md + modules.md alongside the routing docs; D1.
- **Undefined-shorthand — FORWARD NOTE (clean this cycle; flagged for impl).**
  D2/D3 will coin path-names ("the three paths", channel terms); per
  practice 10 each load-bearing new term needs a `spec/glossary.md` entry
  in the same commit. No term committed to rule-text yet. — basis: D2/D3
  are [OUTLINED] (no rule-text); `development-process.md` practice 10.
- **Over-claimed-verification — CLEAN.** The one [VERIFIED] this cycle (D1
  scope) rests on four re-runnable token-searches, not recall; its true
  unit (the routing-contract's corpus spots) is covered by the union of
  those queries. Residual: a routing spot using NONE of the four tokens
  would be missed — narrow risk, re-checkable at convergence. — basis: D1
  basis field (the four executable `rg` queries).

## Out of scope this cycle (cited)

- **Bloat — N/A.** No rule-text added or amended; cycle 1 is investigation
  + design decisions only (D-track entries are tracker artifacts, not
  corpus rule-text). — basis: D-track D1-D5 are decisions, no file edits.
- **Leakage — N/A.** No rule-text added to a domain-general file this
  cycle. — basis: same (no edits to spec/skill-craft).
- **Lossy-render — N/A.** No design decision this cycle targets a rendered
  plugin clause or commits a paraphrase of a source rule; D1-D5 target
  framework-dev routing docs. — basis: D1-D5 targets are
  development-process.md / instantiation-guide.md / spec/README.md /
  repo-structure, none a `plugin/skills/*` clause.
