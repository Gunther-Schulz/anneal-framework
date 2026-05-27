# <Instance> Specification — Run-artifact persistence

The framework requires the tracker to persist across
interruptions (`anneal-framework/spec/core.md` §6) as an
append-only ledger (`spec/modules.md` §3.1). Two additional
artifacts must persist: each cycle's standardized-pass findings
artifact (`spec/modules.md` §3.2) and each design decision's
implementation decomposition (`spec/modules.md` §3.3). The
instance supplies the concrete mechanism per
`anneal-framework/instantiation-guide.md` §2.

## <Instance>'s persistence mechanism

Where the artifacts live:

- **Tracker:** `<location, e.g., .<plugin-skill-name>/runs/<run-name>.md>`
- **Standardized-pass artifacts:** `<location, cycle-stamped>`
- **Implementation decompositions:** `<location, identifying
  the design decision>`

How an in-progress run is found and resumed:

- `<describe the scan and match procedure — at run start the
  orchestrator scans for an in-progress run; resume vs surface
  vs start-fresh per match>`

## Filesystem layout — operator-config vs runtime state

Per `anneal-framework/instantiation-guide.md` §5 (filesystem
layout rule + Project init), declare the two locations:

- **Runtime state** (tracker, standardized-pass artifacts,
  implementation decompositions): `.<plugin-skill-name>/runs/`
  (gitignored).
- **Operator-editable artifacts** (extension toggles, lens
  supplements, any operator-facing config):
  `<plugin-skill-name>.config/` (committed).
