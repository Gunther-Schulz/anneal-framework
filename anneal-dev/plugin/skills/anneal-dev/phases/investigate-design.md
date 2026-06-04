# investigate-design

The first phase of an anneal-dev run: a loop of cycles that builds an
understanding of the task and the rule-corpus and produces a locked
design. It ends at [READY].

## The cycle

investigate-design runs as a loop of cycles. A cycle has two passes
by default, in order:

1. **Investigation pass.** Investigate the corpus surfaces the task
   touches — ad-hoc, by a method derived from the task, not a
   prescribed one. The standardized lens set (`lenses.md`) is known
   going in and informs what to attend to, not how to investigate.
   Record every observation as a finding in the tracker.
2. **Standardized inspection pass.** Apply each standardized lens
   whose scope this cycle's investigation touched — incremental, over
   what this cycle produced. **The lens set the pass iterates is
   core ∪ project supplement** per `references/lenses.md` ("Project
   supplements"); supplements load at this dispatch. Malformed
   supplement file = fail-loud halt — the parse error surfaces as a
   tracker finding at the next closed-artifact presentation. Emit the
   standardized-pass artifact (`tracker.md`): one line for each
   in-scope lens — a finding, or a one-line cited reason it is clean.
   **Each line cites this-cycle basis: a this-cycle tracker entry (F#
   from this cycle's investigation pass, or D# from this cycle's
   design work) or a surface (a located read of the rule-text, a
   wrap-tolerant search query) introduced in this cycle. A line whose
   only basis is prior-cycle entries is malformed — its lens was not
   touched this cycle.** A lens out of scope this cycle is not lined;
   the set is not re-attested every cycle — it is accounted for whole
   once, at [READY].

The standardized inspection pass runs every cycle — not only the
first, not only when something feels off. The convergence cycle
(Convergence cycle requirement, below) adds two more passes —
intent-falsification then mechanical falsification — over its
[VERIFIED] decisions.

**Cycle numbering** is continuous across the run. A loopback from a
downstream phase (implement actioned-finding, verify [ISSUES FOUND])
returns to investigate-design at the next cycle number, not at cycle 1.
Each cycle number is unique within the run.

## Design

Across the cycle, form and update design decisions (`tracker.md`) from
the cycle's findings — the design-formation the phase is named for. The
locked design is the body of those decisions; it locks as each reaches
[VERIFIED].

The task may propose a solution, not only state the goal. A proposed
solution is a strong input, not a locked design: that it is the right
solution is a design premise — grounded on evidence like any other
(`foundations.md`), not assumed because the task named it. Investigate
a proposed solution as any other design decision: confirm, sharpen, or
replace it on evidence.

Every design decision the task raises is **self-resolved**. For each
one:

- [ ] Is this decision recorded in the tracker as a committed
  resolution — a chosen direction with its basis (`foundations.md`)?
  - NO → CANNOT proceed. Resolve per `tracker.md` §Design-decisions
    (posed choices yield no valid artifact); commit to a
    recommendation, record it with its basis.
  - YES → Evidence: the tracker entry, its committed resolution, and
    its basis.

Do not pose design decisions to the operator as choices to make. A
choice to defer, exclude, or not act is itself a committed decision —
"defer X, because Y" is recorded with its basis, not left as an
absence.

A decision that rests on an assumption — including one only the
operator could confirm — is still committed, not posed: record it
[CONDITIONAL], the AI's committed recommendation carrying the
operator-resolvable assumption as its named basis (`foundations.md`).
At [READY], a [CONDITIONAL] decision still resting on its assumption
becomes [AUTO-ACCEPTED] (triggers + semantics per `tracker.md`). The
operator, seeing the recorded decisions in the tracker, retains
free-form override at any point — but the AI never substitutes a posed
menu for a committed decision.

**Committed recommendations default to the thorough-fix shape** — the
option that addresses the situation at its actual scope, not pre-clipped
on perceived cost. Cost is the operator's judgment
(`foundations.md` Recommendation discipline).

## Scope

The scope — the set of spots encoding the contract being changed,
across the whole corpus (every file/section/clause that states,
cross-references, depends on, or RENDERS the contract) — is the
foundational design decision. Establish it first; every other decision
is designed within it. By the basis rule (`foundations.md`) the scope
is a completeness claim: its basis is a **wrap-tolerant search across
the whole corpus** for every spot encoding or cross-referencing the
contract — distinctive single tokens, or newline-flattened input,
because prose wraps across lines and a multi-word pattern can split
mid-match — not a recalled model of the corpus. It reaches [VERIFIED]
only when search-established. When a later cycle grows the set of
intended targets, the scope decision re-opens and is re-searched.
Because [READY] requires every design decision [VERIFIED] or
[AUTO-ACCEPTED] — both modes — an unestablished scope, at neither,
holds the phase at [NOT READY].

## Requirements record

investigate-design captures the original task requirements as a tracked
artifact. The operator's request sets the task and may propose a
solution (Design, above), and the record enumerates the requirements —
the goal — as R1..Rn, **separated from any solution the operator's
request proposes**. The operator's **verbatim request** is captured
alongside the enumeration, in the same artifact. The record is
**header-adjacent** in the tracker — a task-input, not a third track
(the tracker holds exactly two: F-track, D-track) — extending the
header's one-line task summary (`references/tracker.md` Persistence),
and is persisted so the isolated verify reads it (`phases/verify.md`;
verify needs nothing from the run's conversation, where the raw request
otherwise lives). What counts as a requirement, and how it is elicited,
is instance-defined — as the work product and the domain's executable
verification (`phases/verify.md`) are.

## [READY]

### Judgment criteria

[READY] is reached when the working context judges the design complete
— every concern resolved, every design decision at its terminal, and
the last cycle's standardized inspection pass producing no load-bearing
finding. The supporting facts are recorded across the run:

- **Standardized coverage** — the standardized lens set is accounted
  for whole: every lens applied in the cycle(s) where its scope was
  touched, or carrying a cited reason it was out of scope for the run;
  no lens silently absent; the last cycle's pass left no load-bearing
  finding.
- **Tracker state** — no finding is [INVALIDATED], no load-bearing
  finding is below [VERIFIED], every design decision is [VERIFIED] or
  [AUTO-ACCEPTED] (`tracker.md` — triggers per §Design-decisions); and
  every [VERIFIED] design decision's embedded target-naming and count
  premises carry a re-runnable basis (per `references/foundations.md`
  basis-naming for design-decision premises). The convergence cycle's
  intent-falsification findings (Convergence cycle requirement, below)
  must be **dispositioned, not the pass silent**: mechanically-confirmable
  findings resolved, pure-judgment findings terminal at
  [VERIFIED — surfaced] (`references/foundations.md` Finding states); a
  [VERIFIED — surfaced] finding is terminal and does not hold the phase.

These are the status the tracker carries — a notebook of where each
concern stands — that the AI reads when it judges the design complete.
They are not gate-conditions a separate evaluation re-derives.

The supporting facts above check that everything *recorded* is at
terminal. The judgment must also test whether the recording is
*complete*. The strongest single test is **fresh-session
implementability**: would a session with only the tracker (no chat
context, no current-session memory) implement the design without
surfacing a new design decision? If not, another cycle is warranted
regardless of recorded statuses.

### Artifact-produced result line

**[READY]'s judgment is artifact-produced.** The fresh-session
implementability test above produces a named result line in the closed
artifact at [READY] presentation: PASSED with **per-implementer-step
external evidence** — for each step a fresh implementer would take to
carry out the locked design, cite the basis form per the basis rule
(`foundations.md`): citation + observable fact for a located read of
the rule-text; executable query with output for a wrap-tolerant search.
Or FAILED with the specific gap identified. PASSED without per-step
external citation is a malformed artifact: the test answers from the
recall pool that wrote the design rather than from external evidence,
which is the failure shape that allows false-[READY]s. Without the
result line itself, the closed-artifact form (`SKILL.md`) is also
malformed and the [READY] declaration unenforced. The result line is
recorded in the tracker for post-run review in both modes.

### Convergence cycle requirement

**[READY] requires a convergence cycle.** After the working context
judges the supporting facts above met and the fresh-session
implementability test produces a PASSED artifact, the [READY]
declaration requires one more cycle — a **convergence cycle** — to
produce **zero D-track deltas** (no new design decisions, no amendments
to existing ones).

A convergence cycle is a full cycle (investigation pass + standardized
inspection pass + intent-falsification pass + mechanical falsification
pass over [VERIFIED] decisions; see Intent-falsification pass and
Mechanical falsification pass below), not a final lens application on
accumulated state. The two falsification-style passes are **sequenced**,
not run unconditionally-both: the intent-falsification pass runs
**first**; if it produces a D-track delta the mechanical falsification
pass is **skipped** that cycle (the design is about to change, so the
mechanical run would be stale) and the cycle records "mechanical
skipped: intent-delta this cycle" (the skip carve-out that reconciles
`references/tracker.md` The mechanical falsification-pass artifact's
no-line-malformed rule for that cycle). Only when the
intent-falsification pass comes up clean does the mechanical
falsification pass run. The re-trigger reuses the behavior-preserving
classification (`phases/verify.md`): a behavior-preserving mechanical
fix does not re-open the intent-falsification pass (the design's
character is unchanged, so the intent-clean result carries forward); a
non-behavior-preserving mechanical fix re-opens it. Its investigation
pass must enumerate **new surfaces
investigated this cycle**, where each surface is **new** by at least one
of: (a) cites a file path not in any prior cycle's artifact this run;
(b) cites a search query whose query string differs verbatim from every
prior cycle's; (c) cites a located read covering at least one location
not covered by any prior cycle's citation of the same source. A
convergence cycle that produces no new-surface citations (only
re-attestations of prior surfaces) is a malformed artifact.

