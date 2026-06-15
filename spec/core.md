# Anneal Framework — Core

The stable spine of the spec: the model, the mechanisms, the
grounding discipline, the phase specs, the status-state machine, and
the orchestrator. Built on `glossary.md`; terms are used as defined
there.

---

## Purpose

The framework exists to secure two things in the AI's work — the
rubric every prescription is judged against:

1. **Grounded claims.** No assertion without its basis. Every
   load-bearing claim is backed by evidence or explicitly marked as
   inferred.
2. **A coherent, complete picture.** Every concern is held,
   visible, and carries a state. A superseded aspect is reconciled
   or invalidated, never silently dropped.

**The mechanism: structural, not willed.** These goals are secured
by shifting rigor from the AI's discipline to **structural
enforcement** — because a rule that depends on the AI *choosing*
rigor leaks: it loads but does not fire. Each load-bearing step is
bound to an evidence-bearing artifact that a separate, non-producing
context re-derives (§3.1), so adherence is read off the artifact
rather than trusted. The one irreducible exception is the
**operator's verdict** at the genuinely-irreducible judgment (§3.1):
a deliberately-willed terminus, not a gap to close.

Human inspectability is a constraint, not a primary value:
artifacts must stay cognitively palatable rather than bloating
into detail too large to hold.

These two goals operate within the framework's three architectural
contracts (`../foundation.md`: framework arbitrariness, render
completeness, instance domain-binding scope).

---

## 1. Model

A run proceeds through three phases in sequence:

1. **investigate-design** — a loop of cycles that builds
   understanding of the task and the problem space and produces a
   locked design. Ends at [READY], when the operator, presented the
   design, selects `next phase`.
2. **implement** — carries out the locked design, producing the work.
3. **verify** — checks the produced work against the locked design
   and the standardized lenses.

The tracker carries state across the phases: investigate-design
produces it, implement works from it, and verify records its results
into it.

An orchestrator conducts the run — running the phases, holding their
transitions, and honoring any loopback a phase raises (§6).

A run is driven in one of two modes:

- **interactive** — the operator advances the loop and selects at
  menus.
- **auto-battle** — the loop self-advances without per-cycle operator
  input.

The AI self-resolves every design decision and records it as a
tracked design decision (§5.2) with its basis (§3.2) — visible,
never silent. **Committed recommendations default to the
thorough-fix shape — the option that addresses the situation at
its actual scope, not pre-clipped on perceived cost. Cost is the
operator's judgment.** "Defer X, because Y" is itself a recorded
decision, not an absence. A decision resting on an assumption —
including one only the operator could confirm — carries that
assumption as its basis and is recorded [CONDITIONAL] (§5.2). The
operator retains free-form override at any point.

**Operator-expected action bound.** The operator's protocol-
expected actions are bounded to (a) **menu selection** at
closed-artifact presentations and (b) **free-form interjection**
(question, comment, or override against the tracker). Auto-battle
removes (a) and (b) entirely. The spec does NOT design AI behavior
expecting operator detection, inspection, sanity-check, audit, or
any other operator-active work beyond (a)/(b). Where an artifact's
enforcement would otherwise require operator-detection, the
enforcement form is malformed — AI discipline or a fresh-context
checker (verify, convergence cycle §4.1.4) carries it.

The operator's request sets the task; it may also propose a solution.
Such a proposal is a strong input, not a locked design: that it is
the right solution is a design premise — grounded on evidence like
any other (§3.2), not assumed because the operator proposed it. The
AI investigates the proposal as it would any design question —
confirming, sharpening, or replacing it on evidence.

---

## 2. Inspection

The framework's one reusable mechanism is **inspection**: it looks
through a lens at the work so far and yields a finding when the lens
catches something. The lens is ad-hoc — the AI's own task-derived
line of inquiry — or standardized: pre-written, the standardized set
specified by the domain instance.

A standardized lens is specified by the lens-entry shape
(`modules.md`): its name, the question it asks, and its scope, which
carries the trigger that brings it into a cycle.

The run's phase transitions — investigate-design's end at [READY],
the loopbacks — are not mechanisms of this kind. They are not a
mechanical check on accumulated state; they are governed by the phase
specs (§4) and the orchestrator (§6), where what each transition
requires is specified directly.

---

## 3. The grounding discipline

### 3.1 The evidence-bearing-artifact rule

Every load-bearing artifact the protocol requires — a mechanism's
output, a recorded design decision — must be **evidence-bearing**:
producing it requires doing the work it represents, so a
non-adherent AI cannot produce it by pattern alone. A bare claim —
"checked all consumers" — is satisfiable whether or not the work
happened; a located enumeration — for code, "consumers: [file:line, …]" — is
not.

Evidence-bearing is a gradient, not an absolute — no artifact an AI
produces is un-fakeable, since it can fabricate one. An artifact's
strength is how far faking it requires active fabrication rather than
mere omission, and how cheaply a checker catches the fake. A
**strong** artifact points at external, re-checkable truth — a search
result, a located read, an executed verification's output: faking it
means fabricating something a checker re-runs and catches. A **weak**
artifact is a claim about the run's own state — a status tag, a
self-assessment that work is complete: there is no external truth to
check it against.

- An inspection's finding, or its cited reason that a lens is clean,
  must cite evidence that required looking.
- A design decision's artifact is its committed resolution and its
  basis (§3.2). An open question, or a choice posed to the operator,
  is the absence of a resolution — so the design-decision track cannot
  hold one.

A weak artifact is not self-enforcing — the protocol cannot rest on
the artifact alone. It is enforced by a **separate checker**: a
context that did not produce the artifact re-derives it (verify's
isolated subagent §4.3, the convergence cycle §4.1.4). The
artifact still earns its place — it makes faking require
fabrication, and gives the checker something concrete to check —
but the bind comes from the checker's **producer-independent
re-derivability**, not from its say-so. A checker BINDS when its
verdict is re-derivable by a context that did not produce the
artifact — terminating at a re-checkable fact (an executed output,
the work exercised by verify §4.3, a render re-derived by a
non-producing context, the git log) or at the operator's
irreducible verdict. A verdict the producing context self-records
that no non-producing context can re-derive is itself a weak
artifact — a **strong surfacer**, not a guarantee: it makes the
concern visible for the separate checker but does not discharge it.

The operator's verdict is a binding terminus only at the
genuinely-irreducible judgment — and only through the bound actions
(§1, menu selection / soundness pass), never operator-detection
(§1: where enforcement would require the operator to detect, the
form is malformed). A check a non-producing context can re-derive
(a verify leg, a falsification pass §4.1.4) stays author-side; it
must NOT be downgraded to "the operator will catch it." Naming the
operator as terminus licenses no such downgrade.

This rule reaches the protocol's behavioral rules, not its
mechanisms alone: a rule whose adherence cannot be read off an
artifact is not enforced. A load-bearing rule is specified so
that following it produces an artifact and not following it
produces none.

### 3.2 The basis rule

Every load-bearing claim and every design premise carries a named
basis — the evidence it rests on. The basis is the artifact itself
(§3.1): (a) a search result with its executable query, OR (b) a
located read of the source paired with **exactly one observable
fact** about the cited range (count, identifier, type) that the
citation grounds. **Cardinality is one per citation** — a
citation paired with multiple stacked facts is malformed. A basis
may contain multiple per-citation pairs when the claim genuinely
rests on multiple facts (each pair one fact per citation); the
basis as a whole stays on one entry. A stacked-fact citation is
audited first for over-statement — rationale, cross-references,
or summaries dressed as facts — and reduced to the actual facts;
entry-splitting is required only when multi-fact analysis reveals
multi-claim structure (each fact supports a different independent
claim). Verifiers (§4.3) and convergence cycles (§4.1.4) re-open
each citation to verify both the location AND the observable
fact. A free-text claim of having looked, a paraphrase of what
was read, or a summary without an observable fact is not a basis.

