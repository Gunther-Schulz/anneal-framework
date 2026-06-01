# anneal-dev Specification — Lens-supplement mechanism

The lens-set slot extends with a project-supplement mechanism — a
way for projects using anneal-dev to add their own lenses (lens
supplements) on top of the instance's closed core set
(`lens-set.md`). Per `instantiation-guide.md` §4 "Optional:
project-supplemental lenses". This file declares the mechanism
(required, per the always-ready principle); specific supplemental
lenses are project-supplied later.

## anneal-dev's supplement mechanism

- **Location:** `anneal-dev.config/lenses.md` (operator-editable,
  committed; per the filesystem-layout rule, distinct from
  `.anneal-dev/runs/` runtime state).
- **Format:** each supplemental lens fills the Name / Question /
  Scope shape per `anneal-framework/spec/modules.md` §2.1.
- **Loading:** the orchestrator reads supplements at
  standardized-pass dispatch; the runtime lens set is
  core ∪ supplement, closed at the project's runtime.
- **Absence semantics:** file absent OR empty body = no
  supplements (core-only).
- **Malformed semantics:** parse failure halts standardized-pass
  dispatch with the parse error surfaced as a tracker finding; the
  operator sees the malformed supplement at the next
  closed-artifact presentation and corrects it. Fail-loud, not
  fail-safe — the supplement file's contents are evidence-bearing
  input to the standardized pass.

## Constraints carried from the framework

Supplemental lenses are bound by the framework's constraint list
(`instantiation-guide.md` §4): same Name / Question / Scope shape;
closed at project level; operator-supplied (not invented at
runtime); **additive-only** (no disabling, narrowing, or override
of core lenses); reviewed against the same skill-craft form
discipline as core lenses.

If a core lens consistently mismatches a project's needs, the fix
is at the instance-spec level (sharpen the core lens in
`lens-set.md`), not at the project level (silence it).

**A likely supplement for this domain:** a project maintaining one
specific corpus may add a lens for its own house conventions — e.g.,
a citation-format lens, or a per-repo cross-reference-syntax lens —
that the domain-general core set does not carry. Such project-house
rules are exactly the additive content the supplement slot is for.
