# Run: provenance-basis-naming

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** Home the provenance-at-handoff principle in the framework basis rule
  (`core.md` §3.2.1 basis-naming edge): a name/label/docstring asserting WHAT AN
  ARTIFACT MEANS (provider, perspective, unit, value-domain, identity) is an embedded
  CLAIM, grounded at the artifact's SOURCE/PRODUCER (where it is set), not trusted at
  its use-site/label. Producer→consumer SEMANTICS seam (distinct from §3.2.2's
  co-producer producer↔producer FORMAT seam). (b)-direction (operator-locked):
  framework-general basis-rule home, clippy trace-to-producer fire-point = render-debt.
  Method-kernel edit; spec-only release.

## Requirements record (task-input; separated from the proposed solution)

**Verbatim operator request (chain):** [AI presented the (a)/(b) fork resolution: (b)-direction
— basis-rule home, framework-general, clippy fire-point as render; #1-salience vs #2-sharpen to
be settled by investigating §3.2.1] → "yes".

**Proposed solution (operator-locked direction, NOT the full design — the #1/#2 form is
investigated):** home provenance in the basis rule (b); within (b), settle #1-salience vs
#2-sharpen via the three-fix-shapes cut by investigating whether §3.2.1 already asks the
value-provenance question.

**Requirements (the goal):**
- **R1** — A consumer's reliance on a value's name/label/docstring to know WHAT THE VALUE
  MEANS (provider, perspective, unit, value-domain, identity) is treated as a CLAIM requiring
  grounding at the value's PRODUCER (where it is set), not trusted at the use-site — so a
  mismatch (the producer sets a different meaning than the label asserts) is caught.
- **R2** (operator-locked constraint) — homed in the framework BASIS RULE (framework-general),
  NOT a discrete clippy-only lens (lens-crowding-respecting); the clippy trace-to-producer
  fire-point is the instance render (render-debt).
- **R3** (three-fix-shapes investigation) — settle #1-salience vs #2-sharpen by investigating
  whether §3.2.1's embedded-claims edge already asks the value-provenance question; edit
  Edit-as-Pareto accordingly, not a bolt-on.
- **R4** (framework discipline) — framework-general phrasing (coding concretions — id/provider/
  perspective — bound by the clippy render); evidence-bearing (the grounding is a located read
  at the producer, per §3.2(b)).
- **R5** (completeness) — dependents of the edited basis-naming clause accounted for (§4.1.1,
  glossary Basis, instance lens render); plugin/instance renders → render-debt.

## F-track (findings)

- **F1** [VERIFIED — non-issue] §3.2.1 basis-naming enumerates embedded-claim forms — "implicit
  premises in target-naming decisions, cited rules or prior decisions, completeness counts
  asserted as facts" — but NOT a value/artifact's semantic/identity label asserting its meaning.
  basis: read `core.md:216-225` to bullet close; observable fact: three enumerated forms, none a
  semantic-meaning/provenance label.
- **F2** [VERIFIED — non-issue] §3.2(b) grounds a basis in "a located read of the source" but
  does not specify that for a value's MEANING the source is the PRODUCER (where set), not the
  use-site label. basis: read `core.md:185-187`; observable fact: "located read of the source"
  is unqualified re: producer-vs-use-site.
- **F3** [VERIFIED — non-issue] No existing provenance/distrust/ground-at-source principle in the
  spec (no fragmentation); the basis-naming "embedded claims" clause lives only at `core.md`
  §3.2.1 (:219-224); one dependent at §4.1.1 (:409-411 "embedded target-naming and count
  premises"). basis: corpus grep `embedded claim`/`target-naming`/`implicit premise`/`provenance`/
  `distrust` (cycle-1); observable fact: hits = core.md:219-224 + :410 only.
- **F4** [VERIFIED — non-issue] No instance lens renders basis-naming/provenance (the 8 core
  lenses: Bloat/Fragmentation/Leakage/Missed-dependents/Unenforced-rule/Undefined-shorthand/
  Lossy-render/Over-claimed-verification); the clippy trace-to-producer fire-point is a NEW
  instance rendering → render-debt. basis: grep `lens-set.md` `^### ` headers; observable fact:
  8 lens headers, none basis-naming/provenance.
- **F5** (three-fix-shapes determination) [VERIFIED — non-issue] This is **#2 (sharpen the
  question)**, not #1 (salience): §3.2.1's general "embedded claims" reaches a semantic label in
  principle, but the specific FORM (semantic/provenance label) + the ground-at-PRODUCER direction
  are NOT named → adherence does not fire for value-provenance. Same shape as the §3.2.2
  co-producer work (general clause exists; name the specific search-blind form). basis: F1+F2 +
  the three-fix-shapes cut (`forcing-function-dose-discriminator`).
