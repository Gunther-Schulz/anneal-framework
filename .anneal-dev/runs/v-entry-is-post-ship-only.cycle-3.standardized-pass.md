# Cycle 3 — standardized inspection pass

Run: `v-entry-is-post-ship-only` · cycle 3 (D2 rework per β). Scope this cycle:
edits to `dev-notes/validation-watch/README.md` (a dev-notes companion doc — not a
domain-general spec file, not a plugin render). Lenses lined per scope touched.

- **Bloat** — clean. D2-β's added prose is load-bearing: the WATCHING re-frame
  (`:42-45`) carries the contradiction-fix (the old "no structural fix shipped yet"
  reads pre-fix, contradicting practice 8); the canonical exclusion sentence
  (preamble `:26-39`) carries R1 (un-implemented gap → backlog); the FIX-SHIPPED
  axis-sharpen (`:47-58`) carries the WATCHING↔FIX-SHIPPED distinction F-A flagged as
  collapsing. No restatement — the exclusion is stated ONCE, not duplicated into each
  state def. basis: D2-β delta (b).
- **Fragmentation** — clean. The V-vs-backlog principle lives across README +
  practice 8 (D4) + CLAUDE.md (D3) BY DESIGN as cross-confirming, not duplicated: the
  README lifecycle is canonical; the exclusion's canonical home is the README preamble
  (one place); practice 8 + CLAUDE.md reference the post-ship/backlog split, they do
  not restate the lifecycle. The run's whole purpose is removing a CONTRADICTION (drift)
  and replacing it with cross-confirmation. basis: F1 + D2-β/D3/D4 (README canonical,
  others reference).
- **Unenforced-rule** — clean (appropriately). The filing-shape ("is this an
  un-implemented gap or a shipped-thing-watch?") is a judgment discipline, not
  mechanizable; the doc states it as the discipline, backstopped by the post-run
  self-review + Q7's per-state walk + the operator. Filing shape resists mechanization;
  prose-discipline is the right enforcement form here. basis: D2-β (c)/(d) + Q7 `:84-89`.
- **Undefined-shorthand** — clean. "shipped choice" and "remedial fix" are descriptive
  phrases, not coined terms requiring a glossary entry; they read off plain meaning and
  are used consistently (WATCHING = shipped choice; FIX-SHIPPED = remedial fix). No new
  multiply-defined shorthand. basis: D2-β delta (b) + Vocab `:127-134`.
- **Missed-dependents** — clean. D0 enumerated dependents under β: in-file references to
  the WATCHING/FIX-SHIPPED states (transitions `:78-82`, RESOLVED `:60-71`, INVALIDATED
  `:73-76`) reference the states **by name**, not by the pre/post-fix axis being
  re-framed → unbroken by the re-frame. Cross-doc: Q7 (`post-run-review.md`,
  definition-agnostic walk — F5, no-edit), CLAUDE.md (D3, β-consistent), practice 8 (D4,
  β-consistent). The 28 V-entry Status labels: β preserves (no relabel). basis: D0 +
  F5 + located reads `:60-82`.
- **Leakage** — N/A. `validation-watch/README.md` is a project dev-notes companion, not
  a domain-general spec/skill-craft file; the framework-arbitrariness test does not
  apply.
- **Lossy-render** — N/A. No design decision this cycle targets a rendered plugin clause;
  no source-rule paraphrase committed.
- **Over-claimed-verification** — N/A. No new completeness/verification claim recorded
  this cycle beyond the located-read bases already audited in D2-β's basis field.
