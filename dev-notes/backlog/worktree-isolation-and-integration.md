# Worktree isolation + integration — path-relocation, cherry-pick silent-drop, stale base

**Status:** OPEN — finding (cross-session clippy run, 2026-06-02). Git-native
isolation/integration gaps on the **parallel-worktree** dispatch path (per Cycle G:
parallel-eligible units → worktree + cherry-pick; sequential/single → main-tree).
Relates to [[clippy-run-findings-dispatch-coupling]] (Cycle 2 isolation + Cycle G
Main-tree integrity check), [[harness-tool-runstate-unsourced]].

## (a) Worktree placement allows an escape to operator's main
The Agent-tool worktree lands at `<operator-main>/.claude/worktrees/agent-<id>/`
— *inside* operator's main tree. From the subagent's cwd, `cd ../..` lands in
operator's repo; a defensive cwd-resilience habit (`cd <repo-root>`) then finds
operator's main and uses it — not malice, the alternate repo is right there. The
azuro episode hit exactly this (a subagent's work landed in operator's main).

**Fix — path-relocation, not mechanism-replacement:**
- Worktree at a distinct top-level path with **no parent-escape to main**:
  `git worktree add /tmp/clippy-wt-<run-id>-<unit-id> <head-commit>`. From there
  `cd ../..` lands in `/tmp` (clearly not a repo), so the defensive-cd habit fails
  harmlessly.
- Worktree on a **unique branch** `clippy/<run-id>/<unit-id>` (operator can
  audit / merge / discard).
- **Brief path discipline:** paths in the brief are cwd-relative (`./src/…`),
  never absolute; never leak `/…/main` into the brief — denies the agent the
  *knowledge* of operator's main, not just the path.
- **Post-return verification:** orchestrator snapshots `git -C <main> rev-parse
  HEAD` before dispatch and confirms it didn't move after. Moved → contamination
  → halt + surface.
- git-native (no separate clones), language-agnostic; **bootstrap (venv/deps) is
  a project-level concern** — the spec stays agnostic about it.

## (b) Integration trusts the cherry-pick (silent hunk-drop)
A `git cherry-pick` of the worktree commit onto a **diverged** main auto-merges
and can **silently drop hunks** without raising a conflict (observed: a unit's
three arb-site lines dropped on integration). The Integrity check verifies the
subagent didn't *contaminate* main (HEAD pre/post, clean tree) — but **not** that
the unit's change *fully landed* and the unit's **acceptance criteria still hold
on the integrated tree**. It leans entirely on final verify → surfaces the gap
**globally and late** instead of **locally at integration**.

**Fix:** a per-unit post-integration check — change landed completely
(diff-equivalence vs the worktree commit) **and** acceptance re-passes on the
integrated tree, *before* the next unit.

## (c) Stale-base worktree (harness bug, not spec)
The harness provisioned worktrees from an *older* commit (missing two recent
migrations). The spec (`implement.md`) correctly says "worktree from current main
HEAD at dispatch"; the harness didn't honor it → a fail-loud `worktree base ==
main HEAD at dispatch` check is warranted. Cross-ref
[[harness-tool-runstate-unsourced]].

## (d) Test-execution dependencies in the isolated copy (operator-raised 2026-06-06)
The isolation moves each unit's copy to a distinct top-level path with **remotes stripped**
((a) above) — `/tmp/anneal-dev-copy-…` / `git worktree add /tmp/…`. For a **test-running
instance** (clippy: a unit's verify runs the suite), that copy needs the **build/dependency
cache** — `node_modules`, cargo/`target`, a venv, DB fixtures — which a fresh `/tmp` copy does
NOT have. The spec currently **punts**: implement.md "Provisioning" + (a) above both say
"project bootstrap (venv/deps) stays the operator's concern, out of scope." That punt is
**insufficient for a test-running unit**: with no cache, the isolated test run fails or is
prohibitively slow → the parallel-worktree path becomes unusable exactly where it's most
wanted (parallel test-heavy units). Open question: does the isolated copy get cache access —
via a **shared, read-only cache mount/symlink** (e.g. a shared cargo/npm cache dir the copy
points at, kept read-only so units can't clash), via **copy-on-provision** of the cache, or
does "out of scope" stand (and parallel isolation is simply not for test-running instances)?
This is the load-bearing decision that determines whether worktree isolation is viable for
clippy at all. Compose with the Provisioning rule (run-inputs provisioned, excluded from
integration) — the cache is a read-only run-input, not a tracked work-product, so it fits that
shape if provisioned read-only.

**Level.** Framework (§4.2 isolation/integration) + clippy render; (a)/(c) also
harness. Relates to [[clippy-run-findings-dispatch-coupling]],
[[harness-tool-runstate-unsourced]]. Also informs
[[impl-dispatch-workflow-substrate]] — these defenses (a: path-relocation,
b: cherry-pick landing-check) are what a Workflow substrate would have to
**re-script in-agent** rather than fix as rules; a live argument in that
substrate trade-off.