- **F6** [PENDING] (Leakage) The provenance source item is coding-flavored (market_id, Pinnacle,
  handicap sign/perspective). `core.md` §3.2.1 is domain-general — the form must be stated
  generally (a name/label asserting an artifact's meaning, grounded at its source/producer),
  coding concretions (id/provider/perspective) → clippy render. basis: Leakage lens scope +
  the item's coding vocabulary.

## D-track (design decisions)

- **D1** [PENDING] Scope: edit `core.md §3.2.1` basis-naming edge (extend the embedded-claims
  enumeration). Dependent-checks: `core.md §4.1.1` (:409-411 — confirm no edit, D4); glossary
  "Basis" (:49 — confirm no edit, the form is an example not a new term). Render-debt: clippy
  basis-naming/provenance fire-point (NEW instance rendering, F4) → `instance-reinstantiation`.
  basis: corpus greps (F3/F4). [PENDING on D4 + glossary confirm.]
- **D2** [OUTLINED] **#2-sharpen** (F5): extend §3.2.1's basis-naming embedded-claims enumeration
  to NAME a new form — a **name/label/identity asserting an artifact's MEANING or PROVENANCE**
  (its provider, perspective, unit, value-domain, identity) is an embedded claim — grounded by a
  located read at the artifact's **SOURCE/PRODUCER** (where it is set/produced), NOT trusted at
  its use-site/label. Framework-general (applies to corpus-evolution: a title/label asserting
  what a rule does is grounded at the rule's text, not the title). basis: F1/F2/F5 + provenance item.
- **D3** [OUTLINED] Edit-as-Pareto + grounding home: extend the EXISTING §3.2.1 basis-naming
  bullet's embedded-claims list (add the semantic/provenance-label form), no new clause/section;
  the grounding-at-source leverages §3.2(b)'s existing "located read of the source" (the source
  for a value's meaning = its producer, not its use-site). Define the form inline (no new glossary
  term, F-Undefined-shorthand). Keep tight (Bloat/human-inspectability). basis: §3.2.1 structure
  (F1) + §3.2(b) (F2).
- **D4** [PENDING] §4.1.1 dependent (:409-411): the [READY] gate enumerates "embedded
  target-naming and count premises" — already a CURATED SUBSET of §3.2.1's list (it omits "cited
  rules"). Decision direction: do NOT extend §4.1.1 to add the provenance form — §4.1.1 is scoped
  to anneal-dev design-decision premises (target-naming + count), whereas the provenance/semantic-
  label form is primarily a WORK-PRODUCT phenomenon (instance level). My edit does not make §4.1.1
  stale (it already omits "cited rules"). basis: read `core.md:409-411` — observable fact: the
  enumeration is "target-naming and count" (2 of §3.2.1's 3+ forms → a curated subset). [PENDING
  final lock in cycle 2.]

## Cycle 2 (appended — append-only ledger; current state = latest line per entry)

### F-track (cycle 2)

- **F6** [VERIFIED — addressed] Leakage resolved: D2's realized phrasing is domain-general (a
  name/label asserting an artifact's meaning or provenance, grounded at its producer/source);
  coding concretions (id/provider/perspective) bound by the clippy render. basis: D2 realized phrasing.
- **F7** [VERIFIED — non-issue] glossary "Basis" (:49-59) defines a basis as the artifact TYPES
  (search result / located read of the source / construct-whole / runtime), not the embedded-claim
  FORMS that require one (§3.2.1's job; glossary points to §3.2). Adding a claim-form to §3.2.1
  needs no glossary edit. basis: read `glossary.md:49-59` to term close; observable fact: the term
  enumerates basis artifact-types, not claim-forms.

### D-track (cycle 2 — promotions)

- **D1** [VERIFIED] Scope locked. Edit site: `core.md §3.2.1` basis-naming bullet (extend the
  embedded-claims enumeration). NO edit: `core.md §4.1.1` (curated subset, D4), glossary "Basis"
  (artifact-types not claim-forms, F7). Render-debt (deferred, spec-only): clippy basis-naming/
  provenance fire-point (NEW instance rendering, F4) → `instance-reinstantiation`. basis: corpus
  greps (F3/F4) + §4.1.1 read (D4) + glossary read (F7).
- **D2** [VERIFIED] #2-sharpen. Contract (the AI behavior the rule forces): the basis-naming edge's
  embedded-claims enumeration must NAME — as a claim requiring its own basis — **a name or label
  asserting an artifact's MEANING or PROVENANCE** (its source, identity, perspective, unit, or
  value-domain). The required basis is a **located read at the artifact's PRODUCER/SOURCE (where it
  is set/produced)**, NOT the use-site label — distrust the surface assertion, ground at the source.
  Evidence-bearing artifact = that located-read-at-the-producer (per §3.2(b)); re-derived by verify
  (§4.3) / convergence. Framework-general (a title/label asserting what a rule does → grounded at
  the rule's text, not the title). Domain-general; instance binds concrete forms (id/provider/
  perspective). basis: F1 (the enumeration gap) + F2 (§3.2(b) source unqualified) + F5 (#2 shape).
- **D3** [VERIFIED] Edit-as-Pareto + grounding home. Delta: extend the EXISTING §3.2.1 basis-naming
  bullet's list (`core.md:219-221`, "...target-naming decisions, cited rules or prior decisions,
  completeness counts asserted as facts") with the fourth form — a name/label asserting an
  artifact's meaning or provenance, grounded at the producer/source not the use-site. No new
  clause/section; the grounding leverages §3.2(b)'s existing "located read of the source" (the
  source for a value's meaning = its producer). Define inline (no new glossary term, F7). Keep tight
  (one clause; Bloat/human-inspectability). basis: §3.2.1 structure (F1) + §3.2(b) (F2).
- **D4** [VERIFIED] §4.1.1 (:409-411): no edit. It enumerates "target-naming and count" — a curated
  subset of §3.2.1's forms (already omits "cited rules"), scoped to anneal-dev design-decision
  premises; the provenance/semantic-label form is a work-product (instance-level) phenomenon. My
  §3.2.1 addition does not make §4.1.1 stale (it was already non-exhaustive). basis: read
  `core.md:409-411` — observable fact: enumeration = "target-naming and count" (2 of 3+ §3.2.1 forms).

## Cycle 3 — convergence cycle (intent-falsification CLEAN; mechanical running)

Convergence cycle 3: fresh-context intent-falsification (opus `a8c6ac7322dd4225e`,
`.cycle-3.intent-falsification.md`) → CLEAN on the D-track (no new D-delta; #2-vs-#1 call HELD on
3 converging facts: empirical 2/5→5/5 inertness, the §3.2.2 precedent, the distinct distrust-the-label
posture) → mechanical falsification pass RUNS. New surfaces: `provenance-at-handoff-lens.md:43-44`
(empirical inertness of the general rule), the epistemic-posture comparison of the 3 existing forms.

### F-track (cycle 3 — intent-falsification findings)
- **INT-A** [VERIFIED — surfaced] Recognition-gating ceiling: the form fires only once the AI recognizes
  a value's meaning is load-bearing; an unrecognized meaning-dependency never triggers (the §3.2.2 INT-4
  ceiling). Correctly bounded — D2 does not overclaim past it; honest-surface per the discriminator, not
  a D-delta. basis: intent artifact + `forcing-function-dose-discriminator.md:28-29`. For step-4 review.
