# Run: framework-gap-receipt

- **Status:** PASSED — **SHIPPED `6673e29` (main, pushed 2026-06-15).** Backlog item archived; NEXT-UP advanced. (verify [PASSED] isolated, cycle-6/8 convergence clean; operator: "ship".)
- **Phase:** verify
- **Verify result:** [PASSED] (isolated, subagent a357a7758a404a1c2) — 4 checks all cited-clean; D1-D11 all faithfully realized; R1-R6 all covered; lenses clean; coherence (4b) clean; render-fidelity (4a) + skill-quality (4c) N/A (development-process.md/README.md not rendered, not plugin-skill files). No finding short of [VERIFIED]. Finding ledger: F1-F8 [VERIFIED — non-issue], F9 [VERIFIED — addressed], F10 [VERIFIED — non-issue], F11/F12/F13 [VERIFIED — addressed], F14 [VERIFIED — surfaced], F15/F16/F17/F18/F19/F20 [VERIFIED — addressed]. (F14 + the weak class-label/lens-framework residuals are the 2 irreducible [VERIFIED — surfaced] residuals surfaced for operator review.)
- **Mode:** auto-battle (switched from interactive at operator request, cycle 1→2)
- **Task:** Build `framework-gap-receipt` (dev-notes/backlog/framework-gap-receipt.md,
  live NEXT-UP #1) — a periodic, post-hoc, fresh-context, cross-run reader of an
  instance's persisted falsification run-records that tallies falsification findings
  by class, detects recurrence, and routes each recurring class via the boundary
  discriminator (lens / framework / neither). Additive machinery OUTSIDE the per-run
  kernel (does not touch `core.md` / `modules.md §4`).

## Requirements record (R1..Rn — the goal, separated from any proposed solution)

**Operator verbatim request:** "pickup from backlog" → resolved (via
`dev-notes/backlog/README.md` session-15 READ-FIRST) to building
`framework-gap-receipt`, the live NEXT-UP #1. Item spec:
`dev-notes/backlog/framework-gap-receipt.md`.

- **R1** — A periodic, post-hoc, cross-run reader exists that tallies falsification
  findings **by class** across an instance's persisted run-records and detects
  **recurrence** (cross-run frequency; and the sharpest signal — the same class
  recurring within one run, post-[VERIFIED]).
- **R2** — The tally is **split by pass-type** (mechanical vs intent), and the split
  routes: a recurring mechanical class → an enumerable lens-or-re-sequence question;
  a recurring intent class → a stronger framework-gap signal (and almost never a lens).
- **R3** — Each recurring class is **routed** via the boundary discriminator:
  new-thing-to-look-*for* (enumerable, general, uncovered) → **lens**; change to how
  the looking is *structured* (cycle count, convergence criterion, independence,
  sequencing) → **framework**; otherwise → **neither** (the default).
- **R4** — All four load-bearing safeguards are stated/encoded: (1) a single
  falsification firing is NOT a framework failure — recurrence is the signal, a single
  catch is the system working; (2) mechanical detection of the pattern + human
  judgment on the interpretation (operator binds lens/framework/neither — calibrator,
  not per-case adjudicator); (3) recurrence → re-sequence/strengthen EXISTING
  structure by default, a new lens needs novelty+generality and the routing forces
  that justification every time (guards the additive-reflex anti-pattern / lens-crowding);
  (4) outside the kernel — a reader of existing run-records, not a per-run tracker field.
- **R5** — Scope is **caught-side only**: the pass-type split routes only what
  falsification *caught* (pass-type exists only for caught findings). The missed side
  (escapes — no pass-type) is out of scope and routes by `self-review-missed-side`
  (Q2/Q3). This caught/missed split is *why* the receipt and self-review do not merge.
- **R6** — The machinery is **additive and outside the per-run kernel**: it does not
  touch `core.md` cycle machinery or the `modules.md §4` post-run-review minimum-shape;
  it reads what cycles already persist.

---

## F-track (findings)

- **F1** [VERIFIED — non-issue] development-process.md is the declared home of the shared
  framework-dev machinery, and practice 12 (Periodic coherence audit) is the structural
  sibling — a periodic, fresh-context framework-review pass routing findings into
  practice-11. basis: located read `development-process.md:66-72` ("home of the shared
  framework-dev machinery … the coherence-audit cadence") + `:486-555` (practice 12 = a
  periodic pass with mechanical/judgment trigger + handoff + practice-11 routing).
  → grounds D1 (home).
- **F2** [VERIFIED — non-issue] post-run-review.md is per-run, operator-invoked,
  debugging-only, and its output is NOT persisted (persisting prior-run analysis pollutes
  future runs); it is cross-run-distinct from the receipt but shares the
  operator-invoked / output-to-operator / not-mechanically-triggered invocation model.
  basis: located read `post-run-review.md:11-51` ("a debugging tool, not a routine check
  … delivered to the operator in the session — not persisted"). → grounds D2 (invocation).
- **F3** [VERIFIED — non-issue] The coarse pass/route tagging the receipt relies on is
  present in the persisted artifacts: `modules.md §3.4` (mechanical falsification-pass —
  pass-tag) + `§3.4.1` (intent-falsification-pass; per-finding `route ∈
  {mechanical-falsification-candidate, [VERIFIED — surfaced]}`). The pass-type split is
  tallyable from persisted records; only the *fine* class lives in finding prose.
  basis: located read `spec/modules.md:331-513`. → grounds D3, D4.
- **F4** [VERIFIED — non-issue] The receipt's stated downstream consumer — the
  failure-class register — is NOT built machinery: `post-run-review-failure-class-register`
  is archived, ABSORBED (session 14) into `self-review-missed-side` ([DESIGN], unbuilt).
  The receipt's output must stand alone (operator binds routing); feeding recurring classes
  into a future register is a forward-reference, not a dependency. basis: located read
  `dev-notes/backlog/archive/post-run-review-failure-class-register.md:5-8` (CLOSED —
  ABSORBED) + `dev-notes/backlog/self-review-missed-side.md:1-9`. → grounds D7.
- **F5** [VERIFIED — non-issue] `self-review-missed-side` ([DESIGN]) owns the missed-side
  (Q2 known-escape probe + Q3 novel hunt) and names framework-gap-receipt as "the caught
  row (Q1), the opposite mechanism; NOT redundant"; its home (modules §4 + post-run-review.md)
  is distinct from the receipt's → no home-collision. Confirms R5's caught/missed boundary
  and the no-merge. basis: located read `self-review-missed-side.md:6-8` (receipt owns
  Q1/caught) + `:119-121` (relates-to: caught row, NOT redundant). → grounds D7.
- **F6** [VERIFIED — non-issue] The run-records the receipt reads are instance-local /
  cross-repo: clippy persists `.clippy/runs/*.passes.md` (in clippy's repo, not here);
  anneal-dev persists `.anneal-dev/runs/*.falsification.md` + `*.intent-falsification.md`
  (37 + 29 present in this repo). The receipt is framework-general machinery reading
  instance-defined run-records ("and equivalents across instances"). basis: search
  `ls .anneal-dev/runs/*.falsification.md | wc -l` → 37; `…*.intent-falsification.md` → 29.
  → grounds D3, D9.
- **F7** [VERIFIED — non-issue] Enforcement model: the receipt is operator-invoked
  (optional, like post-run-review), so "didn't run it" is not a violation; enforcement
  binds on the *artifact when run* — the evidence-bearing by-class tally + the practice-11
  routing table. The four safeguards map to existing disciplines: SG2↔practice 11
  (subagent detects → AI first-judge → operator second-judge), SG3↔additive-reflex/practice 8,
  SG1↔recurrence mechanical-criteria, SG4↔outside-kernel. basis: located read
  `development-process.md:400-484` (practice 11) + `references/lenses.md` Unenforced-rule.
  → grounds D6, D9.
- **F8** [VERIFIED — non-issue] No existing receipt / cross-run / class-recurrence
  machinery exists anywhere in the corpus (Fragmentation clean — the receipt is additive;
  the pass-type *tags* it consumes are reuse of modules §3.4, not duplication). The
  "framework-gap receipt" coined term needs only a single in-place defining sentence:
  glossary.md carries NO entry for the practice-12 sibling terms (coherence-audit / handoff),
  so the practice-12 precedent is define-in-place, no glossary.md entry. basis: search
  `grep -rniE 'framework-gap|cross-run|class.recurrence' development-process.md post-run-review.md spec/ anneal-dev/spec/`
  → empty; `grep -niE 'coherence-audit|handoff|receipt' spec/glossary.md` → empty.
  → grounds D10.
- **F9** [VERIFIED — addressed] Missed-dependents (standardized pass, cycle 1): the practice-13
  *addition* has one corpus dependent — the intro machinery-enumeration at
  `development-process.md:66-68` names "the coherence-audit cadence" (the receipt's structural
  sibling), so the receipt warrants a parallel mention there. No practice-count / external
  practice-list dependent (append-numbered; cross-doc search empty). basis: located read
  `development-process.md:66-72` + search `grep -rniE 'twelve|practices? 1-12|13 practice'` → empty.
  disposition addressed-by → D11 (impl updates the intro enumeration).
- **F10** [VERIFIED — non-issue] (cycle 2 / convergence, new surface: the umbrella
  `self-improvement-signal-architecture`). The umbrella confirms the design: it places the receipt
  as **Q1 (caught × known)**, specifies a home for the *missed-side* only (modules §4 + post-run-review.md)
  — **not** the receipt's home, so D1 is uncontradicted — and says "Keep separate, do NOT merge:
  framework-gap-receipt" (confirms D7). One reconciliation: the umbrella glosses the receipt as "reads
  the tracker," but precisely the receipt's source is the **falsification-pass artifacts**
  (`.passes.md` / `.falsification.md` / `.intent-falsification.md`) — they carry the pass-type tag that
  IS the router (D4); the tracker carries only the consequences (flips). Also: Q4 (caught × novel) is
  empty by construction → the receipt is caught×KNOWN (tallies known classes + recurrence). No D-delta;
  D3's source = the pass-type-tagged falsification artifacts (made explicit). basis: located read
  `dev-notes/backlog/self-improvement-signal-architecture.md:14-22` (2×2 + Q4-empty) + `:55-57` (do-not-merge)
  + `:30` ("the receipt (which reads the tracker)").
- **F11** [PENDING] (intent-falsification F-a) The by-class tally's evidence-bearing strength is weak at the
  class-LABEL layer: the class is not a persisted field (line shapes `{finding,criterion-attacked,refutation,route}`
  modules.md:477; `{decision-ID,[shapes],aggregate}` modules.md:343 — no class field), so two fresh contexts can
  class the same finding differently → by-class counts/recurrence not stably re-derivable. basis: located read
  modules.md:440-513 + D3. drives → D3 amendment (class-label = weak artifact; cite per-class instances;
  stability via separate-checker). holds phase until D3 re-[VERIFIED].
- **F12** [PENDING] (intent-falsification F-b, mechanical-confirmed FALSIFIED) Post-[VERIFIED] within-run
  recurrence (D8's "sharpest signal") is NOT recoverable from the falsification artifacts alone — the §3.4.1
  intent per-finding line carries no `[VERIFIED]` anchor. orchestrator-computed: candidate
  `expected-match:"[VERIFIED]"` over a `.intent-falsification.md` per-finding line → pattern absent → falsified.
  basis: located read modules.md:413 (mechanical line anchors [VERIFIED]) vs :440-513 (intent line does not).
  drives → D8 [INVALIDATED]→[PENDING] + D3 source amendment (receipt reads falsification artifacts + tracker).
  holds phase until D8 re-[VERIFIED].
- **F13** [PENDING] (intent-falsification F-c) "The pass-type split IS the router" over-claims: an intent-pass
  per-finding line can route `mechanical-falsification-candidate` (modules.md:486-507), so pass-type ⊥ route is
  false at the finding level. basis: located read modules.md:486-507. drives → D4 amendment (split by the
  falsification's LANDED type, not first-surfacing pass). holds phase until D4 re-[VERIFIED].
- **F14** [VERIFIED — surfaced] (intent-falsification F-d) The lens-vs-framework discriminator has a residual
  "fits-both" ambiguity (Unit-31 resolved narratively); SG3's default-to-strengthen-existing is the tiebreaker
  D5 already states, and the residual is the inherent lens/framework judgment (SG2). Terminal — no design
  change; surfaced for operator review. basis: located read item:31-44 + D5 + `references/foundations.md`
  Finding states ([VERIFIED — surfaced]).
- **F15** [PENDING] (intent-falsification F-e) SG2 operator-binds has no binder if the receipt co-runs on
  practice-12's MECHANICAL cadence in auto-battle (the D2 co-run affordance + practice-12 trigger
  `development-process.md:499-512` + no operator). basis: located read D2 + practice 11 + practice 12 trigger.
  drives → D2 amendment (drop co-run-with-mechanical-cadence affordance) + D6 amendment (routing is surface-only,
  operator binds at review). holds phase until D2/D6 re-[VERIFIED].
- **F16** [PENDING] (intent-falsification F-f) Caught/missed mischaracterization risk: an intent-pass finding of
  design-gap CHARACTER carries pass-type=intent, which could read as "missed-side in the caught tally."
  Resolution: a concern a falsification pass CATCHES is caught-side by definition (missed = no pass caught it).
  basis: located read `self-review-missed-side.md:45-67` + D7. drives → D7 clarification ("caught" = a
  falsification pass fired, mechanical OR intent). holds phase until D7 re-[VERIFIED].

- **F11** [VERIFIED — addressed] (cycle 3) addressed by D3 amendment (class-label weak artifact + cited instances + separate-checker). basis: D3 [VERIFIED] cycle 3.
- **F12** [VERIFIED — addressed] (cycle 3) addressed by D8 + D3 amendment (post-[VERIFIED] from tracker flip-history; source = artifacts + tracker). basis: D8 [VERIFIED] cycle 3.
- **F13** [VERIFIED — addressed] (cycle 3) addressed by D4 amendment (split by landed type). basis: D4 [VERIFIED] cycle 3.
- **F15** [VERIFIED — addressed] (cycle 3) addressed by D2 + D6 amendment (drop co-run; surface-only routing). basis: D2, D6 [VERIFIED] cycle 3.
- **F16** [VERIFIED — addressed] (cycle 3) addressed by D7 clarification ("caught" = a pass fired). basis: D7 [VERIFIED] cycle 3.
- **F17** [PENDING] (cycle 4 intent-falsification F-A) D8's post-[VERIFIED] signal rode the bare tracker
  `[INVALIDATED]→[PENDING]` flip, which is OVERLOADED — the amendment-is-contradiction rule fires the same flip
  for target-naming/scope/count/basis changes, none of which is a falsification-class-recurrence. basis: located
  read `references/foundations.md` Design-decision states (amendment-is-contradiction) + grep INVALIDATED
  `.anneal-dev/runs/*.md` (heterogeneous flip causes). drives → D8 + D3 re-amendment (post-[VERIFIED] grounded
  in the falsification artifact as cause, paired with [VERIFIED] status). holds phase until D8/D3 re-[VERIFIED].
- **F18** [PENDING] (cycle 4 intent-falsification F-B) D4's "landed type" for an intent finding routed
  `mechanical-falsification-candidate` is a cross-artifact join (route field reconciled against the same cycle's
  §3.4 mechanical line / skip record), not a single-field read. basis: located read modules.md:486-507 + skip
  carve-out modules.md:423-433. drives → D4 clarification. holds phase until D4 re-[VERIFIED].
- **F19** [PENDING] (cycle 4 intent-falsification F-C) Internal contradiction: F10 pruned "reads the tracker"
  (source = falsification artifacts); F12's fix re-added the tracker as a source without reconciling SG4
  ("reader of run-records, NOT a per-run tracker field"). basis: located read `framework-gap-receipt.md` item:72
  (SG4) + F10 vs D3/D8 cycle-2 lines (tracker re-added). drives → D8 + D3 re-amendment with explicit SG4
  reconciliation (reading existing records ≠ adding a per-run field). holds phase until D8/D3 re-[VERIFIED].
- **F17** [VERIFIED — addressed] (cycle 5) addressed by D8 + D3 re-amendment (post-[VERIFIED] grounded in the falsification cause, not the bare flip). basis: D8, D3 [VERIFIED] cycle 5.
- **F18** [VERIFIED — addressed] (cycle 5) addressed by D4 clarification (landed type via cross-artifact join). basis: D4 [VERIFIED] cycle 5.
- **F19** [VERIFIED — addressed] (cycle 5) addressed by D8 + D3 re-amendment with explicit SG4 reconciliation (reading existing records ≠ a new per-run field). basis: D8, D3 [VERIFIED] cycle 5.
- **F20** [VERIFIED — addressed] (cycle 7, impl self-check Missed-dependents → loopback) A SECOND home of the
  framework-dev-machinery enumeration — `README.md:116-117` ("the home of the framework-dev machinery: the
  development practices, validation-watch governance, the coherence-audit cadence, and the release loop…") —
  names the receipt's sibling but not the receipt; D11/F9's "sole dependent" basis missed it (cycle-1 search used
  spaced "coherence audit"/"practice 12", missing the hyphenated "coherence-audit cadence"). Corrected
  corpus-wide search establishes the FULL dependent set = exactly 2 homes (no third). basis: search
  `grep -rniE 'coherence-audit cadence|shared framework-dev machinery|release/marketplace loop|release loop with its discharge'
  README.md development-process.md instantiation-guide.md spec/ anneal-dev/ instance-template/ CLAUDE.md post-run-review.md`
  → 2 homes only. disposition addressed-by → D11 re-form (cycle 7). (Impl Unit-1's development-process.md edits NOT
  invalidated — F20 extends D11, doesn't contradict; working-tree edits preserved per redo-inheritance.)
- **F21** [VERIFIED — addressed] (release step-4 skill-craft self-review, subagent adf7b968f610150d6; notable,
  fix-now) "lens-crowding" was mis-attributed to skill-craft anti-patterns (it's the framework's own
  `lens-crowding-vs-broad-search` concern; "additive-reflex" is the skill-craft anti-pattern, already cited).
  Fixed at `development-process.md:610-612` (disentangled attribution). basis: `grep -rin lens-crowding` skill-craft → empty.
- **F22** [VERIFIED — addressed] (release step-4 skill-craft self-review; nit, fix-now) "the
  amendment-is-contradiction rule" lacked an anchor. Fixed at `development-process.md:585` (added `core.md §5.2`).
  basis: located read `spec/core.md:1157` (§5.2 Design-decision states) + `:1221` (the clause). Both fixes
  behavior-preserving (citation precision) → **delta-verify**: findings closed, surrounding rule-text + the
  4 keep-as-is/observation skill-craft items unchanged, no new dependent → clean.

---

## D-track (design decisions)

> **Cycle 2 (convergence) D-deltas** — the intent-falsification pass reopened D2, D3, D4, D6, D7, D8 (D8
> mechanically falsified). Each flips [VERIFIED]→[INVALIDATED]→[PENDING], re-formed below with the sharpened
> resolution; re-verified at cycle 3's convergence. Mechanical pass **skipped this cycle** (intent-delta).
> D1, D5, D9, D10, D11 unchanged (still [VERIFIED]/[CONDITIONAL]).

- **D1** [CONDITIONAL] **Home/scope.** Build the receipt as a **new practice 13 in
  `development-process.md`** ("Periodic framework-gap receipt") — the cross-run, caught-side
  sibling of practice 12 (coherence-audit reads the *corpus*; the receipt reads the
  *run-records*). It does NOT touch `core.md` / `modules.md §4` → corpus-evolution edit, not
  method-kernel. (a) target: new practice section in development-process.md; (b) shape: a
  periodic-pass practice paralleling practice 12's structure (trigger + dispatch + findings
  artifact + practice-11 routing); (c) accept: a reader of the section can run the pass and
  produce the routing artifact without a new design decision; (d) failure modes: home-muddle
  if placed in post-run-review.md (per-run-framed); fragmentation if a standalone doc splits it
  from practice-12; (e) basis: F1 + F8. **assumption (operator-resolvable):** development-process.md
  practice 13 is the right home vs. post-run-review.md.
  considered: post-run-review.md (rejected: per-run-framed, "not part of the spec" lighter home,
  would muddy its per-run scope — cross-reference instead, F2); standalone doc (rejected:
  fragments periodic-framework-review machinery from its practice-12 sibling — Fragmentation, F8).
- **D2** [VERIFIED] **Invocation/trigger.** Operator-invoked, optional, at the operator's
  framework-review cadence — NOT a mechanical per-cycle/per-run trigger and NOT a per-run
  obligation (honors R4-SG4 + R6). Stated affordance (not a mechanical bind): it MAY co-run with
  practice-12's coherence-audit cadence (both periodic framework-review passes). basis: item
  ("runs at the operator's framework-review cadence … not per run") + F2 (post-run-review's
  operator-invoked precedent).
- **D3** [VERIFIED] **Mechanism + evidence-bearing artifact.** The pass produces an
  evidence-bearing **by-class tally**: per falsification-finding class observed across the read
  run-records — the count + cited instances (run:cycle:finding) + a **recurrence flag**. Two
  recurrence scopes: cross-run frequency (the tally) and the sharpest signal, same class ≥2×
  within one run post-[VERIFIED] (D8). A fresh context assigns the fine class from finding prose
  (the class is not a tagged field; coarse pass-tag is — F3). (a) target: the practice's mechanism
  clause; (b) shape: evidence-bearing artifact (structural enforcement, practice 8) — producing the
  tally requires doing the work, a fresh context re-derives from the same records; (c) accept: the
  tally cites located instances, not a bare count; (d) failure modes: a bare-count tally with no
  cited instances is malformed; (e) basis: item "what's already free vs needs building" + F3 + F6.
- **D4** [VERIFIED] **Pass-type split as router.** The tally is split by pass-type (mechanical
  §3.4 vs intent §3.4.1 — already-free tags). The split IS the router: a recurring **mechanical**
  class = enumerable → a lens-or-re-sequence question; a recurring **intent** class = judgment →
  a stronger framework-gap signal, almost never a lens candidate. basis: located read modules
  §3.4/§3.4.1 (F3) + item "Split the tally by pass-type — the split is the router".
- **D5** [VERIFIED] **Routing discriminator + SG3.** Each recurring class routes via the boundary
  discriminator — new-thing-to-look-*for* (enumerable, general, uncovered) → **lens**; change to
  how looking is *structured* (cycle count, convergence criterion, independence, sequencing) →
  **framework**; else → **neither** (default). SG3: recurrence is evidence for
  *re-sequencing/strengthening existing structure*, NOT a new lens by default; only novelty+generality
  justifies a new lens, and the practice **forces that justification every time** (guards the
  additive-reflex anti-pattern; cites lens-crowding). basis: item routing discriminator + SG3 +
  `skill-craft/references/anti-patterns.md` Additive-reflex + `lens-crowding-vs-broad-search`.
- **D6** [VERIFIED] **Operator-binds via practice 11.** Mechanical detection of the pattern (tally +
  recurrence flag); the operator **binds** the lens/framework/neither interpretation (RLHF
  calibrator, not per-case adjudicator). Encoded as the practice-11 flow: the AI first-judges each
  routing (cited discriminator-test + observable evidence), the operator second-judges. Auto-promoting
  recurring→lens is forbidden (R4-SG2). basis: located read practice 11 (`development-process.md:400-484`)
  + R4-SG2.
- **D7** [VERIFIED] **Caught-side scope + boundary.** The receipt routes ONLY what falsification
  caught (pass-type exists only for caught findings). The missed side (escapes — no pass-type) is
  out of scope and routes by `self-review-missed-side` (Q2/Q3); the practice cross-references it.
  This caught/missed split is *why* the receipt and self-review don't merge. The receipt does NOT
  depend on the (absorbed/unbuilt) failure-class register; recurring-classes feeding a future
  register is a forward-reference only. basis: F4 + F5 + item scope clause ("Scope of this router —
  caught-side only").
- **D8** [VERIFIED] **SG1 + the recurrence discriminator.** The practice states explicitly that a
  falsification firing is NOT a framework failure — usually the framework succeeding; the narrow
  signal is the same class recurring within one run post-[VERIFIED] (the forming discipline not
  internalizing what falsification keeps teaching → re-sequence). A single catch = system working.
  Mechanical criteria: recurrence count + post-[VERIFIED] position. basis: item SG1 + the Unit-31
  concrete instance (enumeration/co-producer class falsified 2× post-[VERIFIED], cycles 3 & 5).
- **D9** [VERIFIED] **Dispatch to fresh context.** The pass is dispatched to a fresh-context
  subagent — the cross-run independence + the classification's own fresh-context independence
  (R4-SG4 + the item's "fresh-context" property + practice 3 subagents-for-context-heavy-work);
  findings return as a practice-11 ranked table. basis: item "fresh-context" + R4-SG4 + located read
  practice 3 (`development-process.md:143-150`) + practice 11.
- **D10** [VERIFIED] **Terminology.** "Framework-gap receipt" is a coined term defined in-place by a
  single canonical defining sentence in practice 13 — no `spec/glossary.md` entry (glossary.md is the
  method-kernel glossary; the receipt is a dev-process-doc-local term, and the practice-12 sibling
  terms carry no glossary.md entry — define-in-place precedent). basis: F8 + located read practice 10
  (`development-process.md:365-398`, glossary-entry rule scoped to corpus defined-shorthand) +
  practice-12 precedent.
- **D11** [VERIFIED] **Dependent update (Missed-dependents).** Impl adds a parallel mention of the
  receipt to the intro machinery-enumeration (`development-process.md:66-68`), alongside "the
  coherence-audit cadence" (the receipt's sibling). No other dependent (F9). (a) target: the intro
  enumeration sentence; (b) shape: append the receipt to the named-machinery list; (c) accept: the
  enumeration names the receipt; (d) failure modes: none beyond the list growing one item; (e) basis: F9.

### Cycle-2 convergence amendments (append-only re-forms; flip [VERIFIED]→[INVALIDATED]→[PENDING])

- **D2** [PENDING] (amended cycle 2 per F15; was [VERIFIED] cycle 1) **Invocation/trigger.** Operator-invoked,
  optional, at the operator's framework-review cadence — NOT a mechanical per-cycle/per-run trigger and NOT a
  per-run obligation (R4-SG4 + R6). **DROP the prior "may co-run with practice-12's mechanical coherence-audit
  cadence" affordance** — a mechanical (operator-absent) trigger would leave the practice-11 routing unbound
  (F15). The receipt may be *scheduled* at the operator's framework-review cadence, but its routing output is
  surface-only (D6), so operator-absence at firing is safe. basis: F15 + item ("operator's framework-review
  cadence … not per run") + located read practice 12 trigger (`development-process.md:499-512`, mechanical/operator-absent).
- **D3** [PENDING] (amended cycle 2 per F11, F12; was [VERIFIED] cycle 1) **Mechanism + evidence-bearing
  artifact + source.** The pass produces a **by-class tally**: per class — the count + **cited located
  instances** (run:cycle:finding-prose quote) + a recurrence flag. **Source = the falsification-pass artifacts
  (pass-type tag + class prose: clippy `.passes.md`; anneal-dev `.falsification.md` + `.intent-falsification.md`)
  AND the run tracker (the [VERIFIED]→[INVALIDATED]→[PENDING] flip history that carries the post-[VERIFIED]
  position, F12).** Evidence-bearing layering (honest, per `foundations.md`): the counts + cited instances are
  **strong** (located reads of the records, re-checkable); the **class-LABEL is a weak artifact** (judgment) —
  its stability comes from the **separate checker** (operator second-judge per D6, or a fresh re-run), NOT from
  the label being mechanical (F11). The tally cites its per-class instances so the grouping is auditable even
  though the label is judgment. (a) target: the practice's mechanism clause; (b) shape: by-class tally,
  source = artifacts + tracker, class-label weak/separate-checker-enforced; (c) accept: the tally cites located
  instances per class + reads both sources; (d) failure modes: a bare-count tally, or class-label sold as
  mechanical/stable, is malformed; (e) basis: F11, F12, F3, F6, F10.
- **D4** [PENDING] (amended cycle 2 per F13; was [VERIFIED] cycle 1) **Pass-type split as router (by LANDED
  type).** The tally is split by the falsification's **landed type**, not by which pass first surfaced it: a
  **§3.4 mechanical falsification line** (a candidate that falsified a basis — INCLUDING an intent-pass finding
  that routed `mechanical-falsification-candidate` and then falsified) = enumerable → a lens-or-re-sequence
  question; a **§3.4.1 `[VERIFIED — surfaced]` judgment residual** (pure judgment, no mechanical reduction) →
  a stronger framework-gap signal, almost never a lens. basis: F13 + located read modules.md:486-507
  (intent-finding route ∈ {mechanical-candidate, surfaced}) + §3.4/§3.4.1.
- **D6** [PENDING] (amended cycle 2 per F15; was [VERIFIED] cycle 1) **Operator-binds via practice 11 —
  surface-only.** Mechanical detection (tally + recurrence flag) is force-produced; the routing
  (lens/framework/neither) is the AI's **first-judge** disposition, **surfaced for the operator's review and
  NEVER auto-applied** — the operator **binds** it as second-judge whenever they review (the operator-independence
  boundary, `foundations.md`: force-produce the surfacer, never gate on operator presence). This closes the
  auto-battle/operator-absent gap (F15): an unattended firing still only produces a surfaced first-judge artifact;
  no routing is applied without the operator. Auto-promoting recurring→lens is forbidden (R4-SG2). basis: F15 +
  located read practice 11 (`development-process.md:400-484`) + `foundations.md` operator-independence boundary.
- **D7** [PENDING] (amended cycle 2 per F16; was [VERIFIED] cycle 1) **Caught-side scope + boundary
  (clarified).** The receipt routes ONLY what a falsification pass **caught** — where "caught" = a falsification
  pass (mechanical §3.4 OR intent §3.4.1) **fired and caught it**; an intent-pass finding of design-gap character
  is still **caught-side** (it was caught). The **missed side** = concerns NO pass caught (escapes), out of
  scope → `self-review-missed-side` (Q2/Q3). This caught/missed split is *why* the receipt and self-review don't
  merge. No dependency on the (absorbed/unbuilt) failure-class register. basis: F4, F5, F16 + item scope clause.
- **D8** [PENDING] (amended cycle 2 per F12 — mechanically falsified; was [VERIFIED] cycle 1) **SG1 + the
  recurrence discriminator (source-corrected).** The practice states a falsification firing is NOT a framework
  failure — usually the framework succeeding; the narrow signal is the same class recurring within one run
  post-[VERIFIED]. **The post-[VERIFIED] position is read from the TRACKER's flip history**
  ([VERIFIED]→[INVALIDATED]→[PENDING] on the affected entry), NOT from the falsification artifacts alone (which
  carry no [VERIFIED] anchor on the intent side — F12). A single catch = system working. Mechanical criteria:
  recurrence count (from the tally, D3) + post-[VERIFIED] position (from the tracker). basis: F12 + located read
  modules.md:413 (mechanical line anchors [VERIFIED]) + :440-513 (intent line does not) + item SG1 + Unit-31 instance.

### Cycle-3 re-verification (working context locks the amendments; broken-basis check clean — D1/D5/D9/D10/D11 unaffected)

- **D2** [VERIFIED] (cycle 3) Re-formed resolution sound: operator-invoked + surface-only, co-run-with-mechanical-cadence dropped — closes F15. basis: as D2 cycle-2 line.
- **D3** [VERIFIED] (cycle 3) Re-formed resolution sound: source = falsification artifacts + tracker; class-label weak/separate-checker-enforced; cited per-class instances — closes F11, F12. basis: as D3 cycle-2 line.
- **D4** [VERIFIED] (cycle 3) Re-formed resolution sound: split by landed type (§3.4 mechanical line vs §3.4.1 surfaced residual) — closes F13. basis: as D4 cycle-2 line.
- **D6** [VERIFIED] (cycle 3) Re-formed resolution sound: routing is surface-only first-judge, operator binds at review — closes F15's auto-battle gap. basis: as D6 cycle-2 line.
- **D7** [VERIFIED] (cycle 3) Re-formed resolution sound: "caught" = a falsification pass (mechanical OR intent) fired and caught it — closes F16. basis: as D7 cycle-2 line.
- **D8** [VERIFIED] (cycle 3) Re-formed resolution sound: post-[VERIFIED] position read from the tracker flip-history, not the artifacts alone — closes F12. basis: as D8 cycle-2 line.

### Cycle-4 convergence re-amendments (per F17/F18/F19; flip [VERIFIED]→[INVALIDATED]→[PENDING])

- **D3** [PENDING] (re-amended cycle 4 per F17, F19; was [VERIFIED] cycle 3) **Mechanism + evidence-bearing
  artifact + source (re-grounded).** The pass produces a **by-class tally**: per class — the count + **cited
  located instances** (run:cycle:finding-prose quote) + a recurrence flag. **Source = the falsification-pass
  artifacts as the PRIMARY source** (clippy `.passes.md`; anneal-dev `.falsification.md` + `.intent-falsification.md`)
  — they carry the pass-type tag, the class prose, and the falsification CAUSE (what falsified, in which cycle).
  The tracker's **existing status-history** is consulted ONLY to confirm the affected entry's [VERIFIED]
  position for the post-[VERIFIED] qualifier (D8), paired with the falsification cause — **never the bare flip
  signature** (overloaded, F17). **SG4-reconciled (F19):** this is READING existing run-records (artifacts +
  the tracker's existing status-history); it does NOT add a per-run tracker FIELD — reading-existing ≠ a new
  field. Evidence-bearing layering: counts + cited instances are **strong** (located reads); the **class-LABEL
  is a weak artifact** (judgment), stability via the **separate checker** (operator second-judge, D6), not via a
  mechanical label (F11). (a) target: mechanism clause; (b) shape: by-class tally, primary source = falsification
  artifacts, tracker status-history for the [VERIFIED]-position pairing only, class-label weak/separate-checker;
  (c) accept: tally cites located instances per class; post-[VERIFIED] pairs a falsification-cause with a
  [VERIFIED] status, not a bare flip; (d) failure modes: counting bare flips (false positives), or selling the
  class-label as mechanical, is malformed; (e) basis: F11, F12, F17, F19, F3, F6, F10.
- **D4** [PENDING] (clarified cycle 4 per F18; was [VERIFIED] cycle 3) **Pass-type split as router (by LANDED
  type — recoverability clarified).** Split by the falsification's **landed type**: a §3.4 mechanical
  `falsified` line (enumerable → lens-or-re-sequence) vs a §3.4.1 `[VERIFIED — surfaced]` judgment residual
  (→ framework-gap, almost never a lens). For an intent finding routed `mechanical-falsification-candidate`,
  the landed type is read from the route field **reconciled against the same cycle's §3.4 mechanical line (or
  its recorded skip)** — a cross-artifact join, not a single-field read (F18). basis: F13, F18 + located read
  modules.md:486-507 + skip carve-out modules.md:423-433.
- **D8** [PENDING] (re-amended cycle 4 per F17, F19; was [VERIFIED] cycle 3) **SG1 + the recurrence
  discriminator (cause-grounded).** A falsification firing is NOT a framework failure — usually the framework
  succeeding; the signal is the same falsification CLASS recurring within one run. The **post-[VERIFIED]
  sharpest-signal qualifier** is established by **pairing the falsification artifact (the CAUSE — a §3.4
  `falsified` line, or an intent §3.4.1 finding routed-mechanical that falsified — recording what class
  falsified, in which cycle) with the affected entry's [VERIFIED] status before the falsifying cycle**; the
  **bare tracker flip-signature is NOT the signal** (overloaded — F17). A single catch = system working.
  Mechanical criteria: recurrence count (from the tally, D3) + the falsification-cause-paired-with-[VERIFIED]
  position. basis: F12, F17, F19 + located read modules.md:413 (mechanical line iterates the [VERIFIED] set) +
  `foundations.md` amendment-is-contradiction (the flip is overloaded) + item SG1 + Unit-31 instance.

### Cycle-5 re-verification (working context locks the cycle-4 re-amendments; broken-basis check clean — D4→D5, D3→D6 consistent; D1/D2/D5/D6/D7/D9/D10/D11 unaffected)

- **D3** [VERIFIED] (cycle 5) Re-grounded resolution sound: primary source = falsification artifacts; tracker status-history for the [VERIFIED]-position pairing only (never the bare flip); SG4-reconciled; class-label weak/separate-checker — closes F17, F19. basis: as D3 cycle-4 line.
- **D4** [VERIFIED] (cycle 5) Clarified resolution sound: landed type via route field reconciled against the same-cycle mechanical line/skip — closes F18. basis: as D4 cycle-4 line.
- **D8** [VERIFIED] (cycle 5) Re-grounded resolution sound: post-[VERIFIED] = falsification-cause paired with [VERIFIED] status, never the bare flip — closes F17, F19. basis: as D8 cycle-4 line.

### Cycle-6 convergence — CLEAN → [READY]

- **D1** [AUTO-ACCEPTED] (cycle 6, [READY] in auto-battle) Home = new practice 13 in development-process.md — the [CONDITIONAL] home choice (vs post-run-review.md) was not overridden by an operator (auto-battle); recorded [AUTO-ACCEPTED] and **surfaced for operator post-run review**. The mechanical pass confirmed the technical-basis shapes hold (home-declaration + practice-12 sibling present; additive — no existing machinery). basis: cycle-6 mechanical falsification (`.cycle-6.falsification.md` D1 line) + the operator-resolvable home-choice assumption unverified (auto-accept).
- **Convergence status (cycle 6):** CLEAN. intent-falsification CLEAN (`.cycle-6.intent-falsification.md` — all 6 R# served, 2 irreducible [VERIFIED — surfaced] residuals: weak class-label, lens/framework fits-both) + mechanical falsification ALL-HOLDS (`.cycle-6.falsification.md` — 11/11 entries hold, no falsification) + **zero D-track deltas this cycle**. New-surface requirement met (cycle 6 ran new reads/searches: anti-patterns.md:142, lens-crowding item, foundations.md:390-392, the skip-cycle `ls`, the practice-count grep).
- **Fresh-session implementability: PASSED.** A session with only this tracker can implement the design — practice 13 in development-process.md + the intro-enumeration update — without a new design decision. Per-step external evidence:
  1. *Insertion point* — after practice 12, before "## The release loop": located read `development-process.md:486` (practice 12 start) + `:556` ("## The release loop"). 2. *Mechanism (D3)* — `spec/modules.md:331-343` (§3.4 mechanical line) + `:440-513` (§3.4.1 intent line) — the artifacts the receipt reads; class not a tagged field. 3. *Pass-type router (D4)* — `modules.md:486-507` (intent route ∈ {mechanical-candidate, surfaced}). 4. *Routing discriminator + SG3 (D5)* — item `framework-gap-receipt.md:31-44` + `skill-craft/references/anti-patterns.md:142` (Additive reflex). 5. *Operator-binds surface-only (D6) + dispatch (D9)* — `development-process.md:400-484` (practice 11) + `:142-150` (practice 3). 6. *Caught-side scope (D7)* — `self-review-missed-side.md:6-7,120` (owns Q1, NOT redundant). 7. *Practice-8 classification + define-in-place term (D10)* — practices 10/11/12 classification format (`development-process.md:391-398,470-484,545-554`); no glossary entry (`grep spec/glossary.md` empty). 8. *Intro-enumeration update (D11)* — `development-process.md:66-68` (names "coherence-audit cadence"). All steps cite external located reads/searches → PASSED.

### Cycle 7 (post-loopback investigate-design) — re-form D11

- **D11** [INVALIDATED]→[PENDING]→[VERIFIED] (cycle 7, per F20) **Dependent update (Missed-dependents) — completeness-corrected.** Impl adds the receipt to **both** homes of the framework-dev-machinery enumeration: `development-process.md:66-68` (done in Unit 1) **and** `README.md:116-117`. (a) target: the two enumeration sentences; (b) shape: append the receipt beside "the coherence-audit cadence" in each; (c) accept: both name the receipt; (d) failure modes: none beyond each list +1; (e) basis: F20 corrected corpus-wide search → full dependent set = exactly 2 homes. Standardized pass (cycle 7): Missed-dependents re-fired with the corrected search → clean (2 dependents, search-established); other lenses out of scope (receipt mechanism/safeguards/scope unchanged).

### Cycle 8 (convergence re-attempt, post-loopback) — CLEAN → [READY]

- **Intent-falsification CARRIES FORWARD:** the D11 extension is **behavior-preserving** (a corpus-hygiene dependent-add; D2-D10 unchanged → the design's intent-serving character unchanged). Per the re-trigger reuse rule (`phases/investigate-design.md`: a behavior-preserving fix does not re-open the intent pass) the **cycle-6 intent-clean result carries forward** — no re-dispatch. basis: cycle-6 intent CLEAN + behavior-preserving classification.
- **Mechanical falsification (D11 re-check; D1-D10 carry forward cycle-6 holds):** {D11 target-existence `expected-match:"coherence-audit cadence"` → README.md:116 + development-process.md:68 present → **holds**} {D11 target-dependents candidate `grep -rniE 'coherence-audit cadence|shared framework-dev machinery|release/marketplace loop|release loop with its discharge' README.md development-process.md instantiation-guide.md spec/ anneal-dev/ instance-template/ CLAUDE.md post-run-review.md`, predicate `any-outside-scope:{development-process.md:66-68, README.md:115-117}` → result: only those 2 homes → **holds**}. aggregate: **holds**.
- **Convergence (cycle 8): CLEAN** — intent carried forward + mechanical all-holds + zero D-track deltas. Fresh-session implementability PASSED (README edit = same shape as the dev-process intro edit). → **[READY]** (2nd). New impl plan: Unit 1 done (development-process.md, working tree); **Unit 2 = README.md:116-117 edit.**
