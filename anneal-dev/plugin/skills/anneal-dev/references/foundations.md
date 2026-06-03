# Foundations

The model, the grounding discipline, the status-state machine, and the
orchestrator essentials the phases rest on. anneal-dev loads this
reference at activation, before any phase runs.

## Purpose

anneal-dev exists to secure two things in the AI's work — the rubric
every prescription is judged against:

1. **Grounded claims.** No assertion without its basis. Every
   load-bearing claim is backed by evidence or explicitly marked as
   inferred.
2. **A coherent, complete picture.** Every concern is held, visible,
   and carries a state. A superseded aspect is reconciled or
   invalidated, never silently dropped.

Human inspectability is a constraint, not a primary value: artifacts
must stay cognitively palatable rather than bloating into detail too
large to hold.

## The model

A run proceeds through three phases in sequence: **investigate-design**
(a loop of cycles that builds understanding of the task and the
rule-corpus and produces a locked design; ends at [READY], when the
operator, presented the design, selects `next phase`), **implement**
(carries out the locked design, producing the rule-text), and
**verify** (checks the produced rule-text against the locked design and
the standardized lenses). The tracker carries state across the phases:
investigate-design produces it, implement works from it, verify records
its results into it. An orchestrator conducts the run (§Orchestrator).

A run is driven in one of two **modes**: **interactive** (the operator
advances the loop and selects at menus) or **auto-battle** (the loop
self-advances without per-cycle operator input). A run is interactive
by default; auto-battle only when explicitly requested at invocation.

The AI self-resolves every design decision and records it as a tracked
design decision with its basis — visible, never silent. **Committed
recommendations default to the thorough-fix shape — the option that
addresses the situation at its actual scope, not pre-clipped on
perceived cost. Cost is the operator's judgment.** "Defer X, because Y"
is itself a recorded decision, not an absence. A decision resting on an
assumption — including one only the operator could confirm — carries
that assumption as its basis and is recorded [CONDITIONAL]. The
operator retains free-form override at any point.

**Operator-expected action bound.** The operator's protocol-expected
actions are bounded to (a) **menu selection** at closed-artifact
presentations and (b) **free-form interjection** (question, comment, or
override against the tracker). Auto-battle removes (a) and (b) entirely.
The protocol does NOT design AI behavior expecting operator detection,
inspection, sanity-check, audit, or any other operator-active work
beyond (a)/(b). Where an artifact's enforcement would otherwise require
operator-detection, the enforcement form is malformed — AI discipline
or a fresh-context checker (verify, the convergence cycle) carries it.

The operator's request sets the task; it may also propose a solution.
Such a proposal is a strong input, not a locked design: that it is the
right solution is a design premise — grounded on evidence like any other
(basis rule below), not assumed because the operator proposed it. The AI
investigates the proposal as it would any design question — confirming,
sharpening, or replacing it on evidence.

## Recommendation discipline

Every design decision the AI commits — every closed-artifact
recommendation, every menu's next-step proposal, every [CONDITIONAL]
default-take — defaults to the **thorough-fix shape**: the option that
addresses the situation at its actual scope, not pre-clipped on
perceived cost. Cost is the operator's judgment (`tracker.md` carries
the mode-specific surfacing mechanics).

This is the structural enforcement on what goes IN every recorded design
decision (`tracker.md`) and every recommendation in the closed artifact
(`SKILL.md`): the artifact's content is thorough-fix-shaped, not
cost-clipped. A cost-clipped recommendation is a malformed artifact.

## Inspection

anneal-dev's one reusable mechanism is **inspection**: it looks through
a lens at the rule-text and the work produced so far, and yields a
finding when the lens catches something, nothing when it does not. Its
lens is **ad-hoc** — derived from the task, situationally; covers the
task-obvious, bounded by what the AI thinks to look for — or
**standardized**: pre-written in the protocol, the recurring corpus-
evolution blind spots, applied not derived (`lenses.md`).

A standardized lens is specified by the lens-entry shape — its Name, the
Question it asks, and its Scope, which carries the trigger that brings it
into a cycle (`lenses.md`).

