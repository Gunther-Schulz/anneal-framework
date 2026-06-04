---
name: anneal-dev
description: This skill should be used when the user invokes anneal-dev on a corpus-evolution task — by saying "anneal-dev", asking to run anneal-dev, or requesting a structured investigate-design / implement / verify pass on a rule-corpus edit (sharpening a rule, consolidating a fragmented principle, adding a lens, re-rendering a softened clause).
---

# anneal-dev

anneal-dev conducts a corpus-evolution task — a change to the rules a
rule-corpus encodes — through three phases — investigate-design,
implement, verify — holding their transitions, honoring loopbacks, and
surfacing anything it cannot resolve. The corpus is the multi-repo body
of spec-and-skill files that define an AI methodology and its tools;
the work is rule-text, the prose and structure of those files.

## Load this now

- [ ] `references/foundations.md`, `references/tracker.md`, and
  `references/lenses.md` (paths relative to this skill's directory)
  all read this session?
  - NO → CANNOT proceed. Read each now.
  - YES → Evidence: file paths + sections read per file.

## Run start

Detect the run's mode. A run is **interactive** by default; it is
**auto-battle** only when auto-battle is explicitly requested at
invocation. Then locate the run's tracker (see Run lifecycle) and
enter the run's phase — investigate-design for a fresh run, the saved
phase for a resumed one.

**Tracker is the source of truth for run state.** When the harness
provides task-tracking tools (TaskCreate, TaskUpdate, and similar),
they are not used for anneal-dev run-state tracking — the tracker file
under `.anneal-dev/runs/` is the source of truth. Harness task tools
may be used for harness-level work outside the anneal-dev protocol, but
the tracker carries every finding, design decision, and status that
the protocol depends on.

## The pipeline

A run advances through three phases in order — investigate-design →
implement → verify. Each phase has its own procedure file:

- investigate-design → `phases/investigate-design.md`
- implement → `phases/implement.md` — every unit dispatched to a
  subagent; see below
- verify → `phases/verify.md` — conducted in isolation; see below

- [ ] On entering a phase, the corresponding phase file (per the
  mapping above) read this session?
  - NO → CANNOT enter the phase. Read it now.
  - YES → Evidence: phase file path + sections read.

Enter a phase only when its predecessor has reported completion. The
investigate-design → implement transition is [READY]
(`phases/investigate-design.md`): investigate-design ends at [READY]
when the working context judges the design complete and presents it,
and the operator, presented the design, selects `next phase`. The
implement → verify transition is not gated — verify is itself the
check on implement.

The impl plan (`phases/implement.md`) is produced at [READY]
presentation so the operator sees the unit list at the decision
moment: dispatch units derived from the locked design,
dependency-ordered, parallel-eligibility marked with a
search-established disjointness basis (`references/foundations.md`).
Each unit's work is dispatched to a **subagent** — separate-copy
isolated when the unit is parallel-eligible, else run against the
operator's work product in place under the Integrity check
(`phases/implement.md`); the working context runs impl only on the
spawn-fallback path (no subagent). Brief the subagent to load this
skill's `references/foundations.md`, `references/tracker.md`, and
`phases/implement.md`, and to invoke skill-craft via the Skill tool
before any rule-corpus edit (the working context too, on spawn-fallback;
`bindings.md` Skill-craft invocation); and provide the tracker (in full, or reduced
to the unit's in-scope decisions with a cited cause) plus the locked
contracts the unit honors. The subagent implements the in-scope
decisions; before returning state, it (or the working context, on the
spawn-fallback path) self-checks its change-set against the locked
design using the write-time lenses — Lossy-render, Missed-dependents,
Undefined-shorthand, Over-claimed-verification (`references/lenses.md`)
— plus the change-set-vs-listed-scope check, findings returned with
state as fixed-shape ledger lines (see `phases/implement.md`,
Self-check at dispatch boundary). The subagent does not design.
Parallel-eligible units may be dispatched concurrently; the
disjointness basis is what makes concurrent dispatch safe.

**Dispatch model tier (blanket).** Every anneal-dev subagent dispatch —
across **all** dispatch kinds: the investigate-side passes
(intent-falsification and mechanical falsification,
`phases/investigate-design.md`), impl, and verify — runs at the
configured model tier. Cost-downgrading any anneal-dev dispatch below
that tier is **forbidden**. The rule is blanket over all dispatch kinds,
**not** a per-dispatch "is this one sensitive?" judgment. The configured
tier is the model named in `anneal-dev.config/model-tier.md` (Operator-
editable artifacts, First-run bootstrap below); absent or empty, it is
the session model — never downgraded below that. It is a **floor, not a
guarantee**: it avoids handicapping judgment-heavy work whose blast
radius is the whole framework plus every instance, but does not replace
the structural robustness that catches errors — the separate-context
verify and its isolation (`phases/verify.md`), the falsification passes,
and the operator. Enforcement is **observable**: the model parameter on
each dispatch is visible, so a downgraded dispatch shows on the dispatch
itself — no separate artifact required. This binding is anneal-dev-
specific (`bindings.md` Dispatch model tier).

The orchestrator owns the tracker append: a dispatched subagent
returns its state on completion or halt — findings, the unit's
persistence reference, a loopback signal where applicable — and the
orchestrator appends in deterministic order, preserving the
append-only model (`references/tracker.md`). A subagent surfacing any
actioned finding halts and returns a loopback-required result with the
finding; the orchestrator then halts other parallel subagents in
flight, audits the work-state at halt per `phases/implement.md`
(parallel-completed units preserve or revert by scope-disjointness
audit against the new finding; unsaved working-copy changes preserve
for redo inheritance), preserves tracker state, and returns the run to
investigate-design with the new finding (Loopbacks below) — the halt is
required because in-flight subagents may rest on the disjoint-scope
claim the new finding contradicts. Per-unit saves are the checkpoint
discipline: each dispatched unit's integrated changes are saved on
completion; the persistence reference appended to the tracker is what
makes resume after interruption (Run lifecycle) reliable.

verify is conducted in isolation from the run's working context
(`phases/verify.md` §Isolation). At the implement → verify transition,
and on each verify re-run after [ISSUES FOUND], establish the isolated
context (in anneal-dev, by spawning a subagent) and brief it to load
this skill's `references/foundations.md`, `references/tracker.md`,
`references/lenses.md`, and `phases/verify.md`, then conduct verify
against the run's tracker and the produced rule-text — recording its
findings to the tracker. The brief carries the tracker reduced to the
latest line per entry (`references/tracker.md`), produced by the
orchestrator before brief construction; the raw tracker file remains
accessible to the subagent for ledger-history inspection. It reports
[PASSED] or [ISSUES FOUND]; honor the loopback below. If the isolated
context cannot be established (subagent spawn fails), surface "without
isolation" to the operator and conduct verify in-context per
`phases/verify.md` §Isolation.

**Post-verify extensions.** On verify [PASSED], before the run ends,
dispatch any enabled lifecycle extensions registered for
`on-verify-PASSED`. The orchestrator reads
`anneal-dev.config/extensions.enabled` (one name per line, `#`
comments); for each enabled extension, applies the declared action.
Disabled or absent extension = no-op. anneal-dev declares one
extension at this point — `render-and-open-diff`: on a verify [PASSED]
for a spec-level change, re-render the affected plugin skill files from
the now-verified spec and present the rendered diff for the operator's
review (presentation only — it does not commit the render; the operator
owns the render commit). Capability boundary per
`anneal-framework/instantiation-guide.md` §5 (no tracker modification,
no run-completion blocking; writes to non-spec render-output paths
only).

## Loopbacks

A phase may return the run to an earlier phase. Honor the return rather
than proceeding:

- implement returns to investigate-design when any actioned finding
  surfaces during implementation.
- an [INVALIDATED] finding or design decision reopens design work.
- verify ending [ISSUES FOUND] returns the run to investigate-design —
  the single locus for fix resolution. The fix runs through the full
  procedure (investigate-design → implement → verify); no in-place
  shortcut at verify-terminal.

## Modes

In **interactive** mode the operator advances the run. After each
investigate-design cycle and at each phase boundary, present a **closed
artifact** — the tracker (its findings and recorded design decisions),
a recommendation, and the menu — **and nothing else**. Do not pose
design decisions to the operator as questions or choices: they are
recorded in the tracker as committed decisions
(`phases/investigate-design.md`, `references/tracker.md`), never
surfaced as a choice for the operator to make. The **menu** carries
only loop control — the operator selects one option: `another cycle`
(run the loop again) or `next phase` (transition). The operator's input
on a design decision is free-form override against the recorded tracker
— never an answer to a posed choice. Suggest *example* wording
the operator could use — lowering friction without restricting the
reply. Posing a binary or n-ary choice ("A or B?") is the line: it
constrains the operator's input to selected options and is not
permitted.

The menu **persists**. It is the last element of every response until
the operator selects `another cycle` or `next phase`. The operator may
interject free-form instead of selecting — a question, a comment, an
override; answer the question or apply the override, **then**
re-present the menu as the last element of that same response. The
operator never loses the advance choice.

**Closed-artifact form.** The closed artifact contains these named
sections in this order. Each section is required; missing or
out-of-order sections make the artifact malformed:

1. **State summary** — what the operator decides on first: counts
   (findings + decisions by status), the last cycle's
   standardized-pass status (clean or line items), the fresh-session
   implementability result line (PASSED / FAILED per
   `phases/investigate-design.md`), **the convergence-cycle status**
   when at [READY] (the convergence cycle's investigation-pass artifact
   citation + intent-falsification-pass artifact citation + mechanical
   falsification-pass artifact citation, or its recorded skip, +
   zero-D-delta confirmation per `phases/investigate-design.md`
   Convergence cycle requirement), named blockers preventing [READY]
   (open [PENDING] decisions and weak-basis tracker entries), **impl
   plan preview at
   [READY]** — header line with unit count + run-level
   sequential-vs-parallel summary + the disjointness basis citation;
   followed by one line per dispatch unit naming dependencies (after
   which units, or "first" if none) and parallelism (parallel with
   which units, or "sequential"), per `phases/implement.md` The impl
   plan. Decision-relevant content first; detail follows.
2. **Inventories** — findings and design decisions as scannable
   one-per-line ledger entries with status tag and identifier at the
   start; not paragraph-prose summaries.
3. **Persisted artifacts** — citations to where detail lives (the
   tracker file at `.anneal-dev/runs/<run>.md`, the standardized-pass
   artifact alongside). The closed artifact references; it does not
   paragraph-summarize.
4. **Recommendation** — the AI's next-step proposal
   (thorough-fix-shaped per `references/foundations.md` Recommendation
   discipline); rationale and any "not recommended because…" callouts
   in this section. **For each open [CONDITIONAL] decision, the AI's
   committed default surfaces crisply** — what the operator accepts by
   selecting `next phase`; the [CONDITIONAL] then records
   [AUTO-ACCEPTED] (`references/tracker.md`). Operator's free-form
   override against the tracker is available in either mode.
5. **Menu** — `(a)nother cycle` / `(n)ext phase` only; accept `a` or
   `n` as menu selection; plain otherwise; no inline annotations except
   a single `← recommended` tag on the option matching section 4's
   recommendation. The tag is mandatory: every menu has exactly one
   tagged option.

**Presentation.** Search commands, file paths, tracker citations are
presented as code, not buried in prose.

The closed artifact surfaces the design for the operator's menu/
free-form decision moment.

**Auto-battle is interactive minus the operator.** Every protocol
behavior — cycle loop, lens application, basis-rule discipline, tracker
shape, dispatch self-check, verify isolation, [CONDITIONAL] handling —
is identical to interactive. The single difference is the operator slot
at decision moments: in interactive, an operator selects `another
cycle` or `next phase` at the closed-artifact presentation; in
auto-battle, no operator is present, so the AI's committed
recommendation is taken as default automatically.

In **auto-battle** mode the loop self-advances without per-cycle
operator input. Cycles run until the working context judges the design
complete ([READY], `phases/investigate-design.md`). At [READY], where
interactive presents the closed artifact and waits for the operator's
next-phase selection, auto-battle skips the presentation and proceeds
directly — the same default-take of the AI's recommendation, just
without the operator-present-to-attest.

A [CONDITIONAL] decision still resting on its assumption when the
design reaches [READY] is recorded [AUTO-ACCEPTED] in both modes
(triggers + semantics per `references/tracker.md`). Every
[AUTO-ACCEPTED] decision is, by its tag, surfaced in the tracker for
the operator's review of the completed run — never silently.

Verify [ISSUES FOUND] in auto-battle triggers automatic loopback to
investigate-design (Loopbacks above). A finding that closes
[VERIFIED — deferred] (`references/tracker.md`, finding-state #3) does
not trigger loopback — the disposition cites the existing
[AUTO-ACCEPTED] decision and the run completes; the AI's prior judgment
to defer is preserved for the operator's post-run review. A finding that
closes [VERIFIED — surfaced] (`references/tracker.md`, finding-state #3) —
the intent-falsification pass's pure-judgment residual, a judgment-class
concern with no runnable mechanical check — is likewise terminal and
does **not** trigger loopback: it is recorded for the operator's
always-available, never-required review (in auto-battle the surface is
recorded for post-run review, not awaited). Other halt
conditions — phases that genuinely cannot complete on causes other than
[ISSUES FOUND] — remain a separate, not-yet-undertaken effort.

## Run lifecycle

A run starts at investigate-design and ends when verify reports
[PASSED]. Each run has its own tracker — an append-only ledger file
under `.anneal-dev/runs/` (`references/tracker.md`); a new entry or a
status change appends a line rather than rewriting, and a run never
overwrites another run's tracker. Run state is not assumed to share a
container with the work product: the run-state directory
`.anneal-dev/runs/` lives in the repo the operator invoked the run
from, while the work product the run touches may span the corpus's
several repos (`references/foundations.md`, `references/tracker.md`).

At run start, scan `.anneal-dev/runs/` for an **in-progress** run — a
tracker whose header Status is not `PASSED`:

- an in-progress run for the current task → resume it from its tracker
  and phase rather than restarting. Read the tracker reduced-to-latest;
  the phase header names where to re-enter; a mid-implement
  interruption resumes from the impl plan's last-completed unit per its
  persistence reference (`phases/implement.md` Checkpoint).
- an in-progress run for a different task → surface it to the operator
  (a prior run left unfinished), then start a fresh run for the current
  task.
- none in progress → start a fresh run.

A fresh run opens a new tracker file under `.anneal-dev/runs/`.
Completed runs' tracker files are kept — `.anneal-dev/runs/` is the
project's accumulated anneal-dev history; nothing is overwritten.

**First-run bootstrap.** On first run in a project, bootstrap the
filesystem footprint per `references/foundations.md` (Operator-editable
artifacts):

- Add `.anneal-dev/` to the repository's `.gitignore` (creating that
  file if absent) and note the change.
- Create `anneal-dev.config/` with four placeholder files (each per
  `anneal-framework/instantiation-guide.md` §5 Placeholder content
  style — header comment naming the slot + framework spec section
  pointer; empty sections matching the slot's declaration shape;
  commented-out small example optional):
  - `lenses.md` — lens supplement file (header: "Project supplemental
    lenses. Add entries here; each fills the Name / Question / Scope
    lens-entry shape. Additive-only: cannot disable or override
    anneal-dev's core lenses. Malformed file = fail-loud halt at
    standardized-pass dispatch.")
  - `extensions.enabled` — extension toggles file (header: "Enabled
    lifecycle extensions, one name per line; `#` comments. Available in
    this anneal-dev version: render-and-open-diff (fires on
    verify-PASSED; re-renders affected plugin skill files from the
    verified spec and presents the diff — presentation only).
    Uncomment to enable.")
  - `model-tier.md` — dispatch model-tier slot (header: "Dispatch
    model-tier override (anneal-dev model-tier slot; `bindings.md`
    Dispatch model tier). Set the value line to your harness's top-tier
    model identifier — every anneal-dev dispatch (investigate/
    falsification/impl/verify) runs at this tier, never downgraded.
    Absent or empty inherits the session model — the harness default —
    also never downgraded below."); commented/empty on bootstrap
    (default: inherit the session model), filled with a model name to
    pin a tier.
  - `README.md` — operator-facing explainer (one paragraph: "This
    directory is operator-editable: add project lenses to `lenses.md`,
    toggle extensions in `extensions.enabled`, and pin the dispatch
    model tier in `model-tier.md` (the floor every anneal-dev dispatch
    runs at — never downgraded; empty inherits the session model).
    Runtime state lives at `.anneal-dev/runs/` and is gitignored — do
    not edit there.")

## Post-run review (optional)

After verify reports [PASSED], the operator may request a **post-run
review** to surface what the protocol missed or got wrong this run — a
free-text instruction like "post-run review" or "review the run." Do
**not** prompt for it; the operator decides when a run warrants the
analysis.

On request, load `references/post-run-review.md` and conduct the review
per that procedure. Output goes to the operator in the session — do
**not** persist the review or its findings to a file in the project
(persisting prior-run analysis pollutes future runs and clutters the
project directory).

## Halt and surface

When the run cannot advance — a phase cannot complete — halt the run
and surface the reason; do not advance past the incomplete phase. A
decision that needs the operator is not such a case: in interactive
mode it is held [CONDITIONAL] until the operator resolves it; in
auto-battle it becomes [AUTO-ACCEPTED] and the run proceeds (see
**Modes**).
