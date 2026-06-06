# Run: anneal-dev-model-tier-policy

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** Pin anneal-dev subagent dispatches to the top model tier (rule in
  `anneal-dev/spec`, value in `anneal-dev.config`) — a method-kernel edit
  (`anneal-dev/spec/*`), spec-only (render deferred to the batch).

## Requirements record

Verbatim request: "ok let's tackle the next backlog item" → resolves to the
operator-chosen NEXT-UP item `dev-notes/backlog/anneal-dev-model-tier-policy.md`
(operator-authored design sketch is the requirements source).

- **R1** — Every anneal-dev subagent dispatch (all kinds: investigate-side
  falsification, impl, verify, both convergence passes) runs on the top /
  most-capable model tier — never cost-downgraded. Blanket, not per-dispatch
  "is this one sensitive?" judgment.
- **R2** — The tier value is operator-editable without a spec edit (lives in
  `anneal-dev.config`, not spec prose).
- **R3** — No literal model name in the framework spec prose (harness-agnostic;
  a model name there is contract-1 leakage + a staleness trap).
- **R4** — Honest framing: a FLOOR (don't handicap sensitive judgment), NOT a
  safety guarantee that substitutes for structural robustness.
- **R5** — Scope is anneal-dev only; other instances keep the framework default
  (per-task model choice).

---

## F-track (findings)

- **F1** [VERIFIED — non-issue] No model/tier/Sonnet/Opus/cost-downgrade concept
  exists anywhere in the spec corpus today — the contract is wholly new, so the
  change has no pre-existing dependents to update (Fragmentation/Missed-dependents
  clean by construction). — basis: `grep -rniE "\b(model tier|model-tier|top tier|sonnet|opus|haiku|cost-downgrad|downgrad|most capable)\b" --include=*.md .` (excl. dev-notes/.anneal-dev) → empty.
- **F2** [VERIFIED — non-issue] `foundation.md` contract 3 names
  "dispatch-orchestration mechanics" as instance domain-binding scope, "with no
  upstream home — the architecture's instance slot, not framework gaps" — the
  model-tier policy IS dispatch-orchestration mechanics, so it belongs at the
  instance level (anneal-dev/spec) with NO framework-spec change. — basis:
  `foundation.md`:32-39 contract 3, located read, the enumerated member
  "dispatch-orchestration mechanics".
- **F3** [VERIFIED — non-issue] Framework dispatch is harness-agnostic on the
  model: every dispatch site (`core.md` §4.2.2 impl, §4.3 verify, §4.1.4 both
  convergence passes) says "dispatched to a subagent" and names no model — so
  the model is an instance/render concretion, and naming one in the framework
  spec would violate contract 1. — basis: `spec/core.md`:604 ("Every unit is
  dispatched to a subagent"), §4.3:795, §4.1.4:420 — located reads, no model token.
- **F4** [VERIFIED — addressed] anneal-dev precedent: the closed slot-set is
  respected by placing new concretions as binding refinements in `bindings.md`
  (verification battery, wrap-tolerant search), not as invented slots; and
  bindings.md already carries a cross-cutting dispatch-discipline section
  (Skill-craft invocation) that is not a table row. — basis:
  `anneal-dev/derivation-rationale.md`:80-88 (binding-refinement-not-slot
  precedent); `anneal-dev/spec/bindings.md`:210-219 (Skill-craft invocation
  section). Disposition: addressed by D2.
- **F5** [VERIFIED — surfaced] INV-3 (verify isolation) interaction: the policy
  pins verify + the convergence falsification/intent-falsification dispatches to
  the SAME top tier as the working context. INV-3's external anchor (Panickssery
  et al., NeurIPS 2024) warns a verifier sharing the actor's base model inherits
  self-preference bias (model-diversity > self-verification). The kernel's INV-3
  mechanism is CONTEXT-isolation (fresh subagent), which the policy leaves
  intact; the policy sets tier, not diversity, and never regressed diversity
  (dispatches already shared the session model). It does, however, stand in
  tension with a future model-diversity-for-verify sharpening. — basis:
  `dev-notes/foundation-invariants/INV-3-verify-isolation.md` (anchor); `spec/core.md`:795-812
  (INV-3 mechanism = context-isolation, no model claim). Routed to D7 + relate to
  `multivoter-verify-no-predicate-claims`; pure-judgment, no runnable check →
  terminal at [VERIFIED — surfaced], feeds operator soundness pass.

---

## D-track (design decisions)

- **D1** [VERIFIED] **Scope.** The contract ("anneal-dev dispatch model-tier
  policy") is new; the change touches: `anneal-dev/spec/bindings.md` (the rule,
  new section); `anneal-dev.config/model-tier.md` (the value, created this run =
  `opus`); `anneal-dev.config/README.md` (one-line override-visibility note);
  `dev-notes/backlog/instance-reinstantiation.md` (append source-delta to the
  render-debt queue); `dev-notes/backlog/anneal-dev-model-tier-policy.md` (→
  archive on ship) + relate-note into `multivoter-verify-no-predicate-claims.md`.
  Render of `anneal-dev/plugin/skills/anneal-dev/*` is DEFERRED (spec-only;
  queued). No other instance is touched (R5). — basis: F1 (empty corpus search
  → no pre-existing dependents); render-debt policy
  `dev-notes/backlog/instance-reinstantiation.md` "Render-debt queue"; the change
  set is anneal-dev-only (the policy names anneal-dev's own dispatches).
- **D2** [VERIFIED] **Home of the rule = `anneal-dev/spec/bindings.md`, NO
  framework-spec change.** (a) target: a new section in bindings.md. (b) shape:
  a dispatch-orchestration-mechanics binding (foundation contract 3), parallel in
  placement to the Isolation-slot section; not a §3-table row, mirroring the
  existing Skill-craft-invocation dispatch-discipline section. (c) acceptance:
  the framework spec carries zero model tokens after the change (contract 1
  preserved); the rule lives only in the instance spec + config. (d) failure
  mode: putting the rule/value in the framework spec = contract-1 leakage. (e)
  basis: F2 (contract 3 assigns dispatch-orchestration mechanics to the
  instance), F3 (framework silent on model), F4 (binding-refinement precedent).
- **D3** [VERIFIED] **The rule (policy).** Blanket: every anneal-dev subagent
  dispatch — across all phases/passes — runs at the configured tier; cost-
  downgrading any anneal-dev dispatch below it is forbidden. Not a per-dispatch
  "is this sensitive?" judgment (that judgment is itself error-prone — R1). (c)
  acceptance: each dispatch's model param = the configured tier (observable on
  the dispatch → mechanical criterion, practice-8 mechanical form). (d) failure
  mode at boundary: a dispatch passing a cheaper model is the visible violation.
  — basis: backlog item `anneal-dev-model-tier-policy.md`:9-20 (operator-authored
  policy); enforcement-form per `development-process.md` practice 8 (mechanical
  criteria = computed from observable evidence).
- **D4** [VERIFIED] **Home of the value = `anneal-dev.config/model-tier.md`,
  operator-editable; created this run with `opus`.** (b) shape: a one-purpose
  config file holding the model name (matching the single-purpose style of
  lenses.md / extensions.enabled), header comment pointing at the bindings.md
  rule. (c) acceptance: the model name appears ONLY in config, never in
  bindings.md prose (R2/R3); the operator changes it without an anneal-dev run.
  (d) the value is the operator's to maintain (staleness is operator-owned, cheap
  to fix — exactly why a change-prone value lives in config, not spec). — basis:
  backlog item:21-23 ("Rule in spec, value in config"); operator-editable-config
  precedent `anneal-dev/spec/bindings.md`:236-246.
