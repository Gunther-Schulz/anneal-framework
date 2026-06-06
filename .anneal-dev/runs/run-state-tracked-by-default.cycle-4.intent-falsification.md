# Cycle 4 — convergence: intent-falsification pass

Run: `run-state-tracked-by-default` · cycle 4 (convergence on the reworked design). Fresh-context
subagent `aff951b0fb877741b` (opus), criteria-first vs R1–R5 + the resume-durability req. New
surfaces: `core.md §4.2` in-place integrity + the separate-copy Integration step.

## Per-R# attack lines
- **R1/R2/R3 served** (§5 + bindings covered; contract survives on namespace/path discriminant).
- **R4 finding** (F-a — D4's reworked discriminant is wrong/incomplete on the separate-copy path).
- **R5 served-with-residual** (render-debt row is an impl deliverable; F-d).
- **R(resume-durability) findings** (F-b precedence, F-c cadence — both judgment).

## Findings
- **F-a [VERIFIED — surfaced → ACTIONED: reopens D4]** *(the actionable one)*. D4's reworked provisioning rationale rests on "the **uncommitted** current run-state isn't in a base-commit copy" — wrong/incomplete under tracked run-state: a base-commit separate copy now **carries the committed prior run-state**, and "not part of the tracked work product" (`bindings.md:188`) reads false (run-state IS git-tracked). The sound discriminant is **work-product-vs-bookkeeping** (D7's own boundary), NOT tracked/uncommitted. Also: the Integration step ("only the unit's changes," `bindings.md:199`) has NO run-state exclusion for the separate-copy path — asymmetric with D7's in-place exclusion; a copy-side unit touching carried-in run-state could integrate it back. **Fix → rework D4:** rest on work-product-vs-bookkeeping (align with D7); exclude run-state from integration; the orchestrator provisions the CURRENT run-state (not the copy's stale base-commit one). basis: read `bindings.md :187-199` + D4 + base-commit copy `:152-153`.
- **F-b [VERIFIED — surfaced]** committed-vs-on-disk resume precedence unspecified. BUT the append-only "latest line wins" rule (`tracker.md`) resolves it (on-disk reduced-to-latest = state; commits = durability snapshots). Requirement does NOT fail → not actioned (brake). basis: `persistence.md :79-95` + tracker.md append-only.
- **F-c [VERIFIED — surfaced]** in-flight commit cadence unspecified for investigate-design/verify (`anneal-checkpoint:` is impl-per-unit). BUT the durability is AVAILABLE (run-state is trackable/committable); WHEN to commit is operational, not a spec mandate (over-prescription to fix). Requirement met by being trackable → not actioned (brake). D1 rationale tightened: "git-durable resumable checkpoints" = run-state is committable; durability realized at commit points (checkpoint discipline + operator), not a new mandated cadence. basis: `persistence.md :71-74` + `core.md §4.2` Checkpoint.
- **F-d [VERIFIED — surfaced]** `extensions.md:46-52` references clean-before-dispatch as a dirty-tree guard; D7 narrows it (excludes run-state) but the reference stays TRUE for work-product paths → not broken, low-stakes, no scope-add needed. basis: read `extensions.md :46-52`.
- **F-e [VERIFIED — surfaced]** D7 excluding run-state from "no other modification" leaves a unit-writes-to-run-state detection gap — but **parity-preserved** (gitignore hid such writes before); D7 sound, confirms "makes explicit what gitignore did implicitly." basis: `core.md :766-772` + gitignore parity.
- **D6/INV-3 re-confirmed:** D7 touches `core.md §4.2` (contamination guard, INV-3-adjacent) but does NOT breach verify-isolation (the verify subagent reads the tracker regardless). No invariant breached.

## Outcome
**D-track delta** (F-a reopens D4). Mechanical pass **SKIPPED** (intent-delta). Not [READY]. → cycle 5 reworks D4 (work-product-vs-bookkeeping boundary + integration-exclusion); cycle 6 = fresh convergence. The surfaced residuals (F-b/c/d/e) feed operator soundness; D1 rationale tightened per F-c.
