# Cycle 6 — convergence cycle: intent-falsification pass

Run: `v-entry-is-post-ship-only` · cycle 6 (convergence, attacking the corrected D2).
Dispatched fresh-context (subagent `a401635d00c04a6d4`, opus), criteria-first vs R1/R2/R3.
New surfaces: 14 previously-unsampled WATCHING entries (V-3/4/8/9/10/11/14/16/17/18/20/21/22/23)
+ FIX-SHIPPED V-24/28/29. Orchestrator re-ground each finding (basis rule).

## Per-R# attack lines
- **{R1, finding}** — F-R1-1 (the exclusion's accepted-residual / not-yet-built boundary).
- **{R2, finding}** — F-R2-1 (residual pre-ship phrasing survives at two sites until implement;
  a post-implement coverage check, NOT a design contradiction). FIX-SHIPPED vs WATCHING stays
  distinct on the remediation-state axis → the cycle-2 F-A collapse does NOT recur.
- **{R3, SERVED}** — all 14 newly-sampled WATCHING entries fit "an already-shipped decision
  (choice, rule, or accepted residual)"; V-16/V-17 fit via "accepted residual"; the 3 FIX-SHIPPED
  stay distinct (dated commit + remedial fix). No mis-classification, no over-tightening. **The
  cycle-4 failure point is fixed.**

## Per-finding lines (orchestrator disposition)
- **F-R1-1 → ACTIONED (reopens D2).** The cycle-5 exclusion text "a noticed gap, **decided-against**
  or not-yet-built → backlog" COLLIDES with the WATCHING def's "accepted residual" sub-shape — an
  accepted residual (V-25 "the framework accepts this residual"; V-16/V-17 "no dedicated mechanism
  shipped") IS a "decided-against building a mechanism," so the cycle-5 exclusion would wrongly route
  legitimate WATCHING entries to the backlog → an internal contradiction with the WATCHING def. The
  airtight discriminator is practice-8's "genuine uncertainty about a *shipped* decision (watch) vs a
  classifiable not-yet-built fix (backlog)", which the README edit did not carry. Subagent routed
  `[VERIFIED — surfaced]` (wording-sufficiency judgment); **orchestrator ACTIONS** — the collision is a
  real design defect. basis: read V-16 `:7-9` + V-17 `:7-11` + V-25 + cycle-5 D2 exclusion text + practice 8 `:293-299`.
- **F-R2-1 → verify acceptance-criterion (NOT a D-delta).** The pre-ship WATCHING phrasing lives at
  README `:42` AND Vocab `:128` (`grep "no.*fix shipped" → 2 hits`); D2 rewrites `:42` and pointer-izes
  `:127-134`, covering both. The subagent's "mechanical-falsification-candidate" is explicitly a
  *post-implement* `any-match` grep — i.e. a verify check on D2's amendment-completeness, not a
  falsification of D2's basis (the located reads are accurate). Folded into D2's acceptance criteria +
  verify (post-implement `grep -nE "no (structural )?fix shipped yet"` on the README must be empty).
  basis: grep `:42`/`:128` + D2 delta targets.
- **F-R3-1 → [VERIFIED — surfaced]; folds into D6.** V-16/V-17 are the thinnest-fitting (only 2 of 22
  fit via "accepted residual"); the D6 conformance-sweep brief should flag the "accepted-residual vs
  not-yet-built-gap" discriminator as the per-entry test. Not a design defect. basis: `grep "no dedicated
  mechanism shipped" → V-16, V-17`.

## Outcome
**D-track delta this cycle** (D2 [INVALIDATED]→[PENDING] per F-R1-1). Mechanical falsification pass
**SKIPPED this cycle: intent-delta** (per `spec/core.md` §4.1.4). Loop continues: cycle 7 refines the
exclusion (drop "decided-against"; inline the practice-8 discriminator); cycle 8 = fresh convergence.
R3 served + collapse-non-recurrence carry forward as evidence.
