# Release-commit formation from anneal-dev checkpoints (the D7 discharge-attachment gap)

**▶ SHIPPED + ARCHIVED 2026-06-16 — `b8f53df` (main, pushed).** Batched with
`commit-msg-hook-packaging-overmatch` via anneal-dev (run `release-machinery-batch`, auto-battle).
Resolution: the **"final discharge commit, hook-validated"** option — development-process.md step 5 now
specifies the release commit is a FINAL commit re-touching any rule-corpus file the run changed (hook
validates the discharge), not a squash (no interactive rebase) or amend (messy across a merge); exempt-only
runs need no discharge. (The other 2 options rejected per the env/merge constraints.) Verify [PASSED] isolated.

**Status:** SHIPPED (was [READY]) — framework finding, surfaced at the `corpus-flows-redesign` release
(2026-06-03). Small but real; methodology-correctness → operator-judged. Not blocking
(this run handled it pragmatically).

## The gap
D7 (checkpoint ≠ release-commit) established that anneal-dev's per-unit **checkpoint**
commits (`anneal-checkpoint:` prefix) skip the discharge hook, and the **release commit**
carries the Step-4 discharge (release loop step 5). It did NOT specify **how the
discharge-bearing release commit is formed when the run's work lives in N checkpoints** —
squash the checkpoints into one release commit? a final discharge-bearing commit on top?
amend the last checkpoint (dropping its `anneal-checkpoint:` prefix so the hook validates
the discharge)?

For `corpus-flows-redesign`: the rule-corpus checkpoints (`00374a5`, `b48713d`, `d9033ee`)
are **non-contiguous** (split by the subtree-add merge commit `d5ae00d`), and the
environment has **no interactive rebase**, so a clean squash isn't available. The discharge
ended up in a **release-record commit body** (operator-approved), but it was a dev-notes
commit → not hook-validated as a rule-corpus commit. So the hook's structural backstop on
the discharge was bypassed this run (the operator-approval gate held; the hook gate didn't fire).

## Candidate resolutions (for the pass)
- **Final discharge commit, hook-validated.** Define the release commit as a final commit
  that touches a rule-corpus marker (or re-touches the run's primary file) carrying the
  Step-4 discharge — so `hooks/commit-msg` validates it. Specify it in the release loop +
  anneal-dev's checkpoint→release transition.
- **Amend-last-checkpoint.** The last checkpoint drops its `anneal-checkpoint:` prefix and
  gains the discharge → becomes the release commit (hook validates). Simple for contiguous
  runs; messier across a merge.
- **Squash-on-release.** Squash the run's checkpoints into one discharge-bearing release
  commit. Cleanest history; needs a non-interactive squash path (env constraint).
Pick one + specify it so the discharge is reliably hook-validated, not just body-recorded.

## Relates to
- `corpus-flows-redesign.md` (D7 / the run that exposed this); `development-process.md`
  release loop step 5; `hooks/commit-msg` (the discharge gate); anneal-dev `implement.md`
  §Checkpoint + `persistence.md` (the checkpoint convention, D12).
- Method-kernel-adjacent (touches the release loop + anneal-dev checkpoint mechanics) →
  anneal-dev + kernel-independent verify.