- **INT-B** [VERIFIED — surfaced] The producer-not-use-site redirection must survive impl realization or
  the form collapses toward redundancy with §3.2(b)'s generic located-read. Already in D2/D3
  (tracker:127-128, 137-138); IMPL WATCH-POINT, backstopped by verify. basis: §3.2(b) core.md:185-187 +
  F2. No D-track change.

### D-track (cycle 3 — mechanical falsification result)
- **D1** [INVALIDATED] mechanical falsification (cycle-3 `.falsification.md`) found the as-written
  render-debt scope OMITS the anneal-dev/plugin self-renders of the edited §3.2.1/§4.1.1
  (`foundations.md:199-204`, `investigate-design.md:143-145`) — outside the named scope →
  any-outside-scope FALSIFIED. basis: cycle-3 falsification D1 line.
- **D1** [PENDING] re-forming with corrected render-debt scope.
- **D1** [VERIFIED] Scope (corrected). Edit site: `core.md §3.2.1` basis-naming bullet. NO edit:
  `core.md §4.1.1` (curated subset, D4), glossary "Basis" (artifact-types, F7). **Render-debt
  (deferred, spec-only, batched per render-cadence): (i) the anneal-dev/plugin self-render of the
  edited §3.2.1/§4.1.1 (`anneal-dev/plugin/skills/anneal-dev/references/foundations.md` §3.2.1 +
  `phases/investigate-design.md` §4.1.1) + (ii) the clippy basis-naming/provenance fire-point (NEW
  instance rendering, F4) → `instance-reinstantiation`.** basis: corpus greps (F3/F4) + the cycle-3
  mechanical search (the anneal-dev/plugin renders). Fix is **behavior-preserving** (completes the
  render-debt enumeration; no edit changes) → intent-clean carries forward.

