# In-place integrity-check "clean before dispatch" precondition doesn't fit self-hosting (the repo is never clean)

**Status:** OPEN — spec×self-hosting friction, surfaced 2026-06-05 by the `campaign3-enforcement-fidelity` run's post-run review (operator-requested). Low severity (intent satisfiable by attribution; no contamination occurred). Method-kernel-adjacent (`spec/core.md` §4.2.4 + `anneal-dev/spec/bindings.md` isolation-slot) → anneal-dev if pursued. Could fold into / relate-to `worktree-isolation-and-integration` (④a — both are impl-isolation mechanics).

## The gap
`core.md` §4.2.4 (in-place Integrity check) + `bindings.md` (state-marker) require: "confirm each touched **container** is **clean before dispatch** (refuse and surface if not)", where `bindings.md` binds container = repository. But in **self-hosting**, the orchestrator does concurrent `dev-notes/` bookkeeping (backlog grooming, filing spawned items, run-state-adjacent edits) **in the same repo** as the work product (`spec/*`). So the repo is **never clean** at in-place-dispatch time — the literal precondition ("refuse if not clean") would block every in-place impl dispatch in this repo.

**This run:** dispatching U1 (the `core.md` §5.1 edit) in-place, the tree had uncommitted `dev-notes/backlog/` changes (cadence-levels, filed items). The orchestrator did NOT refuse (per the literal rule) — it dispatched and satisfied the integrity **intent** by **attribution** (`git diff`: subagent → `spec/core.md` only; orchestrator → `dev-notes/`, cleanly separable). The intent (no contamination, exactly-the-unit's-change) held; the literal precondition was violated.

## Triage (practice 1)
**Spec gap (underspecification):** the "clean container" precondition does not distinguish **work-product paths** (which must be clean for attribution) from **non-work-product run-bookkeeping** (`dev-notes/`, which is the run's own state-adjacent area and irrelevant to the work-product container's integrity). The rule admits the reading "whole-repo-clean," which self-hosting routinely violates without any integrity loss. The intent is "the unit's change is cleanly attributable on the work-product paths" — not "the whole repo tree is pristine."

## Candidate fix (classifiable — structural, scope-narrowing)
Narrow the in-place clean-precondition to the **work-product paths the unit touches** (search-established disjoint from any *other* uncommitted change), not the whole container: "confirm the unit's touched work-product paths are clean before dispatch; uncommitted changes on disjoint paths (incl. run-bookkeeping) do not block — the integrity check confirms the touched paths advanced by exactly the unit's change." This is the attribution the orchestrator already does, made the rule. Edit-as-Pareto: replaces a precondition that self-hosting can't meet with the operative one (path-scoped attribution).

## Compounding instance + partial fix (2026-06-06 — `run-state-tracked-by-default`)
**Compounded.** That kernel run made run-state **tracked** (no longer gitignored). So the run's
OWN tracker (`.anneal-dev/runs/<run>.md`), written continuously during a run, is now a **tracked
file in the work-product container** — a SECOND routine source of in-place-clean-precondition
collision, beyond the `dev-notes/` bookkeeping in the original instance. The repo is now
*guaranteed* dirty during any run (the live tracker), not merely incidentally.

**Partially fixed (a subset).** That run added **D7**: the in-place integrity check + restore
**exclude the run-state directory** (`core.md §4.2.4` + `bindings.md`; orchestrator bookkeeping,
not work product), so the run-state tracker no longer trips clean-before-dispatch nor is
discarded on restore. **But D7 is a narrow carve-out** (run-state only); this item's candidate fix
(narrow the precondition to the unit's **work-product paths**, disjoint from ANY other uncommitted
change) is **broader and subsumes it** — it also covers `dev-notes/` bookkeeping and any disjoint
uncommitted change. When this item is worked, **generalize D7's run-state carve-out into the full
work-product-path-scoping** (D7 becomes one case of the general rule).

**Self-referential demonstration (the vivid one).** The run-state-tracked-by-default run — whose
whole point was the D7 exclusion — **could not use the dispatched-in-place integrity path on
itself** during its own implement: D7 wasn't live yet AND the tracker was already tracked, so the
formal in-place check would have tripped on the run's own run-state → the run implemented in the
**working context** (spawn-fallback) instead. The kernel edit couldn't cleanly run its own
machinery on itself — the sharpest evidence that the precondition needs the path-scoping fix.

## Relates to
- `worktree-isolation-and-integration` (④a) — sibling impl-isolation mechanics (parallel-copy path); this is the in-place path's precondition. Possible co-home.
- Self-hosting clause (`CLAUDE.md`) — the same self-hosting reality (work product + dev-process machinery co-located) that this friction stems from.
- Origin: `campaign3-enforcement-fidelity` U1 in-place dispatch (post-run review).
