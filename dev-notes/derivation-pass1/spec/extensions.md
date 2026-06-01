# anneal-dev Specification — Lifecycle extensions

Lifecycle extensions are instance-declared behaviors that fire at
framework-defined points in the cycle (`instantiation-guide.md` §5).
The framework defines the closed set of points; an instance hooks
one or more by declaring them here. Every extension ships
**disabled by default**; the operator toggles per project.

This file declares the **enable mechanism** (required, per the
always-ready principle, `instantiation-guide.md` §5 Project-init)
and one declared extension.

## Enable mechanism

- **Location:** `anneal-dev.config/extensions.enabled` (per the
  filesystem-layout rule — operator-editable, committed, distinct
  from `.anneal-dev/runs/` runtime state).
- **Format:** one enabled extension name per line; lines starting
  with `#` are comments.
- **Absence semantics:** file absent OR name absent = disabled
  (fail-safe per `instantiation-guide.md` §5 "Disabled by
  default").

## Extensions

### on-verify-PASSED · render-and-open-diff
**Action:** when verify reaches [PASSED] on a spec-level change,
re-render the affected plugin skill files from the now-verified
spec and present the rendered diff for the operator's review
(does not commit it — presentation only, the operator owns the
render commit).
- Affected renders derived from: the tracker's verified D-entries
  whose targets are rendered plugin clauses (`bindings.md`).
**Side-effect target:** the local working tree of the affected
plugin repo(s) — writes the re-rendered files for the operator to
inspect.
**Failure handling:** log + continue (the operator can re-render
manually; the run's [PASSED] stands regardless).

Capability-boundary note (`instantiation-guide.md` §5): this
extension writes to **non-spec paths** only (rendered plugin
files, which are render output, not spec source) — permitted at
`on-verify-PASSED`. It does NOT write to framework spec, instance
spec, or modify tracker state. It is a bookend, not a gate.

(No `on-instance-start` gate is declared. A dirty-tree refusal was
considered and rejected: the impl-phase Main-tree integrity check
(`core.md` §4.2) already refuses-and-surfaces on a dirty tree at
dispatch, so an `on-instance-start` gate would duplicate an
existing framework check — the Additive-reflex anti-pattern. The
slot stays available via the enable mechanism above.)
