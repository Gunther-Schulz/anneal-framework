# The tracker

The structured state record of an anneal-dev run — its findings and
design decisions, each carrying a status tag. investigate-design
produces the tracker, implement works from it, verify records its
results into it. It carries the run's state across phases: a run
interrupted mid-flight resumes from the tracker.

## The two tracks

A status tag records the state of a **finding** or a **design decision**
— the tracker's two tracks. Three tags appear in both, track-scoped, one
consistent sense each: **[PENDING]** (recorded, not yet at a terminal),
**[VERIFIED]** (a verified terminal), **[INVALIDATED]** (a verified
terminal contradicted by later evidence). The full state machine —
every state and transition for both tracks — is in `foundations.md`
(The status-state machine); this file carries the tracker artifact
shape and how the tags appear on ledger lines.

Each tracker entry — finding or design decision — is a **fixed-shape
ledger line**: a status tag, a summary, and an evidence-or-basis field,
and **nothing else**. The evidence-or-basis field holds a basis-rule
artifact (`foundations.md`) — a located read of the rule-text, or, for a
completeness claim, the re-runnable wrap-tolerant search behind it (the
executable query, not the count it returned) — **not prose describing
one**: a free-text account of having looked is not a basis
(`foundations.md`), and neither is a bare count with no query behind it
— in a tracker entry, each is a malformed field. The summary is one
sentence by default; multi-sentence is permitted where each additional
sentence carries a cited rationale or premise (the basis-rule discipline
applies within the summary, not only at the basis field). An entry has
**no narrative field**: floating uncited reasoning does not belong in
the tracker — the tracker is the run's ledger, not its design narrative.
**Derivation walk-throughs** — multi-step prose tracing *how* a
conclusion follows from citations ("the rule at §A cross-references §B,
which restates the closed set at §C, therefore…") — are working context,
not basis: record the conclusion, omit the steps. The standardized-pass
artifact (below) is a separate per-cycle artifact, persisted alongside
the tracker, not part of it.

A design decision may carry, as an optional sub-line under its peer
entry, a structured **considered** field — one line per alternative in
the shape `considered: <alternative> (rejected: <reason>)`. The
rejection reason carries a cited basis (`foundations.md`) where
applicable; loose narrative does not belong here. The field is optional
— fabricating alternatives degrades the ledger. Use it where
alternatives were genuinely weighed and naming them informs a later
reader (the operator at [READY] or post-hoc debugging).

### Findings

A finding is an observation recorded by inspection — a fixed-shape
ledger line: a status tag, a summary of what was found, and its
verification evidence (a basis-rule artifact, `foundations.md`, not
prose). Its state machine — [PENDING] → [PARTIALLY VERIFIED] →
[VERIFIED] (with the closed disposition enum addressed / non-issue /
deferred) → [INVALIDATED], and the F-entry resolution closure — is in
`foundations.md` (Finding states). On a ledger line the [VERIFIED]
disposition is cited as a tagged suffix: `[VERIFIED — <disposition>]`; a
[VERIFIED] without a cited disposition is a malformed artifact. A finding
whose stated content is found inaccurate during verification is
corrected — appended as a new line at its current status (Persistence
below); verification continues.

### Design decisions

A design decision is the AI's resolved choice about what to build — a
**committed position**, including a choice to defer or exclude. As a
fixed-shape ledger line it is a status tag, a summary of the committed
position, and its **basis** (`foundations.md`) — and nothing else. It is
never an open question or a choice posed to the operator: a posed
question is the absence of a resolution and yields no valid artifact
(`foundations.md`), so the design-decision track holds none. The basis
is the evidence the choice rests on — a basis-rule artifact, not prose
describing one — or, where it rests on an assumption, that assumption
named. The basis is mandatory; a decision whose basis is an assumption
cannot reach [VERIFIED]. A decision the operator could resolve is
recorded [CONDITIONAL] — the AI's committed recommendation carrying the
operator-resolvable assumption — never a posed choice; the operator
overrides it free-form from the tracker.

**Body shape.** A design decision body specifies: (a) the **target** —
the element of the rule-text being committed (a rule, a defined term, a
section, a file, or a rendered plugin clause), or a behavior of one; (b)
the **shape** — for a new element, its **contract surface**
(`anneal-framework/spec/glossary.md`; for corpus-evolution: the AI
behavior the rule forces, the evidence-bearing artifact it requires, the
closed set it names, the source clause it renders); for an amendment to
an existing element, the change as a delta against current state; (c)
the **acceptance criteria** — observable conditions for the decision to
count as implemented; (d)
the **side effects and failure modes** — what's observable on success
and at boundaries; (e) the **basis** per `foundations.md` (for amendment
decisions, (e) carries the completeness enumeration of references +
behaviors preserved/dropped; (b) carries the shape of the delta).
**Brevity discipline:** the body covers exactly (a)-(e) above — what a
fresh session needs to implement the decision — and no **realization
output** beyond what the contract surface and its cited sources already
convey. The **realization output** — the element's internal content; for
a rule, the exact sentences — is produced at impl, not recorded in the
design decision body.

The decision's state machine — [OUTLINED] / [PENDING] / [CONDITIONAL] /
[VERIFIED] / [AUTO-ACCEPTED] / [INVALIDATED], the transitions between
them, the amendment-is-contradiction rule, and broken-basis reopening —
is in `foundations.md` (Design-decision states).

## The standardized-pass artifact

Each cycle's standardized inspection pass emits a findings artifact: one
line for each lens whose scope the cycle touched (`lenses.md`) — a
finding, or a one-line cited-clean reason. **Each line cites this-cycle
basis: a this-cycle tracker entry (F# from this cycle's investigation
pass, or D# from this cycle's design work) or a surface (a located read
of the rule-text, a wrap-tolerant search query) introduced in this
cycle. A line whose only basis is prior-cycle entries is malformed — its
lens was not touched this cycle.** A lens out of scope that cycle is not
lined; the standardized set is not re-attested every cycle — it is
accounted for whole once, at [READY].

The artifact is **persisted** and carries its **cycle number** — a
per-cycle run artifact at
`.anneal-dev/runs/<run-name>.cycle-<N>.standardized-pass.md`, kept
alongside the tracker, not filed into it. Persistence is what lets the
working context, at [READY], account for the standardized set whole —
every lens applied in the cycle(s) its scope was touched, the last
cycle's pass clean — without it, that [READY] condition is unauditable.

## The falsification-pass artifact

The convergence cycle's falsification pass
(`phases/investigate-design.md`) emits a per-decision artifact: one line
per [VERIFIED] D-entry at the start of the convergence cycle, carrying a
**candidate set** — one candidate per coupling shape the basis depends
on (`anneal-framework/spec/glossary.md` Coupling shape). Line shape:

`{decision-ID, [{shape, candidate, falsification-predicate, result, holds-or-falsified}, …], aggregate-holds-or-falsified}`

Produced by the fresh-context falsification subagent dispatched per
`phases/investigate-design.md`; the orchestrator coverage-checks the
returned artifact on return (`phases/investigate-design.md` Coverage
check on return).

- **decision-ID** — the D# being attempted.
- **shape** — one of: `target-existence`, `target-dependents`,
  `target-behavior` (closed set per
  `anneal-framework/spec/glossary.md` Coupling shape).
- **candidate** — an executable wrap-tolerant search query or located
  read of the rule-text whose result, applied through the falsification
  predicate, would invalidate the entry's basis on this shape. Form
  follows the basis rule's search-establishment shape (`foundations.md`)
  — the candidate is a search-established artifact, not a recalled
  hypothesis.
- **falsification-predicate** — the rule the orchestrator applies to the
  candidate's result to compute holds-or-falsified. Closed set:
    - `any-match` — any non-empty positive result on the candidate is
      falsifying.
    - `any-outside-scope:<scope>` — any evidence outside the named
      `<scope>` is falsifying; `<scope>` is the instance's
      evidence-locator form (for corpus-evolution: a file path, glob, or
      directory).
    - `expected-match:<pattern>` — the evidence LACKING `<pattern>` is
      falsifying (used when the basis claims something present; absence
      falsifies). `<pattern>` is in the instance's pattern form (a
      literal substring (default), or a regex marked `regex:<expr>`),
      matched accordingly.
  Shape-coherence: `target-dependents` candidates use `any-match` or
  `any-outside-scope`; `target-existence` and `target-behavior`
  candidates use `expected-match` (the basis claims a property present;
  the predicate names what must be in the evidence for the property to
  hold). A predicate not from the closed set, or shape-incoherent for
  its tagged shape, is malformed.
