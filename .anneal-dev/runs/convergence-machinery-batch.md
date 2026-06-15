# Run: convergence-machinery-batch

- **Status:** PASSED
- **Phase:** verify
- **Mode:** auto-battle (switched by operator 2026-06-15; gated-kernel cadence — operator soundness at ship is irreducible)
- **Task summary:** Batch backlog #2 `intent-falsification-coverage-binding` +
  #3 `investigation-pass-lens-priming` as ONE convergence-machinery cycle.
  Method-kernel edits to `core.md` §4.1/§4.1.4 + `modules.md` §3.4.1 (+ `glossary.md`
  dependents). **Experiment parameters (run-conduct, not corpus requirements):**
  token-batching pilot — both items one investigate/converge/verify pass; lever (B)
  lean dispatch briefs; gated-kernel cadence (operator soundness per shipped edit;
  lever (A) / skip-convergence NOT taken). Self-hosting: live co-located `spec/*`
  governs; plugin renders are render-debt.

## Requirements record

**Verbatim request (operator):** "i have some backlog entries but doing them one by
one takes too long and takes too many tokens. i want to experiment with batching them
aggressively" → [proposal: batch #2+#3 as one convergence-machinery campaign, token
reduction primary, lever B lean briefs, gated-kernel] → "ok lets try it and you are
correct, my main concern is actually tokens, not wall-time".
(Corpus-change requirements R1–R5 derive from backlog items #2/#3, operator-set +
agreed as session-14 NEXT-UP; R6 is the run-conduct experiment, not intent-attacked.)

