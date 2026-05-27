# <Instance> Specification — Lifecycle extensions

**OPTIONAL — delete this file if your instance does not declare
any lifecycle extensions.**

Lifecycle extensions are instance-declared behaviors that fire
at framework-defined points in the cycle. The framework defines
the closed set of extension points; an instance hooks one or
more by declaring them here. Per
`anneal-framework/instantiation-guide.md` §5.

Every extension ships **disabled by default**. The operator
toggles per project.

## Enable mechanism

- **Location:** `<e.g., <plugin-skill-name>.config/extensions.enabled>`
  (per the filesystem layout rule in §5 — operator-editable,
  distinct from runtime state)
- **Format:** `<e.g., one enabled extension name per line>`
- **Absence semantics:** `<e.g., file absent OR name absent =
  disabled>` (fail-safe per
  `anneal-framework/instantiation-guide.md` §5 "Disabled by
  default")

## Extensions

### on-<extension-point> · <extension-name>
**Action:** `<e.g., invoke `gh pr create --title <T> --body <B>`
  with T derived from the cycle's task summary, B derived from
  tracker reduced to verified F/D entries>`
**Side-effect target:** `<e.g., GitHub remote>`
**Failure handling:** `<e.g., log + continue>`

<repeat per declared extension. Each extension hooks one of the
framework's named extension points (on-instance-start /
on-cycle-end / on-verify-PASSED / on-instance-complete) and is
bounded by the seven capability-boundary clauses in §5.>