- **D5** [VERIFIED] **No new bootstrapped placeholder; document the override in
  the existing (bootstrapped) `anneal-dev.config/README.md`.** The §5 Project-init
  bootstrap mandate covers "every operator-editable SLOT KIND the framework
  recognises" (extension-enable, lens-supplement) — the model-tier is an
  instance-specific override, not a framework-recognized slot kind, so it is NOT
  under the bootstrap mandate. It has a sensible default (D6), so a placeholder
  is not needed for the default to work; visibility is carried by a one-line
  README note. (Pareto: avoids expanding the bootstrap list + the SKILL.md /
  foundations.md render-debt for marginal visibility.) — basis:
  `instantiation-guide.md`:378-385 (Project-init: framework-recognized slot
  kinds) + :352-356 ("any future operator-editable instance-side artifact" under
  the layout rules); practice-7 proportionality / Additive-reflex.
  considered: bootstrap a commented placeholder config file (rejected: over-
  provisions an override with a working default; expands the bootstrap list +
  adds SKILL.md/foundations.md render-debt; the README note + bindings rule
  already document the capability).
- **D6** [VERIFIED] **Default when config absent = inherit the session model;
  never downgrade.** Fail-safe: an absent/empty `model-tier.md` is read as
  "inherit the session model" (the harness default); the no-downgrade clause
  still binds. The config file PINS a tier above the session model when present
  (the case the floor bites — session lower than top). — basis: backlog item
  Note:30-33 (dispatches already inherit the session model; the rule formalizes a
  FLOOR); Agent-tool default = inherit main-loop model (harness behavior).
