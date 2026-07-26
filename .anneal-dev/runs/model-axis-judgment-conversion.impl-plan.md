# Impl plan — model-axis-judgment-conversion (produced at [READY], cycle 13)

6 dispatch units, dependency-ordered. Disjointness basis: unit targets are file-disjoint —
each target file appears in exactly one unit (enumeration below is the complete target set
of the locked design: D2/D4/D5/D6 → core.md; D2/D4/D6 → modules.md; D7 → glossary.md;
D3 → bindings.md; D3 → config artifacts; D8 → dev-notes files). U1–U4 parallel-eligible
(separate-copy isolation); U5 after U4; U6 after U1+U4. Every unit dispatched at opus-4.8
(configured floor; decision-complete briefs per D9), subagent invokes skill-craft before
any rule-corpus edit, self-checks with write-time lenses, returns fixed-shape ledger lines.

- **U1 — `spec/core.md`** (first; parallel with U2/U3/U4): §4.1.4 two-axis independence
  clause + coverage-check relation re-derivation clause + spawn-fallback doubled-residual
  sentence (D2 (i)-(v), (viii)); §4.1.4 domain-claim re-derivation sentence incl.
  data-beats-commentary (D6); §4.1.4 worked-example presence-check sentence (D5);
  §3.2.2 closed-value-set completeness paragraph (D4); §5.2 Body-shape (c)
  boundary-example clause (D5); §4.1.1 supporting-facts item (D5). Kernel wording
  tier-abstract throughout (D1/F1).
- **U2 — `spec/modules.md`** (parallel with U1/U3/U4): §3.4.1 header fields
  checker-capability relation (bare enum) + ordering-basis: declared/assumed (D2 (vii));
  §3.4.1 refutation-field claimed/re-derived pair doc (D6); §3.4 closed-set always-include
  sentence (D4); §3.3 intent-falsification brief clause (c) relation inputs (D2 (vi)).
- **U3 — `spec/glossary.md`** (parallel): new entry "Checker-capability relation"
  (definition + closed enum + citations) + extend "Intent-falsification pass" entry with
  the two-axis sentence (D7); no-collision re-check post-edit (F10).
- **U4 — `anneal-dev/spec/bindings.md`** (parallel): §Dispatch model tier — kind-keyed
  elevation (three-step relation rule), comparison-free boundary cell, inert-by-default
  named + arming step, ordering-declaration format, bootstrap placeholder text (D3).
- **U5 — `anneal-dev.config/model-tier.md` + `anneal-dev.config/README.md`** (after U4):
  header/explainer texts carrying floor + elevation in operator-facing words (D3);
  PLUS the proposed operator-owned line `order: fable-5 > opus-4.8 > sonnet-5` — staged
  but LANDS ONLY via the operator's commit approval (D3/D9).
- **U6 — dev-notes** (after U1+U4, needs the canonical wording): re-render
  `dev-notes/modellwahl-und-anneal.md` rule 3 to the shipped carve-out wording (D8 (c),
  F6); append the render-debt row to `dev-notes/backlog/instance-reinstantiation.md` —
  instances: anneal-dev plugin (self), coding-clippy (render tree + spec/bindings.md
  §Dispatch models reconcile obligation), daneel (locate-source-first; rendered machinery
  at plugin cache `daneel/daneel/0.2.50`), campaign-craft/bauleitplan (locate-source-first
  per matrix precedent) (D8 (a)/(b)); PREPARE backlog successor notes incl. the corrected
  F25 label (below-actor cross-model, not diverse — F28) and D10's reopen trigger —
  transitions themselves only at release on operator word.

Not in any unit (post-verify/release, operator-gated): backlog status transitions; the
final report's PBS Vorgriff deletion flag (report-only, single-writer); step-4 discharge
artifact + foundation-invariant ledger (INV-3) for the operator's soundness verdict;
release commit.