**Mechanical falsification pass.** Iterates each [VERIFIED] D-entry at the
convergence cycle's start. Entries still [CONDITIONAL] or
[AUTO-ACCEPTED] rest on an unverified assumption and are **not**
falsified textually here — that assumption is discharged by verify
(`verify.md`) exercising the work, per `references/foundations.md`
(Replacement, removal, or amendment). The pass is **dispatched to a
fresh-context subagent**, applying the separate-checker requirement
from `references/foundations.md` — an artifact produced and judged in
the same context is not self-enforcing. The subagent is briefed per the
falsification dispatch-brief template below: it loads the
orchestrator's skill files, reads the tracker reduced-to-latest
projection, and iterates each [VERIFIED] D-entry. For each, the
subagent names a search or read whose positive result would invalidate
the entry's basis, runs it, and cites the result. The subagent returns
the artifact and does not initiate further dispatches. Produces a
per-decision artifact (`references/tracker.md` The mechanical
falsification-pass artifact): one line per [VERIFIED] entry carrying a
**candidate set** —
one candidate per coupling shape the basis depends on
(`anneal-framework/spec/glossary.md` Coupling shape; closed set:
**target-existence** / **target-dependents** / **target-behavior**).
Each candidate is tagged with its shape and carries a **falsification
predicate** — the rule the orchestrator applies to the candidate's
result to compute holds-or-falsified (closed set per
`references/tracker.md` The mechanical falsification-pass artifact:
`any-match` / `any-outside-scope:<scope>` / `expected-match:<pattern>`).
The line aggregates to `holds` only if every per-shape candidate holds.
The candidate's falsifying-capability check is mechanical — the
predicate specifies what positive result on this candidate falsifies
the basis on the tagged shape; the orchestrator applies the predicate
to the result and computes holds-or-falsified (no subagent judgment). A
candidate with a malformed predicate (not from the closed set, or
shape-incoherent for its tagged shape — e.g., a `target-dependents`
candidate with a predicate referencing no scope) is malformed. A
candidate set whose shape coverage does not include every shape the
basis claims is also malformed. A [VERIFIED] entry whose
aggregate-holds-or-falsified is `falsified` flips through
[INVALIDATED]→[PENDING] (per `references/tracker.md` Design decisions)
and the cycle continues.