- **R1** (item #3) — The investigation pass must NOT be primed by the standardized
  lens set; remove the priming so the discovery leg stays pure (un-enumerable discovery).
- **R2** (item #3, soundness-critical — the kernel verify must confirm this) — Removal
  must preserve standardized-lens coverage: lens-application driven by the cycle's
  **work / edit-set scope**, not by what (now-unprimed) investigation attended to.
- **R3** (item #2 Sharpening 1) — Bind requirement-coverage **completeness** at
  convergence: every R# served by ≥1 decision; an empty row HOLDS the phase and forces
  an explicit disposition (serve / descope / reject-the-requirement). Mapping *quality*
  stays judgment; only *completeness* binds.
- **R4** (item #2 Sharpening 1, consolidation) — The R#→D# coverage matrix is ONE
  explicit artifact, read at both convergence (pre-implement bind) and verify §4.3
  (isolated re-check) — moving the catch to the cheapest (pre-implement) point.
- **R5** (item #2 Sharpening 2, weaker) — Criteria-first derives success criteria from
  the **verbatim** request (not the pre-chewed enumeration) and attacks whether the R#
  enumeration faithfully captures the verbatim — pulling verify §4.3's soft-judgment
  enumeration-faithfulness leg upstream to convergence.
- **R6** (run-conduct experiment; NOT intent-attacked) — execute as the token-batching
  pilot: both items one cycle, lever-B lean briefs, gated-kernel, no lever A.

---

## F-track (findings)

- **F1 [VERIFIED — non-issue]** The §4.1 investigation pass carries a lens-set priming
  clause to remove. basis: located read `spec/core.md:345-346` — "The standardized lens
  set is known going in and informs what the AI attends to (not how it investigates)."
- **F2 [VERIFIED — non-issue]** The lens-application trigger is INCONSISTENT across the
  corpus: `core.md:349` "this cycle's **investigation** touched" vs `glossary.md:301`
  "the cycle's **work** touched" vs `modules.md:245` "the cycle touched". basis: located
  reads `spec/core.md:349`, `spec/glossary.md:301`, `spec/modules.md:245` (three
  variants, one observable fact each). → the R2 re-anchor aligns core.md to the
  glossary's already-correct "work touched" framing = Fragmentation consolidation, not addition.
- **F3 [VERIFIED — non-issue]** Requirement-coverage is already checked in TWO places
  with no single explicit matrix artifact: informally in the §3.4.1 per-R# attack lines,
  and formally at verify §4.3. basis: located reads `spec/modules.md:450-460`
  (per-R# line `{R#, attempted-refutation, outcome}`), `spec/core.md:981-983` (verify
  coverage check). → R4's single-matrix consolidation.
- **F4 [VERIFIED — non-issue]** Criteria-first currently derives from the requirements
  record [enumeration] (`core.md:600`), and the verbatim-vs-enumeration faithfulness
  check exists only at verify §4.3 as a post-implement soft-judgment leg. basis: located
  reads `spec/core.md:600`, `spec/core.md:987-991`. → R5 pulls it upstream.
- **F5 [VERIFIED — non-issue]** An R# with no serving decision currently routes to
  `[VERIFIED — surfaced]` (dispositionable-away); there is no binding completeness gate.
  basis: located read `spec/core.md:616-630` (routing: mechanical-candidate else surfaced;
  absence-of-serving-decision has no entry to falsify → surfaced). → the gap R3 closes.
- **F6 [VERIFIED — deferred]** Missed-dependents: the priming clause + intent-falsification
  machinery are RENDERED in the plugin (`anneal-dev/plugin/skills/anneal-dev/phases/investigate-design.md:15,18,293`).
  basis: grep match (3 lines). disposition: deferred — render-debt, not this run's edit
  (self-hosting: live spec governs, render batches as hygiene). Trigger: the next
  instance-render sweep (`dev-notes/backlog/instance-reinstantiation.md`). Owed: a
  render-debt row at ship.

## D-track (design decisions)

- **D1 [VERIFIED]** Scope (foundational). Edit-set across the corpus: `core.md` §4.1
  pass-1 (D2) + pass-2:349 (D3) + §4.1.4 criteria-first:597-612 (D6) + §4.1.4 routing
  /convergence-gate:616-680 (D4) + §4.3 coverage cross-ref:981-991 (D5); `modules.md`
  §3.4.1 per-R# line:450-510 (D4/D6); `glossary.md` Intent-falsification-pass:227 (D6) +
  Requirements-coverage-check:428-432 (D5). Plugin renders = render-debt (F6), OUT of
  edit-scope. basis: corpus-wide wrap-tolerant search — queries
  `informs what|attends to|investigation touched|known going in|priming` and
  `requirements.coverage|served by|criteria.first|verbatim request|every R#` over
  `spec/ anneal-dev/ foundation.md development-process.md post-run-review.md`; hit-set =
  the targets enumerated above + the F6 plugin renders; no other dependent.
- **D2 [VERIFIED]** (R1) Remove the priming clause from §4.1 investigation pass. target:
  `core.md:345-346` (pass-1, the sentence "The standardized lens set is known going in
  and informs what the AI attends to (not how it investigates)."). shape: delete that
  sentence; the investigation pass becomes pure ad-hoc discovery (no lens-set priming).
  acceptance: §4.1 pass-1 contains no lens-set priming sentence; no other clause relies
  on the investigation being primed (F1 basis + scope search D1). side-effects: none —
  coverage is preserved by D3, not by priming. basis: located read `core.md:345-346`;
  scope search D1 (no dependent relies on priming).
- **D3 [VERIFIED]** (R2 — soundness-critical) Re-anchor the standardized-inspection-pass
  lens-application trigger from "this cycle's **investigation** touched" to "this cycle's
  **work** touched". target: `core.md:349`. shape: replace the single word
  "investigation" with "work" (aligning to `glossary.md:301`'s existing "the cycle's work
  touched"); §4.1.1:413 ("its scope was touched") and §4.1.3:458 ("touched its scope")
  are already attention-neutral → no edit (minimal change). acceptance: §4.1 pass-2 gates
  lens-application on the cycle's work/edit-set, attention-independent; the three corpus
  phrasings (core.md:349, glossary.md:301, modules.md:245) now agree. basis: located reads
  `core.md:349`, `glossary.md:301`, `modules.md:245` (F2); confirms re-anchor closes the
  Fragmentation, no further dependents.
  - considered: leave :349 as "investigation" and add a compensating coverage clause
    (rejected: would ADD text to preserve a coupling the glossary already avoids — the
    re-anchor is strictly leaner and fixes F2's inconsistency).
- **D4 [VERIFIED]** (R3) Bind coverage completeness at convergence. target: `modules.md`
  §3.4.1 per-R# attack line + `core.md` §4.1.4 convergence gate. shape: (i) extend the
  §3.4.1 per-R# line `{R#, attempted-refutation, outcome}` → `{R#, serving-decisions:[D#…],
  attempted-refutation, outcome}` (the R#→D# matrix); (ii) in §4.1.4 add a binding
  completeness condition — an R# whose `serving-decisions` set is empty is a **coverage-gap
  that holds the phase** (sibling to a `falsified` mechanical entry holding the phase),
  forcing one of three explicit dispositions recorded as a D-track decision: **serve**
  (add/amend a decision → D-track delta → another cycle), **descope** (committed decision
  "R# out of scope, because Y"), **reject-the-requirement** (committed "R# mis-enumerated").
  Mapping *quality* of a non-empty row stays the per-R# `served`/`finding` judgment
  (surfaced if pure judgment); only the empty-row *completeness* binds. acceptance: a
  convergence cycle with any empty `serving-decisions` row is [NOT READY] until each
  resolves to a disposition decision. basis: located reads `modules.md:450-460` (current
  line shape), `core.md:616-630` (current routing — F5 gap), `core.md:548-552`
  (falsified-entry-holds-phase precedent the bind mirrors).
  - considered: a third route in the closed per-finding routing set
    {mechanical-candidate, surfaced} (rejected: completeness is a matrix-level property,
    not a per-finding route; a new route muddies the closed set — the bind belongs at the
    convergence-gate level, parallel to the mechanical `falsified` hold).
- **D5 [VERIFIED]** (R4 — consolidation) Single coverage-matrix source of truth. target:
  `core.md` §4.3:981-983 + `glossary.md` Requirements-coverage-check:428-432. shape:
  verify §4.3's requirements-coverage check references the §3.4.1 matrix as the artifact
  it re-checks (isolated re-derivation), not a from-scratch re-derivation; §4.1.4 binds it
  pre-implement; §4.3 retains its check as the independent post-implement backstop;
  glossary entry adds a pointer that the matrix is bound pre-implement at §4.1.4.
  acceptance: one matrix artifact, two readers (§4.1.4 bind, §4.3 re-check); verify §4.3
  coverage check NOT removed (independence retained). basis: located reads `core.md:981-991`
  (verify coverage + the soft verbatim leg), `glossary.md:428-432` ("Specified in §4.3").
- **D6 [CONDITIONAL]** (R5 — Sharpening 2, the weaker one) Criteria-first from verbatim +
  enumeration-faithfulness attack. target: `core.md:597-612` + `glossary.md:227-230`.
  shape: change criteria-first's derivation source from "the requirements record
  [enumeration]" to "the operator's **verbatim** request"; add to the intent pass an
  attack "does the R# enumeration faithfully capture the verbatim?" (surfaces
  enumeration-capture errors at convergence — the soft-judgment leg currently at verify
  §4.3, pulled upstream); glossary Intent-falsification-pass entry updated to "verbatim
  request" criteria-source. honest bound (recorded): shrinks the capture-error residual,
  NOT the unstated-intent residual; uneven value for terse requests.
  **assumption (operator-resolvable):** Sharpening 2's modest + uneven value justifies its
  added convergence surface. **At [READY] → [AUTO-ACCEPTED] unless the operator descopes.**
  basis: located reads `core.md:600` (current enumeration source), `core.md:987-991`
  (the verify §4.3 leg pulled upstream); item #2's own "weaker of the two / uneven value" flag.

---

## Cycle-2 appends (convergence cycle; append-only ledger)

Intent-falsification pass (cycle 2) verdict INTENT-CLEAN by routing; orchestrator acts on Finding 1.
Mechanical falsification SKIPPED cycle 2: intent-delta this cycle (D3 amended → design changed).
Artifact: `.anneal-dev/runs/convergence-machinery-batch.cycle-2.intent-falsification.md`.

- **F7 [PENDING]** (cycle 2 intent pass) D3's one-word swap re-anchors :349 but does not
  self-evidence attention-independence: "work" is undefined and retained :350 "over what this
  cycle produced" can read as attention-derived in a design cycle. → drives the D3 amendment
  (working-context acts on the surfaced R2-soundness-critical finding). basis: located read
  `core.md:348-350`; glossary.md:301 + modules.md:245 carry no edit-set definition of "work".
- **F8 [VERIFIED — surfaced]** (cycle 2 intent pass) D6 [CONDITIONAL] is R5's only serving
  decision; the verbatim-derivation shift (kernel-behavior change) can reach [AUTO-ACCEPTED]
  rather than forcing operator soundness — but closed by gated-kernel run-conduct (every shipped
  kernel edit routes through operator soundness). terminal. basis: located read D6 tracker line.
- **D3 [INVALIDATED]** amended per F7 (cycle 2) — the one-word swap is necessary but not
  self-evidencing on the soundness-critical R2 leg.
- **D3 [PENDING]** (D3' — amended resolution) Re-anchor AND explicitly anchor the trigger to the
  edit-set. target: `core.md:348-350`. shape: replace ":349-350" trigger so it reads (≈) "Apply
  each standardized lens whose scope this cycle's **edit-set** (the rule-text added or amended)
  touched — independent of what the investigation attended to; incremental, over what this cycle
  produced." This makes attention-independence self-evident in the rule-text (closes F7), still
  aligned to glossary.md:301/modules.md:245. The added disambiguation clause is load-bearing (the
  R2 anchor) → passes Bloat. Awaiting cycle-3 convergence re-verify. basis: F7; located read
  `core.md:348-350`; glossary.md:301 (existing "work touched" framing).

### Cycle-3 appends (convergence re-cycle; append-only ledger)

Intent-falsification pass (cycle 3) INTENT-CLEAN, no D-delta — D3' confirmed on R2; R1/R3/R4/R5
undisturbed. Artifact: `.anneal-dev/runs/convergence-machinery-batch.cycle-3.intent-falsification.md`.
- **F7 [VERIFIED — addressed]** D3' (cycle-2 amendment) addresses F7 — the edit-set trigger
  self-evidences attention-independence; basis: cycle-3 intent pass + the 8 edit-set-phrased lens
  Scopes (lenses.md). cited D#: D3' (same observable behavior — lens-application coverage).
- **D3 [VERIFIED]** (D3' resolution) Re-anchor + explicit edit-set anchoring of the standardized-
  inspection-pass trigger at `core.md:348-350`. Confirmed by cycle-3 fresh-context intent pass
  (R2 served) + the edit-set-phrased lens Scopes. Awaiting cycle-3 mechanical falsification (technical
  basis). basis: located reads `core.md:348-350`, `glossary.md:301`, `lenses.md` (8 Scopes edit-set-phrased).

### Convergence + [READY] (end of cycle 3)

**Convergence cycle CLEAN** (cycle 3): intent-falsification INTENT-CLEAN + mechanical-all-holds +
zero new D-track delta. (A cycle 4 would have no new surface → malformed per the new-surface rule;
cycle 3 IS the converged cycle — the cycle-2 intent finding was fixed via D3', cycle-3 re-attack
confirmed clean on both legs.) Artifacts: `.cycle-3.intent-falsification.md`, `.cycle-3.falsification.md`.

**Fresh-session implementability: PASSED.** Per-implementer-step external evidence:
- D2 (remove priming) — `core.md:345-346` reads the priming sentence verbatim.
- D3' (re-anchor + edit-set) — `core.md:349` "this cycle's investigation touched"; glossary.md:301
  "work touched" = alignment target.
- D4 (matrix bind) — `modules.md:453` `{R#, attempted-refutation, outcome}`; `core.md:548-552`
  falsified-holds-phase precedent.
- D5 (consolidation) — `core.md:981-983` verify coverage; `glossary.md:428-432` "Specified in §4.3".
- D6 (verbatim criteria) — `core.md:599-600` enumeration-source; `core.md:987-991` verify soft verbatim leg.
D1–D5 [VERIFIED]; D6 [CONDITIONAL]→[AUTO-ACCEPTED] (auto-battle; surfaced for post-run review);
F8 [VERIFIED — surfaced]; F6 [VERIFIED — deferred] (render-debt). → [READY]; auto-proceed to implement.

## Implement (1 unit, in-place) + Verify

**Implement:** dispatched (opus, skill-craft-gated). D2–D6 edited into `spec/core.md`, `spec/modules.md`,
`spec/glossary.md`. Subagent 4-lens self-check CLEAN; all edits in listed scope. Integrity check PASSED
(diff = exactly the 3 spec files; HEAD unchanged, no contamination). Not committed (orchestrator owns
the single release commit at step 5; checkpoint consolidated into it — self-hosting run-state friction).

**Verify — isolated anneal-dev battery: [PASSED] (isolated).** Planned-vs-actual D2–D6 all cited-clean;
requirements-coverage R1–R5 all served; 8 lenses clean (Fragmentation: D3' resolves the F2 trigger
inconsistency; Lossy-render N/A spec-only); battery (a) render-fidelity N/A spec-only, (b) coherence
clean — adjudicated the D5/D6 asymmetry as **defensible** (matrix = shared artifact needs both-end
wiring; verbatim leg = independent re-derivation, one-way framing correct, symmetric wiring would
falsely couple §4.3 to upstream and harm INV-3 isolation), (c) skill-quality N/A no skill files.

**Verify — skill-craft self-review (method-kernel-mandated, outside-kernel form check): PASS w/ 1 NOTABLE.**
- **F9 [PENDING]** (skill-craft self-review) Amendment asymmetry: D5 wired the coverage-matrix
  bidirectionally (§4.1.4↔§4.3, "one matrix, two readers") but D6's verbatim-faithfulness leg uses
  "rather than at verify (§4.3)" (move-language) while §4.3's pre-existing faithfulness leg is untouched
  and unaware of the new upstream sibling — the cross-file restatement shape the edit cured one paragraph
  away for the matrix. basis: located reads `core.md:604-610` (new leg) + `core.md:1011-1016` (pre-existing
  §4.3 leg, untouched). **Orchestrator first-judge: fix-now (operator second-judges at ship gate).** The
  two reviews disagree (battery: defensible; skill-craft: notable) — both partly right: the "rather than"
  wording imprecisely implies a *move* (skill-craft correct), and the fix must NOT couple §4.3 to upstream
  (battery's INV-3 point correct). Reconciling fix: tighten §4.1.4 ONLY — "rather than at verify (§4.3)" →
  "earlier than verify §4.3's retained independent backstop." Behavior-preserving → delta-verify if applied.
  All-3 dispositions (other skill-craft findings): observations, keep-as-is (grounded inline).

**Foundation-invariant focusing artifact (method-kernel; aims operator soundness — NOT a verdict):**
- INV-1 (basis rule) — touched lightly (new `serving-decisions` artifact); HOLDS (basis-bearing: cites D#s).
- INV-2 (complete state) — touched (D4); HOLDS, **strengthens** (no R# silently dropped; bound upstream).
- INV-3 (verify isolation) — touched (D5 §4.3, D6 intent pass); HOLDS (re-check stays in verify's isolated
  context; intent pass stays fresh-context). **Operator confirm: D5 does not collapse verifier into actor.**
- INV-4 (loopback / not-settled) — touched (D4 empty-row-holds-phase); HOLDS, **strengthens**.
- INV-5 (exclusion keystone; completeness≠soundness) — touched (§4.1.4 region); HOLDS (mechanical falsifier
  untouched; D4 adds a completeness FLOOR, design explicitly keeps quality=judgment+operator verdict).
  **Operator confirm (keystone): the completeness bind must not be read as a soundness certificate.**

**SHIP (operator "ship" 2026-06-15):**
- **Operator soundness verdict: SOUND → ship.** The irreducible method-kernel verdict, originated by the
  operator's ship approval (the focusing artifact's INV-3/INV-5 confirm-points accepted; INV-2/INV-4 strengthen).
- **F9 [VERIFIED — addressed].** Fix applied to `core.md` §4.1.4 ONLY: "rather than at verify (§4.3)" →
  "earlier than verify §4.3's retained independent backstop" (§4.3 untouched — INV-3 independence preserved).
  Behavior-preserving (wording tightening, no rule/closed-set/must changed) → **delta-verify in-context**
  (substance already isolated-[PASSED]; in-context neighborhood coherence confirmed; §4.3 leg untouched).
- **D6 [AUTO-ACCEPTED]** (Sharpening 2; auto-battle default-take; surfaced for post-run review).
- **F6 [VERIFIED — deferred]** render-debt → next instance-render sweep.

**Verify result: [PASSED] (isolated battery) + skill-craft self-review PASS (F9 fixed) + operator soundness SOUND.**
Released to main + pushed (spec-only; no plugin version bump — renders deferred render-debt). RUN COMPLETE.