- **D7** [VERIFIED] **INV-3 interaction recorded, not silently foreclosed.** The
  rule's prose carries the FLOOR framing only (R4: top tier avoids handicapping
  sensitive judgment; NOT a substitute for structural robustness — fresh-context
  verify/isolation, the falsification/dogfooding passes, the operator). The
  INV-3 model-diversity tension (F5) is NOT rule-text (would be Bloat — it is
  rationale): it is recorded here + carried into the verify focusing artifact
  (INV-3 line) + cross-referenced into `multivoter-verify-no-predicate-claims.md`
  (the item that owns the model-diversity axis), so a later model-diversity-for-
  verify sharpening resolves the conflict with this policy rather than colliding
  silently. — basis: F5; Bloat lens (rationale → not rule-text); CLAUDE.md
  "file, don't defer" (the relate-note is the filing).
- **D8** [VERIFIED] **Render cadence = spec-only; queue the source-delta.** The
  anneal-dev plugin re-render is deferred to the batch (`instance-reinstantiation`);
  `render-and-open-diff` stays DISABLED (the render-debt-queue corollary). The
  source-delta appended to the queue is anneal-dev-only (bindings.md new section +
  config). — basis: `dev-notes/backlog/instance-reinstantiation.md` "Render-debt
  queue" + "Corollary — render-and-open-diff stays DISABLED"; `anneal-dev.config/extensions.enabled`
  (render-and-open-diff commented out).
- **D9** [VERIFIED] **New terms defined inline in bindings.md; no `spec/glossary.md`
  entry.** "model tier" / "top tier" is a harness concept — a `spec/glossary.md`
  entry would leak a harness/cost concept into the domain-general glossary
  (contract 1), so the term is defined where introduced (the bindings.md section),
  mirroring how `dev-notes/foundation-invariants/README.md` defines its own terms
  locally rather than in the spec glossary. — basis: `development-process.md`
  practice 10 (new term → glossary) vs. contract-1 harness-agnosticism of
  `spec/glossary.md`; local-definition precedent
  `dev-notes/foundation-invariants/README.md`:78-108.

---

## Cycle 2 (convergence attempt 1) — new-surface investigation appends

