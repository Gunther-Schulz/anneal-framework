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

**Level.** Framework (§4.2 isolation/integration) + clippy render; (a)/(c) also
harness. Relates to [[clippy-run-findings-dispatch-coupling]],
[[harness-tool-runstate-unsourced]].