**Coverage check on return.** The orchestrator counts the returned
artifact's lines against the [VERIFIED] D-entry set at the convergence
cycle's start AND checks each line's mechanical form: (i) candidate set
non-empty, (ii) each candidate carries a shape tag from the closed set
(`anneal-framework/spec/glossary.md` Coupling shape), a candidate field
(a located read or re-runnable query per `references/foundations.md`),
a falsification-predicate from the closed set (`references/tracker.md`
The mechanical falsification-pass artifact; shape-coherent for the
candidate's tagged shape), a result field, and a per-candidate
holds-or-falsified value; (iii) the orchestrator computes the per-candidate
holds-or-falsified by applying the predicate to the result, and the
returned value must match the computed value (a mismatch is a malformed
line); (iv) the line's aggregate-holds-or-falsified equals the
conjunction of per-candidate holds. A missing line OR a
mechanically-malformed line is a malformed return; the orchestrator
re-dispatches with the gap's D-entry IDs explicit, and the subagent
fills the gap. All checks are computed from the artifact. **Residual
delegation** — whether the candidate set's shape coverage matches the
basis's claimed shapes (`references/tracker.md` The mechanical
falsification-pass artifact) — is the subagent's responsibility per the
falsification dispatch-brief template (d); per-candidate falsifying
capability is now mechanical (predicate-applied-to-result; no subagent
judgment).

**Isolation fallback.** If an isolated context cannot be established
(subagent spawn fails), the pass — mechanical or intent-falsification —
is conducted in the working context per the rules above and the
artifact records "without isolation" — the spawn-fallback; an
un-isolated pass is never silently taken as though it were independent
(parallel to `phases/verify.md` §Isolation).

