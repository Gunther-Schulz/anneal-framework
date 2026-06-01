# anneal-dev Specification — Run-artifact persistence

The framework requires the tracker to persist across interruptions
(`anneal-framework/spec/core.md` §6) as an append-only ledger
(`spec/modules.md` §3.1). Two additional artifacts must persist:
each cycle's standardized-pass findings artifact
(`spec/modules.md` §3.2), each design decision's implementation
decomposition / impl plan (`spec/modules.md` §3.3), and — at the
convergence cycle — the falsification-pass artifact
(`spec/modules.md` §3.4). The instance supplies the concrete
mechanism per `instantiation-guide.md` §2.

## anneal-dev's persistence mechanism

Each run's tracker is its own append-only markdown file under
`.anneal-dev/runs/`, named for the run — holding a header (the
run's status, the current phase, mode, a one-line task summary) and
the two tracks (F-track, D-track). A new entry, a status change, or
a correction appends a ledger line; existing lines are never
rewritten. An entry's current state is its latest peer-level line
plus its sub-annotations; where current state is needed — [READY], a
resume, verify (`core.md` §4.3), the convergence-falsification
dispatch (`core.md` §4.1.4), the closed artifact — the tracker is
read reduced to the latest line per entry.

**Header enum values** (instance-defined closed enums per
`modules.md` §3.1):
- **Status:** `IN-PROGRESS`, `PASSED`.
- **Phase:** `investigate-design`, `implement`, `verify`.

Where the artifacts live:

- **Tracker:** `.anneal-dev/runs/<run-name>.md`
- **Standardized-pass findings artifacts:** `.anneal-dev/runs/<run-name>.cycle-<N>.standardized-pass.md`
  (cycle-stamped; per `modules.md` §3.2)
- **Falsification-pass artifact:** `.anneal-dev/runs/<run-name>.cycle-<N>.falsification.md`
  (the convergence cycle's per-decision artifact; per
  `modules.md` §3.4)
- **Impl plan / decompositions:** `.anneal-dev/runs/<run-name>.impl-plan.md`
  (the dispatch-unit list, dependency-ordered, parallel-eligibility
  marker + listed element/contract scope per unit; per
  `modules.md` §3.3)

These are per-cycle and per-phase run artifacts kept beside the
tracker, not filed into it (`modules.md` §3.2, §3.3, §3.4).

## How an in-progress run is found and resumed

At run start the orchestrator scans `.anneal-dev/runs/` for an
in-progress run — a tracker whose header Status is not `PASSED`:

- an in-progress run for the current task → resume it (read the
  tracker reduced-to-latest; the phase header names where to
  re-enter; a mid-implement interruption resumes from the impl
  plan's last-completed unit per its commit reference, `core.md`
  §4.2 Checkpoint).
- an in-progress run for a different task → surface it to the
  operator, then start a fresh run.
- none → a fresh run, in a new file.

Completed runs' tracker files are kept; `.anneal-dev/runs/`
accumulates as the project's anneal-dev history — no run overwrites
another.

**Multi-repo resume caveat (a strain — see
`derivation-rationale.md`).** The corpus spans multiple repos, but a
run's `.anneal-dev/runs/` lives in one repo — the run-anchor repo
(where the operator invoked the run). On resume the orchestrator
reads run state from the anchor repo; cross-repo edits a unit made
(integrated via cherry-pick into other repos, `bindings.md`) are
recorded by commit reference in the tracker, so resume re-derives
their state from the tracker, not from scanning every repo. The
anchor-repo-holds-the-run-state choice is the resume model; it is
recorded as a strain because the framework's persistence is written
assuming the run's work product and its state share one tree.

## Filesystem layout — operator-config vs runtime state

Per `instantiation-guide.md` §5 (filesystem layout rule + Project
init):

- **Runtime state** (tracker, standardized-pass artifacts,
  falsification-pass artifacts, impl plans): `.anneal-dev/runs/`
  (gitignored — `git check-ignore` true).
- **Operator-editable artifacts** (extension toggles, lens
  supplements, operator-facing config): `anneal-dev.config/`
  (committed — `git ls-files` tracked).

The namespace (`anneal-dev` / `.anneal-dev`) is unique to this
instance per the namespace-uniqueness rule, preventing collision
when anneal-dev runs in a project that also hosts another
anneal-derived instance.
