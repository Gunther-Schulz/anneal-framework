# <Instance> Specification — Lens-supplement mechanism

**OPTIONAL — delete this file if your instance does not declare
a lens-supplement mechanism.**

The lens-set slot may extend with a project-supplement
mechanism — a way for projects using <Instance> to add their
own lenses (lens supplements) on top of the instance's closed
core set. Per `anneal-framework/instantiation-guide.md` §4
"Optional: project-supplemental lenses".

## <Instance>'s supplement mechanism

- **Location:** `<e.g., <plugin-skill-name>.config/lenses.md>` (per the
  filesystem layout rule in §5 — operator-editable, distinct
  from runtime state)
- **Format:** `<each supplemental lens fills the
  Name / Question / Scope shape per
  anneal-framework/spec/modules.md §2.1>`
- **Loading:** `<the orchestrator reads supplements at
  standardized-pass dispatch; runtime set = core ∪ supplement,
  closed at project runtime>`
- **Absence semantics:** `<e.g., file absent OR empty = no
  supplements; core-only>`

## Constraints carried from the framework

Supplemental lenses are bound by the framework's constraint
list — full list at `anneal-framework/instantiation-guide.md`
§4 "Optional: project-supplemental lenses". Operator-relevant
highlights: same Name / Question / Scope shape; additive-only
(no override of core lenses); operator-supplied.

If a core lens consistently mismatches a project's needs, the
fix is at the instance-spec level (sharpen the core lens in
`lens-set.md`), not at the project level (silence it).
