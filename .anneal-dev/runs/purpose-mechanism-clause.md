# Run: purpose-mechanism-clause

- **Status:** PASSED
- **Phase:** verify  *(investigate-design → implement → verify; operator selected `next phase` at
  [READY] — step-4 soundness verdict originated, 2026-06-06)*
- **Mode:** auto-cycle (gated-kernel) — cycles self-advance; the [READY] operator-soundness
  verdict remains the irreducible gate (method-kernel edit; anneal-dev never self-certifies its
  own foundation, per `development-process.md` step-4 + project `CLAUDE.md`)
- **Task summary:** **WS1 (method-kernel) only:** add a tight "Mechanism: structural, not
  willed" bridge clause to `spec/core.md` Purpose, connecting the two goals to §3.1's
  structural-enforcement mechanism (cite §3.1, do not restate). **WS2 de-scoped** (operator
  decision 2026-06-06): the anneal-dev run-state render-sync reverts to the queued
  `instance-reinstantiation` render-debt (already fully captured there); not done in this run.

## Requirements record

**Verbatim operator request (across turns):** "I also lean (a) but let's try to defend or
refute it for a moment first" → settled home (a) = append clause to core.md Purpose; "let's do
it now"; "Note a known divergence - please fold [in] that single seeming fix in this run as well"
(the stale run-state render).

- **R1** — `core.md` Purpose makes legible that its two goals are *secured by* the
  structural-enforcement mechanism (today inferable only from §3.1, deep in the grounding section).
- **R2** — the mechanism statement is accurate to the canon: does NOT overclaim "all rigor
  structural" against the deliberately-irreducible operator gate (operator = willed exception, not
  a gap to close).
- **R3** — the rationale is grounded (observed mode: a rule depending on the AI choosing rigor
  leaks — loads but does not fire), NOT the categorical "the AI is a satisficing reasoner."
- **R4** — the addition cites §3.1 and does not restate it (Pareto: closes the goals↔mechanism
  inferential gap; no Fragmentation, no Bloat).
- **R5** — the asymptote / V1-definability framing is EXCLUDED from core.md (dev-trajectory, not
  run-spec).
- **R6** — the anneal-dev plugin's run-state statements are corrected to match the live
  tracked-by-default source, COMPLETELY across all dependents (no partial / half-corrected render).

Proposed solution (home (a); the draft clause; the WS2 6-spot sync) is a strong input —
investigated, not assumed.

## F-track (findings)

- **F1 [VERIFIED — non-issue]** core.md Purpose states two goals + human-inspectability constraint
  + the three-contracts reference, but NOT the securing mechanism. Basis: located read
  `spec/core.md:10-28` — observable fact: no sentence in Purpose names how the goals are secured.
- **F2 [VERIFIED — non-issue]** §3.1 already carries the mechanism, the operator terminus, and the
  loaded-but-inert mitigation → WS1 is a bridge+pointer, not a new rule. Basis: located read
  `spec/core.md:111-169` — observable fact: §3.1 contains "a non-adherent AI cannot produce it by
  pattern alone" (mechanism), "the operator's irreducible verdict" (terminus), and "a rule whose
  adherence cannot be read off an artifact is not enforced" (loaded-but-inert).
- **F3 [VERIFIED — non-issue]** WS1 render-dependents + cross-refs enumerated; none breaks on
  adding a *mechanism* clause (it is the means, not a third goal). Basis: search
  `grep -rln "Grounded claims"` → {`anneal-dev/.../foundations.md`, `README.md`, `spec/core.md`};
  cross-refs `spec/README.md:107,148,152`, `instantiation-guide.md:77` ("the two **values**" =
  goals).
- **F4 [VERIFIED — non-issue]** WS2 stale-render dependents = 6 spots / 4 files. Basis: search
  `grep -rn "gitignore" anneal-dev/plugin/` → `foundations.md:462,469`; `tracker.md:402`;
  `SKILL.md:315,347`; `implement.md:160`. Observable: `implement.md:160` carries a provisioning
  rationale ("gitignored, so absent from a copy"), not a bare bootstrap-gitignore line.
- **F5 [VERIFIED — non-issue]** WS2 live source already tracked-by-default → render-lag only.
  Basis: located read `anneal-dev/spec/persistence.md:97-118` (observable: "both tracked",
  "not gitignored", "no longer gitignores") + `bindings.md:313-314`.

