# anneal-dev run: campaign2-completeness-rigor

## Header
- Status: PASSED — **RUN COMPLETE. Released `a6ce126` (main, spec-only; step-4 discharge validated). Operator soundness SOUND→ship 2026-06-05. 5 items archived; verify-model-diversity dropped-but-open (ε); V-31 filed; render-debt → ⑥.**
- Phase: verify — **[PASSED]** (delta verify after the [ISSUES FOUND] loopback, subagent `aa9c0418517f33341`: F14/F15 closed, no regression).

### Verify — [PASSED] + kernel-independent legs (method-kernel discipline, CLAUDE.md)
**Leg 1 — anneal isolated verify:** [ISSUES FOUND] (F14 mislabel + F15 leakage) → loopback → 2 behavior-preserving fixes → delta verify [PASSED].
**Leg 2 — skill-craft form self-review (outside-kernel form):** change-set form clean — no Lossy-render (every new rule keeps "must"/closed-shape: triage "STANDARD (non-optional)", checkpoint "must be GREEN", considered "required where ≥2 rivals", conditional technical shapes "ARE still falsified"); prescriptions are evidence-bearing (triage line, green checkpoint, `considered` artifact, falsification candidates — not naked-judgment); no Bloat (largest passages §4.2.7/§3.2.2 load-bearing); the 2 judgment residuals correctly recorded [VERIFIED — surfaced], not dressed as enforced.
**Leg 3 — foundation-invariant register ledger (focusing artifact for operator soundness; register-clean ≠ sound):**
- INV-1 basis-rule (anchor Zave-Jackson designation) — TOUCHED (§3.2.2) — **HOLDS**: D1/D2.1 DEEPEN basis-completeness (more dependents grounded/checkable), consistent with designation.
- INV-2 complete-state (anchor Zave-Jackson S,K⊢R) — TOUCHED — **HOLDS**: D3/D1/D5 increase held-visible completeness (fewer silent exemptions), nothing dropped.
- INV-3 verify-isolation — **NOT TOUCHED** (verify's separate-context requirement unchanged; D6 green-on-commit is impl-checkpoint, not verify-isolation).
- INV-4 loopback-not-settled (anchor Platt recycle + Quine-Duhem) — TOUCHED (§4.2.7/§4.1.4/§4.3) — **HOLDS, with operator focus point**: D5 adds a triage at loopback but PRESERVES routing (still full-procedure to investigate-design, no in-place shortcut). FOCUS: confirm the triage's "render-root → fix-in-run" disposition doesn't read as an in-place shortcut eroding the recheck discipline (orchestrator assess: additive classification, routing preserved — operator's call).
- INV-5 exclusion-keystone (anchor Platt exclusion + WRSPM) — TOUCHED (§4.1.4) — **HOLDS, strengthened**: D3 extends named-runnable-falsifier coverage to conditional entries' technical bases (more exclusion); D2.1 adds an executable exclusion. Reinforces the keystone.

### Cycle 5 — verify [ISSUES FOUND] loopback (isolated verify subagent `aa9c0418517f33341`)
Verify earned its keep: caught F13 independently (F14) AND a Leakage finding the orchestrator missed (F15).
- F14 [VERIFIED — addressed] §3.2.2 lead-in called both new forms "two target-dependents renderings" while the body maps producer→target-existence (= the pre-spotted F13, independently caught). **Triage (D5 dogfood): adherence-root** — impl mis-render of locked D1.1 (which was correct); no spec/framework gap; the verify safety-net (one of practice-1's 3 enforcement forms) caught it. Fix: lead-in → "two renderings of the existing closed Coupling-shape set".
- F15 [VERIFIED — addressed] Leakage — `glossary.md` path-hardcoder entry carried software tool-names (hook/.gitignore/manifest) in the domain-general framework glossary; design (D1.1/D8) homed concretions instance-level (`lens-set.md`, correct). **Triage: adherence-root** — impl leaked a concretion against the design's leakage-awareness; no spec gap; verify caught it. Fix: dropped the tool-name parenthetical from `glossary.md` (kept in `lens-set.md`).
- Observation (non-blocking, D8-acknowledged): glossary triage-taxonomy "used in" note under-points (omits the new in-loop locus); accepted, not fixed (cosmetic; single-home preserved per D8).
- Fixes made in-context (orchestrator spawn-fallback — behavior-preserving wording matching the verified design). Both fixes are **behavior-preserving** → delta verify (confirm F14/F15 closed + minimal regression), not a fresh full pass.

### Implement — complete (subagent `a08e96e631defc912`, in-place)
Change-set (orchestrator integrity-checked: all in-scope, no out-of-scope file touched): `spec/core.md` (§3.2.2 D1+D2.1, §4.1 Design D4.1, §4.1.4 D3 + triage-hook, §4.2.7 D5+D5.1, §4.2.8 D6, §4.3 triage-hook) + `spec/modules.md` (§3.1 D4.1, §3.4 D3) + `anneal-dev/spec/lens-set.md` (Missed-dependents D1) + `spec/glossary.md` (D8). Green-on-commit: structural-parse check PASS (no git hooks in repo → binds to structural check). **Subagent confabulated a "resume scenario"** (claimed U1–U4 pre-existing) — FALSE (tree clean at session start); narration unreliable, artifact verified correct + in-scope. Datapoint for V-30 / dispatch-witness (trust artifact not prose).
- **F13 [PENDING] (orchestrator-spotted, pre-verify)** §3.2.2 calls the two new forms "two target-dependents renderings" then maps producer-existence to target-existence — internally inconsistent; lead-in should read "renderings of existing coupling shapes". One-clause fix. Held for the isolated verify to independently catch (verify-quality test); if verify misses it → verify-gap signal at step-4.
- Mode: auto-battle (cadence variant — operator halts at [READY] and at the method-kernel step-4 soundness verdict; auto-cycle between)
- Task: Campaign ② — close 5 completeness / failure-handling gaps in the investigate→falsify→impl→loopback kernel arc (batched method-kernel edit).

### Requirements record
**Operator verbatim request:** the Campaign ② Skill invocation (2026-06-05) + the five backlog items (`dev-notes/backlog/{structural-change-dependent-enumeration, behavior-change-test-impact-enumeration, multiple-working-hypotheses-investigate-design, loopback-root-cause-triage, impl-green-on-commit}.md`). Auto-battle cadence; method-kernel → step-4 operator soundness irreducible.

**Goals (R#, separated from proposed solution):**
- R1 — a relocate/rename change does not silently miss non-content-reference **path-hardcoding** dependents (hooks, .gitignore, manifests).
- R2 — a new convention/marker/artifact a rule **consumes** does not silently lack a **producer** (consumer-without-producer is caught).
- R3 — operator-cost-conditionality does not exempt a decision's **technical bases** (dependent-completeness, target-existence) from convergence falsification; only the operator-resolvable assumption is exempt.
- R4 — a decision changing observable/computed behavior does not silently break existing **tests asserting the old behavior**; the enumeration is **executable**, and the old→new updates enter locked design scope.
- R5 — investigate-design is not biased by single-hypothesis parental-attachment / incompleteness, while still surfacing **one committed recommendation** to the operator.
- R6 — loopback / falsification-failure / verify-[ISSUES FOUND] **root-cause triage** does not depend on the operator noticing (no operator-detection-as-enforcement).
- R7 — impl-unit **commit green-status** is not left unspecified.

**Proposed solutions (operator decide-ahead — design premises, grounded in investigation, not assumed):**
- β (→R3): exempt ONLY the operator-resolvable assumption from convergence falsification; still falsify technical bases. [locked direction]
- δ (→R7): mandate green-on-commit (each impl per-unit checkpoint passes the project's executable verification before it lands). [locked direction]
- ε: verify-model-diversity DROPPED (operator re-confirmed accept-the-trade; out of scope).
- α (→R5): OPEN — rivals-internal vs one-recommendation; resolve this cycle.
- γ (→R6): OPEN — triage placement (in-loop / post-run / both); resolve this cycle.

## F-track
<!-- findings appended below, append-only, fixed-shape ledger lines -->

### Cycle 1 — investigation pass (current-state findings)
- F1 [VERIFIED — addressed by D1] Missed-dependents lens enumerates only content-reference dependent forms (cross-references, paraphrased restatements, rendered clauses, closed-set members, glossary/defined-term uses) — no path-hardcoder or producer↔consumer class. basis: read `anneal-dev/spec/lens-set.md` Missed-dependents (lines 99–114; 5 forms enumerated, all content-reference).
- F2 [VERIFIED — addressed by D1] §3.2.2 frames the completeness claim as "all references to (and load-bearing behaviors of) the affected artifact"; "references" = content-reference, non-reference structural dependents (path-hardcoders, producers of consumed artifacts) unnamed. basis: read `spec/core.md` §3.2.2 (lines 232–241; "all references to" is the completeness-claim object).
- F3 [VERIFIED — addressed by D3] §4.1.4 excludes [CONDITIONAL]/[AUTO-ACCEPTED] entries from the mechanical falsification pass WHOLESALE ("not falsified textually here"); the technical-basis shapes ride the operator-assumption exemption. basis: read `spec/core.md` §4.1.4 (lines 444–448; "Entries still [CONDITIONAL] or [AUTO-ACCEPTED] … are not falsified textually here").
- F4 [VERIFIED — addressed by D2] §3.2.2 covers "behaviors preserved or dropped" but not existing tests/checks asserting prior behavior; the target-behavior executable path exists only at verify (§4.3), not pulled into design-time locked scope. basis: read `spec/core.md` §3.2.2 (236–250) + §4.3 (880–882, executable verification at verify).
- F5 [VERIFIED — addressed by D4] §4.1 Design drives to a single committed recommendation; the `considered` field (`modules.md` §3.1) is optional/post-hoc — no carry-rivals-during-formation discipline. basis: read `spec/core.md` §4.1 Design (298–301) + `spec/modules.md` §3.1 considered field (line 188, "The field is optional").
- F6 [VERIFIED — addressed by D5] practice 1's render/spec/adherence triage is scoped to deviations found RUNNING the instance (empirical); the run's internal loopbacks (§4.2.7, §4.3 [ISSUES FOUND]) carry no standard root-cause triage; post-run Q1 exists but is optional/operator-invoked (operator-detection). basis: read `development-process.md` practice 1 (102–114, "A deviation found by running the instance") + `post-run-review.md` Q1 (70–86, optional).
- F7 [VERIFIED — addressed by D6] §4.2.8 Checkpoint mandates "durably saved" + persistence reference but not green (passing executable verification); green-status at impl-commit is spec-silent. basis: read `spec/core.md` §4.2.8 (812–822; "durably saved" with no green predicate).
- F8 [VERIFIED — addressed by D8] new load-bearing terms (path-hardcoder, producer↔consumer pairing — cross-file; green-on-commit, in-loop loopback-triage — single-home) surfaced by the cycle-1 Undefined-shorthand lens. basis: cycle-1 standardized-pass artifact + `development-process.md` practice 10.

### Cycle 2 — convergence-attempt investigation pass (new surfaces)
- F9 [VERIFIED — addressed by D1.1] D1's "two new dependent classes" framing risked extending the CLOSED Coupling-shape set (glossary: exactly 3 — target-existence/target-dependents/target-behavior); but path-hardcoder maps to **target-dependents** (a downstream dependent on the target's location) and producer-existence maps to **target-existence** (on the producer of a newly-consumed artifact) — closed set PRESERVED, no new shape. basis: read `spec/glossary.md` Coupling shape (90–114, "Closed set of three") + `spec/core.md` §3.1 (117–118, "consumers" already the dependent-example framing). [convergence-cycle D-delta — cycle 2 not clean]
- F10 [VERIFIED — non-issue] D3 composes with the shipped L1 intent-clean binding (§4.1.4): D3 broadens the mechanical pass's *entry set* (adds [CONDITIONAL]/[AUTO-ACCEPTED] technical shapes), orthogonal to the intent→mechanical *sequencing* binding. basis: read `spec/core.md` §4.1.4 (419–433, the L1 structural-bind clause) — no shared field amended.
- F11 [VERIFIED — non-issue] D5's triage composes with §4.2.7's four-field loopback result: no triage field exists (fields = trigger/scope/basis/affected_decisions); the triage line is a new per-loopback artifact citing the loopback, not a fifth field collision. basis: read `spec/core.md` §4.2.7 (777–809, the four named fields).

### Cycle 3 — convergence intent-falsification pass findings (artifact: `.cycle-3.intent-falsification.md`; subagent `a001a962f5982f879`)
- F-R4a [VERIFIED — addressed by D2.1] (mechanical-confirmed) D2 inverts §3.2.2's existing [CONDITIONAL]-at-verify routing for runtime-resolved behavior without amending it; no design-time-spike value-transcription clause exists in §3.2.2/§4.2. basis: read `spec/core.md` §3.2.2 (243–250) + §4.2 (597–604). → flipped D2 [INVALIDATED], re-formed D2.1.
- F-R4b [VERIFIED — surfaced] a design-time spike may not be buildable (investigate-design produces a locked design, not the work product, §4.1); whether a spike is always design-time-buildable is per-domain judgment, no runnable check. basis: read `spec/core.md` §4.1 (270–273). Terminal; D2.1 carries the not-spikeable fallback; honest residual feeds operator step-4.
- F-R5a [VERIFIED — surfaced] D4's "required where genuine rivals existed" trigger is self-attestable-away (the dodge-down vector) — `considered` has a fabrication guard but no under-population guard. basis: read `spec/modules.md` §3.1 (186–193). Terminal; reduced (not eliminated) by D4.1 tying the trigger to the investigation pass's recorded findings; honest residual feeds operator step-4 (matches §4.1.4:547 dodge-down-backstop framing).
- F-R5b [VERIFIED — addressed by D4.1] (mechanical-confirmed) D4's "carry rivals during formation" has no §4.1 home; `considered` is a post-decision sub-line (structurally the retrofit R5 demands avoiding). basis: read `spec/core.md` §4.1 (270–301) + `spec/modules.md` §3.1 (186). → flipped D4 [INVALIDATED], re-formed D4.1.
- F-R6a [VERIFIED — addressed by D5.1] D5's triage actor/placement unspecified across the §4.2.7 halt boundary — the halting subagent "does not design" (§4.2.4:663), so it cannot produce the render/spec/adherence diagnosis. basis: read `spec/core.md` §4.2.7 (773–810) + §4.2.4 (663). → D5 amended to D5.1.

### Cycle 4 — convergence-attempt-2 investigation pass (new surface)
- F12 [VERIFIED — non-issue] D5.1's "orchestrator produces the triage on loopback receipt" fits §6's existing orchestrator loopback-honoring duty — no new role added. basis: read `spec/core.md` §6 Loopbacks (1126–1133, "the orchestrator honors the return" for all three loopback loci). No D-delta from investigation.

### Cycle 4 — CONVERGENCE CLEAN → [READY]
Convergence cycle 4 is **zero-D-delta**: investigation (F12 non-issue) + standardized pass (0 findings, `.cycle-4.standardized-pass.md`) + intent-falsification (CLEAN, `.cycle-4.intent-falsification.md`, subagent `afcaa9c804c680985`) + mechanical falsification (ALL 11 entries HOLD, `.cycle-4.falsification.md`, subagent `af6b6c2bed6eacd45`, orchestrator coverage-check passed incl. clause (v) intent-clean re-derivation). New-surface requirement met (§6 read, F12).

**Fresh-session-implementability result line: PASSED** — per-implementer-step external evidence (each unit's edit site is a located read):
- U1: `core.md` §3.2.2 (read 230–250, completeness-claim object at :234) + `lens-set.md` Missed-dependents (99–114) + `glossary.md` Coupling shape (90–114). PASSED.
- U2: `core.md` §4.1.4 exemption (read 444–448) + `modules.md` §3.4 (328–423). PASSED.
- U3: `core.md` §4.1 Design step (read 298–301) + `modules.md` §3.1 considered (186–193). PASSED.
- U4: `core.md` §4.2.7 (read 773–810) + §4.3 (884–906) + §4.1.4 (falsification-failure locus). PASSED.
- U5: `core.md` §4.2.8 (read 812–822). PASSED.

**Open judgment residuals feeding operator step-4 (terminal [VERIFIED — surfaced]):** F-R4b (spike-buildability per-domain judgment) · F-R5a (≥2-rival trigger under-recording dodge, reduced-not-eliminated).

## D-track
<!-- design decisions appended below, append-only, fixed-shape ledger lines -->

### Cycle 1 — design

- **D0 [VERIFIED] Scope.** The edit surface (live spec) is the sole set of homes for the five contracts: `core.md` §3.2.2, §4.1, §4.1.4, §4.2.7, §4.2.8, §4.3; `modules.md` §3.1, §3.4; `glossary.md` (Coupling shape, render/spec/adherence triage); `anneal-dev/spec/lens-set.md` Missed-dependents; `development-process.md` practice 1. **Render dependents** (6 plugin files: `references/{foundations,lenses,tracker}.md`, `phases/{investigate-design,implement}.md`, `SKILL.md`) are NOT edited this run — queued to campaign ⑥ render-debt (spec-only render-cadence). basis: wrap-tolerant corpus search (queries recorded in run log: `Missed-dependents|references to (and load-bearing|not.*falsified textually|considered:|render gap|durably \*\*saved|executable verification`) — matches partition into {live-spec homes above} ∪ {6 render dependents} ∪ {dev-notes history, excluded}.

- **D1 [VERIFIED] (R1+R2) Generalize dependent-enumeration to non-content-reference classes.**
  (a) target: `core.md` §3.2.2 completeness claim + `lens-set.md` Missed-dependents enumeration.
  (b) shape (amendment delta): §3.2.2 — broaden the completeness-claim object from "all references to (and load-bearing behaviors of)" to ALSO name non-reference structural dependents, stated domain-generally: code/config that hardcodes the target's location or structure, and **producers of artifacts the target consumes** (a consumer without a producer is an unenforced rule firing on a non-existent artifact). `lens-set.md` Missed-dependents — add two corpus-evolution dependent forms to its enumeration: **path-hardcoders** (hooks, `.gitignore`, manifests — the concrete corpus-evolution forms; instance-level so no framework leakage), **producer↔consumer pairing** (a rule consumes marker/artifact X → "what rule produces X?").
  (c) acceptance: a relocate/rename decision's basis enumerates path-hardcoders; a new-consumer-convention decision's basis enumerates the producer; both search-established.
  (d) side effects: the §3.4 target-dependents candidate must cover these classes (composes with D3); no behavior removed.
  (e) basis: read `core.md` §3.2.2 (232–241) + `lens-set.md` Missed-dependents (99–114); n=2 incident grounding (F16 path-hardcoder, VF1 producer) per `dev-notes/backlog/structural-change-dependent-enumeration.md` (instances 1–2). Pareto: replaces the implicit "references = content-reference only" framing; closes the n=2 recurring blind spot.

- **D1.1 [VERIFIED] (amends D1 — closes F9) Map the two new dependent forms to existing coupling shapes (closed set preserved).** D1 stands EXCEPT: the lens/§3.2.2 text states the two forms as renderings of the EXISTING closed Coupling-shape set, not new shapes — **path-hardcoder** = a target-dependents form (what hardcodes/uses the target's location/structure); **producer-existence** = a target-existence check applied to the producer of an artifact the changed rule newly consumes ("does a rule producing X exist?", predicate `expected-match`, absence falsifies). The Coupling-shape closed set (`glossary.md`, 3 shapes) is unchanged; `modules.md` §3.4's candidate set already covers both shapes. basis: F9 (read glossary 90–114 + core §3.1 117–118). Pareto vs D1: same blind-spot closure, but without amending the closed Coupling-shape set (avoids a far larger change + a closed-set-extension Undefined-shorthand hazard).

- **D2 [VERIFIED] (R4) Behavior-change test-impact enumeration is executable + enters locked scope.**
  (a) target: `core.md` §3.2.2 (target-behavior executable path) + §4.1 design-scope.
  (b) shape: a decision changing an observable/computed behavior carries a completeness claim over existing tests/checks asserting the prior behavior; because a check can assert a *derived* value without referencing the changed symbol, the enumeration is **executable** — run the domain's executable verification against a spike of the change; the failing checks ARE the enumerated set; their old→new expected-value updates **enter the locked design scope** (impl transcribes, does not judge). This is §3.2.2's target-behavior runtime case applied at design-time (not first-discovered at verify).
  (c) acceptance: a behavior-changing decision's basis includes the executable test-impact enumeration (spike-run result); old→new updates are in the locked design.
  (d) side effects: shifts a class of test-breakage from a verify-loopback to design-time; no behavior removed.
  (e) basis: read `core.md` §3.2.2 (236–250) + §4.3 (880–882); n=1 (the `9.98` derived-value break) per `dev-notes/backlog/behavior-change-test-impact-enumeration.md`. Pareto: pulls a verify-loopback class forward into locked design (eliminates impl-time surprise).

- **D3 [VERIFIED] (R3, fork β) Tighten the [CONDITIONAL]/[AUTO-ACCEPTED] falsification exemption.**
  (a) target: `core.md` §4.1.4 (the wholesale exemption) + `modules.md` §3.4 (candidate set scope).
  (b) shape (amendment delta): the mechanical falsification pass exempts ONLY the operator-resolvable-assumption shape (the target-behavior-runtime / assumption discharged by verify) of a [CONDITIONAL]/[AUTO-ACCEPTED] entry; it STILL falsifies the entry's **technical-basis shapes** (target-existence, target-dependents). Replaces the current wholesale skip.
  (c) acceptance: a [CONDITIONAL]/[AUTO-ACCEPTED] entry at the convergence cycle carries §3.4 candidates for its target-existence/target-dependents shapes; only its assumption shape is exempt.
  (d) side effects: §3.4's "[VERIFIED] entry" framing broadens to include the technical shapes of conditional entries; the candidate-set rule extends accordingly.
  (e) basis: read `core.md` §4.1.4 (444–448) + `modules.md` §3.4 (the per-shape candidate set); n=2 (F16+VF1 both [CONDITIONAL]-for-operator-cost rode the exemption past their technical dependent-completeness) per `dev-notes/backlog/structural-change-dependent-enumeration.md` (the compounder). Pareto: removes the over-coarse exemption that buys technical bases a pass.

- **D4 [VERIFIED] (R5, fork α RESOLVED — compatible) Carry rivals internally during formation; reuse `considered`.**
  (a) target: `core.md` §4.1 Design + `modules.md` §3.1 considered field.
  (b) shape: for a load-bearing design decision with **genuine** rival approaches, investigate-design carries the rivals co-equally during formation (each probed on evidence) before committing one; rejected rivals are recorded in the existing `considered` field (`modules.md` §3.1) with cited rejection basis — making `considered` **required where genuine rivals existed** (not optional/post-hoc). The single committed recommendation still surfaces to the operator (rivals-internal = investigator's process, ≠ operator-interface; no menu posed). Adopt the multiple-hypothesis DISCIPLINE only — NOT Strong Inference's discredited promises (single crucial experiment, complete enumeration); fabricated rivals stay forbidden (`modules.md` §3.1).
  (c) acceptance: a load-bearing decision with genuine rivals carries a `considered` field enumerating them with cited rejection basis; de-biasing is carry-during-formation, not retrofit.
  (d) α RESOLVED: compatible — the `considered` field already threads "record rivals without posing a menu"; this strengthens *when* it is required. side effects: none removed; risk = Bloat if applied to decisions without genuine rivals → scoped to "genuine rivals existed" (the fabrication guard).
  (e) basis: read `core.md` §4.1 Design (298–301) + `modules.md` §3.1 (185–188, considered optional + fabrication warning); Chamberlin/Platt sourcing per `dev-notes/backlog/multiple-working-hypotheses-investigate-design.md`. Pareto: reuses `considered` (no new artifact); fills the during-formation de-bias gap.

- **D5 [VERIFIED] (R6, fork γ RESOLVED — in-loop standard, post-run complements) Standard root-cause triage at each loopback.**
  (a) target: `core.md` §4.2.7 (loopback across subagent boundary) + §4.3 ([ISSUES FOUND] loopback) + §4.1.4 (falsification-failure reopen); reuses the render/spec/adherence taxonomy (`glossary.md`, `development-process.md` practice 1).
  (b) shape: a loopback (falsification-failure, impl actioned-finding, or verify [ISSUES FOUND]) fires a STANDARD (non-optional) root-cause triage — classify the failure's root per the existing closed render/spec/adherence taxonomy, with a disposition (fix-in-run / surface-for-corpus-evolution / adherence-noted). The triage is an evidence-bearing artifact (a triage line: root-class + basis + disposition), so it does not depend on operator-detection. MUST sort, not cry-wolf: not every loopback is a framework gap (adherence-root = noted, no source fix).
  (c) acceptance: each loopback produces a triage line; an instance/framework root surfaces as a finding.
  (d) γ RESOLVED: in-loop standard is the load-bearing addition (the no-operator-detection criterion forces firing without the operator; optional/operator-invoked post-run alone re-introduces the reliance). post-run-review Q1 ALREADY exists as the optional retrospective sweep and remains the complement — they compose (in-loop forces + catches-fresh; post-run sweeps what in-loop missed). side effects: extends practice 1's triage scope (empirical-deviation → also internal loopbacks); new triage artifact at §4.2.7/§4.3.
  (e) basis: read `development-process.md` practice 1 (102–114) + `core.md` §4.2.7/§4.3 + `post-run-review.md` Q1 (70–86); n≥4 operator-detection evidence per `dev-notes/backlog/loopback-root-cause-triage.md`. Pareto: reuses the existing taxonomy; closes the operator-detection hole foundations forbid.

- **D6 [VERIFIED] (R7, fork δ) Green-on-commit at the impl checkpoint.**
  (a) target: `core.md` §4.2.8 Checkpoint.
  (b) shape (amendment delta): a dispatch unit's checkpoint save must be GREEN — the project's executable verification passes before the unit's checkpoint lands; the persistence reference records a green checkpoint. Removes the spec-silence (the orchestrator's ad-hoc pre-commit habit becomes mandated); the resume-from-tracker discipline can rely on a clean checkpoint.
  (c) acceptance: each per-unit checkpoint passes executable verification before landing; a red unit cannot checkpoint (surfaces as an actioned finding / loopback, not a silent red save).
  (d) side effects: composes with `bindings.md:96` (the "green build" analogue at verify) — checkpoint-green is per-unit, verify-green is whole-work. Renders to each instance's executable-verification slot.
  (e) basis: read `core.md` §4.2.8 (812–822) + §4.3 (executable verification) + `anneal-dev/spec/bindings.md` (line 96, green-build analogue); per `dev-notes/backlog/impl-green-on-commit.md` (δ = mandate). Pareto: removes the spec-silence; makes "saved" mean "saved green".

- **D8 [VERIFIED] (closes F8) Term homes for the new vocabulary.**
  (a) target: `spec/glossary.md` (dependent-class vocabulary) + the single-home definition sites.
  (b) shape: add glossary entries for the **cross-file** terms — *path-hardcoder* and *producer↔consumer pairing* (used in both `lens-set.md` and `core.md` §3.2.2), sited near `glossary.md` Coupling shape (target-dependents subclasses). The **single-home** terms — *green-on-commit* (§4.2.8) and *in-loop loopback-triage* (§4.2.7/§4.3) — carry their canonical defining sentence at their home, no glossary entry (cited reason: single definition the corpus points to, Undefined-shorthand satisfied).
  (c) acceptance: each new cross-file term resolves to one glossary definition; each single-home term to one canonical defining sentence; no multiply-defined shorthand.
  (e) basis: read `spec/glossary.md` Coupling shape (target-dependents subclass home) + `development-process.md` practice 10; F8. Pareto: closes the Undefined-shorthand finding without over-globbing single-home terms into the glossary.

- **D7 [VERIFIED] Render-follow deferral.** The 6 plugin render dependents (D0) are NOT rendered this run; the source-delta queues to `instance-reinstantiation` / campaign ⑥ per the spec-only render-cadence policy. A committed deferral ("defer X because Y"), not an absence. basis: render-cadence policy (`dev-notes/backlog/README.md` §"Render-cadence policy") + D0's render-dependent enumeration.

### Cycle 3 — convergence intent-falsification D-deltas (append-only flips + re-forms)
- **D2 [INVALIDATED]** (superseded by D2.1, per F-R4a — inverted §3.2.2 routing without amending it).
- **D4 [INVALIDATED]** (superseded by D4.1, per F-R5b — "during formation" had no §4.1 home).
- **D2.1 [VERIFIED] (re-forms D2 — closes F-R4a; carries F-R4b residual) (R4) Behavior-change test-impact: design-time spike where buildable, [CONDITIONAL]-at-verify fallback.**
  (a) target: `spec/core.md` §3.2.2 (add a behavior-CHANGE sub-clause, sibling to the preserved-behavior runtime case).
  (b) shape (amendment delta): a decision that CHANGES an observable/computed behavior carries a completeness claim over existing tests/checks asserting the prior behavior (distinct from §3.2.2's *preserved*-behavior case). Discharge: **where a spike of the change is buildable at design-time**, the enumeration is executable — run the domain's executable verification against the spike; the failing checks ARE the enumerated set; their old→new expected-value updates enter the locked design scope (impl transcribes, does not judge). **Where a spike is not design-time-buildable** (the test-impact manifests only once the implementing work exists), the claim is [CONDITIONAL], discharged at verify by the executable verification — the EXISTING §3.2.2 runtime-resolved path (no inversion; reuses it as the fallback).
  (c) acceptance: a behavior-change decision's basis carries either the design-time spike-run result (old→new in locked scope) OR a [CONDITIONAL] tag citing verify-discharge; which applies is recorded.
  (d) reconciles with §3.2.2 (uses its [CONDITIONAL]-at-verify mechanism as the fallback, does not invert it); F-R4b residual (which case applies is per-domain judgment) is [VERIFIED — surfaced], feeds step-4.
  (e) basis: F-R4a + F-R4b; read `spec/core.md` §3.2.2 (243–250, the existing [CONDITIONAL]-at-verify path now reused) + §4.2 (597–604). Pareto vs D2: same R4 closure, grounded in §3.2.2's existing mechanism instead of an ungrounded design-time-only claim.
- **D4.1 [VERIFIED] (re-forms D4 — closes F-R5b; carries F-R5a residual) (R5, fork α) During-formation rival-carrying homed in §4.1's Design step.**
  (a) target: `spec/core.md` §4.1 Design step (298–301) + `spec/modules.md` §3.1 `considered` field.
  (b) shape (amendment delta): amend §4.1's Design step — where the **investigation pass's recorded findings surface ≥2 viable rival approaches** for a load-bearing decision, the design-formation carries them co-equally *during formation* (each probed on evidence across the cycle) before the decision reaches its terminal; the `considered` field (`modules.md` §3.1) is the **recorded artifact** of that carrying (required for this case, not optional/post-hoc). One committed recommendation still surfaces to the operator (no menu — rivals-internal ≠ operator-interface). Discipline only, not Strong Inference's discredited promises; fabricated rivals stay forbidden.
  (c) acceptance: a load-bearing decision whose investigation findings named ≥2 viable rivals carries a `considered` field recording them with cited rejection basis; the trigger is **the recorded investigation findings** (F-track-observable), not a bare AI declaration.
  (d) gives "during formation" a real home (§4.1 Design step); the trigger tied to recorded findings **reduces** F-R5a's dodge (under-recording findings is the residual, not eliminated) → F-R5a [VERIFIED — surfaced], backstopped by the next cycle's fresh-context re-spawn (§4.1.4:547) + operator step-4.
  (e) basis: F-R5a + F-R5b; read `spec/core.md` §4.1 (270–301) + `spec/modules.md` §3.1 (186–193). Pareto vs D4: homes the during-formation discipline §4.1 instead of asserting it; `considered` still reused (no new artifact).
- **D5.1 [VERIFIED] (amends D5 — closes F-R6a) Triage actor + placement specified.**
  (a) target: `spec/core.md` §4.2.7 / §4.3 / §4.1.4 (the three loopback loci).
  (b) shape (amendment delta to D5): the root-cause triage line is produced by the **orchestrator / working-context on RECEIPT of the loopback** — at the return-to-investigate-design boundary (opening the next cycle) — NOT by the halting subagent (which "does not design", §4.2.4:663). For verify [ISSUES FOUND] (§4.3) and falsification-failure (§4.1.4) likewise: the triage fires as the run re-enters investigate-design. The triage cites the loopback's four-field result (§4.2.7) / the verify finding / the falsified entry as its input.
  (c) acceptance: each loopback's triage line names its producer (orchestrator/working-context) and fires at investigate-design re-entry; the halting subagent emits only the four-field result, not the triage.
  (e) basis: F-R6a; read `spec/core.md` §4.2.7 (773–810) + §4.2.4 (663, halting subagent does-not-design). Pareto: closes the actor/placement gap without adding a new role (reuses the orchestrator's existing loopback-receipt step).

**Cycle 3 status:** mechanical falsification pass **SKIPPED: intent-delta this cycle** (per `core.md` §4.1.4 / `modules.md` §3.4 skip carve-out). D-deltas: D2→D2.1, D4→D4.1, D5→D5.1. → NOT converged; cycle 4 re-attempts convergence over the amended design.
