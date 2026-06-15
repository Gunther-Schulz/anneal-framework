# Impl plan — convergence-machinery-batch

**1 unit, strictly sequential, in-place (Integrity check).** Touched container: the
`anneal-framework` repo only (`spec/core.md`, `spec/modules.md`, `spec/glossary.md`). No
parallelism (single unit → no disjointness basis needed). Plugin renders = render-debt (F6),
out of scope. Run-state under `.anneal-dev/runs/` is gitignored (not part of the work product).

## Unit 1 — implement D2, D3', D4, D5, D6 (the convergence-machinery edit-set)
Element scope: `core.md` §4.1 pass-1 (D2) + pass-2 (D3'); `core.md` §4.1.4 intent-falsification +
the new completeness-bind (D4, D6); `core.md` §4.3 requirements-coverage (D5); `modules.md` §3.4.1
per-R# line (D4); `glossary.md` Intent-falsification-pass entry (D6) + Requirements-coverage-check
entry (D5). Contract scope: the convergence-cycle intent machinery + the standardized-pass trigger.

Dependency order: none cross-unit (one unit). Within the unit the edits are independent text
changes; the subagent integrates them coherently (practice 6).

Dispatch: in-place subagent, opus floor, briefed to invoke skill-craft before any edit, apply the
4 write-time self-check lenses, commit an `anneal-checkpoint:` save, return state. Orchestrator
runs the Integrity check (clean-before, HEAD snapshot, advanced-by-exactly-the-change-after).