The run's phase transitions — investigate-design's end at [READY], the
loopbacks — are not mechanisms of this kind. They are not a mechanical
check on accumulated state; they are governed by the phase procedures
and the run pipeline (`SKILL.md`), where what each transition requires
is specified directly.

## The evidence-bearing-artifact rule

Every load-bearing artifact the protocol requires — a mechanism's
output, a recorded design decision — must be **evidence-bearing**:
producing it requires doing the work it represents, so a non-adherent AI
cannot produce it by pattern alone. A bare claim — "checked all
dependents" — is satisfiable whether or not the work happened; a located
enumeration — "dependents: [file:section, …]" — is not.

Evidence-bearing is a gradient, not an absolute — no artifact an AI
produces is un-fakeable, since it can fabricate one. An artifact's
strength is how far faking it requires active fabrication rather than
mere omission, and how cheaply a checker catches the fake. A **strong**
artifact points at external, re-checkable truth — a search result, a
located read of the rule-text, an executed battery check's output:
faking it means fabricating something a checker re-runs and catches. A
**weak** artifact is a claim about the run's own state — a status tag, a
self-assessment that work is complete: there is no external truth to
check it against.

- An inspection's finding, or its cited reason that a lens is clean,
  must cite evidence that required looking.
- A design decision's artifact is its committed resolution and its basis
  (basis rule below). An open question, or a choice posed to the
  operator, is the absence of a resolution — so the design-decision
  track cannot hold one.

A weak artifact is not self-enforcing — the protocol cannot rest on the
artifact alone. It is enforced by a **separate checker**: a context that
did not produce the artifact re-derives it (verify's isolated subagent
`phases/verify.md`, the convergence cycle per
`phases/investigate-design.md`). The artifact still earns its place — it
makes faking require fabrication, and gives the checker something
concrete to check — but the guarantee comes from the checker, not the
artifact.

This rule reaches anneal-dev's behavioral rules, not its mechanisms
alone: a rule whose adherence cannot be read off an artifact is not
enforced. A load-bearing rule is specified so that following it produces
an artifact and not following it produces none.

## The basis rule

Every load-bearing claim and every design premise carries a named
**basis** — the evidence it rests on: (a) a **wrap-tolerant search
result with its executable query**, OR (b) a **located read of the
rule-text** — the clause read to its visible close (the full
sentence/paragraph/section the rule lives in, not a fragment) — paired
with **exactly one observable fact** about the cited range (a count, an
enumerated member, the cited identifier) that the citation grounds.
**Cardinality is one per citation** — a citation paired with multiple
stacked facts is malformed. A basis may contain multiple per-citation
pairs when the claim genuinely rests on multiple facts (each pair one
fact per citation); the basis as a whole stays on one entry. A
stacked-fact citation is audited first for over-statement — rationale,
cross-references, or summaries dressed as facts — and reduced to the
actual facts; entry-splitting is required only when multi-fact analysis
reveals multi-claim structure. Verify (`verify.md`) and convergence
cycles re-open each citation to verify both the location AND the
observable fact. A free-text claim of having looked, a paraphrase of
what was read, or a summary without an observable fact is not a basis.

A basis that resolves to recall — "assumed," "inferred," "obviously so"
— or to deferral — "will verify in cycle N," "impl-phase will produce,"
"TBD" — is an **assumption**, not a basis. An assumption does not ground
a decision; it holds the run short of [READY] until converted to
evidence or the operator resolves it. The mechanical tell of a blind
spot is the basis the AI cannot produce.

**Load-bearing** means a claim or premise a design decision, a
recommendation, or [READY] rests on. **Operational test:** the claim is
load-bearing if, were it false, a [VERIFIED] design decision OR the
[READY] declaration changes — testable by naming which D-entry or which
[READY]-supporting fact the claim feeds. A claim with no namable feeder
is not load-bearing. A claim of bounded, contained cost does not carry
the basis apparatus.

The rule rejects **silent substitution**: missing or malformed evidence
defaulted to a plausible proxy that propagates as if it were the basis —
a recalled count where a search is needed, a free-text claim of having
looked, a sampled subset where the whole set is the unit. Surface the
gap, do not substitute.

The rule has two edges — basis-naming and true-unit basis.

### Basis-naming