**Convergence status:** cycle 3 NOT converged (D1 amended — behavior-preserving render-debt
completeness fix). Cycle 4 = re-converge (intent carries forward per the behavior-preserving rule;
re-run mechanical with corrected D1 scope).

## Cycle 4 — convergence cycle (RE-CONVERGED; CLEAN) → [READY]

Convergence cycle 4: the cycle-3 D1 fix is behavior-preserving → the cycle-3 intent-falsification
clean result CARRIES FORWARD (per `phases/investigate-design.md` re-trigger rule). New surface this
cycle: the anneal-dev/plugin render dependents (`foundations.md:199-204`, `investigate-design.md:143-145`)
that the cycle-3 mechanical surfaced — now inside D1's corrected render-debt scope.

### Mechanical falsification (cycle 4 — orchestrator re-computation, `.cycle-4.falsification.md`)
D1 (corrected scope): same cycle-3 candidate + result; with the render-debt set now including
`anneal-dev/plugin/*`, the any-outside-scope predicate → **holds** (the two plugin hits are inside
scope). D2/D3/D4: unchanged [VERIFIED], cycle-3 mechanical lines hold. **All four hold → zero new
D-delta → CONVERGED.**

### Fresh-session implementability — PASSED
A fresh session with only this tracker implements the design with no new design decision. One edit step:
- **Step 1** (D2/D3): edit point `core.md:219-221` — read confirms the §3.2.1 basis-naming bullet's
  three-form list ("...target-naming decisions, cited rules or prior decisions, completeness counts
  asserted as facts") to extend with the FOURTH form — a name/label asserting an artifact's
  meaning/provenance, grounded by a located read at the artifact's PRODUCER/SOURCE (where set), not its
  use-site label. Reuses §3.2(b) (`core.md:185-187`) located-read. PASS (located-read external citation;
  content locked in D2/D3; INT-B watch-point — the producer-not-use-site phrase must survive).
No §4.1.1 / glossary edit (D4/F7). Render-debt deferred (D1).



## Implement progress
- **Unit 1** [COMPLETE] `spec/core.md` §3.2.1 basis-naming bullet (D2+D3). Subagent (opus, in-place).
  Self-check clean (4 lenses + scope ∅); INT-B redirection CONFIRMED in rule-text (distrust-the-label
  + ground-at-producer + not-the-use-site explicit); no loopback. Integrity PASS (HEAD `3f62dc8`
  unchanged; only `spec/core.md` modified, +8/−1). Realized text faithful (`core.md:219-228`).
- **Implement COMPLETE** → verify.

## Verify — [PASSED] (isolated)
Isolated verify subagent (opus `a84d819050c492498`, skill-craft invoked). Four checks + battery, all accounted.
Verify result: **[PASSED] (isolated)**
Finding ledger:
- F1–F7 [VERIFIED — non-issue/addressed] (carried; gap real, Leakage resolved, glossary no-edit)
- INT-A [VERIFIED — surfaced] recognition-gating ceiling (terminal)
- INT-B [VERIFIED — surfaced] producer-not-use-site survival — re-confirmed PRESENT in text (`core.md:224-228`)
- VF1 [VERIFIED — addressed] planned-vs-actual D1–D4 all realized; no material element uncovered
- VF2 [VERIFIED — non-issue] R1–R5 + verbatim leg covered; no overclaim past INT-A/INT-B
- VF3 [VERIFIED — non-issue] 8 lenses clean; **#2-vs-#1 distinctness HOLDS in realized text (not Bloat)**
- VF4 [VERIFIED — addressed] battery (a) render-fidelity spec-only / (b) coherence (§3.2(b) xref resolves) / (c) skill-quality form

## RUN COMPLETE — verify [PASSED] 2026-06-07
Spec-only release (1 file: `spec/core.md` §3.2.1, +8/−1; HEAD `3f62dc8`, uncommitted). Method-kernel edit
→ release pending operator soundness (INV-1/INV-2 strengthened; INV-5 — weigh the INT-A recognition-gated
provenance teeth, same posture as §3.2.2/INT-4) + commit. Render-debt: anneal-dev/plugin self-render of
§3.2.1 + clippy trace-to-producer fire-point → instance-reinstantiation. Backlog: archive
provenance-at-handoff-lens (shipped (b)-direction; (a) fire-point = render-debt).