- **F6** [VERIFIED — addressed] **Clippy precedent — instance-level
  dispatch-model config with ZERO framework presence.** clippy ships a released
  per-unit dispatch-model SELECTOR (`coding-clippy/spec/bindings.md` §Dispatch
  models; rendered `SKILL.md` "Dispatch model selection"; value in
  `clippy.config/models`) — and clippy Finding 1 records the operator decision
  that "Model-selection has **zero** framework/template presence … stays
  instance-level." This (a) CONFIRMS D2 (dispatch-model is instance-level, no
  framework touch) + D4 (value in instance config) with a live, released
  precedent; (b) shows OPPOSITE polarity — clippy's is an opt-in per-unit
  cost-DOWNGRADE selector, anneal-dev's is a blanket anti-downgrade FLOOR
  (confirms D3's "blanket, not per-dispatch"); (c) clippy's per-unit selector
  carries a known failure class (silent-inert `impl: sonnet`,
  `surface-non-task-observations.md`:23) that anneal-dev's blanket policy avoids
  by construction. Disposition: addressed by the D1 amendment (clippy relate-note)
  + the D2/D4 sub-annotations below. — basis:
  `dev-notes/backlog/clippy-run-findings-dispatch-coupling.md`:14-37 (Finding 1:
  selector home + "zero framework/template presence" + instance-only) and
  :202-229 (Cycle G — the framework dispatch decomposition carried NO model token),
  located reads.

- **D1** [INVALIDATED] scope amended — see re-formed line below.
- **D1** [PENDING] **Scope amended** — add a relate-note from this run's backlog
  item into clippy's `clippy-run-findings-dispatch-coupling.md` (sibling
  dispatch-model precedent; cross-reference). No new framework-level item filed:
  clippy Finding 1 already settled that dispatch-model selection stays
  instance-level, so the cross-instance relationship is a relate, not an open
  question. Re-forms to [VERIFIED] next cycle (amendment forces cycle-another). —
  basis: F6.

- D2 [VERIFIED] (unchanged resolution)
  - basis strengthened (cycle 2): `coding-clippy/spec/bindings.md` §Dispatch
    models — a live precedent that an instance carries dispatch-model selection in
    its OWN bindings.md with zero framework presence (clippy Finding 1).
- D4 [VERIFIED] (unchanged resolution)
  - basis strengthened (cycle 2): `clippy.config/models` — a live precedent for an
    operator-editable instance dispatch-model config value.
- D5 [VERIFIED] (unchanged resolution)
  - basis strengthened (cycle 2): clippy bootstraps a `clippy.config/models`
    placeholder (Finding 1 fix-shape iii) — CONSIDERED and DISTINGUISHED: clippy's
    is an ACTIVE per-unit selector (placeholder aids per-unit configuration);
    anneal-dev's is a set-once FLOOR with a working default (D6), effectively a
    SINGLETON instance in this repo (no fleet of fresh anneal-dev projects to
    bootstrap into), and this run commits a concrete `model-tier.md` = opus — so
    the README note suffices; the no-bootstrap resolution stands.

---

## Cycle 3 (clean convergence) — new-surface investigation + D1 re-form

- **D1** [VERIFIED] **Scope (re-formed).** As cycle-1 D1, plus the clippy
  relate-note (cycle-2 amendment now incorporated): touches
  `anneal-dev/spec/bindings.md` (rule), `anneal-dev.config/model-tier.md` (value
  = opus), `anneal-dev.config/README.md` (override note),
  `dev-notes/backlog/instance-reinstantiation.md` (render-debt source-delta),
  `dev-notes/backlog/anneal-dev-model-tier-policy.md` (→ archive),
  `dev-notes/backlog/clippy-run-findings-dispatch-coupling.md` +
  `multivoter-verify-no-predicate-claims.md` (relate-notes). Render of the
  anneal-dev plugin deferred (D8). — basis: F1 (empty corpus search → no
  pre-existing contract dependents), F6 (clippy relate), F7 (no collision in
  anneal-dev/spec), render-debt policy.