## D-track (design decisions)

- **D1 [PENDING]** WS1 — add a Mechanism bridge clause to `spec/core.md` Purpose, placed between
  the two numbered goals and the "Human inspectability" paragraph.
  - (a) target: `spec/core.md` Purpose section (amendment — additive clause).
  - (b) contract surface: a Purpose-altitude orientation clause carrying exactly four claims —
    {stance: the goals are secured by structural enforcement, not the AI's discipline; rationale
    (grounded, R3): a rule depending on the AI *choosing* rigor leaks — loads but does not fire;
    mechanism-pointer: each load-bearing step is bound to an evidence-bearing artifact a separate
    non-producing context re-derives, **cite §3.1**, do not restate; operator-exception (R2): the
    operator's verdict is the one irreducible, deliberately-willed gate — not a gap to close — since
    the AI cannot certify its own foundation, **cite §3.1**}. EXCLUDES the asymptote/V1 framing (R5).
  - (c) acceptance: a reader of Purpose learns the means + the operator exception with a §3.1
    pointer; no new enforceable rule introduced (orientation, like the existing contracts line); the
    clause is tight (≈3-4 sentences) and every sentence carries one of the four claims.
  - (d) side-effects/failure modes: render-debt to all instances (the Purpose render) — see D2;
    failure mode to avoid = restating §3.1 (Fragmentation) or ballooning into §3.1's
    weak/strong/gradient mechanics (Bloat).
  - (e) basis: F1 + F2. Realization output (exact sentences) produced at impl (skill-craft invoked).
  - considered: home (b) dedicated VISION.md (rejected: the only genuinely-philosophical part — the
    asymptote — is excluded anyway, so VISION would duplicate README's newcomer-why; the mechanism is
    operative rationale → Purpose). Basis: prior-turn defend/refute, F2.
- **D2 [PENDING]** WS1 ships SPEC-ONLY; the Purpose-mechanism render to instances is queued to the
  `instance-reinstantiation` render-debt batch, NOT rendered in this run — INCLUDING anneal-dev's
  own `foundations.md` Purpose (kept separate from WS2's run-state sync to avoid a partial
  cross-contract render). Basis: render-cadence policy (`dev-notes/README.md` — framework runs ship
  spec-only; renders batch) + F3.
- **D3 [PENDING]** WS2 — correct ALL 6 stale run-state render spots (F4) to match live source (F5):
  tracked, not gitignored.
  - (a) target: the 6 spots in `anneal-dev/plugin/skills/anneal-dev/{foundations.md, tracker.md,
    SKILL.md, phases/implement.md}` (amendment).
  - (b) shape: each statement re-rendered from its live source — `foundations.md`/`SKILL.md`
    bootstrap + Operator-editable-artifacts text → run-state TRACKED (no gitignore-on-first-write);
    `tracker.md:402` Persistence text → tracked; `implement.md:160` → the provisioning model
    (run-state is tracked but a separate copy predates the live run-state, so it is *provisioned*
    into the copy — `bindings.md:199-215`), NOT a bare gitignore→tracked swap.
  - (c) acceptance: no remaining anneal-dev-plugin statement says `.anneal-dev/` is gitignored / "add
    to .gitignore"; the render faithfully reflects `persistence.md`/`bindings.md`/`core.md §4.2.4`.
  - (d) side-effects/failure modes: this is a RENDER edit (verify = render-fidelity, not method-kernel
    soundness); failure mode = a partial fix leaving the render self-contradictory (Missed-dependents).
  - (e) basis: F4 + F5.
- **D4 [CONDITIONAL]** WS2 is done in THIS run (operator directive), pulling anneal-dev's run-state
  render-slice out of the batched `instance-reinstantiation` render-debt; mark that slice done there.
  Assumption (operator-resolvable): the operator wants the COMPLETE 6-spot fix (incl. `implement.md`'s
  provisioning correction), not just the simple bootstrap lines. Default if unoverridden: do all 6.
  Basis: operator directive + render-debt queue (`instance-reinstantiation`) — assumption named.

### Ledger updates — cycle 1 (post operator override, 2026-06-06)

