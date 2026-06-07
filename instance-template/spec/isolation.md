# <Instance> Specification — Isolation mechanism

The framework fixes the impl-phase isolation **guarantees**
(`anneal-framework/spec/core.md` §4.2, §4.2.3) and requires them
to hold: a dispatched unit works without reaching the operator's
work product, and the integrity check confirms each touched
container changed in exactly the authorized way. The instance
supplies the concrete mechanism per
`anneal-framework/instantiation-guide.md` §2.

## <Instance>'s isolation mechanism

How a separate copy is made and made escape-resistant, the unit
identifier, the markers the integrity check reads, the restore
mechanism, and which non-tracked run-inputs are provisioned:

- **Separate copy:** `<how, and where, a separate copy of each
  touched container is made — the location, outside the operator's
  work-product tree>`
- **Unit identifier:** `<the auditable identifier that scopes the
  unit's recorded changes>`
- **Escape-resistance:** `<how the copy is denied knowledge or
  access of the operator's work-product location, so a defensive
  traversal cannot reach it>`
- **State marker:** `<the marker the integrity check reads, per
  touched container>`
- **Restore mechanism:** `<what restores the pre-dispatch state on
  an integrity mismatch>`
- **Provisioned run-inputs:** `<which non-tracked run-inputs are
  provisioned into the copy, and so excluded from integration>`