A basis that resolves to recall — "assumed," "inferred,"
"obviously so" — or to deferral — "will verify in cycle N,"
"impl-phase will produce," "TBD" — is not a basis but an
assumption. An assumption does not ground a decision; the work
is held short of [READY] until the assumption is converted to
evidence. The mechanical tell of a blind spot is the basis the
AI cannot produce.

The rule rejects **silent substitution**: missing or malformed
evidence defaulted to a plausible proxy that propagates as if it
were the basis. Surface the gap, do not substitute.

#### 3.2.1 The two edges

- **Basis-naming.** Every load-bearing claim and every design
  premise names its basis or stands as an assumption. This
  reaches design premises, not findings alone, AND it reaches
  **claims embedded within larger statements** — implicit
  premises in target-naming decisions, cited rules or prior
  decisions, completeness counts asserted as facts, and **a name
  or label asserting an artifact's meaning or provenance** — its
  source, identity, perspective, unit, or value-domain: its basis
  is a located read at the artifact's **producer** (where it is
  set or produced), *not* its use-site label — distrust the
  surface assertion and ground the meaning where the artifact is
  produced (§3.2(b)'s "located read of the source," resolved to
  the producer, not the consuming site that labels it). Each
  embedded claim carries the basis-rule requirement *separately*
  from the surrounding statement: the surrounding claim's basis
  does not cover the embedded one. An embedded claim with no
  separate basis is an assumption and cannot reach [VERIFIED].
- **True-unit basis.** A basis must cover the claim's true unit,
  not a coarser proxy. A claim about a *complete set* (a scope,
  an element's dependents, an input's value-classes, a flaw
  class's instances) has the whole set as its unit; its basis is
  an exhaustive search recorded as the **re-runnable search
  itself** — the executable query, not the count it returned. A
  search narrowed by where the members are assumed to live is a
  declared scope wearing a search's clothing — including a search
  of "everywhere else" that excludes the change site, where
  co-located members hide. A claim about a
  *construct* (a unit of the work product that must be taken
  whole) has the whole construct as its unit; its basis is a
  read to the construct's visible close.

#### 3.2.2 Replacement, removal, or amendment as completeness claim

A design decision involving **replacement, removal, or amendment
of an existing artifact** carries an implicit completeness claim:
that all references to, load-bearing behaviors of, AND
**non-reference structural dependents** of the affected artifact
have been accounted for. Non-reference structural dependents are
renderings of the existing closed Coupling-shape set
(`glossary.md`; not a new shape): code or config that **hardcodes the target's
location or structure** (it breaks on a relocate/rename without
naming the target by content-reference), a **producer of an
artifact the target consumes** (a consumer without a producer is
an unenforced rule firing on a non-existent artifact —
producer-existence is the target-existence shape applied to the
producer), and a **co-producer**: when the target produces a
value written to a shared site consumed by equality (two or more
artifacts must emit a matching value because a downstream consumer
compares them), the obligation enumerates **every producer/writer
of that shared site** — a reference-search on the target's name
does not reach a *sibling* producer; the dependency resolves
through the shared sink's *format contract*, the symmetric
analogue of the producer↔consumer mediation, so it too is a
target-dependents rendering, not a new shape. By target role:
target-as-consumer → enumerate its producer; target-as-producer →
enumerate the sibling producers of the shared sink. The basis must
include the re-runnable search enumerating references and these
dependents AND — for replacements introducing a successor — an
explicit enumeration of behaviors preserved or dropped, covering
behaviors the replaced artifact **emits rather than returns** —
effects produced *within* its body (an emission, write, or call),
which a reference-search cannot surface (it surfaces callers, not
internal effects). The method differs by target: for the body's
emitted effects, **read the replaced artifact's body** for
effect-producing operations, not a reference-search of its
callers; for a co-producer, **search the shared site's writers**,
not the target's references — enumeration keyed on the target's
references misses both, and the search is aimed at the right
target instead. Each enumerated emitted effect must have a
successor in the replacement (an effect with no successor
falsifies — `target-behavior`/`expected-match`); a co-producer
whose emitted format diverges from the target's falsifies
(`target-dependents`/`any-match`). Without both enumerations where
applicable, the decision is missing its true-unit basis and cannot
reach [VERIFIED]. This is the forcing function for Coupled-change
adherence.

A preserved-behavior claim a read cannot exhibit — because the
behavior resolves at runtime through a dependent the reference-
search does not surface (the instance supplies the mechanical
trigger for this case) — is not statically dischargeable: it is
recorded [CONDITIONAL], its basis the affected behavior exercised
by the domain's executable verification (verify, §4.3), not a
read. A static enumeration substituted for it is the silent
substitution the basis rule forbids (§3.2).

A decision that **changes** an observable or computed behavior
(distinct from the *preserved*-behavior case above) carries a
completeness claim over existing tests or checks asserting the
prior behavior — a check can assert a derived value without
referencing the changed symbol, so the reference-search does not
surface it. Where a **spike of the change is buildable at
design-time**, the enumeration is executable: run the domain's
executable verification against the spike; the failing checks ARE
the enumerated set, and their old→new expected-value updates enter
the **locked design scope** (impl transcribes them, does not
judge). Where a spike is **not** design-time-buildable (the
impact manifests only once the implementing work exists), the
claim is [CONDITIONAL], discharged at verify by the executable
verification — the same runtime path as the preserved-behavior
case above. Which case applies is recorded in the basis.

#### 3.2.3 Secondary sources

A secondary source — a sub-agent report, a prior session's notes, an
audit summary — is not itself a basis. A direct citation it carries
(the artifact's located read with an observable fact)
relays the artifact and can stand as a basis; its interpretation,
synthesis, or recommendation cannot, and is re-grounded against the
actual artifact before anything rests on it.

#### 3.2.4 Scope: load-bearing only

Only load-bearing claims and premises carry the basis apparatus; a
claim of bounded, contained cost does not.

---

## 4. Phase specs

### 4.1 investigate-design

investigate-design runs as a loop of cycles and produces a locked
design recorded in the tracker. It ends at [READY].

**A cycle** has two passes by default, in order:

1. **Investigation pass.** The AI investigates the relevant surfaces
   — ad-hoc inspection, by its own task-derived method, not a
   prescribed one. Findings are recorded in the tracker.
2. **Standardized inspection pass.** Apply each standardized lens
   whose scope this cycle's **edit-set** (the rule-text it adds or
   amends) touched — independent of what the investigation attended
   to; incremental, over what this cycle produced. The pass emits the
   standardized-pass
   findings artifact (`modules.md` §3.2 carries the artifact-shape
   and citation requirements). The standardized lens set is
   specified by the domain instance.

The standardized inspection pass runs every cycle. The convergence
cycle (§4.1.4) adds a third pass — falsification — over its
[VERIFIED] decisions.

**Cycle numbering** is continuous across the run — a loopback from
a downstream phase (implement actioned-finding, verify [ISSUES
FOUND]) returns to investigate-design at the next cycle number,
not at cycle 1. Each cycle number is unique within the run.

**Design.** Across the cycle the AI forms and updates design decisions
(§5.2) from the cycle's findings — the design-formation the phase is
named for, §1's synthesis into the evolving design. The locked design
is the body of those decisions; it locks as they reach [VERIFIED].
Where the cycle's **recorded investigation findings** surface ≥2
viable rival approaches for a load-bearing decision, formation
carries them co-equally — each probed on evidence across the cycle —
**before** the decision reaches its terminal, and records them in the
`considered` field (`modules.md` §3.1), which is the required artifact
of that carrying for this case (not optional). One committed
recommendation still surfaces to the operator (rivals-internal ≠
operator-interface; no menu posed). The trigger is the recorded
findings, not a bare declaration; fabricated rivals stay forbidden
(`modules.md` §3.1). This is the multiple-hypothesis discipline only,
not Strong Inference's discredited promises (a single crucial
experiment, complete enumeration).

