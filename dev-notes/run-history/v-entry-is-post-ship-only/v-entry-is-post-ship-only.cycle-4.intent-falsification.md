# Cycle 4 — convergence cycle: intent-falsification pass

Run: `v-entry-is-post-ship-only` · cycle 4 (convergence). Dispatched fresh-context
(subagent `a15cf254269e1d5fe`, opus), criteria-first against the requirements record
R1/R2/R3. Orchestrator re-grounded each finding against the actual entries per the
basis rule (secondary-source interpretation re-checked, `foundations.md`).

## Per-R# attack lines
- **{R1, served}** — attacked the exclusion delta for a shape between "already shipped"
  and "not-yet-implemented gap" (a designed-but-uncommitted fix). Served: "not-yet-
  implemented" catches the uncommitted-design case (no commit = backlog), and "fires →
  spawns a backlog item" closes the firing path. No residual shape.
- **{R2, finding}** — attacked the unchanged transitions table + RESOLVED/INVALIDATED
  + Q7 against β's new WATCHING def. Finding F9 (transitions-table coverage). Q7 `:169`
  is genuinely definition-agnostic (walks a production signal, not a lifecycle position)
  → D0's no-edit-on-Q7 claim HOLDS.
- **{R3, finding}** — read 8 real WATCHING entries vs β's "original design decision"
  wording. Finding F8 (the wording over-narrows / mis-fits fix-residual + class-watch
  entries).

## Per-finding lines (with orchestrator re-grounding + route)
- **F8 → ACTIONED (reopens D2).** β's WATCHING wording "an uncertain **shipped choice**
  — an **original design decision**" mis-fits a subset of the 22 WATCHING entries.
  Orchestrator re-ground: **V-30** (class-recurrence quality-watch over multiple shipped
  fixes — not an "original design decision") and **V-31** (watches shipped rule D4.1's
  dodge-residual) genuinely don't fit; **V-25** DOES fit (its "fix" is the hypothetical
  future catcher; the shipped thing is the choice-to-accept-the-residual — subagent
  over-read). The defect: D2-β's "choice vs remedial-fix" axis contradicts the
  operator-confirmed **D1** (a V-entry watches a shipped fix OR a shipped choice — an
  umbrella over BOTH states, not the WATCHING/FIX-SHIPPED separator). Route: the subagent
  tagged `[VERIFIED — surfaced]` (semantic-fit judgment, no coupling-shape reduction);
  the **orchestrator ACTIONS it as a D-delta** (the design's wording is wrong — cycle-2
  F-A precedent). basis: read V-25 full, V-30 full, V-31 full + D1 boundary.
- **F9 → [VERIFIED — surfaced]; folded into D6.** The transitions table (`:78-82`)
  models only WATCHING→FIX-SHIPPED→RESOLVED/INVALIDATED, but V-30/V-31 describe closing
  WATCHING→RESOLVED/INVALIDATED. Orchestrator: this is a **pre-existing** lifecycle-
  coverage question (not introduced by β) and **out of this run's R1/R2/R3 scope**
  (which is post-ship-vs-backlog clarity, not transition-table completeness). Folded
  into D6's conformance-sweep brief (reconcile each entry's closing rule against the
  table; flag table-coverage gaps) rather than expanding this run's edit scope. basis:
  read V-30/V-31 closing rules + transitions table `:78-82`.
- **F10 → ACTIONED (folds into D2).** Vocab WATCHING (`:128`, "no fix shipped yet")
  already drifted from the lifecycle def (`:42`, "no **structural** fix shipped yet") —
  it dropped "structural"; D2's "Vocab mirrors" was under-specified, risking re-drift
  (the exact fragmentation the run fights). Route: ACTIONED — corrected D2 makes the
  Vocab state lines a **pointer** to the canonical lifecycle def (one canonical home),
  resolving the pre-existing duplication. basis: grep `:42` vs `:128` (non-identical
  today).

## Outcome
**D-track delta this cycle** (D2 [INVALIDATED]→[PENDING] per F8/F10). Per
`spec/core.md` §4.1.4 sequencing, the **mechanical falsification pass is SKIPPED this
cycle** (intent-delta) — recorded "mechanical skipped: intent-delta this cycle." Loop
continues: cycle 5 reworks D2 to corrected β; cycle 6 = fresh convergence.
