# Design-decision implication-depth gaps — three classes of "model saw the fact, didn't connect it to the decision"

**Status:** [DESIGN] — operator-raised 2026-06-05, evidenced by retrospective
root-cause analysis of 6 post-ship bugs in the beat-the-books clippy instance
(3 within-scope of a Clippy run that missed them; 3 out-of-scope — only the
within-scope misses are in scope here). **Empirical, strongly evidenced (n=3
distinct classes, each with a confirmed production instance).** The three classes
share a unifying shape but require distinct fixes.

**Campaign placement + level (2026-06-05, integrated from a stray marketplace-clone copy).** Correctly homed in the **anneal-framework** backlog (not skill-craft): the THREE specific classes are clippy-evidenced/coding-flavored, but the **unifying shape is framework-level** — "saw the fact, didn't connect it to the decision" (reasoning-depth at design-lock) is **not coding-specific**: it recurs in anneal-dev's OWN work (the campaign-③ `v-entry-is-post-ship-only` side-quest hit the same shape this session — saw the WATCHING blurb, didn't connect it to the lifecycle state machine; *every change is bigger than its diff*). So it pairs with `framework-blindspot-class-analysis` as its **empirical core** (that item = the proactive-enumeration *method*; this = *3 confirmed classes + fixes*). It does NOT fold into a single campaign; fixes route by level:
- **Class 2** (execution-context) = the one new artifact → **clippy instance** (`coding-clippy/spec/lens-set.md`; explicitly coding-domain).
- **Class 1** (input-dimension) → a Canonical-ID-lens sharpen (clippy) **OR** a design-decision **body-shape (d) parameter-completeness check** (framework — sibling of campaign ②'s shipped `structural-change-dependent-enumeration`; "enumerate consumed dimensions vs parameters" is coding-general).
- **Class 3** (write-without-reader) — already **covered** (convergence `target-dependents`); optional Consumer-enum read-side sharpen.
- **Framework-level open question** (anneal-dev's, not just clippy's): do the intent-falsification + convergence passes *suffice* for the reasoning-depth shape, or is a forcing function warranted across instances? Cross-class obs 3: reducible, not eliminable by process. NOT campaign ③.

## The unifying shape

In all three cases the model **had the relevant information in context** — read
the file, noted the field, cited the parameter — and **did not connect it to the
design decision it was locking.** The lenses passed clean, the convergence cycle
(where it existed) found no delta, and verify inherited the same framing. This
is not a context-window or information-access failure; it is a
**reasoning-depth** failure at design-lock time, where the model satisficed on
the primary complexity of the decision and did not probe secondary implications.

The three classes are structurally distinct — each has a different mechanism gap
and a different candidate fix — but they cluster under one backlog item because
they were surfaced by the same retrospective pass and share the "saw it, didn't
connect it" shape.

## Class 1 — Premature input-dimension categorization

**Instance (n=1).** Unit 7 (replay engine), `derive_outcome_result` — the model
designed a new settlement function that takes `(home_score, away_score,
market_type, outcome, handicap, total, team_qualifier)`. The detection schema
carries a `period` column (first_half, full_game, etc.); the match-key tuple
explicitly includes `period`; the `ReplayPickRow` envelope carries
`period: PeriodType`; the `market_signature` example string
`'spread|full_game|home|-1.5'` was quoted in the run. The model **saw `period`
at least 4 times** across different cycle artifacts — and categorized it as a
routing/identity dimension (for matching picks to markets), never as a
settlement-logic dimension (affecting which scores to compare). The branch table
was locked along `market_type × outcome`; period was not a dimension. Result:
13k+ non-full-game picks settled against the full-game score — corrupts the EV
calibration the scaling gate depends on (Unit 27).

**Why current framework partially covers but doesn't guarantee.** The
**intent-falsification pass** (post-Unit-7 addition) gives the best shot: a
fresh-context subagent deriving success criteria from requirements BEFORE reading
the design could independently arrive at "must handle different period types."
The **mechanical falsification** `target-behavior` shape could catch it if the
subagent independently thinks "what about non-full-game periods?" The
**Canonical-ID-dropped-at-handoff lens** SHOULD have fired (producer=detection
schema carries `period`, consumer=settlement function doesn't receive it) — but
the model framed the function as "new code I'm designing," not "a consumer at a
data-handoff boundary." Two fresh-context passes improve the odds (~60/40 vs the
prior ~10/90), but neither structurally **forces** the model to enumerate all
input dimensions of the consumed data against the function's parameter list.

**Mechanism gap.** No rule forces: "when designing a function that consumes a
record with N identity/data dimensions, enumerate which dimensions the function
needs and which it intentionally drops — with a cited basis for each drop." The
Canonical-ID lens asks the right question at handoff boundaries but doesn't
trigger when the model frames the consumer as new code rather than a
handoff-boundary consumer. The Branch-coverage lens checks branches on the
function's actual inputs — it can't flag a missing input it doesn't know about.

**Candidate fix direction.** Sharpen the Canonical-ID-dropped-at-handoff lens
scope to fire not only at serialization/deserialization boundaries but also
when a new function's **input record** (the data it will consume at runtime)
carries dimensions the function's **parameter list** does not accept — framed as
"a dimension present in the input record but absent from the consumer's
interface is a drop that requires a cited basis (intentional, with reason) or is
a bug." Alternatively, a **parameter-completeness check** as part of the
design-decision body shape (d) "side effects and failure modes": when a design
decision introduces a function consuming a structured record, the record's
dimensions are enumerated against the parameter list in (d), with intentional
drops cited. Either form forces the enumeration the model skipped.

## Class 2 — Execution-context blindness (resource-hold during new code)

**Instance (n=1).** Unit 14 (data completeness), D9 — the model designed adding
`fetch_bet_calculation` HTTP calls inside `capture_market_snapshots`. The
function's signature was read and `uow` (unit-of-work / open database
transaction) was noted as a parameter. The model never asked what happens to
the Postgres session while HTTP calls run inside the UoW's scope. Slow Azuro
responses held sessions `idle in transaction` up to 35 minutes, wedging the
60s analyze tick. Pre-existing since Unit 14; unmasked by a later idempotency
fix (Rev 32).