**Scope.** The scope — the set of elements the work will modify — is
the foundational design decision; every other decision is designed
within it. By §3.2 it is a completeness claim: its basis is an
exhaustive search of every intended target's dependents across the
problem space, not the AI's model of it. It is established first and
reaches [VERIFIED] only when search-established. When a later cycle
grows the set of intended targets, the scope decision re-opens and is
re-searched. Because [READY] requires every design decision
[VERIFIED] or [AUTO-ACCEPTED] (§5.2) — applies in both modes — an
unestablished scope, at neither, holds the phase.

**Requirements record.** investigate-design captures the original
task requirements as a tracked artifact: the operator's request sets
the task and may propose a solution (§1), and the record enumerates
the requirements — the goal — as R1..Rn, separated from any proposed
solution. The operator's **verbatim request** is captured alongside
the enumeration, in the same artifact. The record is header-adjacent
in the tracker — a task-input, not a third track (§5 holds exactly
two) — extending the header's one-line task summary (`modules.md`
§3.1), and is persisted so the isolated verify reads it (§4.3; verify
needs nothing from the run's conversation, where the raw request
otherwise lives). What counts as a requirement and how it is elicited
is instance-defined, as the work product (`glossary.md`) and the
domain's executable verification (§4.3) are.

#### 4.1.1 [READY] — judgment criteria

**[READY]** is reached when the working context judges the design
complete — every concern resolved, every design decision at its
terminal, and the last cycle's standardized inspection pass producing
no load-bearing finding. The supporting facts are recorded across the run:
the standardized lens set is accounted for whole — every lens applied
in the cycle(s) where its scope was touched, or carrying a cited
reason it was out of scope for the run, no lens silently absent; the
last cycle's pass left no load-bearing finding; every design decision is
[VERIFIED] or [AUTO-ACCEPTED] (§5.2) — both modes; **and every
[VERIFIED] design decision's embedded target-naming and count
premises carry a re-runnable basis** (per §3.2 basis-naming for
design-decision premises); no finding is left open. The
convergence cycle's intent-falsification findings (§4.1.4) must be
**dispositioned, not the pass silent**: mechanically-confirmable
findings resolved, pure-judgment findings terminal at
[VERIFIED — surfaced] (§5.1); a [VERIFIED — surfaced] finding is
terminal and does not hold the phase. These are the
status the tracker carries (§5.2) — a notebook of where each
concern stands — not a mechanical check the run self-passes.

The supporting facts above check that everything *recorded* is
at terminal. The judgment must also test whether the recording is
*complete*. The strongest single test is **fresh-session
implementability**: would a session with only the tracker (no
chat context, no current-session memory) implement the design
without surfacing a new design decision? If not, another cycle is
warranted regardless of recorded statuses.

#### 4.1.2 [READY] — artifact-produced result line

**[READY]'s judgment is artifact-produced.** The fresh-session
implementability test produces a named result line in the closed
artifact at [READY] presentation: PASSED with **per-implementer-
step external evidence** — for each step a fresh implementer
would take to carry out the locked design, cite the basis per
§3.2 form (citation + observable fact for a read; executable query
with output for a search) — or FAILED with the specific gap
identified. PASSED without per-step external
citation is a malformed artifact: the test answers from the
recall pool that wrote the design rather than from external
evidence, which is the failure shape that allows false-[READY]s.
Without the result line itself, the closed-artifact form
(`modules.md` §1.1) is also malformed and the [READY] declaration
unenforced. The result line is recorded in the tracker for
post-run review in both modes.

#### 4.1.3 [READY] — cycle-another recommendation

The AI recommends cycle-another whenever the fresh-session
implementability test fails, or a lens in scope was not applied
in the cycle that touched its scope. Cost-asymmetry does not
enter the recommendation; per §1, the operator judges cost.
**The recommendation's justification enumerates observations** —
open findings, [PENDING] decisions, lens-applications still
required, fresh-session-implementability gaps — not costs
(effort, budget, time, "cheaper than"). A justification framed
in cost comparison is malformed.

At [READY] the AI does not certify itself ready: it presents the
design — the tracker, the recorded design decisions, and a
recommendation — for the operator's judgment. The cycle-history
facts (the standardized lens set accounted for whole; the last
cycle's pass clean) are part of what is presented and weighed,
not a self-passed gate. The operator's selection of `next phase` is
the transition to implement; until the operator proceeds, the
phase continues and the loop may run further cycles.

#### 4.1.4 [READY] — convergence cycle requirement

**[READY] requires a convergence cycle.** After the working context
judges §4.1.1's supporting facts met and §4.1.2's fresh-session
implementability test produces a PASSED artifact, the [READY]
declaration requires one more cycle — a **convergence cycle** — to
produce **zero D-track deltas** (no new design decisions, no
amendments to existing ones).

A convergence cycle is a full cycle (investigation pass +
standardized inspection pass + intent-falsification pass +
mechanical falsification pass over [VERIFIED] decisions; see
`modules.md` §3.4), not a final lens application on accumulated
state. The two falsification-style passes are **sequenced**, not
run unconditionally-both: the intent-falsification pass runs
**first**; if it produces a D-track delta the mechanical
falsification pass is **skipped** that cycle (the design is about
to change, so the mechanical run would be stale) and the cycle
records "mechanical skipped: intent-delta this cycle" (so
`modules.md` §3.4's no-falsification-line-malformed rule is
reconciled — its skip carve-out is specified there). Only when the
intent-falsification pass comes up clean does the mechanical
falsification pass run. This sequencing **binds structurally**,
not on the ordering prose alone: the mechanical pass's input
carries this cycle's intent-clean verdict (`modules.md` §3.3
dispatch-brief (c)), its artifact **cites** that verdict
(`modules.md` §3.4 header field), and the coverage check on
return **re-derives** intent-clean from this cycle's §3.4.1
artifact and rejects a mismatch (clause (v) below) — a
producer-independent re-derivation against the intent artifact
(§3.1's bind/surface gradient), not the keyword alone.

The intent-falsification pass runs **every convergence cycle**;
the mechanical pass's governing intent-clean verdict is **always
this cycle's** (no carry-forward across cycles). The §3.4 skip
for a *this-cycle* intent-delta still applies (intent-delta →
mechanical skipped + recorded, that cycle).
Its investigation pass must enumerate **new
surfaces investigated this cycle**, where each surface is
**new** by at least one of: (a) cites a file path not in any
prior cycle's artifact this run; (b) cites a search query whose
query string differs verbatim from every prior cycle's; (c)
cites a located read covering at least one location not covered
by any prior cycle's citation of the same source. A convergence cycle that
produces no new-surface citations (only re-attestations of
prior surfaces) is a malformed artifact.

The **mechanical falsification pass** iterates each [VERIFIED]
D-entry at the convergence cycle's start. For an entry still
[CONDITIONAL] or [AUTO-ACCEPTED], only the
**operator-resolvable-assumption shape** (the target-behavior
runtime case discharged by verify, §3.2.2) is exempt — that
assumption is discharged by verify (§4.3) exercising the work; the
entry's **technical-basis shapes** (target-existence,
target-dependents) ARE still falsified textually here, since a
search can falsify them now. The pass is **dispatched to a fresh-
context subagent**, applying §3.1's separate-checker
requirement — an artifact produced and judged in the same
context is not self-enforcing. The subagent is briefed per
`modules.md` §3.3 dispatch-brief schema (convergence-
falsification variant): it loads the orchestrator's skill
files, reads the tracker reduced-to-latest projection, and
iterates each [VERIFIED] D-entry. For each, the subagent names
a search or read whose positive result would invalidate the
entry's basis, runs it, and cites the result. The subagent
returns the artifact and does not initiate further dispatches.
The pass produces the per-decision falsification artifact
(`modules.md` §3.4): a candidate set per [VERIFIED] entry — one
candidate per coupling shape the basis depends on (`glossary.md`
Coupling shape) — each carrying a **falsification predicate** the
orchestrator applies to the candidate's result to compute
holds-or-falsified. The artifact's line shape, the predicate
closed set, and the malformed-line conditions are specified in
`modules.md` §3.4. A [VERIFIED] entry whose aggregate is
`falsified` flips through [INVALIDATED]→[PENDING] (§5.2) and the
cycle continues; the orchestrator produces the loopback root-cause
triage on this reopen (§4.2.7), citing the falsified entry as its
basis.