**Intent-falsification pass.** A pure judgment surfacer: a
fresh-context, **criteria-first** adversarial attack on whether the
locked design **serves its intent**, against the requirements record
(Requirements record, above) — distinct from the mechanical
falsification pass, which attacks each [VERIFIED] D-entry's basis.
Criteria-first means the subagent derives the success criteria from the
requirements record **before** reading the design — the independence
lever; the design is the attack's target, not its criteria source. It
is **dispatched to a fresh-context subagent** (the same separate-checker
requirement, `references/foundations.md`), briefed per the
falsification dispatch-brief template below, and produces the
intent-falsification artifact (`references/tracker.md` The
intent-falsification-pass artifact): a per-R# attack line per
requirement (every requirement attacked, so a clean pass is
**evidenced** clean, not asserted — an anti-flood and audit-trail bound,
not rubber-stamp prevention) plus a per-finding line. The intent-model
is the captured requirements record; a requirement never captured there
is invisible to the pass (the never-captured-requirement residual,
reduced by verify's requirements-coverage check (`phases/verify.md`),
not eliminated).

Each finding **routes** by whether a runnable check exists:

- A concern that **reduces to a coupling-shape falsification of a
  [VERIFIED] D-entry's basis** (`references/tracker.md` The mechanical
  falsification-pass artifact) is a **mechanically-confirmable** finding:
  it is formatted as a candidate + closed predicate and the orchestrator
  computes the verdict (no subagent judgment, per the mechanical pass
  above); a confirmed flaw flips the affected [VERIFIED] entry through
  [INVALIDATED]→[PENDING] (`references/tracker.md` Design decisions) and
  the cycle continues — this is the **intent-delta** that **skips** the
  mechanical pass that cycle (recorded "mechanical skipped: intent-delta
  this cycle"). A runnable-but-not-coupling-shape concern (e.g. an
  edit-set that includes a render path a requirement forbids) does not
  force a cycle this way — its input shape is the mechanical
  falsification-pass line, not "any runnable check" — and is recorded
  `surfaced` like any judgment concern.
- A **pure-judgment** concern with **no such reduction** is recorded on
  the F-track as **[VERIFIED — surfaced]** (`references/foundations.md`
  Finding states) — terminal, surfaced for the operator's never-required
  review, never blocking the phase and never a loopback. The dodge-down
  vector (classify a checkable concern as judgment to skip the cycle) is
  judgment-adjacent but backstopped by the next cycle's fresh-context
  re-spawn (operator-independent), which re-attacks the same design.

**The operator-independence boundary.** The pass's value is
operator-**independent**: it force-fixes the checkable concerns (the
mechanical-falsification route — the teeth) and honestly records the
judgment residual ([VERIFIED — surfaced]), neither waiting on the
operator. The recorded residual **feeds** the operator's soundness pass
— for a method-kernel edit that is the kernel-mandated step-4 soundness
verdict (`anneal-framework/development-process.md`), originated by the
operator via the permitted [READY]/`next phase` menu selection (not a
forbidden operator-detection); for an instance run there is no such
required gate (the residual is honest-record-for-review, the
[AUTO-ACCEPTED] contract). The pass **feeds** that gate; it never
becomes it or depends on it, and introduces no forbidden
operator-detection-as-enforcement. A clean intent-falsification pass is
**not a soundness certificate**: for a method-kernel edit the operator's
design-vs-intent soundness verdict is irreducible; the pass feeds it,
never replaces it.

If the convergence cycle surfaces D-track deltas (new decisions,
amendments, or falsified [VERIFIED] entries reopened), the design is
not [READY]: the deltas feed into the next cycle and the loop
continues. [READY] is presented only after a convergence cycle is
observed clean — for the intent-falsification pass, **clean means its
findings are dispositioned, not the pass silent**: every
mechanically-confirmable finding resolved (the affected entry
re-[VERIFIED] across a cycle, bounded by the zero-D-delta convergence)
and every pure-judgment finding terminal at [VERIFIED — surfaced]. A
perpetually-skeptical pass converges: its surfaced concerns terminate
and accumulate in the record; only an open mechanically-confirmable
finding holds the phase, so the cycle cannot loop forever on judgment
surfacing. The convergence cycle's outputs (investigation pass
artifact + intent-falsification pass artifact + mechanical
falsification pass artifact, or its recorded skip + zero-D-delta status)
form part of the [READY] artifact alongside the fresh-session result
line.