- **F7** [VERIFIED — non-issue] **No dispatch-model collision; the model tier is
  orthogonal to the dispatch-brief schema.** No anneal-dev/spec file handles a
  per-dispatch model parameter (the only `model` hit is "the framework's method —
  the model", the method-model, not dispatch-model), and the framework
  dispatch-brief schema (`spec/modules.md` §3.3, sections (a)-(d): load /
  tracker / unit-scope / return-state) names NO model slot — the model tier is
  the Agent-call parameter, orthogonal to the brief. So D3's policy collides with
  nothing and adds no brief-schema dependent. bindings.md section order
  (Bindings / Verification battery / Isolation slot / Operator-editable artifacts)
  confirms the new "Dispatch model tier" section lands among the dispatch-mechanics
  sections (after Isolation slot), per D2. — basis:
  `grep -niE "model" anneal-dev/spec/*.md` → only bindings.md:6 (method-model);
  `spec/modules.md` §3.3 located read (no model section); `grep -nE "^## "
  anneal-dev/spec/bindings.md` → 4 section headers.

---

## Cycle 3 — intent-falsification results (3 findings → D5 delta; mechanical pass skipped)

Artifact: `.anneal-dev/runs/anneal-dev-model-tier-policy.cycle-3.intent-falsification.md`.
`mechanical skipped: intent-delta this cycle` (per `core.md` §4.1.4 / `modules.md` §3.4 skip carve-out).

- **F8** [VERIFIED — surfaced] **Blanket pin mandates verify-on-the-actor's-tier,
  foreclosing the cross-tier-diversity independence lever.** INV-3's anchor warns
  a verifier sharing the actor's base model inherits self-preference bias; the
  framework's own Arm C (`anneal-empirical-validation-experiment.md`:69) leans
  toward a different-model verifier. R1's blanket pin makes same-tier-as-actor
  verify mandatory. Pure judgment, no runnable check → terminal; feeds the
  operator's soundness pass. NOT acted on by exempting verify — that contradicts
  R1's explicit blanket intent (verify is judgment-heavy, the floor's core
  target); the tradeoff is the operator's to weigh/override. — basis:
  `spec/core.md`:795-812 (verify isolation = context-only, no model);
  `dev-notes/foundation-invariants/INV-3-verify-isolation.md`:14-21;
  `anneal-empirical-validation-experiment.md`:69. Routed to the relate-to
  `multivoter-verify-no-predicate-claims` (D7 strengthened).
- **F9** [VERIFIED — surfaced] **Self-governing render-debt — the floor is
  unenforced in the running tool until re-render+reinstall.** anneal-dev's rule
  lives in `anneal-dev/spec/bindings.md`, rendered into the running plugin; D8
  defers that render, so the cached/active plugin (0.1.2) does not carry the tier
  rule until reinstall. Terminal; resolved by the operator's post-run activation
  request (re-render + reinstall anneal-dev). D8's spec-only cadence stands. —
  basis: `dev-notes/backlog/instance-reinstantiation.md` render-debt policy +
  cache-not-updated-until-reinstall; D8.

- **D5** [INVALIDATED] superseded — see re-formed line below.
- **D5** [PENDING → VERIFIED] **FLIPPED: bootstrap a commented `model-tier.md`
  placeholder** at first-run, alongside lenses.md / extensions.enabled / README.md.
  (b) shape: a header-comment placeholder (default commented = inherit session per
  D6) explaining the floor + how to pin the harness's top-tier model; an
  instance-specific operator-editable artifact (beyond the framework-recognized
  slot kinds — permitted: `instantiation-guide.md` §5 covers "any future
  operator-editable instance-side artifact", and §5 Project-init does not forbid
  bootstrapping more than the recognized kinds). (c) acceptance: a fresh
  anneal-dev install surfaces the model-tier slot as a file (the un-fakeable §5
  visibility signal), not only a README line — closing F-finding-2's
  silent-absence-of-the-floor in installed-elsewhere/low-session projects. In THIS
  project the placeholder content is replaced by the concrete `opus` value (D4 +
  §5 "later adds a declared item replaces the placeholder"). — basis: cycle-3
  intent-falsification Finding 2 (R1 weakened by absent-by-default pin);
  `instantiation-guide.md`:352-356 + :380-401; practice-7 (foundation discipline:
  design-time placement beats the downstream tax of a silently-absent floor).
  considered: keep no-bootstrap + README note only (rejected: Finding 2 — the
  README note is weaker visibility than the un-fakeable placeholder file, and
  leaves the floor silently absent in a low-session installed-elsewhere run).