- **result** — the actual output of running the candidate: cited matches
  for a search, content for a read.
- **holds-or-falsified** — binary per-candidate, **computed by the
  orchestrator** by applying the falsification-predicate to the result:
  `holds` if the predicate yields no falsifying evidence; `falsified`
  otherwise. The subagent declares the candidate and predicate; the
  orchestrator computes holds-or-falsified (no subagent judgment).
- **aggregate-holds-or-falsified** — binary per-line, computed from the
  candidate set: `holds` if every per-shape candidate holds; `falsified`
  otherwise. `falsified` flips the entry through
  [INVALIDATED]→[PENDING].

A candidate set whose shape coverage does not include every shape the
basis claims is a malformed line — the basis specifies its shape
dependencies, the candidate set mirrors. Amendment decisions
(Replacement, removal, or amendment — `foundations.md`) always include
target-dependents in the basis's claimed shapes; the candidate set's
target-dependents candidate re-runs that reference enumeration as its
search.

A [VERIFIED] entry without a falsification-pass line at the convergence
cycle is a malformed artifact — the [READY] declaration requires the
pass complete across all [VERIFIED] entries
(`phases/investigate-design.md`).

The artifact is per-cycle, fired only at the convergence cycle (not at
every cycle's standardized pass). Persisted alongside the cycle's
standardized-pass findings at
`.anneal-dev/runs/<run-name>.cycle-<N>.falsification.md`.

## The impl plan

The impl plan is produced at [READY] presentation so the operator sees
the unit list at the decision moment (`SKILL.md` Closed-artifact form,
State summary): dispatch units derived from the locked design,
dependency-ordered, parallel-eligibility marked with a search-established
disjointness basis (`foundations.md`). The plan is persisted alongside
the tracker at `.anneal-dev/runs/<run-name>.impl-plan.md` — kept for the
run's history and for resume. Detail is in `phases/implement.md`.

## [READY]

[READY] is investigate-design's terminal — the point at which the
working context judges the design complete and presents it. The tracker
state it weighs in that judgment: no finding is [INVALIDATED], no
load-bearing finding is left below [VERIFIED], and every design decision
is [VERIFIED] or [AUTO-ACCEPTED] — both modes. [READY] also weighs the
cycle-history conditions specified in the investigate-design phase.

These are the status the tracker carries — a notebook of where each
concern stands — that the AI reads when it judges the design complete
and presents it. They are not gate-conditions a separate evaluation
re-derives. Until they hold, the design is not complete and the loop
continues — the phase is [NOT READY].

## Persistence

Each run has its own tracker — an append-only markdown file under
`.anneal-dev/runs/`, named for the run (`.anneal-dev/runs/<run-name>.md`)
— holding a **header** (the run's status, the current phase, mode, a
one-line task summary) and the two tracks (F-track, D-track), and
**nothing else**. The standardized-pass findings artifact, the
falsification-pass artifact, and the impl plan (above) are persisted
alongside the tracker — per-cycle / per-phase run artifacts — not filed
into it.

**Status** is one of (instance-defined closed enum):

- `IN-PROGRESS` — the run is active in some phase
- `PASSED` — verify terminal, no [ISSUES FOUND]

**Phase** is one of (instance-defined closed enum):
`investigate-design`, `implement`, `verify`.

The header is mutable run-state distinct from the append-only ledger:
updates to header fields at phase transitions or terminal moments
(status `IN-PROGRESS` → `PASSED`, phase investigate-design → implement)
are not edits to ledger lines. Two malformed annotation shapes:
within-field qualifier on a bare enum value (e.g. "PASSED (1st pass)" —
the common-word-qualifier symptom, skill-craft
`references/anti-patterns.md` Naked-judgment); and cross-field
conflation (e.g. "verify PASSED" — embedding the Status value inside the
Phase field, or vice versa).

The tracker is **append-only** at the **ledger** layer. A new entry, and
every later change to an entry — a new status, a corrected summary — is a
new fixed-shape ledger line appended to the file; existing ledger lines
are never edited or rewritten. Each ledger line carries its entry's
identifier (`F1`, `D3`, …); an entry's **current state is its latest
line**. Where current state is needed — at [READY], a resume, verify
(`phases/verify.md`), the convergence-falsification dispatch
(`phases/investigate-design.md`), the closed artifact — read the tracker
**reduced to the latest line per entry**. Appending rather than
rewriting is cheaper — only the new line is written — and the
un-rewritten ledger history is the run's audit trail: no past ledger
line is altered. This holds in both modes.

A **basis-only refinement** on a terminal-status entry ([VERIFIED], or
[AUTO-ACCEPTED] for an auto-battle design decision) — same status and
summary, strengthened basis (a search now grounds what previously rested
on a weaker basis) — is appended as a **sub-annotation** under the
entry, not as a new peer-level ledger line. Format: an indented bullet
beneath the entry's latest peer line, carrying the strengthened basis on
one line — e.g.

```
- D2 [VERIFIED] §3.2 is the sole home of the basis rule — basis: search …
  - basis strengthened (cycle 3): corpus-wide search, F17
```

Reduce-to-latest: an entry's current state is its latest peer-level line
together with any sub-annotations attached. The append-only property
holds — no past line is rewritten, the sub-annotation is itself a new
appended line — preserving the audit trail without the duplicate-line
tax of re-emitting a peer line for an evidence-only update.

**Sub-annotations are scoped to basis-only refinement of the parent
entry's own claim** (same status, same summary, strengthened basis).
Cross-unit observations, recurrence-confirmations (e.g. "the pattern
observed in F-N also appears in Unit X's rule-text"), and findings that
surface a new claim — even one related to or confirming a prior entry —
appear as peer-level F-entries with their own basis, not as
sub-annotations under the related entry. The discriminator: does the new
evidence strengthen the parent's own claim verbatim, or does it
constitute its own observation? Verbatim-strengthening → sub-annotation;
new observation → peer-level entry.

**Run state spans containers.** The corpus is multi-container — a unit's
edits may land across several repos. The run-state directory
`.anneal-dev/runs/` lives in one repo — the repo the operator invoked
the run from — while the work product the run touches spans the repos in
scope. Resume reads the tracker from the run-state repo and the recorded
per-container persistence references; it does not re-derive work-product
state by scanning every repo.

A completed run's tracker file is kept; `.anneal-dev/runs/` accumulates
as the project's anneal-dev history — no run overwrites another.
`.anneal-dev/` is local run state; anneal-dev gitignores it on first
write. The run lifecycle (`SKILL.md`) specifies how a run start finds an
in-progress run to resume (a tracker whose header Status is not
`PASSED`), or opens a fresh tracker.