**Why current framework does NOT cover this.** Every lens was checked:

- **Failure-path** — asks whether errors degrade without signal; the problem is a
  *slow success* holding a DB lock, not an error. Doesn't prompt "what if this
  succeeds slowly?"
- **Performance** — asks about repetition/batching; not about what resource is
  held open during the work.
- **Silent-substitution-at-boundary** — data-level silent substitution, not
  resource-hold consequences.
- **Contracts** — closest (patterns verified against actual code), but the UoW
  pattern (no network calls inside open transactions) is a convention, not a
  typed contract the lens checks.
- **Fitness** — output-consumer fitness, not execution-context safety.
- **Design-decision body shape (d)** — requires "side effects and failure
  modes," but the model must recognize the txn-hold as a side effect, which is
  the exact reasoning it didn't perform.
- **Behavioral-coupling discharge (Finding 3 fix)** — addresses
  subtype/inheritance coupling; different class.

No lens, no rule, no falsification shape asks: **"for code inserted into an
existing scope, what execution context (open transactions, held locks,
connection pools, rate-limit budgets) wraps it, and is the new code's
worst-case timing profile safe within that context?"**

**Mechanism gap.** The lens set has no entry for execution-context / resource-hold
safety. This is a genuinely uncovered class — not an adherence failure on an
existing rule.

**Candidate fix direction.** A new **Clippy lens** (instance-level, not
framework — execution-context is a coding-domain concern):

> **Execution-context lens** — *Question:* for code inserted into an existing
> function or scope, does the caller's execution context — open transactions,
> held locks, connection-pool checkouts, rate-limit budgets, timeout windows —
> remain safe given the new code's worst-case timing profile? A network call
> inside a database transaction is the canonical failure shape; a retry loop
> inside a held lock is the sibling. *Scope:* any new code (design decision or
> implementation) inserted into an existing function whose signature or body
> holds a resource (a `uow`/`session`/`connection`/`lock` parameter, a
> `with`/`async with` block, a context-manager scope). Fires at the insertion
> site; the basis cites the resource's scope and the new code's timing bound.

The lens is **mechanical** in its trigger (the insertion site's enclosing
scope holds a resource — searchable) and **judgment** in its evaluation (is
the timing profile safe) — matching the existing lens-entry shape. It catches
the Unit 14 bug class and generalizes to retry-inside-lock, unbounded-loop-
inside-connection-checkout, and similar resource-hold violations.

## Class 3 — Write-without-reader (basis-rule adherence on future-consumer claims)

**Instance (n=1).** Unit 14 (data completeness), D9 — the model added per-outcome
`fetch_bet_calculation` API calls to populate `max_bet_by_position` on the
snapshot model. Stated purpose: "liquidity-trajectory analysis." The model never
identified a concrete downstream reader. Consumer-enumeration found zero
constructors break (write-side only); the Fitness lens accepted the future
analysis as a consumer. Rev 35's falsification pass confirmed zero readers across
replay, sizing, analytics, exports, and dashboard — the enrichment was dead code
and the dominant source of self-inflicted Azuro API volume.