**Coverage check on return.** The orchestrator counts the
returned artifact's lines against the [VERIFIED] D-entry set at
the convergence cycle's start AND checks each line's mechanical
form: (i) candidate set non-empty, (ii) each candidate carries
a shape tag from the closed set (`glossary.md` Coupling shape),
a candidate field (a located read or re-runnable query per §3.2), a
falsification-predicate from the closed set (`modules.md` §3.4;
shape-coherent for the candidate's tagged shape), a result
field, and a per-candidate holds-or-falsified value; (iii) the
orchestrator computes the per-candidate holds-or-falsified by
applying the predicate to the result, and the returned value
must match the computed value (a mismatch is a malformed line);
(iv) the line's aggregate-holds-or-falsified equals the
conjunction of per-candidate holds; (v) the orchestrator
re-derives "intent-clean" from **this cycle's** §3.4.1
intent-falsification artifact (no `mechanical-falsification-
candidate` finding) and verifies the artifact's cited
this-cycle intent-clean verdict (`modules.md` §3.4 header
field) matches it. **Mechanical falsification-pass lines
present in a cycle whose this-cycle intent artifact shows a
`mechanical-falsification-candidate` finding (a D-track delta),
OR a mechanical artifact with an absent or unmatched
intent-clean citation, is a malformed return.** This composes
with the absence-of-lines skip carve-out (`modules.md` §3.4):
the carve-out covers absence of lines in an intent-delta cycle;
(v) covers presence of lines. A missing line OR a
mechanically-malformed line is a malformed return; the
orchestrator re-dispatches with the gap's D-entry IDs explicit,
and the subagent fills the gap. All checks are computed from
the artifact. **Residual delegation** — whether the candidate
set's shape coverage matches the basis's claimed shapes
(`modules.md` §3.4) — is the subagent's responsibility per the
brief (d); per-candidate falsifying capability is now mechanical
(predicate-applied-to-result; no subagent judgment).

**Spawn-fallback.** If an isolated context cannot be
established (subagent spawn fails), the pass — mechanical or
intent-falsification — is conducted in the working context per
the rules above and the artifact records "without isolation" —
the spawn-fallback (§4.2.2); an un-isolated pass is never
silently taken as though it were independent.

The **intent-falsification pass** is a pure judgment surfacer: a
fresh-context, criteria-first adversarial attack on whether the
locked design **serves its intent**, against the requirements
record (§4.1). Criteria-first means the subagent derives the
success criteria from the operator's **verbatim request** (§4.1 —
the requirements record's raw-request component, not the working
context's R# enumeration) **before** reading the design — the
independence lever; the design is the attack's target, not its
criteria source. The pass additionally attacks whether the R#
enumeration **faithfully captures** the verbatim request, surfacing
an enumeration-capture error (a verbatim requirement the enumeration
dropped) at convergence — earlier than verify §4.3's retained
independent backstop. This faithfulness leg is a **soft judgment**
(no mechanical predicate): it
shrinks the capture-error residual, not the never-captured-intent
residual. It is dispatched to a
fresh-context subagent (§3.1's separate-checker requirement),
briefed per `modules.md` §3.3, and produces the
intent-falsification artifact (`modules.md` §3.4.1): a per-R#
attack line (every requirement attacked, so a clean pass is
**evidenced** clean, not asserted — an anti-flood and audit-trail
bound, not rubber-stamp prevention) plus a per-finding line. The
intent-model is the captured requirements record; a requirement
never captured there is invisible to the pass (the inherited
never-captured-requirement residual, reduced by verify's
requirements-coverage check, §4.3, not eliminated).

Each finding routes by whether a runnable check exists:

- A concern that **reduces to a §3.4 coupling-shape falsification
  of a [VERIFIED] D-entry's basis** is a mechanical-falsification
  finding: it is formatted as a candidate + closed predicate and
  the orchestrator computes the verdict (no subagent judgment, per
  the mechanical pass above); a confirmed flaw flips the affected
  [VERIFIED] entry through [INVALIDATED]→[PENDING] (§5.2) and the
  cycle continues (this is the intent-delta that skips the
  mechanical pass that cycle). A runnable-but-not-coupling-shape
  concern (e.g. an edit-set that includes a render path a
  requirement forbids) does not force a cycle via §3.4 — its input
  shape is the §3.4 line, not "any runnable check" — and is
  recorded `surfaced` like any judgment concern.
- A concern with **no such reduction** (pure judgment) is recorded
  on the F-track as **[VERIFIED — surfaced]** (§5.1) — terminal,
  surfaced for the operator's review, never blocking the phase and
  never a loopback. The dodge-down vector (classify a checkable
  concern as judgment to skip the cycle) is judgment-adjacent but
  backstopped by the next cycle's fresh-context re-spawn
  (operator-independent), which re-attacks the same design.

**Requirement-coverage completeness binds.** The per-R# coverage
matrix (`modules.md` §3.4.1 — each R#'s serving-decisions) binds
completeness: an R# with an empty serving-decisions set is a coverage
gap that holds the phase (parallel to a `falsified` mechanical entry,
above), forcing an explicit disposition recorded as a design decision
(§5.2) — **serve** (add or amend a decision serving R#), **descope**
(a committed decision that R# is out of scope, with basis), or
**reject** (a committed decision that R# was mis-enumerated). Only
completeness binds; the *quality* of a non-empty mapping stays the
per-R# `served`/`finding` judgment (`surfaced` where pure judgment).
This is the enumerable coverage check pulled upstream from verify
(§4.3) to bind pre-implement.

**The operator-independence boundary.** The pass's value is
operator-**independent**: it force-fixes the checkable concerns
(the mechanical-falsification route — the teeth) and honestly
records the judgment residual ([VERIFIED — surfaced]), neither
waiting on the operator. The recorded residual **feeds** the
operator's soundness pass; for a method-kernel edit that pass is
the kernel-mandated step-4 soundness verdict
(`development-process.md`, the "Dev-on-anneal" entry-condition —
the operator originates it via the permitted [READY]/`next phase`
menu selection (§1 action (a)), not forbidden operator-detection),
and for an instance run there is no such required gate (the
residual is honest-record-for-review, the [AUTO-ACCEPTED]
contract, §5.2). The pass **feeds** that gate; it never becomes it
or depends on it, and introduces no forbidden
operator-detection-as-enforcement (§1 operator-expected action
bound).

A clean intent-falsification pass is **not a soundness
certificate**: for a method-kernel edit the operator's
design-vs-intent soundness verdict is irreducible; the pass feeds
it, never replaces it.

If the convergence cycle surfaces D-track deltas (new decisions
or amendments, or falsified [VERIFIED] entries reopened), the
design is not [READY]: the deltas feed into the next cycle and
the loop continues. [READY] is presented only after a
convergence cycle is observed clean — for the intent-falsification
pass, **clean means its findings are dispositioned, not the pass
silent**: every mechanically-confirmable finding resolved (the
affected entry re-[VERIFIED] across a cycle, bounded by the
zero-D-delta convergence) and every pure-judgment finding terminal
at [VERIFIED — surfaced]. A perpetually-skeptical pass converges:
its surfaced concerns terminate and accumulate in the record;
only an open mechanically-confirmable finding holds the phase, so
the cycle cannot loop forever on judgment surfacing. **The
convergence cycle's outputs (investigation pass artifact +
intent-falsification pass artifact + mechanical falsification pass
artifact, or its recorded skip + zero-D-delta status) form part of
the [READY] artifact** alongside §4.1.2's fresh-session result
line.

The convergence cycle fires in both modes (interactive and
auto-battle). In auto-battle no operator override is available;
the AI cycles until convergence is observed, then proceeds.

### 4.2 implement

implement carries out the locked design recorded in the tracker,
producing the work.

The locked design is the authority. The existing work product and
surrounding conventions are context, not authority — where they
diverge from the locked design, the design governs. The work is derived from the
design first; existing patterns are evaluated for fit afterward.

implement makes no design decisions. Any finding surfaced during
implementation routes through exactly two paths: **loopback** to
investigate-design (when the finding needs action), or
**[VERIFIED — deferred]** (when the operator chooses not to act
now, basis cites the explicit trigger condition per §5.1).
Inline-fix is not a path; attempting to address a finding within
the impl phase by editing the work product is malformed. Local-clarification-
and-continue is not a path; the impl phase does not absorb new
findings into the unit's in-flight work.

The choice between loopback and defer is the operator's per §5.1
(b); the AI's first-judge recommendation surfaces with the
finding. The pre-classification judgment ("is this finding
major-new-scope or local?") is eliminated — every actioned
finding loops back. The loopback cost (one investigate-design
cycle) is the designed trade for eliminating the
inline-misjudgment cost (partial-state save, scope creep,
tracker drift). No
work is lost when loopback fires.

#### 4.2.1 The impl plan

The impl plan is produced at [READY]
presentation — the locked design's decisions grouped into
**dispatch units**, dependency-ordered, with a
parallel-eligibility marker on each — so the operator sees the
unit list at the decision moment (`modules.md` §1.1 State
summary). A planning artifact, not a new tracker construct.
Parallel-eligibility is a load-bearing claim per §3.2: a unit's
element and contract scopes are listed and the disjointness from
any in-flight unit's scope established by the re-runnable search
behind the claim, not by recall. A unit whose disjointness is
not search-established is sequential. The plan is persisted
alongside the tracker (`modules.md` §3.3).

#### 4.2.2 Dispatch

Every unit is dispatched to a subagent — the
orchestrator does not implement in its own context. A
parallel-eligible unit (its disjointness search-established per
§4.2.1) works on a separate copy per the Isolation mechanism
(§4.2.3); a
strictly-sequential unit — including the single unit of a one-unit
plan — runs in a subagent against the operator's work product in
place under the Integrity check (§4.2.4). If a subagent cannot be
spawned, the orchestrator implements that unit in the working
context and surfaces "without isolation" — the **spawn-fallback**, a
degraded path that waives the isolation guarantee, mirroring
verify (§4.3). The subagent is briefed
artifact-driven, mirroring verify (§4.3): it loads the
orchestrator's skill files and receives the tracker plus the
locked contracts the unit honors. The default is the full
tracker; reduction to the unit's in-scope decisions is permitted
only when the orchestrator cites a concrete cause (e.g., tracker
size exceeds the subagent's context budget), recorded as the
basis (§3.2) for the reduction. It implements the in-scope
decisions; it does not design — any actioned finding halts it
(below).
Parallel-eligible units may be dispatched concurrently; the
disjointness basis makes that safe. **Dispatch is continuous,
not wave-batched.** The orchestrator maintains a
**dispatchable set** — the not-yet-dispatched units whose
dependencies are all completed AND whose listed element and
contract scopes are disjoint from every in-flight unit. After
each subagent completion, the orchestrator recomputes the
dispatchable set and fires every newly-eligible unit. A unit
fires when it becomes dispatchable, not when a "wave" is
reached; the disjointness check uses the same scope basis the
impl plan declared at [READY].

#### 4.2.3 Isolation mechanism (parallel-eligible units)

A parallel-eligible unit's subagent works on a **separate copy** of
the work product the unit touches, so concurrent units cannot clash
and the unit's changes reach the operator's work product only
through Integration below — never directly. The separate copy is
**escape-resistant**: the subagent is denied both access to and
knowledge of the operator's work product's location, so a defensive
traversal cannot reach it. The unit's changes are
recorded under a **unit identifier** the operator can audit and
integrate. The framework requires these guarantees; the instance
binds the concrete mechanism — the **isolation slot**
(`instantiation-guide.md` §2) — which carries copy creation, the
identifier, escape-resistance, the **state marker** the Integrity
check reads, the restore mechanism, and which non-tracked run-inputs
are provisioned. **Provisioning:** run-inputs a dispatched unit
reads that are not part of the tracked work product (named in the
isolation slot) are provisioned into the separate copy before
dispatch and excluded from integration; project bootstrap — what the
project needs merely to be runnable — stays out of scope, the
project's concern, not the framework's. **Integration:** after the
unit's changes are verified clean (self-check passed and the
Integrity check confirms no contamination), the orchestrator
integrates **only the unit's changes** into the operator's work
product — no copy-side metadata crosses over.

#### 4.2.4 Integrity check

The orchestrator verifies that the operator's
work product changed in exactly the authorized way and no more. A
work product may span **multiple containers** (a repository, a
document set, a dataset) that are independently isolable; each
container the unit touches is checked independently against the
**state marker** the instance binds (the isolation slot). The check
takes two forms by dispatch path:

- **Isolated (parallel-eligible) units** — each touched container
  was **untouched** during the unit's work (the unit worked on its
  separate copy). The orchestrator snapshots the marker before
  dispatch and confirms it unchanged after; a changed marker means
  the unit escaped isolation and contaminated the operator's work
  product — halt and surface (cause uncertain, so the state is not
  auto-restored).
- **In-place (sequential/single) units** — the subagent runs
  against the operator's work product directly, reading run state
  and the runnable environment natively (no provisioning). The
  orchestrator confirms each touched container is **clean before
  dispatch** (refuse and surface if not), snapshots the marker, and
  after the subagent returns confirms the container advanced by
  **exactly the unit's intended change** and no other modification.
  On mismatch it **restores** the pre-dispatch state (discarding the
  subagent's writes) and halts and surfaces — contamination is
  contained, not merely detected. **The run-state directory is
  excluded from all three of these checks** (clean-before-dispatch,
  the no-other-modification comparison, and restore): run-state is the
  orchestrator's own bookkeeping — written during the run, not the
  unit's work product — so the Integrity check, which guards the work
  product against the unit, neither counts a run-state change as
  contamination nor discards it on restore. The instance binds the
  concrete run-state path.

#### 4.2.5 Self-check at dispatch boundary

Before returning state, the
dispatched subagent (or the working context, on the spawn-fallback
path) applies the standardized lenses most relevant to write-time
issues — the instance specifies which ones (`modules.md` §2.2) —
to its change-set against the unit's in-scope locked design
decisions. **Change-set-vs-listed-scope check:** the subagent
additionally verifies its change-set stays within the unit's listed
scope (`modules.md` §3.3; change-set-referenced identifiers ∖ listed
scope = ∅). A change-set entry referencing identifiers outside the
unit's listed scope is an actioned finding (per the always-loopback
rule above). Findings
are entered as fixed-shape ledger lines (`modules.md` §3.1) and
returned with state; the orchestrator appends per Tracker writes
below. The self-check compounds with the design-time forcing
function for delete/replace/amend decisions (§3.2): the basis
enumerates references as of [READY]; the self-check catches
references and behaviors introduced post-design (new content,
new control paths, new failure modes the unit's change-set
introduces). The
check is unconditional — applied at every dispatch boundary (and
by the working context on the spawn-fallback path). A self-check
finding triggers the loopback (§4.2.7) (or [VERIFIED — deferred] per
the operator's first-judge recommendation, §5.1 (b)).

#### 4.2.6 Tracker writes

The orchestrator (§6) owns the tracker append.
A dispatched subagent does not write directly; on completion or
halt it returns state — findings, the unit's persistence reference, a
loopback signal where applicable — and the orchestrator appends in
deterministic order. Subagent return-state findings carry **batch-
local identifiers** (`F-batch-1`, `F-batch-2`, … sequential within
the return); intra-batch cross-references use these batch-local
forms. The orchestrator maps batch-local to run-global identifiers
at append, re-targeting intra-batch cross-references. A return-
state finding carrying a run-global identifier is a malformed
artifact — return-state cannot know the run-global namespace. The
append-only model (`modules.md` §3.1) is preserved without
concurrency machinery.

#### 4.2.7 Loopback across the subagent boundary

A subagent surfacing
any actioned finding halts and returns a loopback-required result
with four fields:

- **trigger** — the artifact, site, or signal the subagent
  encountered
- **scope** — what's outside the locked design (specific element,
  contract, or behavior)
- **basis** — the re-runnable search or read that surfaced it
  (per §3.2)
- **affected_decisions** — locked design decisions invalidated or
  extended (cited by §5.2 identifier)

On receiving it, the orchestrator halts other in-flight parallel
subagents and audits the work-state at halt. **Parallel-completed
units** (saved before the halt arrived) are audited by
**enumerated set intersection** against the new finding:

- **decision intersection** — does the unit's implemented decision
  set (D# identifiers cited by its impl plan entry, `modules.md`
  §3.3) overlap the new finding's `affected_decisions`?
- **element/contract intersection** — does the unit's listed
  element + contract scope (from its impl plan entry's parallel-
  eligibility scope, §4.2.1) overlap the new finding's `scope`
  field (named elements, contracts, or behaviors — a behavior
  resolves to its implementing element)?

Empty intersection on both → preserve the save and tracker entry.
Non-empty intersection on either → revert (the save discarded,
tracker entry moved to [INVALIDATED]). **Halted subagents' unsaved
work** in their working copy is preserved for redo inheritance —
the new investigate-design cycle reads it alongside the tracker,
and the redesign may incorporate, audit, or discard. Tracker state
is preserved across all cases. The run returns to investigate-
design with the four-field result feeding the new cycle. The
pattern mirrors verify's [ISSUES FOUND] return (§4.3, §6).

**Loopback root-cause triage.** On receipt of any loopback — this
boundary, verify [ISSUES FOUND] (§4.3), or a falsification-failure
reopen (§4.1.4) — the orchestrator (the receiving working context,
not the halting subagent, which does not design, §4.2.4) produces
a STANDARD (non-optional) triage line classifying the failure's
root per the existing render/spec/adherence taxonomy (`glossary.md`
Render gap / spec gap / adherence gap; `development-process.md`
practice 1), with a disposition: render-root → re-render in-run;
spec-root → surface for corpus-evolution; adherence-root → noted
(no source fix). The line cites the loopback's input (the
four-field result here, the verify finding at §4.3, or the
falsified entry at §4.1.4) as its basis — an evidence-bearing
artifact, so the triage does not depend on the operator noticing.
It must **sort**, not cry-wolf: an adherence-root loopback is noted,
not surfaced as a framework gap.

#### 4.2.8 Checkpoint

On completion a dispatch unit's work product is
durably **saved green** as an instance-specific persistence artifact,
and the orchestrator appends its **persistence reference** to the
tracker. **Green** means the project's executable verification (§4.3)
passes before the checkpoint lands; the persistence reference records
a green checkpoint, so resume-from-tracker inherits a clean state.
A red unit cannot checkpoint — its failure surfaces as an actioned
finding / loopback (§4.2.7), not a silent red save. This is the
per-unit composition of the whole-work verify-green (§4.3); it does
not replace verify, which still runs the executable verification over
the completed work. The save plus tracker line is the unit's
persistence artifact: a run interrupted mid-implement resumes from the
tracker — the last-completed unit, the next per the impl plan (§6, Run
lifecycle). Without a per-unit save-point, resume must re-derive
from work-product state — a silent-substitution shape this rule
closes.

implement reports completion when every unit in the impl plan is
completed. The implement→verify transition is not gated: verify
(§4.3) is itself the check on implement, so an incomplete
implementation surfaces as verify findings rather than passing
silently.

### 4.3 verify

verify checks the completed work against the locked design and the
standardized lenses.

verify is conducted in a context **isolated** from the run's working
context — the context that conducted investigate-design and
implement. An actor checking its own work carries its own anchoring
and blind spots into the check; isolation is what makes verify an
independent check and not the actor re-reading itself. verify is
artifact-driven — the four checks below work from the current
run's tracker, the standardized lens set, and the work product,
and need nothing from the run's conversation — so the isolated
context is fully equipped. Prior-run trackers are not basis
material (§3.2); the current tracker must carry re-grounded basis
for anything verify checks against.
The isolation is unconditional: that verify runs isolated is not a
judgment the run makes per task. verify's recorded result names the
context it was conducted in, so a [PASSED] carries whether the check
was independent. If an isolated context genuinely cannot be
established, verify is still conducted, without isolation — the
spawn-fallback (§4.2.2) — and its result records that; an un-isolated
verify is never silently taken as though it were independent.

- **Planned vs actual** — every locked design decision is checked
  against what the work actually does. **The work is also checked
  for material elements not covered by any locked decision**
  (design-completeness audit): a material element surfaces as a
  finding classifying why it wasn't surfaced at design time
  (judged-non-material, forgotten, scope-overflow, missed-pattern,
  or cited-other). "Material" means: implementing the same locked
  decision in a way that yields a different value at a named
  **contract surface** (`glossary.md`; instance-defined — for
  code: external contract, error pattern, API-surface naming,
  persisted behavior). Impl-detail (variable naming, internal
  organization, test fixture choice) does not yield such a
  value-change.
- **Requirements coverage** — each requirement in the requirements
  record (§4.1) is checked for coverage by a locked decision; an
  uncovered requirement surfaces as a finding. This re-checks, in
  verify's isolated context, the same R#→D# coverage matrix bound
  pre-implement at convergence (§4.1.4, `modules.md` §3.4.1) — one
  matrix artifact, two readers: the upstream bind, and this
  independent post-implement re-check. This is the dual of
  the design-completeness audit above: that audit catches a material
  element no decision designed (fact-correct); this catches a
  requirement no decision covers (intent-correct). The record's
  enumeration is also checked against the captured verbatim request
  (§4.1) — a requirement present in the raw request but never
  enumerated is a finding. This second leg is a **soft judgment**: it
  has no mechanical predicate, so it reduces but does not eliminate
  the residual of a requirement that escaped capture entirely.
- **Standardized lenses** — the standardized lens set is applied to
  the produced work.
- **Executing the verification** — the domain's executable
  verification is run and its output shown. verify does not pass on
  static inspection alone.

verify accounts for every check. Each planned-vs-actual check, each
requirement's coverage check, and every standardized lens — applied
where it is in scope, or given a cited reason it is not — either
holds, recorded as a cited-clean line, or yields a divergence from
the locked design, an uncovered requirement, or a lens issue;
a failed run of the executable verification is likewise an issue.
Any non-failure output the executable verification surfaces is
also a finding unless the project has explicitly de-prioritized
that output class. **De-prioritization** requires an artifact:
a project config naming the class, or a tracker entry recording
the class + reason. De-prioritization without an artifact is
the silent-substitution shape (§3.2) the rule rejects. Every
divergence or issue is recorded as a **finding**, entering the
finding track (§5.1) at [PENDING].

verify's terminal result is **[PASSED]** — every check accounted for
and no finding short of [VERIFIED] — or **[ISSUES FOUND]**. The
result is recorded as an evidence-bearing artifact (§3.1): the result
line is paired with a **finding-status ledger** enumerating every
recorded finding's current status. A [PASSED] alongside any finding
short of [VERIFIED] is a malformed artifact.

[ISSUES FOUND] returns the run to investigate-design (§6 loopback),
and the orchestrator produces the loopback root-cause triage on
receipt (§4.2.7), citing the verify finding as its basis.
The fix runs through the full procedure: investigate-design →
implement → verify. There is no in-place shortcut at verify-terminal
— no fix-in-implement bypass and no accept-as-followup at the
verify boundary in either mode. The re-run is a **delta
verify** (confirm finding closed + minimal regression) when the
fix is **behavior-preserving** (instance-defined); otherwise a
**fresh verify pass** (full re-attest). Classification recorded
in tracker; un-classified defaults to fresh.

---

## 5. The status-state machine

A status tag records the state of a finding or a design decision.
There are two tracks. ([PASSED] and [ISSUES FOUND] — verify's phase
result — are not a track; they are specified in §4.3.)

Three tags appear in both tracks, track-scoped and with one
consistent sense: **[PENDING]** (recorded, not yet at a terminal),
**[VERIFIED]** (a verified terminal), **[INVALIDATED]** (a verified
terminal contradicted by later evidence). The reuse is deliberate —
one vocabulary across both tracks.

### 5.1 Finding states

A finding — an observation recorded by inspection — moves through:

1. **[PENDING]** — recorded; not yet verified.
2. **[PARTIALLY VERIFIED]** — verification begun but incomplete. A
   finding fully verified in one step moves [PENDING] → [VERIFIED]
   directly; [PARTIALLY VERIFIED] holds a finding whose verification
   spans steps or cycles.
3. **[VERIFIED]** — verification complete: the finding's content is
   established on evidence. A [VERIFIED] tag carries a cited
   **disposition** naming which of four cases applies (closed enum):

   - **addressed** — the cited D# names the same observable
     behavior the finding observes (an element of the work
     product, or its contract surface); citation-equivalence is
     the check.
   - **non-issue** — basis cites (a) a re-runnable search whose
     result is empty, or (b) a located read + observable fact
     contradicting the finding's premise (§3.1).
   - **deferred** — one of: (a) re-observes a gap an existing
     [AUTO-ACCEPTED] decision deferred (basis cites that
     decision's tracker ID; the finding is appended as a
     re-surfacing notation alongside the original
     [AUTO-ACCEPTED] tag); or (b) operator-pull defer of a
     load-bearing finding the operator chooses not to act on
     now (basis cites an explicit trigger condition — a named
     observable event class, instance-defined; canonical
     classes: a file change, an executable-verification output
     class, a named dependency change — that would re-fire on
     the deferred finding; defer-without-trigger or
     trigger-without-observable-class is malformed); or
     (c) deferred-pending-authoring — the deferral's discharge is
     the authoring of an artifact: the watch lives in a
     to-be-authored artifact, not (as in (a)) an existing
     [AUTO-ACCEPTED] decision nor (as in (b)) an already-existing
     observable trigger. The basis cites the artifact's path, which
     §3.2 re-opens like any basis citation; an absent path makes the
     basis malformed (§3.1), so the finding cannot reach
     `[VERIFIED — deferred to <path>]` — §4.3 forces [ISSUES FOUND]
     on the absent artifact. The artifact's existence is the
     un-fakeable evidence: faking the disposition requires authoring
     the artifact, which is doing the work. The artifact kind is
     instance-defined (for corpus-evolution: a validation-watch
     V-entry).
   - **surfaced** — a judgment-class concern raised by the
     intent-falsification pass (§4.1.4) with no runnable
     mechanical check and no observable re-fire trigger. Its
     citable basis-form is the fresh-context intent-falsification
     attack artifact (`modules.md` §3.4.1): the attack ran and
     classified the concern as having no runnable check. Terminal,
     surfaced for the operator's always-available, never-required
     review (the [AUTO-ACCEPTED] mode-keyed contract, §5.2: in
     auto-battle the surface is recorded for post-run review, not
     awaited). A `surfaced` without its cited attack-artifact
     basis is malformed (§3.1), the same shape as the dispositions
     above.

   The disposition is cited as a tagged suffix on the status line:
   `[VERIFIED — <disposition>]`. A [VERIFIED] without a cited
   disposition is malformed (§3.1). A finding with none of the
   four dispositions citable stays at its prior status; §4.3
   then forces [ISSUES FOUND].

A finding whose stated content is found inaccurate during
verification is corrected — appended as a new line at its current
status (`modules.md` §3.1); verification continues.

A [VERIFIED] finding can then be invalidated:

4. **[INVALIDATED]** — a [VERIFIED] finding contradicted by later
   evidence. An [INVALIDATED] finding reopens — it reverts to
   [PENDING] for re-verification — and holds the phase (§5.3) until
   it does. Only a [VERIFIED] finding becomes [INVALIDATED]; one
   contradicted before [VERIFIED] is simply corrected.

**F-entry resolution closure.** F-entries resolve through
exactly five paths: one of the four [VERIFIED — disposition]
cases above, or [ISSUES FOUND] → loopback (§4.3). Inline-fix —
modifying the work product to address a finding without one of
the five resolutions — is not a path; attempting one is
malformed (§3.1). The closure applies to F-entries from any
source: verify findings, impl-phase self-check findings,
investigation-pass findings.

### 5.2 Design-decision states

A design decision is the AI's resolved choice about what to build — a
**committed position**, including a choice to defer or exclude. It is
never an open question or a choice posed to the operator: per §3.1 a
question is the absence of a resolution and yields no valid artifact,
so the design-decision track holds none. It carries that resolution,
a **basis** (§3.2) — the evidence the choice rests on, or, where it
rests on an assumption, that assumption named — and a status. A
decision the operator could resolve is recorded [CONDITIONAL] — the
AI's committed recommendation carrying the operator-resolvable
assumption — never a posed choice; the operator overrides it from the
tracker (§1). The basis is mandatory; a decision whose basis is an
assumption cannot reach [VERIFIED].

**Body shape.** A design decision body specifies: (a) the **target** —
the element of the work product being committed, or a behavior of one;
(b) the **shape** — for a new element, its **contract surface**
(`glossary.md`); for an amendment to an existing element, the change as
a delta against current state; (c) the
**acceptance criteria** — observable conditions for the decision to
count as implemented; (d) the **side effects and failure modes** —
what's observable on success and at boundaries; (e) the **basis** per
§3.2 (for amendment decisions, (e) carries the §3.2.2
completeness enumeration; (b) carries the shape of the delta).
**Brevity discipline:**
the body covers exactly (a)-(e) above — what a fresh session needs
to implement the decision — and no realization output beyond what the
contract surface and its cited sources already convey. The
**realization output** — the element's internal content — is produced
at impl, not recorded in the design decision body.

It moves through:

1. **[OUTLINED]** — a committed direction; concrete detail not yet
   investigated.
2. **[PENDING]** — a concrete decision whose detail still needs
   investigation.
3. **[CONDITIONAL]** — a concrete decision resting on an unverified
   assumption; the assumption is recorded with it.
4. **[VERIFIED]** — a concrete decision, complete and locked, its
   basis evidence, detailed enough that implementing it introduces no
   new design decision.
5. **[AUTO-ACCEPTED]** — a [CONDITIONAL] decision the AI's committed
   recommendation was taken as default when the operator did not
   override: in interactive mode, by the operator selecting `next phase` at
   the closed-artifact presentation without overriding any open
   [CONDITIONAL] (`modules.md` §1.1); in auto-battle mode, by the
   absence of an operator (`modules.md` §1.2). The recommendation
   stands; the assumption it rested on was not verified —
   [AUTO-ACCEPTED] records exactly that, and does not claim the
   verification that [VERIFIED] does. Both modes reach this state; the
   difference is who-or-what occupies the decision-moment.
6. **[INVALIDATED]** — a [VERIFIED] or [AUTO-ACCEPTED] decision
   contradicted by later evidence.

**Transitions between concrete states.** A [PENDING] decision
found to rest on an unverified assumption becomes [CONDITIONAL];
a [CONDITIONAL] decision becomes [VERIFIED] when its assumption
is verified, and reverts to [PENDING] if the assumption is
disproved. A [CONDITIONAL] decision still resting on its
assumption at [READY] becomes [AUTO-ACCEPTED] (triggers per #5).
An [INVALIDATED] decision reverts to [PENDING], and any decision
that depended on it reverts with it; the phase holds (§5.3)
until re-formed. **Contradiction includes amendment of recorded
resolution** (target naming, scope, completeness counts, basis
source); any such change to a [VERIFIED]/[AUTO-ACCEPTED] decision
flips through [INVALIDATED]→[PENDING] (forces cycle-another
§4.1.3). Silent in-place edit (same status, changed resolution)
is a malformed artifact. Basis-only refinement (`modules.md` §3.1
sub-annotation, resolution unchanged) is not amendment.

A design decision's basis can be broken by another decision,
not only by external evidence. When a decision is locked or its
meaning changes, examine it against the run's other recorded
decisions — does it break what any of their bases rest on. A
broken-basis decision is reopened per the rule above
([INVALIDATED] or revised). The examination is incremental, not
pairwise: the newly locked/changed decision against existing
ones. This holds whether or not the affected decision's work
product exists yet — the contradiction is between decisions,
not in the work product.

### 5.3 Relationship to [READY]

The status tags gate [READY] (§4.1.1): an [INVALIDATED] finding, a
load-bearing finding short of [VERIFIED], or a design decision short
of [VERIFIED]/[AUTO-ACCEPTED] (§5.2) is an unresolved concern that
holds the phase — the loop continues until it resolves. Only a
finding short of [VERIFIED] holds the phase; a [VERIFIED — surfaced]
finding (§5.1) is at [VERIFIED] — terminal — and therefore does not
hold it. These are the
status the tracker carries, read at the [READY] judgment (§4.1.1),
not a gate a separate evaluation re-derives.

---

## 6. Orchestrator

The orchestrator conducts a run through the phase pipeline. The
phases (§4) and the status-state machine (§5) define the work and its
transitions; the orchestrator runs the phases in order, holds the
transitions, and manages the run's lifecycle.

**Run start.** The orchestrator detects the run's mode (§1) and
enters investigate-design. Mode detection and the per-mode conduct of
the run are specified in `modules.md` §1.

**Sequencing and transitions.** The orchestrator advances
investigate-design → implement → verify, entering a phase only when
its predecessor has reported completion. The investigate-design →
implement transition is [READY] (§4.1, §5.3): implement is not entered
until the operator, presented the design, selects `next phase`. The
orchestrator establishes verify in a context isolated from the one
that ran the work, each time verify is conducted — on first reaching
it, and on each re-run after [ISSUES FOUND] (§4.3).

**Dispatch in implement.** The orchestrator carries out the impl-phase
dispatch protocol specified in §4.2: dispatching every unit to a
subagent (isolated on a separate copy when parallel-eligible, in
place otherwise), owning the tracker append,
honoring the loopback shape across the subagent boundary. The
mechanics live in §4.2.

**Loopbacks.** A phase may return the run to an earlier phase; the
orchestrator honors the return rather than proceeding. The specific
returns are specified at their source: implement → investigate-design
on any actioned finding (§4.2.7, including the dispatched-subagent
boundary case); [INVALIDATED] finding or design decision reopens design work
(§5); verify ending [ISSUES FOUND] returns the run to
investigate-design — the single locus for fix resolution; the fix
runs through the full procedure before verify re-runs (§4.3).

**Run lifecycle.** A run starts at investigate-design and ends when
verify reports [PASSED]. A run's state — the tracker (§5) and the
phase it is in — persists across interruptions in an instance-bound
location, not assumed to share a container with the work product; a
run interrupted mid-flight resumes from that state rather than
restarting.

**Halt and surface.** When the orchestrator cannot advance — a phase
cannot complete — it halts the run and surfaces the reason; it does
not advance past the incomplete phase. A decision that needs the operator is
not such a case: in interactive mode it is held as [CONDITIONAL]
until the operator resolves it; in auto-battle it becomes
[AUTO-ACCEPTED] and the run proceeds (§5.2, `modules.md` §1.2).
Auto-battle's remaining halt conditions are part of that mode's
design (`modules.md` §1.2).
