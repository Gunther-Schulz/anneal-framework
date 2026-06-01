# Clippy-run findings — dispatch model/isolation + behavioral-coupling discharge

Working record of three framework/instance findings surfaced by a
clippy run (azuro impl, 2026-05-29) where a single-unit plan was
operator-directed to dispatch. Captured per `development-process.md`
practice 9 (design, then decide, then implement) so the three edit
cycles are recorded before any spec edit. Not spec. Delete or fold
into history once all three cycles close.

Each is a **separate edit cycle** (practice 5: one scope of change per
cycle) at a different level — own re-grounding + skill-craft invocation
when its edits start.

## Finding 1 — model selector silently inert for single-unit plans (RELEASED — clippy v0.9.90, 9ce6ff3)

**Gap.** clippy's `impl` dispatch-model selector
(`coding-clippy/spec/bindings.md` §Dispatch models, "per impl-plan
dispatch unit") applies *at the dispatch boundary*
(`SKILL.md` Dispatch model selection: "At each impl-unit dispatch …
pass it as the Agent call's `model:`"). A single-unit plan runs in
the working context with **no dispatch** (`anneal-framework/spec/core.md`
§4.2 lines 493–496; clippy `phases/implement.md` Dispatch 61–64), so a
**present** `impl: sonnet` runs on the parent (opus). The binding's
Absence-semantics enumerates absent / commented / present-at-dispatch /
malformed — it has **no case for "present, no dispatch boundary."**
The AI pattern-completes it → silent override. Intent (per-unit) vs
mechanism (at-dispatch) diverge for the single-unit case.

**Triage.** Spec gap, not adherence (the AI followed the rules; the
enumeration was loose enough to admit the violating reading —
practice 1). Not auto-battle-caused: the `[READY]` impl-plan preview
(`modules.md` §1.1) never names per-unit model in *either* mode, so
even interactive only lets an operator *infer* it; auto-battle removes
the inference point.

**Level.** Instance-only (clippy). Model-selection has **zero**
framework/template presence (grep `spec/` + `instance-template/`).
Framework §4.2 single-unit→working-context is correct and
model-agnostic — stays untouched.

**Decision (operator, 2026-05-29).** Go the *other* way from
force-dispatch (F1): single-unit plan **stays in the working context on
the parent model; the selector is scoped to dispatched units, by
design.** Rationale: `impl: sonnet`'s cost saving is a multi-unit
phenomenon (many impl dispatches stacking); a single unit on the parent
is a bounded one-off, and the "keep the orchestrator out of impl
context" motivation is cheap to give up for one small unit. The only
residual given up is model-diversity in the verify cross-check for
single-unit runs — which the context-hygiene rationale never required.

**Fix-shape (Cycle 1).** Convert "silent ignore" → "documented scope
limit." (i) `bindings.md` §Dispatch models: state the scope (`impl`
applies per dispatched unit; single-unit working-context → parent
model) + close the absence-semantics enumeration. (ii) `SKILL.md`
Dispatch model selection: render the scope clause. (iii) the
`clippy.config/models` placeholder/README (SKILL.md bootstrap ~334–340):
operator-facing note so the scope is discoverable **at config-write
time**. F1 (force single-unit dispatch to honor the model) = the
behavioral thorough-fix, operator-rejected with cited rationale above.
F2 (per-`[READY]` model surfacing) dropped — documentation handles
discoverability; per-run surfacing would be over-build.

## Finding 2 — worktree isolation excludes the run's non-tracked inputs (RELEASED — framework Cycle F2 + clippy v0.9.91)

**Gap.** A dispatched unit's worktree is `git worktree add <head-commit>`
(`core.md` §4.2 Isolation mechanism 518–546; clippy `implement.md`
91–120) → **tracked files at HEAD only.** The run's gitignored
`.clippy/runs/…` (tracker, standardized-pass artifacts, decompositions,
capture evidence — `bindings.md` Run-artifact persistence; `.clippy/`
gitignored per first-run bootstrap) and the project venv are **absent**.
A unit needing non-tracked input (e.g. curating fixtures from
`.clippy/runs/evidence/*.json`) can't reach it: brief discipline forbids
absolute paths into operator's main; bulk data isn't inline-able;
"Bootstrap is out of scope" (§4.2 541–546) punts the env. Result: the
worktree gets *abandoned* (main-tree dispatch), silently losing
isolation.

**Triage.** Spec gap (the in-run main-tree dispatch was an adherence
deviation against the *current* spec, but its root is the spec
over-applying/under-provisioning the worktree — fix the source, not the
symptom, per practice 1). Now a **multi-unit** problem (single-unit
never dispatches per Finding 1 → W1 "single-unit → main-tree" is moot;
the in-run #2 wouldn't have arisen).

**Level.** Framework (`core.md` §4.2 Isolation mechanism + dispatch-brief)
+ clippy render.

**Constraint shaping the fix.** Concurrent units **must** stay isolated
(parallel-write-safety is the worktree's real job), so multi-unit can't
just fall back to main-tree.

**Fork (resolve at Cycle 2 design surface).**
- **W2a (provision — AI lean):** orchestrator provisions the run's
  non-tracked inputs into the worktree (cwd-relative copy; preserves
  brief discipline). Split the carve-out: framework run-state in scope
  to provision; project deps (venv) stay operator's. Granularity
  sub-question: unit-declared inputs vs whole current-run
  `.clippy/runs/<run>/` (lean: whole-run, bounded + simple).
- **W2b (sanctioned main-tree fallback):** lighter, but invalid when a
  sibling is concurrently in flight → can't cover the parallel case.
  Partial, not a replacement.

## Finding 3 — design-phase grounding is static-blind to behavioral coupling (RELEASED — framework Cycle F3 + clippy v0.9.92)

**Gap.** `target-behavior` is a real coupling shape (`glossary.md`:
"the target's behavior under input classes") — but every discharge
form for it is **static**: the falsification predicate closed set
(`glossary.md` 163–173 + `core.md` §4.1.4) is `any-match` /
`any-outside-scope` / `expected-match`, all computed from a
**search/read result** (§4.1.4: candidate = "a search or read"); the
basis rule (`core.md` §3.2 / `foundations.md`) admits only (a)
search-query, (b) read + one observable fact — both static; the
Coupled-change lens (clippy `lenses.md` 43–51) names behavioral
preservation but specifies no discharge standard → routes to the static
basis. So a behavioral coupling is "falsified" only if it leaves a
textual trace a grep finds. Couplings through inheritance / dispatch /
reflection / validation break at a site that mentions the *subtype*,
not the changed base → invisible to every predicate.

**The n=1 (azuro).** Adding `sort: str` (required) to `RestOutcome`
propagated via inheritance to `EnrichedRestOutcome`, whose enrich
constructs it from a dict lacking `sort` → ValidationError → whole-game
skip → 0 markets in prod. Three design-phase checks all shared the
blind spot: (1) basis "unsupplied-inherited ⇒ None" = recall dressed as
behavioral-parity enumeration; (2) falsification candidate was a
reference-grep on `RestOutcome`, which the break never textually
mentions; (3) the designed guard validated the raw path only, never
exercised enrich. **Caught only** by the implement-phase write-time
Coupled-change self-check applied *behaviorally* (actually constructing
the object) — a backstop accident, which per practice 1 is "partial
recovery, not the intended discipline."

**Level.** Framework (`core.md` §3.2 evidence forms + §4.1.4 / `glossary`
predicate closed set + `modules.md` §3.4) + Coupled-change lens + clippy
render. Domain-general principle ("a behavioral claim needs behavioral
evidence; static search is blind to runtime couplings"); instance binds
what "exercise the path" means.

**Fix-shape.** Add a **behavioral discharge form** to the apparatus,
**mandatory** via a mechanical trigger: **the changed target has
subtypes/implementors** (searchable). When true, a `target-behavior`
candidate discharged by textual search alone is malformed — it must
construct each subtype at its real construction site. Classifies
(practice 8): mechanical trigger (has-subtypes computed) + structural
enforcement (exercised-path artifact).

**Fork (resolve at Cycle 3 design surface).**
- **F3a — design executes:** convergence falsification runs the path.
  Cost: design-phase env needed (collides with Finding 2's worktree
  bootstrap) + blurs the design/implement boundary.
- **F3b — designate to write-time self-check (AI lean):** a
  behavioral-parity claim on a subtype-bearing target is declared
  not-statically-dischargeable → design *flags* it (mechanical trigger
  forces the flag instead of false static [VERIFIED]); discharge
  designated to the implement-phase write-time self-check, made
  mandatory + behavioral for the trigger. Lighter; no design-phase
  execution; matches what actually caught it; corrects design's
  *overclaim* rather than bolting execution onto design.

## Cycle plan

Three separate edit cycles, each via the release loop
(`development-process.md`): diagnose → fix at source → re-render →
verify (step-4 discharge) → operator-approve → commit+push → release
instance. Each gets its own re-grounding (practice 5) + skill-craft
invocation before edits (gate).

1. **Cycle 1 — Finding 1** (instance-only; smallest; decided). clippy
   `bindings.md` + `SKILL.md` + config placeholder. ✓ RELEASED
   v0.9.90 (9ce6ff3); F1 render-fidelity fix applied at step-4.
2. **Cycle 2 — Finding 2** (framework §4.2 + render). W2a adopted
   (provision the run's non-tracked inputs; whole `.clippy/runs/`).
   ✓ RELEASED framework Cycle F2 + clippy v0.9.91; step-4 F1/F2
   applied (source integration-safety guarantee; accurate gitignore
   mechanism in renders).
2.5. **Cycle 2.5 — bindings.md slot-collapse** — ⏸️ DEFERRED (operator,
   2026-06-01) into the planner-exploration **finding-3/finding-4
   cleanup cycle, post-derivation**. Grounding (Cycle 2 step-4 F3
   follow-up) found this is not hygiene but an open fork — finding 3:
   template over-split vs clippy drift — which the dev-note itself
   defers to the planner derivation (still pre-build); leaning now
   pre-empts it and risks a revert. Parked with it: the `implement.md`
   stale citation to a non-existent `anneal-framework/spec/bindings.md`
   (fix-direction touches finding 4's glossary-interface principle) —
   **citation half fixed in Cycle G** (→ `core.md` §4.2); the
   slot-collapse half stays deferred.
3. **Cycle 3 — Finding 3** (framework §3.2.2 + glossary + render;
   highest severity). ✓ RELEASED framework Cycle F3 + clippy v0.9.92.
   Adopted neither F3a nor F3b literally — the refined
   **guard-caught-by-verify**: the instance trigger (target has
   subtypes/implementors) forces the behavioral-parity claim to
   [CONDITIONAL] (design flags, no execution); basis = a guard
   exercising each subtype's construction site, run by verify's
   existing executable verification; fallback = [AUTO-ACCEPTED]
   residual. Tighter than scoped (no §4.1.4/predicate change). Step-4
   F1 cross-reference applied (glossary target-behavior → §3.2.2).

Independence: F3b (no design execution) keeps Cycles 2 and 3
independent. If F3a is chosen, Cycle 3 depends on Cycle 2's worktree
resolution (design-phase env).

## Cycle G — dispatch-model decomposition (RELEASED — framework Cycle G + clippy v0.9.93)

Operator-raised after the cluster shipped: the §4.2 dispatch rule
fused two decisions on unit-count (≥2 → subagent+worktree; 1 →
working context). **Decomposed:** every unit → a subagent (the
orchestrator never does impl in its own context); **worktree iff
parallel-eligible** (reuse the existing marker); sequential/single →
subagent in the operator's **main tree** under a **Main-tree
integrity check** (clean-at-dispatch precondition + HEAD-exact/
clean-tree detect + restore-to-snapshot recover); **spawn failure →
working-context fallback** ("without isolation", mirrors verify).

**Revises shipped cycles** (coherently, removing their root causes):
Cycle 1 — selector now applies to **all** units (single-unit→parent
special case dissolves); Cycle 2 — provisioning scoped to **parallel
worktrees** only (main-tree units read `.clippy/runs/` + venv
natively, so the azuro worktree-friction class can't arise for
single/sequential). Closed the Cycle 2.5 **citation** half.

**Homes:** core.md §4.2 + §6 + glossary (Self-check, Working context)
+ clippy implement.md + SKILL.md + bindings.md. Step-4: 1 blocking
(SKILL.md stale ≥2-trigger remnant, line-wrap-hidden) + 1 notable,
both fixed by a coherent paragraph rewrite.

**Follow-on:** wrap-tolerant practice-4 grep → `development-process.md`
(separate cycle — a line-grep missed the wrapped remnant; only a
newline-flattened scan caught it).