Every load-bearing claim and every design premise names its basis or
stands as an assumption. This reaches **design premises**, not findings
alone — such as the premise that a clause or term is the work's alone to
change. A design premise with no named basis is an assumption and holds
the run short of [READY] until grounded.

This rule also reaches **claims embedded within larger statements** —
implicit premises in target-naming decisions (file/section/clause),
cited rules or prior decisions, completeness counts asserted as facts.
Each embedded claim carries the basis-rule requirement *separately* from
the surrounding statement: the surrounding claim's basis does not cover
the embedded one. An embedded claim with no separate basis is an
assumption and cannot reach [VERIFIED].

### True-unit basis

A basis must cover the claim's true unit, not a coarser proxy.

- A claim about a **complete set** (a scope, an element's dependents, an
  input's value-classes, a flaw class's instances) has the whole set as
  its unit. Its basis is a corpus-wide wrap-tolerant search recorded as
  the **re-runnable search itself** — the executable query, not the
  count it returned. A search narrowed by where the members are assumed
  to live (to other files, leaving out the file being changed) is a
  declared scope wearing a search's clothing — including a search of
  "everywhere else" that excludes the change site, where co-located
  members hide.
- A claim about a **construct** (a unit of the rule-text that must be
  taken whole) has the whole construct as its unit. Its basis is a read
  to the construct's **visible close** — the syntactic close of the
  rule-bearing unit: the sentence's terminal punctuation, the
  paragraph's blank-line boundary, the section's next-heading boundary,
  or a closed set's final enumerated member — the complete clause, the
  defining sentence of a term, the full enumeration of a closed set, or
  — for an amendment — the rule plus the cross-references that bind to
  it. Not a window that catches part of it.

### Replacement, removal, or amendment

A design decision involving **replacement, removal, or amendment of an
existing artifact** carries an implicit completeness claim: that all
references to (and load-bearing behaviors of) the affected artifact have
been accounted for. Its basis must include the re-runnable search
enumerating references to the affected artifact, AND — for replacements
introducing a successor — an explicit enumeration of behaviors preserved
or dropped at the replacement. A delete/replace/amend decision whose
basis is just "X is replaced by Y" without the references search and
(where applicable) the behavioral-parity enumeration is missing its
true-unit basis; it cannot reach [VERIFIED]. This is the forcing
function for the Missed-dependents lens (`lenses.md`).

A preserved-behavior claim a read cannot exhibit — because the behavior
resolves at render-time through a dependent the reference-search does
not surface (a paraphrase a rendered plugin carries that a corpus search
cannot exhibit) — is not statically dischargeable: it is recorded
[CONDITIONAL], its basis the affected behavior exercised by the domain's
executable verification (the render-fidelity / coherence checks at
verify, `phases/verify.md`), not a read. This is the **target-behavior**
runtime case (the rule's behavior resolving *through* that
render-resolved dependent), the native path for the **target-behavior**
coupling shape (`anneal-framework/spec/glossary.md` Coupling shape). A
static enumeration substituted for it is the silent substitution the
basis rule forbids.

### Secondary sources

