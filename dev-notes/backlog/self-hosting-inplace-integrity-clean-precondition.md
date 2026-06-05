# In-place integrity-check "clean before dispatch" precondition doesn't fit self-hosting (the repo is never clean)

**Status:** OPEN — spec×self-hosting friction, surfaced 2026-06-05 by the `campaign3-enforcement-fidelity` run's post-run review (operator-requested). Low severity (intent satisfiable by attribution; no contamination occurred). Method-kernel-adjacent (`spec/core.md` §4.2.4 + `anneal-dev/spec/bindings.md` isolation-slot) → anneal-dev if pursued. Could fold into / relate-to `worktree-isolation-and-integration` (④a — both are impl-isolation mechanics).

## The gap
`core.md` §4.2.4 (in-place Integrity check) + `bindings.md` (state-marker) require: "confirm each touched **container** is **clean before dispatch** (refuse and surface if not)", where `bindings.md` binds container = repository. But in **self-hosting**, the orchestrator does concurrent `dev-notes/` bookkeeping (backlog grooming, filing spawned items, run-state-adjacent edits) **in the same repo** as the work product (`spec/*`). So the repo is **never clean** at in-place-dispatch time — the literal precondition ("refuse if not clean") would block every in-place impl dispatch in this repo.

**This run:** dispatching U1 (the `core.md` §5.1 edit) in-place, the tree had uncommitted `dev-notes/backlog/` changes (cadence-levels, filed items). The orchestrator did NOT refuse (per the literal rule) — it dispatched and satisfied the integrity **intent** by **attribution** (`git diff`: subagent → `spec/core.md` only; orchestrator → `dev-notes/`, cleanly separable). The intent (no contamination, exactly-the-unit's-change) held; the literal precondition was violated.

## Triage (practice 1)
**Spec gap (underspecification):** the "clean container" precondition does not distinguish **work-product paths** (which must be clean for attribution) from **non-work-product run-bookkeeping** (`dev-notes/`, which is the run's own state-adjacent area and irrelevant to the work-product container's integrity). The rule admits the reading "whole-repo-clean," which self-hosting routinely violates without any integrity loss. The intent is "the unit's change is cleanly attributable on the work-product paths" — not "the whole repo tree is pristine."

## Candidate fix (classifiable — structural, scope-narrowing)
Narrow the in-place clean-precondition to the **work-product paths the unit touches** (search-established disjoint from any *other* uncommitted change), not the whole container: "confirm the unit's touched work-product paths are clean before dispatch; uncommitted changes on disjoint paths (incl. run-bookkeeping) do not block — the integrity check confirms the touched paths advanced by exactly the unit's change." This is the attribution the orchestrator already does, made the rule. Edit-as-Pareto: replaces a precondition that self-hosting can't meet with the operative one (path-scoped attribution).

## Relates to
- `worktree-isolation-and-integration` (④a) — sibling impl-isolation mechanics (parallel-copy path); this is the in-place path's precondition. Possible co-home.
- Self-hosting clause (`CLAUDE.md`) — the same self-hosting reality (work product + dev-process machinery co-located) that this friction stems from.
- Origin: `campaign3-enforcement-fidelity` U1 in-place dispatch (post-run review).
