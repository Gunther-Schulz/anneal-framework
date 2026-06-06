# intent-falsification-convergence-pass

- **Status:** PASSED
- **Phase:** verify
- **Mode:** auto-battle (operator authorized auto-cycle-to-READY; interactive at [READY])
- **Task:** Integrate intent-falsification (judgment-class design-vs-intent soundness check)
  into core anneal's convergence cycle, as the STANDING form of the discovery validated ad-hoc
  in the foundation-invariants-register run. Method-kernel edit to core anneal. Decide-ahead
  COMPLETE (forks A-D operator-ratified; B confirmed "exactly correct").

## Requirements record (R1..Rn — fork D's independent criteria source; per core.md §4.1)
Operator's verbatim ask: "integrate intent-falsification into core anneal's verify/convergence"
+ "B rec is exactly the correct way" + "auto-advance to READY" + recursive-dogfooding directive.
- R1 — intent-falsification becomes a STANDING core-anneal mechanism (not ad-hoc) — the
  judgment-class soundness check the mechanical falsification structurally can't perform.
- R2 — it MUST hold both kernel constraints: (i) judgment stays OUT of the falsification-style
  verdict (no subagent judgment determines a [VERIFIED]/[INVALIDATED] terminal); (ii) NO
  operator-detection-dependence (foundations.md Operator-expected-action-bound).
- R3 (fork A) — placement: a pass in the CONVERGENCE CYCLE (beside the mechanical falsification
  pass), catching design-soundness flaws pre-implement.
- R4 (fork B) — fresh-context; findings SPLIT mechanically-confirmable (→ runnable check →
  orchestrator computes → hard finding → loopback) vs pure-judgment (→ [CONDITIONAL] →
  [AUTO-ACCEPTED], surfaced for OPTIONAL override); dismissals evidence-bearing + surfaced;
  the split-tag itself evidence-bearing (mechanically-confirmable IFF a runnable check named).
- R5 (fork C) — iterate-until-clean, bounded (via the convergence cycle's existing
  loop-until-zero-delta), not a single fire.
- R6 (fork D) — criteria-independence: success criteria derived from R1..Rn (the requirements
  record) BEFORE reading the design (the SGV lever); reuse the requirements-record machinery.
- R7 — spec-only (renders into clippy/daneel/bauleitplan deferred to the batch per cadence);
  recursive-dogfooding: this run applies ad-hoc intent-falsification to its OWN design at verify.

## F-track
- F1 [VERIFIED — non-issue] Scope: the convergence/falsification contract is encoded at
  spec/core.md §4.1.4 + spec/modules.md §3.4/§3.3 + spec/glossary.md + anneal-dev/spec/persistence.md;
  RENDERED into coding-clippy/daneel/bauleitplan plugin skills (deferred to batch, R7) — basis:
  `grep -rliE 'convergence cycle|falsification pass'` over spec/foundation/anneal-dev-spec/instances.

## D-track (locked from the decide-ahead forks; scope search-established)
- D1 [VERIFIED] SCOPE / edit sites (spec-only): core.md §4.1.4 (add the pass), modules.md §3.4
  (add the intent-falsification artifact sibling), glossary.md (new terms, D6), anneal-dev/spec/
  persistence.md (artifact persistence binding). Renders to instances DEFERRED (R7; queued in
  instance-reinstantiation). foundation.md §3.1 isolation + §5.2 [CONDITIONAL]/[AUTO-ACCEPTED]
  REUSED (not changed). basis: F1.
