# Run: enumeration-target-blindness

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** Sharpen `core.md` §3.2.2 (replacement/amendment completeness
  claim) with an "enumeration-target-blindness" consolidation bundling two
  backlog items — `replacement-side-effect-behavior-parity` (behaviors clause:
  side-effects produced inside replaced code) + `co-producer-format-parity`
  (dependents clause: co-producers of a shared equality-compared sink). One
  clause-family, one cycle; both render the existing closed Coupling-shape set.
  Method-kernel edit; spec-only release; instance/plugin renders are render-debt.

## Requirements record (task-input; separated from the proposed solution)

**Verbatim operator request (chain):** "ok in the backlog i tink theer are two
proposed clipyp lenses. we may want to do those first before doing a rerender" →
[AI: there are 3 lens-shaped items + 1 caution; recommend bundling the two §3.2.2
items (`co-producer` + `replacement-side-effect`) into one kernel cycle, then the
provenance lens, then the re-render] → "yes".

**Proposed solution (a strong input, NOT a locked design — investigated like any
premise):** sharpen §3.2.2 by naming the two search-blind forms + their mechanical
fire-points, consolidated as one "enumeration-target-blindness / grep the right
target" treatment.

**Requirements (the goal):**
- **R1** — A replacement/removal/amendment that drops a **side-effect** produced
  *inside* the replaced code (an effect not returned: a notification, log, external/
  network call, queue emit, non-return write) is caught by the §3.2.2 completeness
  claim: the behaviors clause NAMES the side-effect behavior form and specifies the
  enumeration METHOD (read the replaced code's bodies, not grep its callers).
- **R2** — A change to the **format/shape** of a value written to a **shared,
  equality-compared sink** that leaves a **co-producer** of that sink un-updated is
  caught: the §3.2.2 completeness claim NAMES the co-producer form and specifies the
  enumeration METHOD (enumerate the sink's writers, not grep the changed symbol).
- **R3** (consolidation constraint, operator-chosen) — R1+R2 land as ONE coherent
  §3.2.2 treatment (the shared meta-shape "enumeration keyed on X misses Y because Y
  is unreachable by an X-grep"), Edit-as-Pareto extending existing clauses, not two
  bolted-on rules.
- **R4** (framework invariant) — The closed Coupling-shape set (three shapes) is
  preserved: both new forms are RENDERINGS of the existing set (target-dependents /
  target-behavior), not a fourth shape — matching the precedent at `glossary.md`
  Coupling shape + `lens-set.md` Missed-dependents.
- **R5** (framework discipline) — Each new form carries a **mechanical fire-point**
  + a **convergence falsification candidate** (the teeth, per the evidence-bearing-
  artifact rule + the shipped dependents-clause precedent), not prose-only.
- **R6** (completeness) — Every dependent of the changed §3.2.2 contract is
  accounted for: spec-level (glossary Coupling-shape, lens-set Missed-dependents,
  modules §3.4) edited or confirmed-clean; instance/plugin renders queued as
  render-debt (spec-only release per render-cadence).

## F-track (findings)

- **F1** [VERIFIED — non-issue] §3.2.2 behaviors clause is bare — it requires "an
  explicit enumeration of behaviors preserved or dropped" but names no behavior
  FORMS and no enumeration method. basis: read `core.md:256-257` to clause close;
  observable fact: the clause's only behavior-language is "behaviors preserved or
  dropped" (no side-effect form, no read-the-bodies method).
- **F2** [VERIFIED — non-issue] §3.2.2 dependents clause names exactly two
  non-reference renderings (path-hardcoder + producer-of-consumed-artifact); no
  producer↔producer / co-producer form. basis: read `core.md:246-254`; observable
  fact: two enumerated forms ("hardcodes the target's location or structure" + "a
  producer of an artifact the target consumes").
- **F3** [VERIFIED — non-issue] The closed Coupling-shape set is a held invariant:
  "Closed set of three" + non-content-reference forms "render the existing closed
  Coupling-shape set (not new shapes)" (`glossary.md:99,112-113`); "All seven forms
  render the existing closed Coupling-shape set (no fourth shape)" (`lens-set.md:118-119`).
  basis: those two located reads; observable fact: both assert no fourth shape.
- **F4** [VERIFIED — non-issue] `modules.md` §3.4 candidate machinery is keyed on the
  three closed shapes, not on dependent forms; a new form rendering an existing shape
  leaves §3.4 untouched. basis: read `modules.md:358-359` (shape closed set) +
  `:409-410` ("target-dependents candidate re-runs §3.2.2's reference enumeration");
  observable fact: §3.4 references the three-shape closed set, not the dependent-form list.
- **F5** [VERIFIED — non-issue] Spec-level dependents of the §3.2.2 contract:
  `core.md` (§3.2.2; §5.2 body-shape cross-ref `:1124`), `glossary.md` Coupling-shape
  (`:98-127`), `anneal-dev/spec/lens-set.md` Missed-dependents (`:99-137`). The
  `development-process.md`/`instantiation-guide.md` "producer" hits are §3.1
  producer-independence / render-consumed, NOT §3.2.2 dependents; `anneal-dev/plugin/*`
  renders + instance specs (clippy/daneel, separate repos) are render-debt. basis:
  corpus-wide greps `preserved or dropped` / `non-reference structural dependent` /
  `producer` (cycle-1 investigation); observable fact: zero §3.2.2-dependent hits in
  dev-process/instantiation (all are §3.1/render-consumed).
- **F6** [PENDING] (Leakage) The two source items phrase the forms in coding
  concretions (DB column, `EXISTS`/JOIN, Telegram notification). `core.md` §3.2.2 is
  domain-general — the sharpening must state the forms generally (an effect produced
  inside replaced code; a value written to a shared equality-compared sink), with
  coding concretions living in the clippy instance render (render-debt). basis:
  Leakage lens scope (domain-general file = framework spec) + the items' coding vocabulary.
- **F7** [PENDING] (Undefined-shorthand) "co-producer", "shared equality-compared
  sink", and "side-effect" are used load-bearingly; need a single canonical defining
  sentence (inline in §3.2.2; glossary cross-ref) to avoid multiply-defined shorthand.
  basis: Undefined-shorthand lens scope + no existing glossary entry for these terms.

## D-track (design decisions)

- **D1** [PENDING] Scope: edit sites = `core.md` §3.2.2 (behaviors + dependents
  clauses; §5.2 cross-ref `:1124` confirm-only), `glossary.md` Coupling-shape
  target-dependents renderings (`:112-122`), `anneal-dev/spec/lens-set.md`
  Missed-dependents form-list (`:106-119`); `modules.md` §3.4 in-scope-to-confirm-clean
  (gated on D2). Render-debt (deferred — spec-only release per render-cadence):
  `anneal-dev/plugin/*` renders + instance specs (clippy/daneel) → `instance-reinstantiation`.
  basis: corpus searches (F5). [PENDING on the §5.2/modules confirmation + the D2 lock.]
- **D2** [OUTLINED] Both new forms render the existing closed Coupling-shape set —
  **co-producer → target-dependents** (the other writers of a shared equality-compared
  sink depend on its shared-format contract; the producer-side mirror of the existing
  producer↔consumer form), **side-effect → target-behavior** (a load-bearing behavior
  of the replaced code). No fourth shape ⇒ `modules.md` §3.4 untouched (F4). basis:
  closed-set invariant (F3) + the producer↔consumer precedent (`core.md:250-254`).
- **D3** [OUTLINED] §3.2.2 behaviors-clause sharpening: name the non-reference-findable
  behavior form (**side-effects** — effects produced inside the replaced code, not
  returned: notification, log, external/network call, queue emit, non-return write) +
  the enumeration METHOD (read the replaced code's bodies for effect signatures, NOT
  grep its callers) + the **target-behavior convergence candidate** (an enumerated
  effect with no successor in the replacement = falsified). Domain-general phrasing
  (F6). basis: `replacement-side-effect-behavior-parity` + the bare behaviors clause (F1).
- **D4** [OUTLINED] §3.2.2 dependents-clause sharpening: name the **co-producer** form
  (when the target produces a value written to a shared, equality-compared sink, the
  completeness obligation enumerates every PRODUCER/writer of that sink, not only the
  changed symbol's references) + the enumeration METHOD (enumerate the sink's writers,
  not grep the changed symbol) + the **target-dependents convergence candidate** (a
  co-producer whose emitted format diverges from the changed one = falsified).
  Domain-general phrasing (F6). basis: `co-producer-format-parity` + the dependents
  clause's two-form set (F2).
- **D5** [OUTLINED] Consolidation + renderings: present D3+D4 as one
  **"enumeration-target-blindness — grep the right target"** treatment (shared
  meta-shape: enumeration keyed on X misses Y unreachable by an X-grep; X=callers→
  Y=body effects, X=changed-symbol→Y=sink co-producers), Edit-as-Pareto extending the
  existing clauses (no new rule). Canonical home = §3.2.2; `glossary.md` Coupling-shape
  gains the co-producer target-dependents rendering (cross-ref, not a restated rule);
  `lens-set.md` Missed-dependents form-list gains the co-producer form (8th) + a
  reference to the side-effect behavior method. Coined terms defined by a single
  canonical sentence (F7). basis: Fragmentation/Undefined-shorthand lenses + the
  existing rendering precedent (glossary/lens-set cross-ref §3.2.2, F3).
- **D6** [CONDITIONAL] Structural-cure scope: EXCLUDE item-B's "prefer single source
  of truth / flag a known duplicated producer as debt" from §3.2.2 — the basis rule
  governs enumeration-COMPLETENESS, not refactoring prescription; the structural cure
  is a design-quality heuristic (a different concern). File it as a separate
  instance-lens/anti-pattern backlog item (no-silent-deferral). assumption
  (operator-resolvable): the operator agrees the structural cure is out-of-scope for
  the §3.2.2 completeness-basis clause. basis: §3.2.2 is a completeness-of-basis rule
  (F1/F2) — the cure prescribes a code-shape, not an enumeration.

## Cycle 2 (appended — append-only ledger; current state = latest line per entry)

### F-track (cycle 2)

- **F6** [VERIFIED — addressed] Leakage resolved: D3/D4 phrase both forms
  domain-generally; coding concretions bound by the instance render. basis: D3, D4.
- **F7** [VERIFIED — addressed] Undefined-shorthand resolved: "co-producer" defined
  inline in §3.2.2 (canonical), glossary renders a pointer; the emitted-effect form
  described generally (not coined "side-effect" — F9). basis: D5.
- **F8** [VERIFIED — non-issue] §5.2 body-shape cross-ref (`core.md:1123-1124`)
  paraphrases §3.2.2's legs as "references + behaviors preserved/dropped" — omits the
  shipped `dependents` leg (already stale), a Missed-dependents dependent of this
  change. basis: read `core.md:1123-1124` to clause close; observable fact: the
  parenthetical lists "references + behaviors", no "dependents". → reconciled by D7.
- **F9** [VERIFIED — non-issue] Term collision: `core.md:1121` (§5.2(d)) already uses
  "side effects and failure modes" for a *design decision's* observable effects —
  naming the §3.2.2 form "side-effect" multiply-defines it. basis: read `core.md:1121`
  + grep (sole spec occurrence of "side effect" is §5.2(d)); observable fact: one
  pre-existing use, different referent. → general phrasing in D3.

### D-track (cycle 2 — promotions + new)

- **D1** [VERIFIED] Scope locked. Edit sites: `core.md` §3.2.2 (behaviors + dependents
  clauses) + §5.2 cross-ref `:1123-1124` (D7); `glossary.md` Coupling-shape
  target-dependents rendering (`:112-122`); `anneal-dev/spec/lens-set.md`
  Missed-dependents form-list (`:106-119`). `modules.md` §3.4 confirmed-clean — no edit
  (D2). Render-debt (deferred, spec-only release): `anneal-dev/plugin/*` + instance
  specs → `instance-reinstantiation`. basis: corpus searches (F5) + §5.2 read (F8) +
  modules read (F4).
- **D2** [VERIFIED] Both forms render the existing closed Coupling-shape set —
  co-producer→target-dependents, emitted-effect→target-behavior; no fourth shape, so
  `modules.md` §3.4 is untouched AND its predicate machinery already fits: co-producer
  candidate uses `any-match`/`any-outside-scope` (target-dependents), emitted-effect
  candidate uses `expected-match` (target-behavior; "absence falsifies" = each effect
  must have a successor). basis: closed-set invariant (F3) + read `modules.md:358-390`
  (shape set + predicate-coherence) + the producer↔consumer precedent (`core.md:250-254`).
- **D3** [VERIFIED] §3.2.2 behaviors-clause sharpening. Contract (the AI behavior the
  rule forces): for a replacement/removal, the behaviors-preserved/dropped enumeration
  must cover **behaviors the replaced artifact emits rather than returns** — effects
  produced *within* its body (an emission/write/call), invisible to a reference-search
  (which surfaces callers, not internal effects). Method named: **read the replaced
  artifact's body** for effect-producing operations, NOT a reference-search of its
  callers. Evidence-bearing artifact / target-behavior falsification candidate: each
  enumerated emitted-effect must have a successor in the replacement; an effect with no
  successor = falsified (`expected-match`). Domain-general; instance binds concrete
  effect signatures. Delta: extend the existing "behaviors preserved or dropped"
  sentence (`core.md:256-257`) with the form + method + candidate. basis:
  `replacement-side-effect-behavior-parity` + bare clause (F1) + collision (F9).
- **D4** [VERIFIED] §3.2.2 dependents-clause sharpening. Contract: add a THIRD
  non-reference dependent rendering — the **co-producer**: when the amended artifact
  **produces a value written to a shared site consumed by equality** (two+ artifacts
  must emit a matching value because a downstream consumer compares them), the
  completeness obligation enumerates **every producer/writer of that shared site**, not
  only references to the amended artifact (a reference-search on the amended producer's
  name does not reach a *sibling* producer). Method named: search the **shared site's
  writers**, not the amended symbol's references. target-dependents falsification
  candidate: re-run the sink-writers enumeration; a co-producer whose emitted format
  diverges from the amended one = falsified (`any-match` on a divergent writer).
  Domain-general; instance binds concrete sink forms. Delta: add the third rendering to
  the dependents sentence (`core.md:246-254`). basis: `co-producer-format-parity` +
  the two-form set (F2) + the producer↔consumer mirror (`core.md:250-254`).
- **D5** [VERIFIED] Consolidation + renderings. The two sharpenings (D3, D4) are
  presented together in §3.2.2 as one principle — **enumeration keyed on the amended
  symbol's references misses (a) effects inside its body and (b) sibling producers of a
  shared site; aim the search at the right target (the body; the site's writers).**
  Edit-as-Pareto: extends the two existing clauses, no new rule/section. Canonical home
  = §3.2.2. Renderings: `glossary.md` Coupling-shape gains the co-producer as a third
  non-content-reference target-dependents rendering (pointer to §3.2.2, not a restated
  rule); `lens-set.md` Missed-dependents form-list gains the co-producer (eighth form;
  "all eight render the existing closed set, no fourth shape") + the behaviors leg's
  read-the-body method note. "co-producer" defined inline in §3.2.2. basis:
  Fragmentation/Undefined-shorthand resolution + rendering precedent (F3).
- **D7** [VERIFIED] Reconcile §5.2(e) cross-ref. `core.md:1123-1124` paraphrases
  §3.2.2's legs ("references + behaviors preserved/dropped") — stale (omits dependents,
  F8) and drift-prone. De-dup to a pointer: "(e) carries the §3.2.2 completeness
  enumeration" — drops the leg-list, points to the canonical home (prevents recurrence).
  Delta: replace the leg-list paraphrase at `:1123-1124` with the §3.2.2 pointer. basis:
  read `core.md:1123-1124` (F8) + Fragmentation lens (drifting second copy).

## Cycle 3 — convergence cycle (intent-falsification; mechanical SKIPPED: intent-delta)

Convergence cycle 3: fresh-context intent-falsification pass (opus subagent,
`.cycle-3.intent-falsification.md`) produced a D-track delta (D4/D5/D6 refined) →
**NOT converged**; mechanical falsification pass **skipped: intent-delta this cycle**.
New surfaces investigated: `core.md:250-254` (existing rendering's inline shape-licensing),
`co-producer-format-parity.md:38-49` (the bug's producer/consumer role-confusion).

### F-track (cycle 3 — intent-falsification findings)

- **INT-1** [VERIFIED — addressed] The co-producer rendering's closed-set licensing
  (dependency resolves through the shared sink's format contract) must be stated INLINE
  in the rule-text, not only the tracker — else a coherence-audit reads a bare
  sibling↔sibling edge as a fourth shape. basis: intent artifact + `core.md:250-254`
  (existing rendering carries its licensing inline). → addressed by D4'/D5'.
- **INT-2** [VERIFIED — addressed] §3.2.2 will carry two "producer"-keyed forms with
  inverted target-roles (target-as-consumer vs target-as-producer); the rendered
  sentence must disambiguate by role or it reproduces the consumer/co-producer
  conflation that IS the bug. basis: `core.md:250-251` vs the co-producer form +
  `co-producer-format-parity.md:38-49`. → addressed by D4'/D5'.
- **INT-3** [VERIFIED — surfaced] Emitted-effect teeth limit: `expected-match` catches a
  MISSING successor, not a wrong/partial one (multi-call drop). basis: `modules.md:377-382`
  vs `replacement-side-effect-behavior-parity.md:15`. Stated mechanical-floor (source
  item acknowledges `:73-76`); no D-defect. For step-4 review.
- **INT-4** [VERIFIED — surfaced] KEYSTONE teeth limit: the co-producer falsification
  candidate is recognition-gated — it takes the sink as input, so on the unrecognized-sink
  failure mode (the actual bug) the writer-set is empty → vacuous `holds`. R2's
  recurrence-reduction rests on whether the rule's PHRASING makes the AI recognize the
  equality-compared sink (judgment, not candidate-guaranteed). basis:
  `co-producer-format-parity.md:38-49` vs D4 candidate. For step-4 review.
- **INT-5** [VERIFIED — addressed] D6's exclusion of the structural cure is sound ONLY
  if the promised backlog item is actually filed — an unfiled promise re-creates the
  silent-deferral that enabled the original bug (Refactor #58). basis:
  `co-producer-format-parity.md:72-77` vs D6. → addressed by D6' completion obligation.
- **INT-6** [VERIFIED — surfaced] D7 de-dup to a pointer is lossless (reachability
  preserved; canonical legs at `core.md:254-257`). basis: `core.md:1123-1124`. Clean; no change.

### D-track (cycle 3 — amendments; the convergence D-delta)

- **D4** [VERIFIED] (refined — + acceptance criteria) ...as cycle-2 D4... PLUS the
  rendered co-producer sentence must carry (i) **inline closed-set licensing** — the
  dependency resolves through the shared sink's *format contract* (the symmetric
  analogue of producer↔consumer mediation-by-artifact; mirror the inline licensing at
  `core.md:252-253`), and (ii) **target-role disambiguation** — target-as-consumer →
  enumerate its producer; target-as-producer → enumerate sibling producers of the
  shared equality-compared sink. basis: INT-1, INT-2 + the rendering precedent
  `core.md:250-254`.
- **D5** [VERIFIED] (refined — + acceptance criteria) ...as cycle-2 D5... PLUS the
  glossary + lens-set renderings carry the same target-role disambiguation, so the
  co-producer is not conflated with the existing producer↔consumer form. basis: INT-2.
- **D6** [CONDITIONAL] (refined — + completion obligation) ...as cycle-2 D6 (EXCLUDE the
  structural cure)... PLUS: the structural-cure backlog item (`co-producer-format-parity`'s
  "single source of truth / collapse duplicate producers" cure) MUST be filed before run
  completion (no-silent-deferral; INT-5). basis: INT-5 + the no-silent-deferral rule.

**Convergence status:** cycle 3 NOT converged (D4/D5/D6 amended). Next cycle = re-run
the convergence cycle (fresh intent-falsification + mechanical) to confirm zero-D-delta.

## Cycle 4 — convergence cycle (RE-CONVERGED; CLEAN) → [READY]

Convergence cycle 4: fresh-context intent-falsification (`.cycle-4.intent-falsification.md`)
came back CLEAN on the D-track (INT-1/INT-2 CLOSED by the D4'/D5' acceptance criteria;
zero new D-delta) → mechanical falsification pass RAN (`.cycle-4.falsification.md`): all
six [VERIFIED] entries (D1,D2,D3,D4,D5,D7) **hold**, no flip. **Zero D-track deltas →
CONVERGED.** New surfaces this cycle: `core.md:250-254` (precedent re-read for licensing),
`deferred-removal-cross-run-obligation-ledger.md:82-92` (NEW-2 reconciliation),
corpus-wide flattened falsification sweeps.

### F-track (cycle 4)

- **NEW-1** [VERIFIED — surfaced] Bloat/human-inspectability risk: the consolidated §3.2.2
  now absorbs D3 + D4 + the inline-licensing + role-disambiguation in one ~20-line block.
  Realization-adequacy, NOT a D-defect (D5 commits Edit-as-Pareto; brevity discipline
  `core.md:1125-1129` + verify's skill-craft form pass + Bloat lens govern it). basis:
  `core.md:240-260` (current clause size) + D5 Pareto commitment. For step-4 / verify-form.
- **NEW-2** [VERIFIED — addressed] D6's promised structural-cure backlog item was unfiled
  (the `deferred-removal-cross-run-obligation-ledger` explicitly keeps itself separate,
  `:82-92`; the cure lived only inside `co-producer-format-parity.md:72-77`). **FILED** as
  `dev-notes/backlog/co-producer-single-source-of-truth-cure.md` (discharges D6'/INT-5).
  basis: `ls dev-notes/backlog/` post-filing.
- INT-3 / INT-4 / INT-6 re-surfaced as terminal [VERIFIED — surfaced] (mechanical floor /
  recognition-gating / lossless pointer) — carried for step-4; no new finding.

### D-track (cycle 4)

- **D5** [VERIFIED] (basis sub-annotation — resolution unchanged, not a D-delta)
  - basis clarified (cycle 4): the glossary/lens-set renderings inline-RESTATE the
    dependent form-list (glossary:112-122, lens-set:106-119) — they are not pointer stubs;
    the co-producer is added to those restating lists (D5's action already commits this).
    Mechanical pass confirmed no un-reconciled third restatement co-home exists.
- **D6** [CONDITIONAL] filing obligation DISCHARGED (NEW-2 item filed); decision unchanged
  (exclude the structural cure from §3.2.2). Auto-accepts at [READY] unless overridden.

### Fresh-session implementability — PASSED

A fresh session with only this tracker implements the design with no new design decision.
Per-step external evidence (each step = a located read of the edit point; content locked
in the cited D-entry):
- **Step 1** (D3, behaviors clause): edit point `core.md:255-257` — read confirms the bare
  "explicit enumeration of behaviors preserved or dropped" to extend with the emitted-effect
  form + read-the-body method + `expected-match` candidate. PASS.
- **Step 2** (D4, dependents clause): edit point `core.md:246-254` — read confirms the
  two-form set + the producer↔consumer precedent `:250-254` to mirror for inline licensing
  + add the co-producer form/method/`any-match` candidate + role-disambiguation. PASS.
- **Step 3** (D7, §5.2): edit point `core.md:1123-1124` — read confirms the leg-list
  paraphrase to replace with a §3.2.2 pointer. PASS.
- **Step 4** (D5/glossary): edit point `glossary.md:112-122` — read confirms the two
  non-content-reference renderings to extend with the co-producer (target-dependents
  rendering, role-disambiguated). PASS.
- **Step 5** (D5/lens-set): edit point `anneal-dev/spec/lens-set.md:106-119` — read confirms
  the seven-form list to extend to eight (+ the read-the-body method note). PASS.

### Impl plan (preview) — persisted at `.impl-plan.md`
3 units; Unit 1 first (canonical rule), Units 2 ∥ 3 after (renderings, disjoint files).
- **Unit 1** — `core.md` §3.2.2 (D3+D4+D5-core) + §5.2 (D7). First (canonical home; same
  file kept in one unit to avoid intra-file concurrency).
- **Unit 2** — `glossary.md` Coupling-shape co-producer rendering (D5). After Unit 1;
  parallel with Unit 3.
- **Unit 3** — `anneal-dev/spec/lens-set.md` Missed-dependents 8th form + method note (D5).
  After Unit 1; parallel with Unit 2.
- Disjointness basis (2 ∥ 3): Unit 2 touches only `spec/glossary.md`, Unit 3 only
  `anneal-dev/spec/lens-set.md` — disjoint files (search-established; no shared edit target).

## Implement progress

- **Unit 1** [COMPLETE] `spec/core.md` §3.2.2 (D3+D4+D5) + §5.2(e) (D7). Subagent
  (opus, in-place, sequential). Self-check clean (4 lenses + scope ∅); no loopback.
  Integrity check PASS (HEAD `42e5fd7` unchanged; only `spec/core.md` modified, +34/−10).
  Persistence: working-tree edit, release-deferred (spec-only run). Subagent pareto note:
  "two renderings"→uncounted "renderings" (avoids a stale count when a 4th rendering is
  later added) — in-scope phrasing, accepted. Realized text verified faithful
  (`core.md:240-284`, `:1148`).
- **Unit 2** [COMPLETE] `spec/glossary.md` Coupling-shape co-producer rendering (D5).
  Subagent (opus, in-place). Self-check clean; no loopback. Integrity PASS (only
  `glossary.md` modified, +10/−2). Count "Two"→"Three"; co-producer rendering at
  `glossary.md:122-130` with format-contract licensing + role-disambiguation + §3.2.2
  pointer. Release-deferred.
- **Unit 3** [COMPLETE] `anneal-dev/spec/lens-set.md` Missed-dependents 8th form +
  behaviors pointer (D5). Subagent (opus, in-place). Self-check clean (Fragmentation
  watched — item 3 stayed a §3.2.2 pointer, not a restatement); no loopback. Integrity
  PASS (only `lens-set.md` modified, +13/−2). co-producer 8th form at `lens-set.md:118-126`,
  "all eight … no fourth shape"; behaviors-leg emitted-effect pointer at `:132-135`.
  Release-deferred.
- **Implement COMPLETE** — all 3 units done; work-product diff = `spec/core.md` +
  `spec/glossary.md` + `anneal-dev/spec/lens-set.md` (HEAD `42e5fd7` unchanged; spec-only,
  uncommitted, release-deferred). → verify.

## Verify — [PASSED] (isolated)

Isolated verify subagent (opus, fresh-context, skill-craft invoked). Four checks + the
3-check battery, all accounted for.

Verify result: **[PASSED] (isolated)**
Finding ledger:
- F-V1 [VERIFIED — addressed] D1–D7 planned-vs-actual: all realized in the rule-text
- F-V2 [VERIFIED — addressed] R1–R6 + verbatim-request leg: each covered; no overclaim past INT-3/INT-4
- F-V3 [VERIFIED — non-issue] Bloat: §3.2.2 dense (~43 lines) but every segment load-bearing
- F-V4 [VERIFIED — non-issue] Fragmentation: glossary/lens-set restate the form-list + point to §3.2.2; method lives only in §3.2.2; no drift
- F-V5 [VERIFIED — non-issue] Undefined-shorthand: co-producer / emitted-effect / shared-equality-sink defined once, used consistently
- F-V6 [VERIFIED — non-issue] Leakage: §3.2.2 domain-general; coding concretions → instance render
- F-V7 [VERIFIED — non-issue] Over-claimed-verification: R5 stated as floor + recognized-case falsifier, not elimination
- F-V8 [VERIFIED — non-issue] Counts consistent + each internally correct (core uncounted / glossary "Three" / lens-set "eight"); no "fourth shape" assertion
- F-V9 [VERIFIED — addressed] Battery (a) render-fidelity: spec-only; git confirms no plugin render changed — standing render-debt, expected
- F-V10 [VERIFIED — non-issue] Battery (b) coherence: all cross-refs resolve; closed Coupling-shape set intact across core/glossary/lens-set
- F-V11 [VERIFIED — addressed] Battery (c) skill-quality/form: enforcement preserved, evidence-bearing, Edit-as-Pareto
- F-V12 [VERIFIED — addressed] D6 structural-cure backlog item filed (discharges D6'/INT-5/NEW-2)
- F-V13 [VERIFIED — surfaced] NEW-1 §3.2.2 density + INT-3/INT-4 teeth-floor — terminal judgment residuals for operator review

## RUN COMPLETE — verify [PASSED] 2026-06-07

Spec-only release (3 files: `spec/core.md` §3.2.2+§5.2, `spec/glossary.md` Coupling-shape,
`anneal-dev/spec/lens-set.md` Missed-dependents; +57/−14; HEAD `42e5fd7`, uncommitted).
Method-kernel edit → release pending the operator's soundness verdict (focusing artifact:
INV-1/INV-2 strengthened; INV-5 — weigh the INT-4 recognition-gated co-producer teeth) +
commit approval. Render-debt → `instance-reinstantiation` (clippy/daneel + anneal-dev/plugin).
Backlog: archive `co-producer-format-parity` + `replacement-side-effect-behavior-parity`
(shipped to §3.2.2); `co-producer-single-source-of-truth-cure` filed (D6).
