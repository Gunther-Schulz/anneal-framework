# anneal-dev impl-Checkpoint commit conflicts with the rule-corpus discharge hook

**Status:** ✅ DONE — resolved by `corpus-flows-redesign` (release-record `4e77837`):
**D7** (checkpoint ≠ release-commit; `commit-msg` hook skips `anneal-checkpoint:`-prefixed
commits — `00374a5`) + **D12** (anneal-dev's persistence mechanism mandates the prefix, the
producer rule — `d9033ee`). Validated in-run (both checkpoint commits skipped the discharge
gate). Residual spun off → `release-commit-formation-from-checkpoints.md`.

--- original finding (kept for the record) ---
(was) OPEN — method finding, surfaced 2026-06-03 during the
`cite-glossary-not-section-numbers` anneal-dev run (impl loopback, run tracker F9/D7).
Affects anneal-dev itself (`anneal-dev/spec` / `phases/implement.md`), not the spec
this run edits.

## The conflict

- **anneal-dev `phases/implement.md` (Checkpoint)** mandates that each dispatch unit's
  integrated changes are **committed** per touched container, the commit reference
  appended to the tracker as the unit's persistence reference (the resume anchor).
- **anneal-framework `hooks/commit-msg`** (active via `core.hooksPath=hooks/`) **rejects
  every rule-corpus commit** that lacks a complete Step-4 discharge artifact (7 named
  checks: render-fidelity, practice-4 dependent audit, skill-craft full/self reviews,
  practice-6 + cross-spec coherence). The discharge is assembled from the **verify phase
  + operator approval** — which come AFTER implement.

Net: for a rule-corpus run, an implement-phase unit **cannot honestly produce a
per-unit pre-verify checkpoint commit** — the discharge it would need does not exist
yet, and fabricating it / `--no-verify` are both forbidden (over-claimed-verification;
governance bypass). The per-unit commit-as-persistence-reference is impossible here.

## What this run did (the de-facto workaround → candidate resolution)

D7: commit ONCE post-verify with the discharge + operator sign-off; impl's "save" until
then = the staged working tree + the tracker record (resume-recoverable). This worked,
but it means `implement.md`'s Checkpoint (per-unit commit) does not describe how
rule-corpus runs actually persist.

## The question to settle (a future anneal-dev run)

How should `phases/implement.md` Checkpoint reconcile with discharge-at-commit governance?
Candidates: (a) the checkpoint "save" is explicitly NOT a commit for rule-corpus runs —
persistence = staged-tree + tracker record, commit deferred to the release-loop discharge;
(b) per-unit commits allowed only on a branch with a deferred/partial discharge that the
release-merge completes; (c) the discharge hook is scoped to merges-to-main only, freeing
branch checkpoint commits. Decide which, then sharpen `implement.md` (and possibly
`development-process.md` release loop + the hook's scope).

## Relates to
- `corpus-flows-redesign.md` — **DECISION VENUE** (operator-folded 2026-06-03): this is a
  dev-machinery coordination case reconciled *within* the strategy redesign (#3 enforcement),
  not as a standalone run. The three candidate resolutions above are the options it weighs.
- `impl-green-on-commit.md` — sibling impl/commit-discipline item (different axis: green
  state vs discharge presence); check for fold/inform when either is worked.
- `worktree-isolation-and-integration.md` — the parallel-unit integration path also assumes
  per-unit commit/integration; same Checkpoint mechanism.
- run tracker `.anneal-dev/runs/cite-glossary-not-section-numbers.md` (F9, D7) — the surfacing.
