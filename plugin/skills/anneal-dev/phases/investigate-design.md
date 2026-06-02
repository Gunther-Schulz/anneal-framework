# investigate-design

The first phase of an anneal-dev run: a loop of cycles that builds an
understanding of the task and the rule-corpus and produces a locked
design. It ends at [READY].

## The cycle

investigate-design runs as a loop of cycles. Each cycle has two
passes, in order:

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
first, not only when something feels off.

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
  basis-naming for design-decision premises).

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
which is the failure shape that allows false-[READY]s (V-5 in
`anneal-framework/dev-notes/validation-watch.md`). Without the result
line itself, the closed-artifact form (`SKILL.md`) is also malformed
and the [READY] declaration unenforced. The result line is recorded in
the tracker for post-run review in both modes.

### Convergence cycle requirement

**[READY] requires a convergence cycle.** After the working context
judges the supporting facts above met and the fresh-session
implementability test produces a PASSED artifact, the [READY]
declaration requires one more cycle — a **convergence cycle** — to
produce **zero D-track deltas** (no new design decisions, no amendments
to existing ones).

A convergence cycle is a full cycle (investigation pass + standardized
inspection pass + falsification pass over [VERIFIED] decisions; see
Falsification pass below), not a final lens application on accumulated
state. Its investigation pass must enumerate **new surfaces
investigated this cycle**, where each surface is **new** by at least one
of: (a) cites a file path not in any prior cycle's artifact this run;
(b) cites a search query whose query string differs verbatim from every
prior cycle's; (c) cites a located read covering at least one location
not covered by any prior cycle's citation of the same source. A
convergence cycle that produces no new-surface citations (only
re-attestations of prior surfaces) is a malformed artifact.

**Falsification pass.** Iterates each [VERIFIED] D-entry at the
convergence cycle's start. Entries still [CONDITIONAL] or
[AUTO-ACCEPTED] rest on an unverified assumption and are **not**
falsified textually here — that assumption is discharged by verify
(`verify.md`) exercising the work, per `references/foundations.md`
(Replacement, removal, or amendment). The pass is **dispatched to a
fresh-context subagent**, applying the separate-checker requirement
from `references/foundations.md` — an artifact produced and judged in
the same context is not self-enforcing. The subagent is briefed per the
Falsification dispatch-brief template below: it loads the
orchestrator's skill files, reads the tracker reduced-to-latest
projection, and iterates each [VERIFIED] D-entry. For each, the
subagent names a search or read whose positive result would invalidate
the entry's basis, runs it, and cites the result. The subagent returns
the artifact and does not initiate further dispatches. Produces a
per-decision artifact (`references/tracker.md` The falsification-pass
artifact): one line per [VERIFIED] entry carrying a **candidate set** —
one candidate per coupling shape the basis depends on
(`anneal-framework/spec/glossary.md` Coupling shape; closed set:
**target-existence** / **target-dependents** / **target-behavior**).
Each candidate is tagged with its shape and carries a **falsification
predicate** — the rule the orchestrator applies to the candidate's
result to compute holds-or-falsified (closed set per
`references/tracker.md` The falsification-pass artifact:
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
The falsification-pass artifact; shape-coherent for the candidate's
tagged shape), a result field, and a per-candidate holds-or-falsified
value; (iii) the orchestrator computes the per-candidate
holds-or-falsified by applying the predicate to the result, and the
returned value must match the computed value (a mismatch is a malformed
line); (iv) the line's aggregate-holds-or-falsified equals the
conjunction of per-candidate holds. A missing line OR a
mechanically-malformed line is a malformed return; the orchestrator
re-dispatches with the gap's D-entry IDs explicit, and the subagent
fills the gap. All checks are computed from the artifact. **Residual
delegation** — whether the candidate set's shape coverage matches the
basis's claimed shapes (`references/tracker.md` The falsification-pass
artifact) — is the subagent's responsibility per the Falsification
dispatch-brief template (d); per-candidate falsifying capability is now
mechanical (predicate-applied-to-result; no subagent judgment).

**Isolation fallback.** If an isolated context cannot be established
(subagent spawn fails), the falsification pass is conducted in the
working context per the rules above and the artifact records "without
isolation" — the spawn-fallback; an un-isolated falsification pass is
never silently taken as though it were independent (parallel to
`phases/verify.md` §Isolation).

If the convergence cycle surfaces D-track deltas (new decisions,
amendments, or falsified [VERIFIED] entries reopened), the design is
not [READY]: the deltas feed into the next cycle and the loop
continues. [READY] is presented only after a convergence cycle is
observed clean. The convergence cycle's outputs (investigation pass
artifact + falsification pass artifact + zero-D-delta status) form part
of the [READY] artifact alongside the fresh-session result line.

The convergence cycle's role in closing the false-[READY] failure shape
is recorded in V-5 (`anneal-framework/dev-notes/validation-watch.md`).

The convergence cycle fires in both modes (interactive and
auto-battle). In auto-battle no operator override is available; the AI
cycles until convergence is observed, then proceeds.

### Falsification dispatch-brief template

Sections (a) and (d) live here and the subagent reads them on dispatch.
Per-dispatch briefs carry only per-dispatch parameters (b) and (c) —
the brief MUST NOT restate (a) or (d) content; it references them by
section letter only.

**(a) Load instructions** (uniform across falsification dispatches in
this run): the dispatched subagent reads, in order,
`references/foundations.md`, `references/tracker.md`, and this file
(`phases/investigate-design.md`).

**(b) Tracker reference**: the tracker reduced-to-latest projection
(`references/tracker.md` Persistence, reduce-to-latest); the raw
tracker remains accessible to the subagent for ledger-history
inspection.

**(c) Unit scope**: the [VERIFIED] D-entry set at the convergence
cycle's start, cited by tracker D# identifiers.

**(d) Return-state expectations**: the per-decision falsification-pass
artifact (`references/tracker.md` The falsification-pass artifact) —
one line per [VERIFIED] entry carrying a candidate set in
`{decision-ID, [{shape, candidate, falsification-predicate, result, holds-or-falsified}, …], aggregate-holds-or-falsified}`
shape; coverage-checked by the orchestrator on return (Coverage check
on return above). Per-candidate falsification-predicate is from the
closed set (`references/tracker.md` The falsification-pass artifact) and
shape-coherent for the candidate's tagged shape; per-candidate
holds-or-falsified is orchestrator-computed by applying the predicate to
the result (the subagent declares the predicate; the subagent does not
judge holds-or-falsified). Candidate-set shape coverage must match
every coupling shape the basis claims to depend on
(`anneal-framework/spec/glossary.md` Coupling shape) — this remains the
subagent's responsibility.

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
