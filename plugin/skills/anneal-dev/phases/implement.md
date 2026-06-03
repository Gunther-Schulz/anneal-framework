# implement

The second phase of an anneal-dev run: it carries out the locked design
recorded in the tracker, producing the rule-text — editing the prose
and structure of the corpus's spec and skill files.

## The locked design is the authority

Produce the rule-text from the locked design — the body of [VERIFIED]
design decisions in the tracker (`tracker.md`). The existing
rule-corpus and its surrounding conventions are context, not authority:
where they diverge from the locked design, the design governs. Derive
the rule-text from the design first; evaluate existing patterns for fit
afterward.

## Findings during implement

implement makes no design decisions. Any finding surfaced during
implementation routes through exactly two paths: **loopback** to
investigate-design (when the finding needs action), or
**[VERIFIED — deferred]** (when the operator chooses not to act now,
basis cites the explicit trigger condition per `references/tracker.md`
Findings). Inline-fix is not a path; attempting to address a finding
within the impl phase by editing the rule-text is malformed.
Local-clarification-and-continue is not a path; the impl phase does not
absorb new findings into the unit's in-flight work.

The choice between loopback and defer is the operator's; the AI's
first-judge recommendation surfaces with the finding. The
pre-classification judgment ("is this finding major-new-scope or
local?") is eliminated — every actioned finding loops back. The
loopback cost (one investigate-design cycle) is the designed trade for
eliminating the inline-misjudgment cost (partial-state save, scope
creep, tracker drift). No work is lost when loopback fires: the tracker
carries the state, and the run re-enters the investigate-design cycle
loop.

## The impl plan

The impl plan is produced at [READY] presentation — the locked design's
decisions grouped into **dispatch units**, dependency-ordered, with a
parallel-eligibility marker on each — so the operator sees the unit list
at the decision moment (`SKILL.md` Closed-artifact form, State summary).
A dispatch unit is a group of design decisions implemented together as
one piece of work; its entry cites the [VERIFIED] decisions it
implements by their tracker identifiers. The impl plan is a planning
artifact, not a new tracker construct.

Parallel-eligibility is a load-bearing claim per the basis rule
(`foundations.md`): a unit's element and contract scopes are listed —
and so its **touched containers** (the corpus repositories its edits
land in) — and the disjointness from any in-flight unit's scope is
established by the re-runnable search behind the claim, not by recall. A
unit whose disjointness is not search-established is sequential. A
multi-repo unit is not sequential *because* it spans repos; it is
sequential only if its scope is not search-established disjoint from an
in-flight unit's, exactly as for any unit.

The plan is persisted alongside the tracker — a phase-start run artifact
at `.anneal-dev/runs/<run-name>.impl-plan.md` — kept for the run's
history and for resume.

## Dispatch

Every unit is dispatched to a subagent — the orchestrator does not
implement in its own context. A parallel-eligible unit (disjointness
search-established) works on a **separate copy** per the Isolation
mechanism below; a strictly-sequential unit — including the single unit
of a one-unit plan — runs in a subagent against the operator's work
product in place under the Integrity check below. If a subagent cannot
be spawned, the orchestrator implements that unit in the working context
and surfaces "without isolation" — the **spawn-fallback**, a degraded
path that waives the isolation guarantee, mirroring verify (`verify.md`).

The subagent is briefed artifact-driven, mirroring verify (`verify.md`):
brief it to load this skill's `references/foundations.md`,
`references/tracker.md`, and this file, and to **invoke skill-craft via
the Skill tool before any rule-corpus edit** (the working context too,
on the spawn-fallback path; `bindings.md` Skill-craft invocation);
provide the tracker (default:
full; reduction to the unit's in-scope decisions is permitted only with
a cited cause — e.g., tracker size exceeds the subagent's context budget
— recorded as the basis for the reduction per the basis rule,
`foundations.md`) and the locked contracts the unit honors (the rule's
forced AI behavior, its evidence-bearing artifact, the closed sets it
names). The subagent implements the in-scope decisions; it does not
design — any actioned finding halts it (below).

Parallel-eligible units may be dispatched concurrently; the disjointness
basis makes that safe. **Dispatch is continuous, not wave-batched.** The
orchestrator maintains a **dispatchable set** — the not-yet-dispatched
units whose dependencies are all completed AND whose listed element and
contract scopes (and so touched containers) are disjoint from every
in-flight unit. After each subagent completion, the orchestrator
recomputes the dispatchable set and fires every newly-eligible unit. A
unit fires when it becomes dispatchable, not when a "wave" is reached;
the disjointness check uses the same scope basis the impl plan declared
at [READY].

## In-place Integrity check (sequential/single units)

This is the path a one-unit plan exercises. A sequential or single unit's subagent runs
in place against the operator's work product directly — reading run
state and the runnable environment natively, no provisioning. The work
product is **multi-container**: each repository the corpus spans
(framework spec, skill-craft canonical, per-domain instance repos) is
one independently-isolable container, and each container the unit
touches is checked independently against the **state marker**.

anneal-dev's state marker per touched container is the repository's
**HEAD commit**:

- The orchestrator confirms each touched container is **clean before
  dispatch** (`git -C <repo> status --porcelain` empty); if not, refuse
  and surface.
- Snapshots each touched container's HEAD (`git -C <repo> rev-parse
  HEAD`) before dispatch.
- After the subagent returns, confirms each touched container advanced
  by **exactly the unit's intended change** and no other modification.
- On mismatch, **restore** the pre-dispatch state — reset the touched
  container to its snapshotted HEAD and discard uncommitted changes
  (`git -C <repo> reset --hard <snapshot>` + remove untracked),
  discarding the subagent's writes — then halt and surface.
  Contamination is contained, not merely detected.

## Isolation mechanism (parallel-eligible units)

A parallel-eligible unit's subagent works on a **separate copy** of each
touched container — anneal-dev's binding of the framework isolation slot
(`bindings.md` Isolation slot; guarantees enforced by the
**Integrity check**, `anneal-framework/spec/glossary.md`) — so concurrent
units cannot clash and the unit's changes reach the operator's work
product only through Integration below, never directly:

- **Copy:** for each touched container, a separate copy of that repo at
  the unit's base commit, created outside the operator's repository tree
  — path `/tmp/anneal-dev-copy-<run-id>-<unit-id>-<container>`
  (top-level `/tmp/`, outside any operator repo tree).
- **Branch / unit identifier:** `anneal-dev/<run-id>/<unit-id>` — the
  branch name the operator can audit, which scopes the unit's recorded
  changes.
- **Escape-resistance:** after copy creation, declared remotes are
  stripped from the copy, and the subagent's brief carries cwd-relative
  paths only — never an operator repo's absolute path — so a defensive
  traversal cannot reach the operator's work product.
- **State marker (isolated form):** each touched container's HEAD,
  snapshotted on the operator's repo before dispatch and re-read after;
  each is confirmed **unchanged** across the unit's work (the unit
  worked on its separate copy). A changed HEAD means the unit escaped
  isolation and contaminated the operator's work product — halt and
  surface, no auto-restore (cause uncertain).
- **Integration:** after the unit's changes are verified clean
  (self-check passed and the integrity check confirms no contamination),
  the orchestrator integrates **only the unit's changes** into the
  operator's work product, per touched container — no copy-side metadata
  crosses over.

**Provisioning.** Run-inputs a dispatched unit reads that are not part
of the tracked work product — the run-state directory
`.anneal-dev/runs/` (gitignored, so absent from a copy) — are
provisioned into the separate copy before dispatch and excluded from
integration. Project bootstrap (what a repo needs merely to be runnable)
stays the operator's concern, out of scope.

## Dispatch-brief template

Sections (a) and (d) live here and the subagent reads them on dispatch.
Per-dispatch briefs carry only per-unit parameters (b) and (c) — the
brief MUST NOT restate (a) or (d) content; it references them by section
letter only.

**(a) Load instructions** (uniform across dispatches in this run): the
dispatched subagent reads, in order, `references/foundations.md`,
`references/tracker.md`, this file (`phases/implement.md`); **invokes
skill-craft via the Skill tool before any rule-corpus edit** (the
working context too, on the spawn-fallback path; `bindings.md`
Skill-craft invocation); and applies
the standardized lenses specified at "Self-check at dispatch boundary"
below.

**(b) Tracker reference**: default is the full tracker; reduction to the
unit's in-scope decisions is permitted only with a cited cause (e.g.,
tracker size exceeds subagent context budget), recorded as the basis for
the reduction per the basis rule (`foundations.md`).

**(c) Unit scope**: the [VERIFIED] decisions this unit implements (cited
by tracker D# identifiers); the unit's element + contract scopes and the
touched containers (repos); parallel-eligibility disjointness basis if
dispatched concurrently with other units.

**(d) Return-state expectations**: fixed-shape ledger lines for new
findings (`references/tracker.md`), the unit's persistence reference
(the integrated changes' commit reference per touched container), any
loopback signal (per "Loopback across the subagent boundary" below).

## Self-check at dispatch boundary

Before returning state, the dispatched subagent (or the working context,
on the spawn-fallback path) applies these four write-time lenses to its
change-set against the unit's in-scope locked design decisions — each
fires on what an edit *introduces* into the change-set:

- **Lossy-render** — does a change-set edit that renders a source rule
  into a plugin clause soften a "must" to a "should", drop a clause, or
  flatten a closed enum into open prose, against the source clause named
  in the decision's basis?
- **Missed-dependents** — for a rule the change-set changes, removes, or
  replaces, does the basis enumerate every dependent across the whole
  corpus — cross-references, paraphrased restatements, rendered clauses,
  closed-set members, glossary/defined-term uses?
- **Undefined-shorthand** — does the change-set introduce or rely on a
  shorthand term used as if it had a fixed meaning, with no single
  definition the corpus points to?
- **Over-claimed-verification** — does any "verified"/"checked"/
  "confirmed" claim the change-set records assert more than the cited
  basis actually establishes (a basis covering part of the set claimed
  whole, a read of one clause standing in for "all references checked")?

Do NOT load `references/lenses.md` whole at dispatch — the self-check
applies exactly the four lens questions above. The full lens catalogue
(scopes, triggers) lives in `references/lenses.md` and loads at the
standardized inspection pass (per-cycle, via
`phases/investigate-design.md`), not at impl dispatch.

**Change-set-vs-listed-scope check.** The subagent additionally verifies
its change-set stays within the unit's listed scope (the per-unit
element and contract scopes from the impl plan). Mechanical check: the
change-set-referenced identifiers (file paths, clauses, defined terms,
cross-references the change-set adds, modifies, or deletes) ∖ the unit's
listed scope = ∅. A change-set entry referencing identifiers outside the
unit's listed scope is an actioned finding (always-loopback per
`Findings during implement` above).

Findings are entered as fixed-shape ledger lines (`tracker.md`) and
returned with state; the orchestrator appends them per the Tracker
writes discipline below.

The self-check compounds with the design-time forcing function for
delete/replace/amend decisions (`foundations.md`, Replacement, removal,
or amendment): the basis enumerates references as of [READY]; the
self-check catches references and behaviors introduced post-design (new
content, new control paths, new failure modes the change-set
introduces). It is unconditional — applied at every dispatch boundary
(and by the working context on the spawn-fallback path).

A self-check finding triggers the loopback (below) — or
[VERIFIED — deferred] per the operator's first-judge recommendation
(`references/tracker.md` Findings).

## Tracker writes

The orchestrator owns the tracker append. A dispatched subagent does not
write directly; on completion or halt it returns state — findings, the
unit's persistence reference, a loopback signal where applicable — and
the orchestrator appends in deterministic order. Subagent return-state
findings carry **batch-local identifiers** (`F-batch-1`, `F-batch-2`, …
sequential within the return); intra-batch cross-references use these
batch-local forms. The orchestrator maps batch-local to run-global
identifiers at append, re-targeting intra-batch cross-references. A
return-state finding carrying a run-global identifier is a malformed
artifact — return-state cannot know the run-global namespace. The
append-only model (`tracker.md`) is preserved without concurrency
machinery.

## Loopback across the subagent boundary

A subagent surfacing any actioned finding halts and returns a
loopback-required result with four fields:

- **trigger** — the artifact, site, or signal the subagent encountered
- **scope** — what's outside the locked design (specific element,
  contract, or behavior)
- **basis** — the re-runnable search or read that surfaced it (per the
  basis rule, `foundations.md`)
- **affected_decisions** — locked design decisions invalidated or
  extended (cited by tracker identifier)

On receiving it, the orchestrator halts other in-flight parallel
subagents and audits the work-state at halt. **Parallel-completed
units** (saved before the halt arrived) are audited by **enumerated set
intersection** against the new finding:

- **decision intersection** — does the unit's implemented decision set
  (D# identifiers cited by its impl plan entry) overlap the new
  finding's `affected_decisions`?
- **element/contract intersection** — does the unit's listed element +
  contract scope (from its impl plan entry's parallel-eligibility scope)
  overlap the new finding's `scope` field (named elements, contracts, or
  behaviors — a behavior resolves to its implementing element)?

Empty intersection on both → preserve the save and tracker entry.
Non-empty intersection on either → revert (the save discarded, tracker
entry moved to [INVALIDATED]). **Halted subagents' unsaved work** in
their working copy is preserved for redo inheritance — the new
investigate-design cycle reads it alongside the tracker, and the
redesign may incorporate, audit, or discard. Tracker state is preserved
across all cases. The run returns to investigate-design with the
four-field result feeding the new cycle.

On loopback, the impl plan is invalidated: a new plan is produced after
the next [READY], reflecting any changes to the locked design.

## Checkpoint

On completion a dispatch unit's integrated changes are durably **saved**
per touched container, and the orchestrator appends its **persistence
reference** (the integrated changes' commit reference per touched
container) to the tracker. The save plus tracker line is the unit's
persistence artifact: a run interrupted mid-implement resumes from the
tracker — the last-completed unit, the next per the impl plan (see
`SKILL.md`, Run lifecycle). The tracker records each unit's completion
via its persistence reference; resume reads the tracker from the
run-state repo and the recorded per-container references — it does not
re-derive work-product state by scanning every repo.

Without a per-unit save-point, resume must re-derive from work-product
state — a silent-substitution shape this rule closes.

## Completion

Report completion when every unit in the impl plan is completed. The
implement → verify transition is not gated: verify is itself the check
on implement, so an incomplete implementation surfaces as verify
findings — it does not pass silently.