The convergence cycle fires in both modes (interactive and
auto-battle). In auto-battle no operator override is available; the AI
cycles until convergence is observed, then proceeds.

### Falsification dispatch-brief template

Sections (a) and (d) live here and the subagent reads them on dispatch.
Per-dispatch briefs carry only per-dispatch parameters (b) and (c) —
the brief MUST NOT restate (a) or (d) content; it references them by
section letter only.

This template covers both falsification dispatches — the **mechanical
falsification** dispatch and the **intent-falsification** dispatch. (a)
and (d) are uniform within each dispatch kind; (b) and (c) carry the
per-dispatch parameters, with a mechanical variant and an
intent-falsification variant noted below.

**(a) Load instructions** (uniform across falsification dispatches in
this run): the dispatched subagent reads, in order,
`references/foundations.md`, `references/tracker.md`, and this file
(`phases/investigate-design.md`).

**(b) Tracker reference**: the tracker reduced-to-latest projection
(`references/tracker.md` Persistence, reduce-to-latest); the raw
tracker remains accessible to the subagent for ledger-history
inspection. For the **intent-falsification** dispatch, (b)
**additionally** carries the **requirements record** (Requirements
record, above — the criteria source the subagent derives criteria from
before reading the design).

**(c) Unit scope**: for the **mechanical falsification** dispatch, the
[VERIFIED] D-entry set at the convergence cycle's start, cited by
tracker D# identifiers. For the **intent-falsification** dispatch, the
locked [VERIFIED] design (the D-entry set the pass attacks
holistically) plus the requirements record R1..Rn (Requirements
record, above).

**(d) Return-state expectations**:

- For the **mechanical falsification** dispatch: the per-decision
  mechanical falsification-pass artifact (`references/tracker.md` The
  mechanical falsification-pass artifact) — one line per [VERIFIED]
  entry carrying a candidate set in
  `{decision-ID, [{shape, candidate, falsification-predicate, result, holds-or-falsified}, …], aggregate-holds-or-falsified}`
  shape; coverage-checked by the orchestrator on return (Coverage check
  on return above). Per-candidate falsification-predicate is from the
  closed set (`references/tracker.md` The mechanical falsification-pass
  artifact) and shape-coherent for the candidate's tagged shape;
  per-candidate holds-or-falsified is orchestrator-computed by applying
  the predicate to the result (the subagent declares the predicate; the
  subagent does not judge holds-or-falsified). Candidate-set shape
  coverage must match every coupling shape the basis claims to depend on
  (`anneal-framework/spec/glossary.md` Coupling shape) — this remains the
  subagent's responsibility.
- For the **intent-falsification** dispatch: the intent-falsification-
  pass artifact (`references/tracker.md` The intent-falsification-pass
  artifact) — a per-R# attack line per requirement (every requirement in
  the requirements record attacked) plus a per-finding route line whose
  `route` is from the closed set
  {`mechanical-falsification-candidate`, `[VERIFIED — surfaced]`};
  coverage-checked by the orchestrator on return (an R# without an
  attack line, or a route outside the closed set, is malformed).

### Cycle-another recommendation

The AI recommends cycle-another whenever the fresh-session
implementability test fails, or a lens in scope was not applied in the
cycle that touched its scope. Cost-asymmetry does not enter the
recommendation; per `foundations.md` Recommendation discipline, the
operator judges cost. **The recommendation's justification enumerates
observations** — open findings, [PENDING] decisions, lens-applications
still required, fresh-session-implementability gaps — not costs
(effort, budget, time, "cheaper than"). A justification framed in cost
comparison is malformed.

At [READY] the AI does not certify itself ready: it presents the design
— the tracker, the recorded design decisions, the
fresh-session-implementability result line, and a recommendation — for
the operator's judgment. The cycle-history facts (the standardized lens
set accounted for whole; the last cycle's pass clean) are part of what
is presented and weighed, not a self-passed gate. The operator's
selection of `next phase` is the transition to implement; until the
operator selects it, the phase continues and the loop may run further
cycles.

Until the working context judges the design complete, the phase is
[NOT READY] and the loop continues — another cycle.

## Advancing the loop

In **interactive** mode the operator advances the loop: after each
cycle, present the tracker — its findings and recorded design decisions
— with a recommendation, and the operator selects from the menu
(`another cycle` or `next phase`) or overrides free-form. In
**auto-battle** mode the loop self-advances (`SKILL.md` Modes —
auto-battle is interactive minus the operator). In either mode the
operator, seeing the recorded decisions, retains free-form override at
any point.

In interactive mode the menu persists (`SKILL.md` Modes — menu
persistence + interjection handling).