- D2 [VERIFIED] THE PASS (core.md §4.1.4) — the convergence cycle gains an **intent-falsification
  pass** beside the mechanical falsification pass: a fresh-context, criteria-first, adversarial
  attack on whether the locked design SERVES its intent. Input: the locked [VERIFIED] design +
  the requirements record (R1..Rn). Holistic (design-vs-intent), NOT per-D-entry-basis (that is
  the mechanical falsification's job). Re-runs each convergence cycle (R5). basis: R3 + core.md
  §4.1.4 (the convergence-cycle pass structure it parallels).
- D3 [VERIFIED] SPLIT + DISPOSITION (fork B; the kernel-constraint holder) — the pass's findings
  split: (a) mechanically-confirmable — the subagent names a runnable check (search/read whose
  result decides the flaw); the orchestrator runs it; a confirmed flaw → hard finding → loopback
  (mirrors falsification's `falsified`; NO subagent judgment — orchestrator computes; preserves
  R2(i)); (b) pure-judgment — no runnable check; recorded [CONDITIONAL] (the AI's committed
  soundness concern + its assumption), surfaced [AUTO-ACCEPTED] at [READY] for OPTIONAL operator
  override (does NOT block [READY], does NOT trigger loopback; preserves R2(ii) — no
  operator-detection-dependence, the run never WAITS on the operator). The split-tag is
  evidence-bearing: mechanically-confirmable IFF a runnable check is named (a mechanical test,
  not judgment — closes the classify-as-judgment-to-dodge-loopback vector). Dismissals
  (a finding the pass raises then drops) are evidence-bearing + surfaced, never silent. basis:
  R2 + R4 + core.md §5.2 ([CONDITIONAL]/[AUTO-ACCEPTED]) + §4.1.4 (falsification's
  orchestrator-computes-no-judgment property the (a) branch mirrors).
- D4 [VERIFIED] THE ARTIFACT (modules.md §3.4 sibling) — per-finding line:
  {finding, criterion-attacked (R#/intent), refutation, split-tag: [mechanically-confirmable:
  runnable-check + result] | [pure-judgment], disposition: loopback | [CONDITIONAL]→[AUTO-ACCEPTED]}.
  Persisted alongside the falsification artifact (anneal-dev/spec/persistence.md). basis: R4 +
  modules.md §3.4 (the falsification-artifact shape it parallels).
- D5 [VERIFIED] anneal-dev BINDING — anneal-dev instantiates the pass: the fresh-context = the
  subagent spawn (mirrors the convergence-falsification dispatch); the criteria source = the
  requirements record; persistence of the intent-falsification artifact added to
  anneal-dev/spec/persistence.md. It is a PASS, not a lens (no lens-set.md change). basis: D2 +
  anneal-dev/spec/persistence.md (the falsification-artifact persistence it parallels).
- D6 [VERIFIED] TERMINOLOGY (glossary.md) — new terms: "intent-falsification pass",
  "mechanically-confirmable vs pure-judgment finding". Defined in spec/glossary.md (these ARE
  domain-general method terms — they render into instances, unlike the dev-notes register terms;
  so glossary, not a companion README). basis: practice-10 + R1 (standing core mechanism).
- D7 [VERIFIED] RENDER-CADENCE — spec-only; renders into clippy/daneel/bauleitplan deferred to
  instance-reinstantiation (R7). basis: render-cadence policy (framework runs ship spec-only).

## Convergence cycle (cycle 2) — falsification HOLDS, recursive intent-falsification → LOOPBACK

Mechanical falsification (fresh-context, subagent a2377ec952c6386da): D1-D7 all HOLD (bases sound).
- F2 [VERIFIED — non-issue] citation wobble: D1 mislabels "foundation.md §3.1/§5.2" — both are
  spec/core.md (isolation mechanism §4.2.3/§4.3; [CONDITIONAL]/[AUTO-ACCEPTED] §5.2); foundation.md
  has no such sections. → D1 basis-refinement (cite core.md).

Recursive intent-falsification on THIS design (fresh-context, subagent aa774dc49a5e99861;
operator recursive-dogfooding directive) — the new pass dogfooded on its own design. Found:
- F3 [PENDING] (blocking) PURE-JUDGMENT PATH never forces a fix + CATEGORY ERROR: D3 records a
  pure-judgment soundness CONCERN as a [CONDITIONAL] DESIGN DECISION — but §5.2 = a committed
  choice about what to build; a soundness concern is an F-track FINDING (§5.1). AND a new
  [CONDITIONAL] D-entry raised in a convergence cycle IS a D-track delta (§4.1.4 "no new design
  decisions") → contradicts D3's "does NOT trigger loopback". basis: core.md §5.1/§5.2/§4.1.4.
- F4 [PENDING] (blocking) FALSE-COMFORT recreated, worse: a STANDING kernel pass named
  "intent-falsification" (+ a glossary term rendering to instances) reads as "the kernel checks
  soundness" — the exact comfort the origin run (foundation-invariants F10/F11/F12) retreated from
  ("clean ≠ sound; operator irreducible; the check FEEDS the pass"). THIS design did not carry that
  residual INTO the spec. basis: foundation-invariants-register tracker F10-F12 + this design's silence.
- F5 [PENDING] (notable) SPLIT-TAG closes the dodge-DOWN vector (reclassify-to-skip-loopback) but
  not the dress-UP vector (a contrived "runnable check" manufacturing a false verdict); over-claims
  "not judgment". The mechanical falsification has a closed predicate set + orchestrator
  coverage-check; D4 lacks both. basis: core.md §4.1.4 L422-443 vs D4.
- F6 [PENDING] (notable) HOLISTIC pass is rubber-stamp-unbounded (flood-bounded by R#-mapping, but
  nothing forces a per-R# attack line — a "no findings" pass is valid with no work shown). basis:
  §4.1.4 coverage-check (line per D-entry per shape) vs D2/D4.
- F7 [PENDING] (notable) inherits V-28 never-captured-requirement blind spot (criteria = the
  requirements record; a never-captured requirement is invisible AND a clean pass reinforces the
  false comfort); design silent. basis: V-28 + D2/D6 criteria source.

## Loopback fixes — corrected (reframed) design

- D1 [VERIFIED] SCOPE (basis-refined per F2) — reused targets are spec/core.md §4.2.3/§4.3
  (isolation) + §5.2 ([CONDITIONAL]/[AUTO-ACCEPTED]), NOT foundation.md. Edit sites unchanged.
- D2 [VERIFIED] THE PASS (REFRAMED per F4 — surfacer, not certifier) — the intent-falsification
  pass FEEDS the operator's IRREDUCIBLE [READY] soundness judgment; it does NOT certify soundness.
  A clean pass is NOT a soundness certificate. Holistic design-vs-requirements-record attack;
  re-runs each convergence cycle. + per-R# coverage (F6): the artifact carries an attempted-attack
  line per R# (a clean pass is EVIDENCED clean, not asserted). + cites its V-28 never-captured
  inheritance (F7): the intent-model is the captured record; a never-captured requirement is
  invisible. basis: R1/R2 + F4/F6/F7 + foundation-invariants residual precedent.
- D3 [VERIFIED] SPLIT + DISPOSITION (corrected per F3/F5) — findings SPLIT: (a)
  mechanically-confirmable — subagent names a runnable check; the ORCHESTRATOR computes the verdict
  (not subagent-asserted, F5) + a coverage-check that the check decides the criterion; a confirmed
  flaw → hard finding → loopback. (b) pure-judgment — recorded on the **F-TRACK as
  [VERIFIED — deferred]** (§5.1; NOT a [CONDITIONAL] D-entry — fixes the F3 category error + the
  §4.1.4-delta contradiction), trigger-bearing, surfaced at [READY] for OPTIONAL operator override;
  does NOT block [READY], does NOT loopback. R5 asymmetry NAMED: iterate-until-clean is FORCING for
  the mechanically-confirmable class, SURFACING-ONLY for the pure-judgment class. Claim downgraded:
  the VERDICT is orchestrator-computed; the relevance-of-check-to-criterion remains surfaced
  judgment. basis: core.md §5.1 ([VERIFIED — deferred]) + §4.1.4 + F3/F5.
- D4 [VERIFIED] THE ARTIFACT (corrected per F5/F6) — per-R# attack line {R#, attempted-refutation,
  outcome} (coverage, rubber-stamp bound) + per-finding {finding, criterion(R#), refutation,
  split-tag:[mechanically-confirmable: runnable-check + ORCHESTRATOR-COMPUTED result] | [pure-judgment],
  disposition: loopback | F-track [VERIFIED — deferred]}. basis: F5/F6 + modules.md §3.4 parallel.
- D8 [VERIFIED] (NEW per F4) ANTI-FALSE-COMFORT RESIDUAL — core.md §4.1.4 (the pass's spec) + the
  glossary entry carry, in plain words: a clean intent-falsification pass is NOT a soundness
  certificate; the operator's design-vs-intent soundness judgment at [READY] is irreducible; the
  pass FEEDS it, never substitutes. (Mirrors the foundation-invariants register's residual; renders
  to instances with the term.) basis: F4 + register-residual precedent.
- D5/D6/D7 [VERIFIED] unchanged (binding; terms [+ the D8 residual in the glossary entry];
  spec-only render-cadence).

## D9 — convergence-pass ordering (operator-surfaced efficiency refinement, 2026-06-04)

- D9 [VERIFIED] CONVERGENCE-PASS ORDERING — within a convergence cycle the two falsification-style
  passes are SEQUENCED by depth, not run unconditionally-both: intent-falsification (the deep
  design-CHARACTER gate) runs FIRST; if it produces a delta → loopback, the mechanical falsification
  is SKIPPED that cycle (the design is about to change → running it would be wasted). Only when the
  intent-falsification comes up clean does the mechanical falsification (the local GROUNDING gate)
  run. Re-trigger rule (reuses the existing behavior-preserving classification, modules.md / verify
  Re-run scope): a behavior-preserving mechanical fix does NOT re-open intent-falsification (design
  character unchanged → intent-clean carries forward); a non-behavior-preserving mechanical fix
  (amendment / changed resolution) re-opens it. Rationale: the fragility is one-directional —
  mechanical results are stale after any intent rework (character change → all bases shift), but
  intent results survive a behavior-preserving mechanical fix; so running the destabilizing gate
  first minimizes wasted runs. Quality-neutral: both passes still run with full coverage (independent
  claim-classes; no simultaneous-only interaction). basis: this run is the proof case — mechanical-clean
  + intent-flawed (2 blocking, F3/F4) → the cycle-2 mechanical run is now stale after the intent-rework.
  Edit site: core.md §4.1.4 (the convergence-cycle pass sequence). [Adds to D1's edit set; same file.]

## D3 refinement (operator-surfaced 2026-06-04) — auto-accept preserved across the F3 track-move

- D3 [VERIFIED] (refined) — the F3 correction (pure-judgment → F-track [VERIFIED — deferred],
  not [CONDITIONAL] D-track) must NOT break auto-accept. The D-track [AUTO-ACCEPTED] explicitly
  handles "absence of an operator" (core.md §5.2); the F-track deferred disposition is currently
  framed as operator-PULL ("the operator chooses not to act") — which presumes an operator and,
  for a NOVEL pure-judgment finding (no pre-existing [AUTO-ACCEPTED] to cite via disposition (a)),
  has no clean auto-defer in auto-battle / no-override → would wrongly hold the run. FIX: a
  surfaced pure-judgment intent-finding AUTO-DEFERS by default when not overridden — carry
  [AUTO-ACCEPTED]'s absent-operator/no-override semantics onto the F-track disposition (extend the
  deferred disposition (b) from "operator-pull" to "operator-pull OR not-overridden-default", with
  its trigger). Result: the run NEVER waits on the operator (R2(ii) preserved) AND the finding stays
  category-correct (F-track, F3). Auto-accept unaffected. Edit site: core.md §5.1 (finding-state
  deferred disposition) — adds to D1's edit set; + the intent-falsification pass spec §4.1.4 names
  this disposition. basis: operator question + core.md §5.2 [AUTO-ACCEPTED] absent-operator clause
  vs §5.1 deferred operator-pull framing.

  - D9 basis refinement (operator-corrected 2026-06-04): the basis is the DEDUCTIVE argument,
    not the n=1 instance. Each pass's verdict is a function of the design CONTENT; an intent fix
    changes content (character fix) → invalidates the mechanical verdict; a behavior-preserving
    mechanical fix changes no content → does NOT invalidate the intent verdict. One-directional
    invalidation by construction → standard dependency ordering (run the destabilizing gate to a
    fixpoint first). Cost: intent-first runs mechanical only on intent-clean cycles (≤ always-both),
    identical coverage → Pareto-dominates always-both, a priori. This run is a CONFIRMING INSTANCE
    of the magnitude (it exhibited the predicted wasted mechanical run), NOT the basis; the
    direction + dominance are deductive, only the savings-magnitude is empirical.

## Re-convergence intent-falsification (round 2, on corrected design; subagent a35ef4007b64d5a97) → LOOPBACK
F4/F6/F7 fixes + D9 ordering SURVIVE; but 2 MORE blocking + notables (all COMPLETION gaps, not direction):
- F-A [PENDING] (blocking) The pure-judgment [VERIFIED — deferred] finding (F3 fix) has NO citable
  observable trigger → §5.1 makes defer "trigger-without-observable-class" MALFORMED. A pure-judgment
  design-soundness concern, by definition (no runnable check), has no observable event that re-fires it
  (V-28 had a real one; this doesn't). F3 imported V-28's FORM without its valid trigger → blocks [READY]
  (interactive) / malformed disposition. basis: core.md §5.1 deferred-disposition closed set.
- F-B [PENDING] (blocking) The D3 auto-accept refinement ("auto-defers on no-override") IS
  operator-detection — it branches on operator action/inaction at the finding. [AUTO-ACCEPTED] survives
  the bound only by routing through MODE (auto-battle = absence-of-operator, a priori), not per-finding
  override-detection. + auto-battle ride-through: a real pure-judgment flaw auto-defers, completes, no
  observable trigger (F-A) → never re-fires, no operator necessarily ever sees it. basis: foundations.md
  Operator-expected-action-bound + core.md §5.2 #5 (mode-keyed) vs §5.1 (operator-pull).
- F-C [PENDING] (notable→blocking-adjacent) F5 "orchestrator-computed verdict" is a relabel: the
  mechanically-confirmable branch has NO closed predicate/shape set (the mechanical falsification's real
  "no judgment" floor), so "orchestrator computes" reduces to "reads the subagent's stated outcome" →
  dress-up vector open. Fix option (the honest one): DROP the mechanically-confirmable branch — a concern
  WITH a runnable check just IS a mechanical-falsification finding (route to that pass, gaining its closed
  predicate); the rest are pure-judgment. Collapses the split. basis: modules.md §3.4 closed predicate set vs D4.
- F-D [PENDING] (notable) F6 per-R# coverage satisfiable vacuously (a subagent emits a fail-constructed
  line) → it's anti-flood/audit-trail + friction, NOT rubber-stamp prevention; downgrade honestly
  (mirror foundation-invariants F11). basis: free-form per-R# line vs §3.4 recompute.
- F-E [PENDING] (notable) D9 ordering SOUND (no flaw-through, no deadlock) but: (1) the behavior-preserving
  classification is defined for verify-terminal loopback, reused at the convergence-cycle boundary without
  a basis line; (2) a cycle that SKIPS mechanical (intent-delta) trips §3.4's "no falsification line =
  malformed" → needs a skip carve-out. basis: core.md §4.3 L778 + modules.md §3.4 L382.
- F-F SURVIVES: F4 surfacer reframe + D8 residual faithful to the foundation-invariants precedent (not a relabel).
- F-G SURVIVES-WITH-CAVEAT: F7 V-28 inheritance honest, adequate paired with D8.

CONVERGENCE direction: the fixes point at a SIMPLER, more honest design — intent-falsification is a PURE
judgment SURFACER (no mechanically-confirmable branch; runnable concerns route to the existing mechanical
pass); pure-judgment concerns → a NEW finding disposition (operator-reviews-at-completion, mode-keyed like
[AUTO-ACCEPTED], no re-fire trigger). Pending operator ratification (new finding-state = real kernel addition).

## (a) LOCKED + simplified design (operator-ratified 2026-06-04: standing pass, simplified)
Operator chose (a) standing pass; reasoning: serves other instances + auto-battle = surfaced-and-recorded
for post-run review (the [AUTO-ACCEPTED] contract, net-positive in both modes). AI agreed (moved off (b):
the instance-value + net-positive-both-modes resolves the operator-coupling concern).

- D2 [VERIFIED] THE PASS (simplified) — a PURE judgment surfacer in the convergence cycle: a fresh-context,
  criteria-first adversarial attack on whether the locked design serves R1..Rn. NO "mechanically-confirmable
  branch" (dissolves F-C). + per-R# coverage (anti-flood/audit-trail, F-D honest downgrade) + V-28 inheritance
  cited (F7) + the D8 anti-false-comfort residual at the generating site (F4/F-F). basis: R1/R3 + F-C/F-D/F4/F7.
- D3 [VERIFIED] DISPOSITION (re-corrected, fixes F-A/F-B/F-C) — the pass's findings route by whether a
  runnable check exists: (a) HAS a runnable check → it IS a mechanical-falsification finding (formatted as a
  candidate + closed predicate from the existing set; orchestrator computes; → loopback if falsified) — no
  separate branch, reuses the mechanical machinery (dissolves F-C). (b) NO runnable check (pure judgment) →
  [VERIFIED — surfaced] (NEW disposition, D10) — terminal, surfaced for operator judgment; does NOT hold the
  phase, does NOT loopback. Dodge-vector residual (claim-pure-judgment-to-skip-loopback) is judgment-adjacent
  but backstopped (a mis-classified concern is still SURFACED for review). basis: F-A/F-B/F-C + core.md §5.1/§5.2.
- D10 [VERIFIED] (NEW) [VERIFIED — surfaced] FINDING DISPOSITION — the F-track analog of [AUTO-ACCEPTED]: a
  judgment-class concern the AI raises with no mechanical resolution and no observable re-fire; its disposition
  is OPERATOR REVIEW (interactive: at [READY], operator amends→loopback or accepts; auto-battle: surfaced +
  recorded for post-run review, the AI's best-judgment surface accepted by mode, NOT by override-detection).
  Terminal (at [VERIFIED]) → does not hold the phase. Fixes F-A (no re-fire trigger needed — resolution is
  review, not an event) + F-B (mode-keyed, not override-detection). Edit sites: core.md §5.1 (finding states),
  §5.3 ([READY]-gate: [VERIFIED — surfaced] is terminal), glossary.md. basis: F-A/F-B + core.md §5.2
  [AUTO-ACCEPTED] mode-keyed precedent.
- D11 [VERIFIED] CONVERGENCE CRITERION (the "never-satisfying" closer) — [READY] requires the intent pass's
  findings DISPOSITIONED, not the pass CLEAN: mechanically-confirmable → resolved via loopback (bounded by
  zero-D-delta); pure-judgment → [VERIFIED — surfaced] (terminal). A perpetually-skeptical pass converges (its
  surfaced concerns terminate + accumulate in the record for review); only an OPEN mechanically-confirmable
  finding blocks. Cannot loop forever on pure-judgment surfacing. basis: operator "never-satisfying" question +
  core.md §4.1.1 ([READY] = no finding short of [VERIFIED]) + §4.1.4 (zero-D-delta).
- D9 [VERIFIED] (F-E completion) — + basis line: the behavior-preserving classification reuse at the
  convergence-cycle boundary is sound (same content-change semantics; the convergence boundary's "fix" is the
  D-delta). + §3.4 reconciliation: a cycle that skips mechanical (intent-delta) records "mechanical skipped:
  intent-delta this cycle" so §3.4's "no falsification line = malformed" doesn't fire (the converged cycle runs
  both). basis: F-E.
- D4/D5/D6/D7/D8 [VERIFIED] updated to the simplified design (D4 artifact: per-R# attack line + per-finding
  {finding, R#, refutation, route: mechanical-falsification-candidate | [VERIFIED — surfaced]}; D6 glossary +=
  [VERIFIED — surfaced]; D8 residual unchanged; D5 binding; D7 spec-only).

Edit-set update: + core.md §5.1/§5.3 (the new disposition) + §4.1.1 (the dispositioned-not-clean criterion).

## D10/D11 framing fix (operator-caught 2026-06-04) — the value must be operator-INDEPENDENT (core tenet)
The AI re-committed the operator-detection error: D10 framed the pure-judgment disposition's value as
"operator amends at [READY]" — EXPECTING operator intervention, which foundations.md
(Operator-expected-action-bound) forbids (operator action = free-form interjection, always-available /
never-depended-on). Recurring AI blind spot (F-B was the design version; this is the framing version).

- D10 [VERIFIED] (re-framed, operator-INDEPENDENT) — the intent-falsification's value chain holds with
  ZERO operator action: (1) the fresh-context attack GENERATES design-vs-intent concerns (operator-independent);
  (2) mechanically-confirmable → loopback → FORCED fix (operator-independent — the teeth); (3) pure-judgment →
  recorded [VERIFIED — surfaced] as an honest, evidence-bearing soundness-RESIDUAL, and the run DOES NOT claim
  soundness it lacks (the D8 anti-false-comfort residual) — VALUE = honest visibility of the irreducible
  residual, produced whether or not any operator looks; NOT "the operator fixes it". The operator's free-form
  override (amend → loopback) is ALWAYS-AVAILABLE / NEVER-EXPECTED (the [AUTO-ACCEPTED] contract), SYMMETRIC
  across modes (proceeds by default in both; interactive free-form override / auto-battle absence) — NO
  interactive-vs-auto-battle asymmetry in the mechanism (that asymmetry was the operator-detection smell).
  basis: foundations.md Operator-expected-action-bound + core.md §5.2 [AUTO-ACCEPTED] proceeds-by-default precedent.
- D11 [VERIFIED] (consistent) — convergence: pure-judgment findings TERMINATE as the honest residual
  ([VERIFIED — surfaced]) operator-independently; the forcing (loopback) is the mechanically-confirmable half,
  operator-independent. [READY] never waits on / expects the operator. basis: D10 + the tenet.

## Terminology precision (operator-surfaced 2026-06-04) — "another cycle", not "loopback", within the convergence cycle
- D3/D9/D11 rule-text wording fix: a mechanically-confirmable intent-falsification finding raised INSIDE
  the convergence cycle does NOT "loopback" (that term is reserved for cross-phase returns:
  implement→investigate-design, verify [ISSUES FOUND]→investigate-design). It routes to the mechanical
  falsification → the affected [VERIFIED] decision flips [INVALIDATED]→[PENDING] → the design holds at
  [NOT READY] → the investigate-design loop runs ANOTHER CYCLE (matching core.md §4.1.4's falsification-pass
  language "the cycle continues"). The implement-phase rule-text must use the convergence-cycle wording, not
  "loopback". (A true loopback would only arise if the pass ALSO ran at verify — the open fork-A sub-question.)
  basis: operator semantic catch + core.md §4.1.4 ("flips through [INVALIDATED]→[PENDING] and the cycle
  continues") vs SKILL.md Loopbacks (cross-phase returns only).

## Final dogfooding round (subagent ac4476bea352df6ae) → 1 BLOCKING (S1) + caveats. YES-IF-fixed.
- S1 [PENDING] (blocking) The D10 operator-INDEPENDENCE reframe OVER-corrected. It correctly killed the
  forbidden operator-DETECTION-as-enforcement (auto-defer-on-no-override). But it then claimed the residual's
  VALUE is "fully operator-independent / NOT the operator fixes it" — which collides with the method-kernel-edit
  discipline this design IS the standing form of: development-process.md "never self-certify the foundation;
  the operator ORIGINATES the soundness verdict" + foundation-invariants-register "the operator's soundness
  sign-off is the IRREDUCIBLE gate". The conflation: foundations.md Operator-expected-action-bound forbids
  expecting operator DETECTION/inspection/audit (active work beyond a/b) — it does NOT forbid the operator's
  soundness verdict delivered via the PERMITTED menu selection (a) at [READY]/step-4. RECONCILIATION (both hold,
  different layers): (1) the FORCING (mechanically-confirmable → another cycle) is operator-independent [tenet];
  (2) the pure-judgment residual is RECORDED operator-independently, AND for METHOD-KERNEL edits it FEEDS the
  operator's kernel-mandated IRREDUCIBLE soundness gate (delivered via the permitted [READY]/step-4 selection,
  action (a) — NOT forbidden detection); for INSTANCE runs it is honest-record-for-review (the [AUTO-ACCEPTED]
  contract); (3) forbidden operator-detection-as-enforcement stays dead. The asymmetry D10 wrongly DELETED
  (kernel-edit = operator-terminal-via-permitted-gate; instance = honest-record) must be RESTORED. The mechanism's
  VALUE is operator-independent; the kernel-edit SOUNDNESS CERTIFICATION it FEEDS is operator-terminal (kernel law).
  basis: development-process.md §2 + foundations.md Operator-expected-action-bound ((a) menu permitted) +
  foundation-invariants residual. (S1 is itself a judgment-class cross-file framing contradiction no mechanical
  check could catch — exactly what R1 says the pass is for; caught on its own design.)
- S2 [PENDING] (notable) the new [VERIFIED — surfaced] disposition needs LOCKSTEP edits: core.md §5.1's "three
  cases (closed enum)" + "exactly four paths" closure sentences both change; + the citable basis-form for
  `surfaced` (the fresh-context attack artifact, no mechanical citation test) must be specified or it inherits
  the [VERIFIED]-without-cited-disposition malformity. basis: core.md §5.1 closure sentences.
- S3 [PENDING] (notable) (a) the dodge-DOWN backstop is actually the FRESH-CONTEXT re-spawn next cycle
  (operator-independent), stronger than the design's stated "surfaced for review" — under-claimed; (b) DEEPER:
  does an intent-concern-with-a-runnable-check ALWAYS reduce to a §3.4 coupling-shape falsification of a [VERIFIED]
  D-entry? Some runnable intent-concerns (e.g. "edit-set includes a render path R7 forbids") don't fit the §3.4
  line shape → would fall to [VERIFIED — surfaced] structurally. D3a must specify the reduction or name what
  happens to runnable-but-not-coupling-shape concerns. basis: modules.md §3.4 coupling-shape line shape.
- S4 [VERIFIED — non-issue] non-termination CLOSED (D11 sound: surfaced findings are terminal non-D-deltas →
  loop converges). Residual-pile false-comfort bounded by D8 + concerns-in-the-[READY]-artifact — BUT survival is
  COUPLED to the S1 fix (if value is "operator-independent / nobody reads", the pile IS false-comfort).
- S5 [VERIFIED — non-issue] net-positive vs ad-hoc (forcing is operator-independent teeth; D8 prevents
  standing-mechanism false-comfort) — coupled to S1.
- S6 [VERIFIED — non-issue] no new interaction flaw; 2 named required edits (S2 lockstep, §3.4 skip carve-out)
  must not be dropped at implement.

## S1/S2/S3 fixes (operator-confirmed reconciliation 2026-06-04)
- D10 [VERIFIED] (S1 fix, operator-confirmed) — the asymmetry RESTORED, two layers: (1) the MECHANISM'S VALUE
  is operator-independent — it force-fixes the checkable problems + honestly records the judgment residual,
  neither waiting on the operator (the tenet); (2) for METHOD-KERNEL edits, the recorded residual FEEDS the
  operator's IRREDUCIBLE soundness verdict, delivered via the PERMITTED [READY]/next-phase menu selection (a
  permitted, expected operator action — NOT forbidden operator-detection); for INSTANCE runs there is no such
  required gate (honest-record-for-review). (3) Forbidden operator-DETECTION-as-enforcement (relying on the
  operator to CATCH) stays dead. The distinction: "lean on the operator to catch mistakes" = banned;
  "hand the operator a briefing for their go/no-go on foundation-deep changes" = permitted + kernel-required
  for exactly those changes. basis: operator confirmation + development-process.md §2 (operator originates the
  kernel-edit soundness verdict) + foundations.md Operator-expected-action-bound ((a) menu selection permitted).
- D3 [VERIFIED] (S3 fixes) — (a) the dodge-down backstop is the FRESH-CONTEXT re-spawn next cycle
  (operator-independent), not "surfaced for review" (operator-dependent) — framing corrected. (b) D3a SPECIFIES:
  an intent-concern routes to the mechanical pass ONLY if it reduces to a §3.4 coupling-shape falsification of a
  [VERIFIED] D-entry's basis; a runnable-but-not-coupling-shape concern (e.g. "edit-set includes a render path
  R7 forbids") does NOT force-loopback via §3.4 — it is recorded [VERIFIED — surfaced] (honest residual) like
  any judgment concern, since the forcing path's input shape is the §3.4 line, not "any runnable check". (Names
  the boundary honestly rather than overclaiming universal force.) basis: S3 + modules.md §3.4 coupling-shape shape.
- D10/D6 [VERIFIED] (S2 fix) — adding [VERIFIED — surfaced] requires LOCKSTEP edits: core.md §5.1 "three cases
  (closed enum)" → four + "exactly four paths" → five; + the citable basis-form for `surfaced` = the
  fresh-context intent-falsification attack artifact (evidence-bearing: the attack ran + classified the concern
  as having no runnable check) — so [VERIFIED — surfaced] is never a [VERIFIED]-without-cited-disposition.
  basis: S2 + core.md §5.1 closure sentences.
- S4/S5/S6 [VERIFIED — non-issue] now uncoupled from S1 (the S1 fix lands the reader: kernel-edit residuals
  reach the operator's required gate; instance residuals are honest-record). The 2 named implement edits
  (S2 lockstep closure-count, §3.4 skip carve-out) carried to implement.

## Convergence COMPLETE → [READY]
- Final mechanical falsification (fresh-context, subagent a58530f02bb57a162): D1-D11 all HOLD against live
  spec (every edit site + parallel/reuse target present; new terms genuinely new; instance renders untouched).
  - D10 basis sub-annotation (label-only, F2-class): cite the named "Dev-on-anneal" entry-condition (the
    "One channel, three entry-conditions" section), not "development-process.md §2" (doc uses named sections).
    Content verbatim-correct + load-bearing-intact; resolution unchanged.
- Intent-falsification round 4 (subagent a181e7f1491c90e3a): CLEAN, no new blocking; S1/S2/S3 fixes hold,
  source-verified; design serves intent (YES).
- Zero D-track delta (the S1/S2/S3 fixes were the last deltas; round 4 + mechanical confirmed, no new delta).
- Convergence-cycle outputs: intent-clean (round 4) + mechanical-clean (final) + zero-D-delta.
- Fresh-session implementability: PASSED — every edit site externally verified to exist (the final mechanical
  falsification's target-existence checks: core.md §4.1.1/§4.1.4/§5.1/§5.3/§4.3, modules.md §3.4, glossary.md,
  anneal-dev/spec/persistence.md); D1-D11 carry their bases.
- The convergence-confirming discipline iterate-until-clean was honored (the design's own D9/R5) — 4 intent
  rounds, last clean; mechanical re-run on the final design.
→ [READY]. Awaiting operator `next phase` = the kernel-edit operator soundness sign-off (the very gate this
design is about; recursive-dogfooding closure).

## IMPLEMENT — unit completions
- U1 [COMPLETE] core.md (D2/D3/D8/D9/D10/D11 + S2 lockstep) — §4.1.4 intent-falsification pass
  (surfacer; criteria-first; D3 routing; D9 ordering + skip-note; D10/S1 operator-independence boundary
  written explicitly; D8 residual at the generating site; D11 dispositioned-not-clean), §4.1.1
  (dispositioned-not-clean [READY] criterion), §5.1 ([VERIFIED — surfaced] 4th disposition + citable
  basis-form + LOCKSTEP closure flips 3→4 cases / 4→5 paths, verified single-application), §5.3 (terminal,
  doesn't hold phase). Subagent a35d83910ed5eba9f; skill-craft invoked; self-check 4-lens + practice-6
  coherence CLEAN; no loopback. Orchestrator verified: diffstat core.md +130/-23 only; closure flips applied
  ONCE (grep: "which of four cases":901, "exactly five paths":954, no stale "three cases"); pass/disposition/
  residual present. Persistence: working-tree (uncommitted; deferred to operator-approved release).
- U3 [COMPLETE] glossary.md (D6) — added "Intent-falsification pass", "[VERIFIED — surfaced]",
  "mechanically-confirmable / pure-judgment finding" (definition-tied-to-citation: core.md §4.1.4/§5.1/§5.3,
  modules.md §3.4); UPDATED the "Finding disposition" closed-set enum 3→4 (added surfaced) — the sole glossary
  disposition enumeration (grep-verified; Status-tag entry references the suffix, no count). Subagent
  a9b067959244eff80; skill-craft invoked; self-check 4-lens + scope CLEAN (+36/-2, glossary.md only); no loopback.
  Persistence: working-tree (uncommitted; deferred to release).
- U2 [COMPLETE] modules.md §3.4.1 (D4 + D9 skip carve-out) — added the intent-falsification-pass artifact
  (per-R# attack-line [honestly downgraded to anti-flood/audit-trail, not rubber-stamp prevention] + per-finding
  line with the two-member route closed set); + the §3.4 skip carve-out (a convergence cycle whose
  intent-falsification produced a delta records "mechanical skipped: intent-delta this cycle" → that cycle's
  absent mechanical-falsification lines are not malformed; the malformed-line rule is VERBATIM-UNCHANGED for
  non-skip cycles, re-affirmed). Subagent af7a439f596d3eb7f; skill-craft invoked; self-check 4-lens + scope CLEAN;
  no loopback. Orchestrator verified: §3.4.1 present ONCE (line 402; "intent-falsification-pass artifact" count=1),
  malformed-line rule intact (line 385), change-set = spec/{core,modules,glossary}.md + dev-notes only (no rogue
  files; persistence.md pending U4). Persistence: working-tree (uncommitted; deferred to release).
- OBSERVATION (run, n=2): the U1 + U2 implement subagents both mis-narrated their own writes as "pre-existing /
  prior pass." The STATE was correct (orchestrator independently verified single-application + faithfulness +
  scope each time). The masking-risk (trusting "already done" self-reports could hide a rogue edit) is why the
  implement Integrity check's orchestrator-owns-verification is load-bearing — confirmed here. Flag for post-run
  review (candidate: implement-subagent return-state should distinguish "I wrote X" from "X pre-existed" un-fakeably).

- U4 [COMPLETE] anneal-dev/spec/persistence.md (D5) — intent-falsification-pass artifact persistence
  binding (.anneal-dev/runs/<run-name>.cycle-<N>.intent-falsification.md), sibling to the falsification-pass
  binding, in all 3 homes (intro + path-list + gitignored-set — Missed-dependents caught: the gitignored-set
  would've gone stale). Subagent a327a2cd8d8be907e; skill-craft invoked; reported HONESTLY ("I wrote it");
  self-check 4-lens + scope CLEAN (+12/-2, persistence.md only); existing falsification binding intact (L40).
- IMPLEMENT [COMPLETE] — U1 core.md / U2 modules.md §3.4.1 / U3 glossary.md / U4 persistence.md all done +
  orchestrator-verified (single-application, faithful, scoped; change-set = the 4 files + dev-notes only).
  → verify (isolated). NOTE: this run edits kernel source → its RELEASE recursively goes through run-1's
  machinery: the commit-msg hook requires the Foundation-invariant check line (per-touched-invariant holds/
  violates vs the register's 5 invariants) + the operator soundness gate (the very gate this run formalizes).

## verify (isolated, subagent a234edeb376aaed93) → [ISSUES FOUND] → loopback (2 completion-gaps)
D1-D11 all faithfully implemented (planned-vs-actual cited-clean; closure-counts once; operator-independence
boundary + dispositioned-not-clean + skip carve-out correct; Leakage clean — no model/harness/domain leak;
render-fidelity + skill-quality N/A confirmed by `git diff --name-only`). Two findings short of [VERIFIED]:
- F8 [PENDING] (notable, Missed-dependents) core.md §4.1.4 (L480) routes the intent-falsification dispatch
  "briefed per modules.md §3.3", but §3.3's dispatch-brief schema enumerates only implement/verify/
  convergence-falsification — no intent-falsification-dispatch case (its (b) tracker-ref = tracker reduced +
  the requirements record; (c) unit-scope = the [VERIFIED] design + R1..Rn; (d) return-state = the §3.4.1
  artifact). Fix: add the intent-falsification-dispatch case to modules.md §3.3 (mirror the
  convergence-falsification case). basis: verify read of §3.3 vs the new §4.1.4 reference.
- F9 [PENDING] (minor, coherence) core.md L481 cites the artifact "modules.md §3.4"; it is specified in
  §3.4.1 (persistence.md cites §3.4.1 correctly). Fix: §3.4 → §3.4.1. basis: verify cross-ref check.
Both behavior-preserving (additive §3.3 case + cite tighten; no rule/render changed) → delta re-verify.

## F8/F9 fix (loopback) — behavior-preserving → delta re-verify
- F8 [VERIFIED — addressed] modules.md §3.3 gains the intent-falsification-dispatch case ((b) tracker-ref +
  requirements record; (c) unit-scope = locked [VERIFIED] design + R1..Rn; (d) return-state = §3.4.1 artifact)
  — present at modules.md §3.3 (L290/294/301/310); existing dispatch cases untouched. basis: subagent
  a19159e8a6de8a654 + orchestrator grep.
- F9 [VERIFIED — addressed] core.md intent-artifact cites tightened §3.4→§3.4.1 at L481 AND L926 (the §5.1
  surfaced basis-form — F9's true dependent, caught by the fix subagent's Missed-dependents lens; orchestrator
  judges it F9's dependent-set, not a new finding). The 9 mechanical §3.4 cites correctly untouched. basis:
  grep core.md §3.4.1 count=2; no remaining intent-artifact §3.4.
- Classification: BEHAVIOR-PRESERVING (additive §3.3 case + cite-number tighten; no rule/render/other-D
  changed) → delta verify (verify.md Re-run scope; recorded per the fail-closed-to-fresh discipline).

## verify round 2 (delta) → [PASSED] — verify terminal
Delta re-verify (isolated, subagent a5dc16f3cc7d33b68): F8 [VERIFIED — addressed] (modules.md §3.3
intent-falsification-dispatch case present; existing cases byte-for-byte unchanged; cross-refs resolve),
F9 [VERIFIED — addressed] (core.md intent-artifact cites §3.4.1 ×2; 8 mechanical §3.4 cites un-over-corrected;
persistence splits correctly). Behavior-preserving, no regression to D1-D11/lenses/coherence.
Verify result: [PASSED] (isolated, delta). render-and-open-diff extension DISABLED → no render (spec-only).
Next (release, steps 5-7): kernel-independent review = skill-craft (form, dispatching) + operator (soundness,
the release gate); the commit-msg hook requires the Foundation-invariant check (run-1 machinery) on this
kernel-source commit (recursive closure: run 2 ships through run 1's gate).

## Skill-craft self-review (FORM half, kernel-independent; subagent abc3c527cc81cbf33) → findings (practice 11)
Form machinery clean (artifact un-fakeable; closed route-set; closure-count amendments; new disposition
follow the existing shape). Findings (operator second-judged YES to: fix F10/F11/F12, keep F13):
- F10 [VERIFIED — addressed pending fix] (notable, Missed-dependents) glossary "Convergence cycle" +
  "Falsification pass" entries not swept to the mechanical/intent disambiguation. → fix-now (operator-approved).
- F11 [VERIFIED — addressed pending fix] (notable) modules.md §3.4 self-titles bare "falsification-pass
  artifact" while §3.4.1 says "mechanical" — sibling inconsistency. → fix-now (rename title/self-refs; §3.4
  anchor unchanged → cites unaffected). (operator-approved)
- F12 [VERIFIED — addressed pending fix] (nit) glossary "Pass" list line stale ("adds a third, the
  falsification pass"). → fix-now, fold into F10. (operator-approved)
- F13 [VERIFIED — non-issue] (observation) §4.1.4 rationale density (operator-independence boundary + D8
  residual + per-R# bound) — KEEP: the three are DISTINCT honest-limits at distinct mechanisms, load-bearing
  per the dogfooding F4 false-comfort finding; cutting loses the residual at its read-sites. (operator-approved keep)
- Fix = full contract-change sweep (practice 4): disambiguate EVERY bare "falsification pass" home across
  spec/ + anneal-dev/spec (the disambiguation is a contract change; audit the class, not the 3 named).
  Behavior-preserving (naming consistency; no rule prescription changed) → delta re-verify.

## RUN COMPLETE → PASSED
- Terminology sweep (F10/F11/F12) [VERIFIED — addressed]: full contract-change disambiguation swept
  (subagent a78cbc77961c02848 fixed persistence.md gitignored-set; glossary/modules already swept by prior
  units); orchestrator-grep confirmed: every "falsification pass" home qualified mechanical/intent, zero
  bare-ambiguous remaining. F13 [VERIFIED — non-issue] kept (operator-approved). Behavior-preserving → delta
  satisfied by the mechanical grep audit.
- Skill-craft hook investigation (operator probe): the skill-craft-pre-edit hook IS active (~/.claude/settings.json),
  its SPEC_SOURCE_PATTERNS (/spec/.+\.md$ etc.) cover all edited framework-spec + anneal-dev/spec files, it
  resolves the subagent sidechain transcript, and the implement subagents invoked skill-craft (grep-confirmed) →
  the hook fired + allowed on every rule-corpus edit. dev-notes edits correctly NOT gated. No gap.
- OBSERVATION (n=3: U1, U2, terminology-sweep): implement subagents mis-narrate own writes as "pre-existing";
  orchestrator-independent verification caught the true state each time → the Integrity-check's
  orchestrator-owns-verification is load-bearing. (post-run-review candidate, logged.)
- Verify: [PASSED] (isolated battery + delta) + skill-craft form review (findings fixed) + foundation-invariant
  check (INV-3/4/5 HOLD) + operator soundness sign-off (release gate). Status → PASSED. Release: operator-approved.