**Why current framework DOES cover this (adherence gap, not mechanism gap).**
The existing rules should catch it if strictly applied:

1. **Basis rule** (`foundations.md`): "liquidity-trajectory analysis" is an
   **assumption** (a future consumer that doesn't exist), not evidence. The rule
   says "An assumption does not ground a decision; it holds the run short of
   [READY] until converted to evidence or the operator resolves it." Strictly
   applied, D9 stays [CONDITIONAL], not [VERIFIED] — visibly flagging the
   assumption.
2. **Consumer-enumeration lens**: says "every plausible reference shape" —
   doesn't distinguish read from write. Strictly applied, a search for readers
   of `max_bet_by_position` returning zero results is a finding.
3. **Fitness lens**: "do observable outputs carry what their consumers need" —
   an output with no consumer is fitness-wasteful.
4. **Fresh-session implementability** (post-Unit-14 addition): a fresh session
   seeing "writes `max_bet_by_position` for liquidity analysis" would
   reasonably ask "where is the liquidity analysis code?" — surfacing the gap.
5. **Convergence falsification** (post-Unit-14 addition): `target-dependents`
   shape search on `max_bet_by_position` read-consumers = empty = falsified.

**Why it slipped despite coverage.** Unit 14 was an 8-slice unit. D9 (enrichment)
was a small slice alongside much heavier design work (claimed_at naming
collision, cycle_id UPSERT semantics, paper-bet ORM misattribution, settlement
timing). The model resolved D9 quickly (~30 lines/cycle) and moved on. The
attention-dilution in a large unit let the model satisfy the basis rule with a
future-consumer claim it would have interrogated in a smaller-scope run.

**Mechanism gap (secondary).** While the rules cover this, there is no
**structural forcing function** that prevents a future-consumer claim from
reaching [VERIFIED]. The basis rule says assumptions hold the run, but
recognizing "this consumer doesn't exist yet" as an assumption (vs. "this is
the stated purpose") is itself a judgment call the model can miss under load.
The convergence falsification's `target-dependents` shape is the strongest
backstop (a zero-reader search result is mechanical), but it was added after
Unit 14 ran.

**Candidate fix direction.** No new rule needed — the convergence falsification
`target-dependents` shape now mechanically catches zero-reader fields. The
remaining risk is attention-dilution in large units. The **fresh-session
implementability test** (also post-Unit-14) is the natural defense: a fresh
session will question an unjustified write. If warranted, a narrow sharpening
of the Consumer-enumeration lens to explicitly name **read-side** enumeration
(not just "every plausible reference shape," which the model satisfied with
write-side references only) would close the interpretation gap — making it
harder to satisfy the lens with constructor-only searches.

## New instance — anneal-dev's OWN corpus-evolution (2026-06-06; operator-surfaced)
The `run-state-tracked-by-default` run produced **two fresh instances of the unifying shape** —
in anneal-dev's own framework work, not clippy/coding — confirming line-10's claim that the shape
recurs in the kernel's own runs. Both were caught by the **convergence cycle** (the fresh-context
backstop), not by the same-context design:
- **Cycle-2 gap:** the decision "track run-state (un-gitignore the slot)" — the design *did*
  enumerate dependent **spots** (the Missed-dependents lens found the parallel-isolation
  provisioning rule), but did **not trace the behavioral implication** that tracking run-state
  collides with the **in-place integrity check** (the orchestrator's mid-run tracker writes become
  visible to "clean-before-dispatch"; a restore would discard the live tracker). Saw the dependent,
  didn't connect it to the integrity-check implication.
- **Cycle-4 gap:** the decision D7 (exclude run-state from the in-place check) — didn't
  **propagate the boundary** to the parallel separate-copy/integration path (D4 still rested on the
  wrong discriminant). Saw the boundary, didn't connect it to *all* its application sites.

**What this sharpens (the line-14 open question):** the operator asked whether the repeated
convergence-caught gaps could be optimized by a **better design before convergence**. This run is
direct evidence that the answer is the item's open question — *and* points at a concrete
forcing-function candidate at **framework-corpus-evolution** level (not just clippy):

> **Trace, don't just list, dependents.** The Missed-dependents lens (and design-decision
> body-shape (d)) currently force enumerating the dependent **spots** of a changed contract; they
> do **not** force tracing **what the change DOES to each** ("for each dependent of the changed
> contract, state the behavioral effect of the change on it"). Cycle-1 listed the provisioning
> dependent but never asked "what does tracking run-state do to the integrity check." A
> trace-the-implication clause on Missed-dependents / (d) is the design-time analogue of what the
> convergence `target-behavior` pass did after the fact.

This is the **sibling at framework level** of Class 1's "enumerate consumed dimensions vs
parameters" — same shape (enumerate-and-trace, not just enumerate), generalized from
coding-function-parameters to any-changed-contract's-behavioral-dependents. Reinforces cross-class
obs 3: convergence (fresh-context) is the working backstop; a design-time trace-clause would
**reduce** (not eliminate) the convergence-cycle count. NB: distinct from the v-entry gold-plating
(`convergence-surfaced-finding-action-brake`) — that was convergence churning on *non-defects*
(over-fixing); this is convergence catching *real defects the design missed* (depth gaps). Two
different failure modes, two different items.

## Cross-class observations

1. **The intent-falsification pass and convergence falsification (both
   post-dating the bugs) are the single biggest improvements.** Class 3 is now
   mechanically caught by `target-dependents`. Class 1 gets two independent
   fresh-context shots. Class 2 is the only one with zero coverage.

2. **Attention-dilution in large units** compounds all three classes. The 8-slice
   Unit 14 produced both Class 2 and Class 3 bugs from the same D-entry (D9).
   Not a framework gap per se (scope sizing is operator judgment), but a
   pattern worth noting — small units have higher per-decision reasoning depth.

3. **The "saw it, didn't connect it" shape cannot be fully closed by protocol
   rules.** Rules can force enumeration (Class 1 candidate), force resource-hold
   checks (Class 2 candidate), and mechanically falsify dead writes (Class 3,
   already covered). But the underlying reasoning-depth issue — the model
   satisficing on primary complexity and not probing secondary implications —
   is a model capability ceiling, reducible but not eliminable by process.

## Actionability

- **Class 2 (execution-context) is the only one needing a new artifact** — a
  Clippy lens. Instance-level (`coding-clippy/spec/lens-set.md`), not framework.
- **Class 1 (input-dimension categorization)** could be a lens sharpening
  (Canonical-ID scope expansion) or a body-shape (d) addition. Framework or
  instance — the "enumerate consumed dimensions vs parameters" discipline is
  coding-general.
- **Class 3 (write-without-reader)** is covered; a narrow Consumer-enumeration
  lens sharpening (explicit "read-side" language) is optional belt-and-suspenders.

## Relates to
- `framework-blindspot-class-analysis.md` — this is THREE confirmed blind-spot
  classes with production instances; feeds the proactive enumeration.
- `clippy-run-findings-dispatch-coupling.md` Finding 3 — sibling "design-phase
  static-blind" class (behavioral coupling); Class 2 here is the
  execution-context sibling (resource-hold coupling).
- `structural-change-dependent-enumeration.md` — sibling dependent-enumeration
  blind spot (non-content-reference dependents); Class 1 here is the
  input-dimension sibling.
- `behavior-change-test-impact-enumeration.md` — sibling "what does this change
  touch" enumeration discipline.
- `loopback-root-cause-triage.md` — the meta-mechanism that would have surfaced
  these at loopback time; these were instead surfaced by a manual retrospective.
- `verified-integrity-consolidation.md` — Class 3's basis-adherence face
  (incomplete evidence reaching [VERIFIED]).
- `instance-domain-invariant-register.md` — **the complementary half of the same
  retrospective.** That item homes the OTHER class from the original analysis: the
  *out-of-scope / inherited / uncharted-surface* bugs (Class 1 in the original split —
  paper-mode idempotency, `signal_id` identity, overtime period-drop), whose fix is a
  *locked cross-unit-invariant register* every unit derives from. THIS item homes the
  *within-scope reasoning-depth* bugs (Class 2 in the original split). They **overlap in
  evidence** (Unit 7 and `signal_id` appear in both, seen from different angles —
  reasoning-depth-at-design-lock here vs locked-invariant there) and together cover the
  retrospective's 6 production bugs.
- beat-the-books `docs/MULTI_STRATEGY_ARCHITECTURE.md` Rev 32 (Unit 21), Rev 34
  (txn-hold), Rev 35 (dead enrichment), Rev 47–51 (Units 26–27) — the
  production bugs; `.clippy/runs/2026-05-27-unit-7-replay-engine.md` (Class 1)
  and `.clippy/runs/2026-05-25-unit-14-data-completeness-pass.md` (Classes 2+3)
  — the Clippy run transcripts where the evidence lives.
