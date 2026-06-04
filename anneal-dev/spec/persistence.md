# anneal-dev Specification — Run-artifact persistence

The framework requires the tracker to persist across interruptions
(`anneal-framework/spec/core.md` §6) as an append-only ledger
(`spec/modules.md` §3.1). Other artifacts must also persist: each
cycle's standardized-pass findings artifact (`spec/modules.md`
§3.2), the impl plan (`spec/modules.md` §3.3), and — at the
convergence cycle — the mechanical falsification-pass artifact
(`spec/modules.md` §3.4) and the intent-falsification-pass
artifact (`spec/modules.md` §3.4.1, the intent-falsification pass
per `anneal-framework/spec/core.md` §4.1.4). The framework states
run state is **not
assumed to share a container with the work product** (`core.md`
§6 Run lifecycle); the instance supplies the concrete location and
resume mechanism per `instantiation-guide.md` §2.

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
- **Mechanical falsification-pass artifact:** `.anneal-dev/runs/<run-name>.cycle-<N>.falsification.md`
  (the convergence cycle's per-decision artifact; per
  `modules.md` §3.4)
- **Intent-falsification-pass artifact:** `.anneal-dev/runs/<run-name>.cycle-<N>.intent-falsification.md`
  (the convergence cycle's intent-falsification pass artifact —
  the per-R# attack lines + per-finding lines; per `modules.md`
  §3.4.1, the pass per `anneal-framework/spec/core.md` §4.1.4)
- **Impl plan:** `.anneal-dev/runs/<run-name>.impl-plan.md`
  (the dispatch-unit list, dependency-ordered, parallel-eligibility
  marker + listed element/contract scope per unit; per
  `modules.md` §3.3)

These are per-cycle and per-phase run artifacts kept beside the
tracker, not filed into it (`modules.md` §3.2, §3.3, §3.4).

## Run state spans containers; run-state location is one of them

The corpus is multi-container — a unit's edits may land across
several repos (`bindings.md` isolation slot). The framework does not
assume the run's state shares a container with the work product
(`core.md` §6); the run-state directory `.anneal-dev/runs/` lives in
one repo — the repo the operator invoked the run from — while the
work product the run touches spans the repos in scope.

This is the framework's intended shape, not a strain: §6 separates
run-state location from work-product location, and the integrity
check operates per touched container (`core.md` §4.2). A unit's
cross-container changes are integrated into each touched repo
(`bindings.md` isolation slot Integration); the tracker records each
unit's completion via its persistence reference (`core.md` §4.2
Checkpoint) — the integrated changes' commit reference per touched
container. **Each checkpoint commit's first line carries the
`anneal-checkpoint:` prefix** — marking it a working-progress save, not
the release commit — so a deploying repo's release-discharge hook skips
it (`anneal-framework/development-process.md`: checkpoint ≠
release-commit). Resume reads the tracker from the run-state repo and the
recorded per-container references; it does not re-derive work-product
state by scanning every repo.

## How an in-progress run is found and resumed

At run start the orchestrator scans `.anneal-dev/runs/` for an
in-progress run — a tracker whose header Status is not `PASSED`:

- an in-progress run for the current task → resume it (read the
  tracker reduced-to-latest; the phase header names where to
  re-enter; a mid-implement interruption resumes from the impl
  plan's last-completed unit per its persistence reference,
  `core.md` §4.2 Checkpoint).
- an in-progress run for a different task → surface it to the
  operator, then start a fresh run.
- none → a fresh run, in a new file.

Completed runs' tracker files are kept; `.anneal-dev/runs/`
accumulates as the project's anneal-dev history — no run overwrites
another.

## Filesystem layout — operator-config vs runtime state

Per `instantiation-guide.md` §5 (filesystem layout rule + Project
init):

- **Runtime state** (tracker, standardized-pass artifacts,
  mechanical falsification-pass artifacts, intent-falsification-pass
  artifacts, impl plans): `.anneal-dev/runs/`
  (gitignored — `git check-ignore` true).
- **Operator-editable artifacts** (extension toggles, lens
  supplements, operator-facing config): `anneal-dev.config/`
  (committed — `git ls-files` tracked).

The namespace (`anneal-dev` / `.anneal-dev`) is unique to this
instance per the namespace-uniqueness rule, preventing collision
when anneal-dev runs in a project that also hosts another
anneal-derived instance.