- **D4 [VERIFIED]** WS2 (anneal-dev run-state render-sync) is EXCLUDED from this run's scope per
  operator override. Reverts to the queued render-debt. Basis: operator override ("since it's
  bigger, maybe not fold in ws2 … I will follow your recommendation") + located read
  `dev-notes/backlog/instance-reinstantiation.md:140-153` (render-debt complete — all 6 spots +
  the `implement.md:160` provisioning nuance enumerated there independently).
- **D3 [VERIFIED]** WS2 fix deferred to the `instance-reinstantiation` render-debt batch — not
  executed in this run (a committed defer, not an absence). Basis: D4. (F4/F5 remain as the
  investigation that confirmed the render-debt is complete + added the downstream-bite priority note.)

**Run now single-purpose (WS1).** Live design = D1 (the Purpose clause) + D2 (spec-only; render
batched). Verify discipline = method-kernel (skill-craft self-review on form + operator soundness).

- **D1 [VERIFIED]** Mechanism bridge clause in `spec/core.md` Purpose — contract surface locked
  (4 claims, placement, cite §3.1, exclude asymptote, ≈3-4 sentences). Detailed enough that a fresh
  session implements it without a new design decision (exact wording is impl-time realization).
  Basis: F1 (located read core.md:10-28, Purpose names no mechanism) + F2 (located read
  core.md:111-169, §3.1 carries mechanism + operator terminus + loaded-but-inert).
- **D2 [VERIFIED]** WS1 ships spec-only; Purpose-mechanism render queued to `instance-reinstantiation`
  render-debt (not rendered this run). Basis: render-cadence policy (`dev-notes/README.md`) + F3.

Cycle-1 standardized pass: clean, no load-bearing finding
(`.anneal-dev/runs/purpose-mechanism-clause.cycle-1.standardized-pass.md`).

### Cycle 2 — convergence cycle

- **F6 [VERIFIED — non-issue]** Convergence new-surface investigation. (a) `README.md` "What it
  holds" (`:28-38`) stays accurate — lists the two invariants; the mechanism is the *means*, not a
  third, so no inconsistency created (render-dependent, batched). (b) Foundation-invariant register:
  D1 modifies NO registered invariant (INV-1..5 rule-text untouched — D1 is an additive Purpose
  orientation clause, touches no `dev-notes/foundation-invariants/INV-*.md`). Basis: located reads
  `README.md:28-38` + `dev-notes/foundation-invariants/README.md` (membership rule) + the INV-*
  index.
- **Foundation-invariant focusing artifact (per-touched-invariant ledger):** *no registered
  invariant touched/modified.* D1 articulates the stance several invariants rest on — INV-1
  (basis), INV-3 (verify-isolation = a separate non-producing context re-derives), INV-5
  (exclusion-via-named-falsifier). **Soundness focus for the operator (aims, does not replace):**
  does the clause state "structural-not-willed" *without overclaiming against the operator's
  irreducible willed gate* (R2)? — the one place D1 could go wrong against the foundation.
- **Cycle-2 standardized pass:** no rule-text added/amended this cycle (the design rule-text was
  locked in cycle 1) → no lens in scope; the set was accounted for at cycle 1's pass. Persisted:
  `.anneal-dev/runs/purpose-mechanism-clause.cycle-2.standardized-pass.md`.

**Cycle-2 intent-falsification outcome** (artifact: `…cycle-2.intent-falsification.md`; mechanical
skipped this cycle — intent-delta, `…cycle-2.falsification.md`):

- **F7 [VERIFIED — addressed]** Draft over-attributes "the AI cannot certify its own foundation" to
  §3.1; §3.1 does not carry that reason (it's a `CLAUDE.md`/foundation-register idea) — §3.1's ground
  is the "genuinely-irreducible judgment." Route: mechanical-falsification-candidate, target-existence,
  `expected-match:certif` over §3.1 → FALSIFIED. Basis: search `grep -niE "certif|own foundation"
  spec/core.md` → no match in 111-169. Addressed by D1 amendment (below).
- **F8 [VERIFIED — addressed]** Draft "genuinely-human judgment" vs canon "genuinely-irreducible
  judgment" (`core.md:157`). Route: mechanical-falsification-candidate, target-existence → FALSIFIED.
  Basis: search `grep -rniE "genuinely-(human|irreducible)"` → only "genuinely-irreducible" @157.
  Addressed by D1 amendment (D1's surface already specified "irreducible"; the draft drifted).
- **F9 [VERIFIED — surfaced]** "secured by" (clause) echoes the Purpose opener "exists to secure"
  (`core.md:12`) — tightness nick. Terminal, non-blocking; impl-wording call (operator's
  never-required review). Basis: located read `core.md:12` vs the draft's sentence 1.

- **D1 [INVALIDATED]→[PENDING]** amended per F7 (amendment of recorded resolution = contradiction →
  reopen). The operator-exception claim mis-bundled a `CLAUDE.md` reason with a §3.1 cite.

### Cycle 3 — convergence re-run (amended design)

- **D1 [VERIFIED]** (amended). Contract surface unchanged EXCEPT the operator-exception claim: now
  "the operator's verdict at the **genuinely-irreducible judgment** (§3.1) is the one
  deliberately-willed terminus — not a gap to close." DROP the "AI cannot certify its own
  foundation" phrase as a §3.1-attributed claim (§3.1's ground is irreducibility; the
  self-certification framing is foundation-register/`CLAUDE.md`, not run-spec §3.1). Realization uses
  "genuinely-irreducible" (F8). Both §3.1 cites now accurate: separate-checker re-derivation
  (`core.md:139-142`) + genuinely-irreducible judgment (`core.md:156-157`). Basis: F2 + F7 + F8.
  - Amended candidate realization: "**The mechanism: structural, not willed.** These goals are
    secured by shifting rigor from the AI's discipline to **structural enforcement** — because a rule
    that depends on the AI *choosing* rigor leaks: it loads but does not fire. Each load-bearing step
    is bound to an evidence-bearing artifact that a separate, non-producing context re-derives (§3.1),
    so adherence is read off the artifact rather than trusted. The one irreducible exception is the
    **operator's verdict** at the genuinely-irreducible judgment (§3.1): a deliberately-willed
    terminus, not a gap to close." (F9 "secured by" echo left as a surfaced impl-wording call.)

- **Cycle-3 standardized pass:** clean (the D1 amendment reduces + improves cite fidelity;
  `…cycle-3.standardized-pass.md`).
- **Cycle-3 intent-falsification:** CLEAN — R1–R5 served, both §3.1 cites verified present, 3
  findings all `[VERIFIED — surfaced]` (non-blocking); no D-delta. Intent clean → mechanical runs.
  (`…cycle-3.intent-falsification.md`)
- **Cycle-3 mechanical falsification** (`…cycle-3.falsification.md`): D1 HOLDS, D3/D4 HOLDS;
  **D2 FALSIFIED** on its basis citation.
- **F10 [VERIFIED — addressed]** D2's basis cited the render-cadence policy at `dev-notes/README.md`,
  but that file is an 18-line index — the policy lives at `instance-reinstantiation.md:24-36`. The
  mechanical pass caught a citation error in the orchestrator's own tracker. Basis: cycle-3 mechanical
  subagent located read — `expected-match` over `dev-notes/README.md` → zero; policy verbatim at
  `instance-reinstantiation.md:24-36`. Route: mechanical, target-existence → FALSIFIED → addressed by
  the D2 basis correction below.
- **D2 [INVALIDATED]→[PENDING]** basis citation falsified (F10).

### Cycle 4 — convergence re-confirmation (D2 basis corrected)

- **D2 [VERIFIED]** (basis corrected). Resolution UNCHANGED (WS1 ships spec-only; Purpose render
  queued to the batch) — a basis-only correction. Basis now: render-cadence policy at
  `dev-notes/backlog/instance-reinstantiation.md:24-36` ("ships spec-only … does NOT render per-run")
  + the render-dependent enumeration (F3). The corrected citation was located + quoted by the cycle-3
  mechanical subagent (a fresh, non-producing context) — so the corrected basis is separate-context
  verified, not self-asserted.

- **Cycle-4 standardized pass:** no rule-text change (basis-only correction) → no lens in scope; new
  surface `instance-reinstantiation.md:24-36` cited (`…cycle-4.standardized-pass.md`).
- **Cycle-4 intent-falsification:** carried forward clean from cycle 3 (D2 fix behavior-preserving).
- **Cycle-4 mechanical falsification:** every [VERIFIED] entry HOLDS (D1, D2-corrected, D3/D4); zero
  falsified (`…cycle-4.falsification.md`).

### [READY] — convergence clean (cycle 4)

- **Convergence-cycle status:** cycle 4 clean — investigation pass (new surface
  `instance-reinstantiation.md:24-36`) + intent-falsification (carried-forward clean, cycle 3) +
  mechanical falsification (all hold, `…cycle-4.falsification.md`) + **zero D-track deltas**.
- **Fresh-session implementability: PASSED.** A session with only the tracker implements D1 without a
  new design decision: step 1 — locate insertion point after goal #2, before "Human inspectability"
  (`core.md:20`→`:22` boundary; observable: the blank line 21); step 2 — write the amended 4-claim
  clause, both §3.1 cites accurate (`core.md:139-154` separate-checker; `:156-157` genuinely-irreducible
  judgment).
- **Foundation-invariant focusing artifact (aims the operator's soundness pass):** no registered
  invariant modified; D1 articulates the stance INV-1/INV-3/INV-5 rest on. **Soundness focus: does the
  clause state "structural-not-willed" without overclaiming against the operator's irreducible willed
  gate (R2)?** — the cycle-3 intent pass found R2 served; the operator's verdict is irreducible.
- **Phase:** investigate-design → awaiting operator soundness verdict (gated-kernel; `next phase`
  selection originates step-4). Impl plan: `…impl-plan.md`.

### Implement — Unit 1 complete

Dispatched in-place (opus). **skill-craft invoked before the edit** (loaded `PROCEDURE.md` +
`anti-patterns.md`); **nothing flagged** (the Pareto bridge — Purpose named the goals + the
inspectability constraint but never *how* they're secured — justified; descriptive register, no new
rule). Clause inserted at `spec/core.md:22-30` (after goal 2, before the Human-inspectability
paragraph), verbatim per D1, wrapped to the section style. Self-check write-time lenses all
[VERIFIED] (Lossy-render / Missed-dependents / Undefined-shorthand / Over-claimed-verification /
change-set-vs-scope); both §3.1 cites re-verified (§3.1 = 111-171; separate-checker 139-141;
genuinely-irreducible judgment 156-157). No loopback, no actioned finding.

### Verify — [PASSED] (isolated)

Isolated subagent (opus), worked from artifacts alone. All four checks accounted for; no finding
short of [VERIFIED].

- **Check 1 planned-vs-actual:** D1 clause carries exactly its 4 claims, both §3.1 cites present,
  asymptote excluded, 3 body sentences; D2 confirmed spec-only (`git diff anneal-dev/plugin/**`
  empty — no render produced); D3/D4 confirmed (no run-state/gitignore edits). Design-completeness
  audit clean.
- **Check 2 requirements coverage:** R1–R5 each covered by D1; R6 covered by D3/D4 (committed defer);
  enumeration matches both halves of the verbatim request; no escaped requirement.
- **Check 3 standardized lenses:** all eight cited-clean against the clause.
- **Check 4 battery:** (a) render-fidelity **N/A this run** (cited: spec-only, render deferred per
  D2; confirmed no render produced); (b) coherence clean (both §3.1 cites resolve to live content;
  reads coherently among Purpose neighbors; README invariant list uncontradicted); (c) skill-craft
  form review invoked (`PROCEDURE.md` + `anti-patterns.md`) — no anti-pattern fires.

```
Verify result: [PASSED] (isolated)
Finding ledger:
  F1–F6 [VERIFIED — non-issue]   F7 [VERIFIED — addressed]   F8 [VERIFIED — addressed]
  F9 [VERIFIED — surfaced]       F10 [VERIFIED — addressed]  F11 [VERIFIED — surfaced]
```

- **F11 [VERIFIED — surfaced]** This run's insertion (clause at lines 22-30) shifted §3.1 down ~+9
  lines, so the tracker's earlier §3.1 line-cites (`:139-142` / `:156-157`) now resolve at
  `~:149-156` / `~:166-167` live. Both still resolve to the §3.1 content cited — tracker bookkeeping
  staleness, NOT a clause defect. (The spec cites §3.1 by section, not line, so no spec dependent
  breaks — the cite-by-section convention working as intended.)

**Run complete — verify [PASSED].** Deliverable: `spec/core.md:22-30` (the Mechanism clause).
Deferred (tracked elsewhere): D2 Purpose render → `instance-reinstantiation` batch; D3/D4 WS2
run-state render-sync → same batch. Commit gate is the operator's (downstream of [PASSED]); the
working tree carries unrelated edits (eval/, backlog notes) — scope the commit to `spec/core.md` +
`.anneal-dev/runs/` artifacts.