A secondary source — a sub-agent report, a prior session's notes, an
audit summary — is not itself a basis. A direct citation it carries (the
artifact's located read with an observable fact) relays the artifact and
can stand as a basis; its interpretation, synthesis, or recommendation
cannot, and is re-grounded against the actual rule-text before anything
rests on it.

### Scope: load-bearing only

Only load-bearing claims and premises carry the basis apparatus; a claim
of bounded, contained cost does not.

## The status-state machine

A status tag records the state of a finding or a design decision. There
are two tracks. ([PASSED] and [ISSUES FOUND] — verify's phase result —
are not a track; they are specified in `phases/verify.md`.)

Three tags appear in both tracks, track-scoped and with one consistent
sense: **[PENDING]** (recorded, not yet at a terminal), **[VERIFIED]** (a
verified terminal), **[INVALIDATED]** (a verified terminal contradicted
by later evidence). The reuse is deliberate — one vocabulary across both
tracks.

### Finding states

A finding — an observation recorded by inspection — moves through:

1. **[PENDING]** — recorded; not yet verified.
2. **[PARTIALLY VERIFIED]** — verification begun but incomplete. A
   finding fully verified in one step moves [PENDING] → [VERIFIED]
   directly; [PARTIALLY VERIFIED] holds a finding whose verification
   spans steps or cycles.
3. **[VERIFIED]** — verification complete: the finding's content is
   established on evidence. A [VERIFIED] tag carries a cited
   **disposition** naming which of three cases applies (closed enum):
   - **addressed** — the cited D# names the same observable behavior the
     finding observes (an element of the rule-text, or its contract
     surface); citation-equivalence is the check.
   - **non-issue** — basis cites (a) a re-runnable search whose result
     is empty, or (b) a located read + observable fact contradicting the
     finding's premise.
   - **deferred** — one of: (a) re-observes a gap an existing
     [AUTO-ACCEPTED] decision deferred (basis cites that decision's
     tracker ID; the finding is appended as a re-surfacing notation
     alongside the original [AUTO-ACCEPTED] tag); or (b) operator-pull
     defer of a load-bearing finding the operator chooses not to act on
     now (basis cites an explicit trigger condition — a named observable
     event class, instance-defined; canonical classes: a file change, an
     executable-verification output class, a named dependency change —
     that would re-fire on the deferred finding; defer-without-trigger
     or trigger-without-observable-class is malformed).

   The disposition is cited as a tagged suffix on the status line:
   `[VERIFIED — <disposition>]`. A [VERIFIED] without a cited disposition
   is malformed. A finding with none of the three dispositions citable
   stays at its prior status; verify then ends [ISSUES FOUND].

   A finding whose stated content is found inaccurate during
   verification is corrected — appended as a new line at its current
   status; verification continues.

4. **[INVALIDATED]** — a [VERIFIED] finding contradicted by later
   evidence. It reopens to [PENDING] for re-verification and holds the
   phase until it does. Only a [VERIFIED] finding becomes [INVALIDATED];
   one contradicted before [VERIFIED] is simply corrected.

**F-entry resolution closure.** F-entries resolve through exactly four
paths: one of the three [VERIFIED — disposition] cases above, or [ISSUES
FOUND] → loopback (`phases/verify.md`). Inline-fix — modifying the
rule-text to address a finding without one of the four resolutions — is
not a path; attempting one is malformed. The closure applies to
F-entries from any source: verify findings, impl-phase self-check
findings, investigation-pass findings.

### Design-decision states

A design decision is the AI's resolved choice about what to build — a
**committed position**, including a choice to defer or exclude. It is
never an open question or a choice posed to the operator: a posed
question is the absence of a resolution and yields no valid artifact, so
the design-decision track holds none. It carries that resolution, a
**basis** (basis rule above) — the evidence the choice rests on, or,
where it rests on an assumption, that assumption named — and a status. A
decision the operator could resolve is recorded [CONDITIONAL] — the AI's
committed recommendation carrying the operator-resolvable assumption —
never a posed choice; the operator overrides it free-form from the
tracker. The basis is mandatory; a decision whose basis is an assumption
cannot reach [VERIFIED].

It moves through:

1. **[OUTLINED]** — a committed direction; concrete detail not yet
   investigated.
2. **[PENDING]** — a concrete decision whose detail still needs
   investigation.
3. **[CONDITIONAL]** — a concrete decision resting on an unverified
   assumption; the assumption is recorded with it.
4. **[VERIFIED]** — a concrete decision, complete and locked, its basis
   evidence, detailed enough that implementing it introduces no new
   design decision.
5. **[AUTO-ACCEPTED]** — a [CONDITIONAL] decision the AI's committed
   recommendation was taken as default when the operator did not
   override: in interactive mode, by the operator selecting `next phase`
   at the closed-artifact presentation without overriding any open
   [CONDITIONAL]; in auto-battle, by the absence of an operator. The
   recommendation stands; the assumption it rested on was not verified —
   [AUTO-ACCEPTED] records exactly that, and does not claim the
   verification that [VERIFIED] does. Both modes reach this state; the
   difference is who-or-what occupies the decision-moment.
6. **[INVALIDATED]** — a [VERIFIED] or [AUTO-ACCEPTED] decision
   contradicted by later evidence.

**Transitions between concrete states.** A [PENDING] decision found to
rest on an unverified assumption becomes [CONDITIONAL]; a [CONDITIONAL]
decision becomes [VERIFIED] when its assumption is verified, and reverts
to [PENDING] if the assumption is disproved. A [CONDITIONAL] decision
still resting on its assumption at [READY] becomes [AUTO-ACCEPTED]
(triggers per #5). An [INVALIDATED] decision reverts to [PENDING], and
any decision that depended on it reverts with it; the phase holds until
re-formed. **Contradiction includes amendment of recorded resolution**
(target naming, scope, completeness counts, basis source); any such
change to a [VERIFIED]/[AUTO-ACCEPTED] decision flips through
[INVALIDATED]→[PENDING] (forces cycle-another). Silent in-place edit
(same status, changed resolution) is a malformed artifact. Basis-only
refinement (`tracker.md` sub-annotation, resolution unchanged) is not
amendment.

A design decision's basis can be broken by another decision, not only by
external evidence. When a decision is locked or its meaning changes,
examine it against the run's other recorded decisions — does it break
what any of their bases rest on. A broken-basis decision is reopened per
the rule above ([INVALIDATED] or revised). The examination is
incremental, not pairwise: the newly locked/changed decision against
existing ones. This holds whether or not the affected decision's
rule-text exists yet — the contradiction is between decisions, not in
the rule-text.

### Relationship to [READY]

The status tags gate [READY] (`phases/investigate-design.md` [READY]):
an [INVALIDATED] finding, a load-bearing finding short of [VERIFIED], or
a design decision short of [VERIFIED]/[AUTO-ACCEPTED] (Design-decision
states above) is an unresolved concern that holds the phase — the loop
continues until it resolves. These are the status the tracker carries,
read at the [READY] judgment (`phases/investigate-design.md` [READY]),
not a gate a separate evaluation re-derives.

## Orchestrator

The orchestrator conducts a run through the phase pipeline. The phases
and the status-state machine define the work and its transitions; the
orchestrator runs the phases in order, holds the transitions, and
manages the run's lifecycle.

- **Run start.** Detects the run's mode and enters investigate-design
  (`SKILL.md` Run start, Run lifecycle).
- **Sequencing and transitions.** Advances investigate-design →
  implement → verify, entering a phase only when its predecessor has
  reported completion. The investigate-design → implement transition is
  [READY]: implement is not entered until the operator, presented the
  design, selects `next phase`. The orchestrator establishes verify in a
  context isolated from the one that ran the work, each time verify is
  conducted — on first reaching it, and on each re-run after [ISSUES
  FOUND].
- **Dispatch in implement.** Carries out the impl-phase dispatch
  protocol (`phases/implement.md`): dispatching every unit to a subagent
  (isolated on a separate copy when parallel-eligible, in place
  otherwise), owning the tracker append, honoring the loopback shape
  across the subagent boundary.
- **Loopbacks.** A phase may return the run to an earlier phase; the
  orchestrator honors the return rather than proceeding (`SKILL.md`
  Loopbacks).
- **Run lifecycle.** A run starts at investigate-design and ends when
  verify reports [PASSED]. A run's state — the tracker and the phase it
  is in — persists across interruptions in an instance-bound location
  (`.anneal-dev/runs/`), not assumed to share a container with the work
  product; a run interrupted mid-flight resumes from that state rather
  than restarting.
- **Halt and surface.** When the orchestrator cannot advance — a phase
  cannot complete — it halts the run and surfaces the reason; it does
  not advance past the incomplete phase. A decision that needs the
  operator is not such a case: in interactive mode it is held
  [CONDITIONAL] until the operator resolves it; in auto-battle it
  becomes [AUTO-ACCEPTED] and the run proceeds.

## Operator-editable artifacts

Operator-editable artifacts live at `anneal-dev.config/` (committed),
distinct from `.anneal-dev/runs/` (gitignored runtime state). The
operator-editable set: `lenses.md` (lens-supplement mechanism per
`lenses.md` Project supplements), `extensions.enabled` (extension enable
file), `README.md` (operator-facing explainer). On first run in a
project, anneal-dev adds `.anneal-dev/` to the repo's `.gitignore`
(creating it if absent) and bootstraps `anneal-dev.config/` with the
placeholder files (`SKILL.md` First-run bootstrap).