- **D1** [INVALIDATED] superseded — see re-formed line below.
- **D1** [VERIFIED] **Scope (re-formed, cycle 3).** Adds, from the D5 flip:
  `anneal-dev/spec/bindings.md` "Operator-editable artifacts" + "First-run
  bootstrap" now enumerate `model-tier.md` (4 placeholders); render-debt to the
  anneal-dev plugin `SKILL.md` First-run bootstrap + `references/foundations.md`
  Operator-editable artifacts (deferred, D8). All other touched spots unchanged
  from the cycle-3 D1. — basis: D5 flipped; F7 (no other collision).
- D7 [VERIFIED] (unchanged resolution)
  - basis strengthened (cycle 3): the relate-to `multivoter-verify-no-predicate-claims`
    now carries F8's specific framing — anneal-dev's blanket pin forecloses
    verify-cross-tier-diversity; resolve that conflict in the multivoter item
    if/when model-diversity-for-verify is pursued.

---

## Cycle 4 (convergence attempt 2) — new-surface investigation

- **F10** [VERIFIED — addressed] **Clippy bootstraps a 4th, non-recognized-slot-kind
  placeholder (`clippy.config/models`) — direct precedent confirming D5-flipped.**
  clippy's first-run bootstrap creates `clippy.config/` with **four** placeholder
  files (lenses.md / extensions.enabled / README.md + `models`, its
  instance-specific dispatch-model config) — i.e. an instance routinely bootstraps
  an operator-editable artifact BEYOND the three framework-recognized slot kinds.
  So D5-flipped (bootstrap `model-tier.md` as a 4th placeholder) is the
  established sibling pattern, not a novel move. Disposition: addressed by
  D5-flipped. — basis:
  `~/.claude/plugins/marketplaces/coding-clippy/plugin/skills/clippy/SKILL.md`:315-325
  ("Create `clippy.config/` with four placeholder files") + :120
  (`clippy.config/models` per bindings.md Dispatch models), located reads.

---

## Cycle 4 — CONVERGED ([READY])

Convergence cycle clean across all four passes (zero D-track delta):
- investigation → F10 (clippy precedent confirms D5; no delta)
- standardized pass → clean (`…cycle-4.standardized-pass.md`)
- intent-falsification → CLEAN, every R# served, zero new findings (`…cycle-4.intent-falsification.md`)
- mechanical falsification → all 9 D-entries `holds`, zero falsified (`…cycle-4.falsification.md`)

**Framework-pollution check (operator-asked):** the framework spec carries ZERO model
tokens after this change — `rg -niE "(opus|sonnet|haiku|model tier)" spec/*.md foundation.md`
→ EMPTY (D2 target-dependents, mechanical pass). No `spec/*` / `foundation.md` /
`development-process.md` file is in the impl plan. The dispatch-model concretion is
instance + config only (foundation contract 3).

