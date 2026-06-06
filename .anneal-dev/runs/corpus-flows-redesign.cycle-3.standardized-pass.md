# corpus-flows-redesign — cycle 3 standardized inspection pass

Cycle 3 resolved D4 ([VERIFIED]), added D7 ([CONDITIONAL]) + D8 ([VERIFIED]),
dispositioned F3/F6/F7/F8/F10/F11/F12, and surfaced+addressed F13. Still
NO rule-text written (design decisions only).

## In scope this cycle

- **Fragmentation — CLEAN (now structurally closed).** D8 names ONE
  canonical routing home (`development-process.md`) with the other docs
  pointing to it — the 3+ drifting copies (F9) collapse to one statement +
  cross-refs. — basis: D8 + F9.
- **Unenforced-rule — CLEAN (resolved).** D4 locates enforcement correctly:
  the load-bearing sub-guarantees ARE gated (pre-edit hook + commit-msg
  discharge hook); routing is rigor-preference, not under-prescribed prose.
  — basis: D4 + `hooks/commit-msg` 99-230 + `hooks/skill-craft-pre-edit.py`
  262-296.
- **Missed-dependents — FORWARD NOTE (flagged for impl).** D4/D7/D8 edits
  touch dependents to enumerate at implement: `development-process.md`
  (routing intro + the "sibling repo" phrasing under D5), the commit-msg
  hook skip-list (D7, companion code), and D8 makes the other 4 routing
  docs cross-ref dependents. — basis: D4/D7/D8 targets + D1 scope.
- **Undefined-shorthand — FORWARD NOTE (flagged for impl).** Cycle 3 uses
  "checkpoint-save", "release-commit", "entry-condition", "render-tail". If
  any enters rule-text as load-bearing, a `spec/glossary.md` entry is
  required in the same commit (practice 10). None in rule-text yet. —
  basis: D7/D2 + practice 10.
- **Over-claimed-verification — CLEAN, prior watch carried.** D4 rests on
  located reads of both hooks + dev-process step 4 (strong); D7 on F13 (the
  literal active hook, confirmed via `core.hooksPath`); D8 on
  `development-process.md` line 34 (strong). The cycle-2 WATCH stands: D3
  rests partly on a fit-judgment ("derivation fits investigate-design") —
  carried to the convergence falsification pass. — basis: D4/D7/D8 basis
  fields + cycle-2 pass.

## Out of scope this cycle (cited)

- **Bloat — N/A.** No rule-text added/amended; design decisions only. —
  basis: no corpus file edits.
- **Leakage — N/A.** No rule-text added to a domain-general file. — basis: same.
- **Lossy-render — N/A.** No cycle-3 decision targets a rendered plugin
  clause or commits a source-rule paraphrase (D4 a hook stance, D7 a
  hook+prose, D8 a doc-home). — basis: D4/D7/D8 targets.