**Fresh-session implementability: PASSED** (per-step external evidence):
- S1 add "## Dispatch model tier" after Isolation slot — `grep -nE "^## " anneal-dev/spec/bindings.md` → headers 26/53/124/236; insert at 235/236 boundary.
- S2 add `model-tier.md` to bindings.md "Operator-editable artifacts" + "First-run bootstrap" — `anneal-dev/spec/bindings.md`:241-251 (current 3-file enumeration).
- S3 create `anneal-dev.config/model-tier.md` = `opus` + header — style per clippy `SKILL.md`:321-325 + `instantiation-guide.md` §5 placeholder-content-style.
- S4 add override note to `anneal-dev.config/README.md` — current content 3 lines (`README.md`:1-3).
- S5 append render-debt source-delta to `instance-reinstantiation.md` "Queue" — template = the verify-vs-original-requirements entry already there.
- S6 relate-notes into `clippy-run-findings-dispatch-coupling.md` + `multivoter-verify-no-predicate-claims.md` (both exist — mechanical pass confirmed).

**Foundation-invariant focusing artifact (method-kernel edit — aims the operator's soundness pass; NOT a verdict):**
- INV-1 basis rule — UNTOUCHED (holds). · INV-2 complete state — UNTOUCHED (holds). · INV-4 loopback — UNTOUCHED (holds). · INV-5 exclusion-via-falsifier — UNTOUCHED (holds).
- **INV-3 verify isolation — TOUCHED.** Holds against the anchor's *context-isolation* requirement (verify still runs in a separate context — the kernel's INV-3 mechanism is unchanged). BUT F8: the blanket pin makes verify-on-the-actor's-tier mandatory, foreclosing the cross-tier model-*diversity* lever the anchor (Panickssery et al.) + Arm C favor. Operator soundness pass should weigh blanket-including-verify vs. preserving diversity. Not regressed; surfaced.

**Impl plan:** 1 unit, sequential, in-place subagent, single container (anneal-framework repo).
- U1 (first; sequential) — realizes D1–D9: bindings.md "Dispatch model tier" section + bootstrap-list entry; `model-tier.md`=opus; README override note; render-debt queue append; clippy + multivoter relate-notes. (Backlog item archive = release step, not impl.) Disjointness basis: N/A (single unit).

---

## implement + verify

- **U1 complete.** Persistence reference: checkpoint `92fa428` (`anneal-checkpoint:` prefix).
  Integrity check PASSED: HEAD 432e618→92fa428 by exactly one commit, tree clean, exactly
  the 6 intended files, zero model names in bindings.md, `opus` confined to `model-tier.md:8`.
  Self-check clean.
- **Verify — anneal-dev battery (isolated, subagent a55afd8): [PASSED].** planned-vs-actual
  D1–D9 hold; requirements-coverage R1–R5 covered (R3 mechanically EMPTY in framework spec);
  8 lenses clean; coherence clean ("four placeholder files" matches the 4-member set);
  render-fidelity + skill-quality-of-plugin-skills N/A (no `plugin/skills/*` in commit, render
  deferred D8).
- **Verify — skill-craft self-review (kernel-independent form leg, subagent a3811073):**
  PASS-with-1-notable. Section earns its place (fills contract-3 slot; not additive-reflex);
  rule enforceable; per-dispatch sensitivity judgment correctly removed.
  - **F11** [PENDING] **Notable (step-4): spec-vs-artifact clarity.** Binding's bootstrap
    clause says first-run creates a "commented/empty" `model-tier.md`, but committed
    `model-tier.md:8` carries live `opus`. No design contradiction (D4 project-pin; §5 filling
    replaces the placeholder) — but the binding doesn't state the bootstrap-empty vs.
    project-filled distinction, so a reader could misread. First-judge: fix-now (minimal —
    add a half-clause that a project pins by filling the placeholder, as this repo does);
    defensible accept-with-rationale. Operator second-judge at step-4. — basis: subagent
    a3811073.
  - nit ("sensitive"/"weak" descriptive, not control-flow) → keep. observations (clippy
    forward-ref tracked; section passes Pareto) → keep.
- **Operator soundness pass (irreducible) — PENDING.** INV-3 the only touched invariant —
  holds on context-isolation; F8 (blanket pin forecloses verify cross-tier diversity) is the
  surfaced residual for the operator's verdict.
