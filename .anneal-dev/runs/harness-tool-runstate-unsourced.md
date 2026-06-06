# Run: harness-tool-runstate-unsourced

- **Status:** PASSED
- **Phase:** verify
- **Mode:** auto-battle (operator-requested at invocation)
- **Task:** Settle `harness-tool-runstate-unsourced` — the unsourced "don't use harness TaskCreate/TaskUpdate for run-state" half of the run-state block in every rendered SKILL.md (contract-2). Add a harness-general render-time note to `instantiation-guide.md` that sources it. CORPUS-EVOLUTION edit (instantiation-guide ∉ spec/foundation/anneal-dev-spec → no kernel operator-soundness gate; discharge hook still fires).

> Work product: `anneal-framework` (the convention's home). Per-instance re-render of the 4 SKILL.md blocks from the sourced note = downstream Phase B (instance-reinstantiation). Keystone-prep: 2nd of the Phase-A conventions before the anneal-dev re-render.

---

## F-track (findings)

- **F1** [VERIFIED — addressed] The block is in ALL 4 instances' rendered SKILL.md (clippy:29, daneel:33, anneal-dev:32, bauleitplan:42), the same structure — the Phase-B dependent set. — basis: `rg "TaskCreate|TaskUpdate" <instances> -g SKILL.md` → 4 hits. addressed by D1.
- **F2** [VERIFIED — addressed] The block has two halves: SOURCED ("tracker is run-state source of truth") → `core.md §6` (run-state "persists across interruptions in an instance-bound location", core.md:964-966) + the persistence slot; UNSOURCED ("when the harness provides TaskCreate/TaskUpdate they are not used for run-state ... may be used for harness-level work outside the protocol") → no spec clause. — basis: located read clippy/plugin/skills/clippy/SKILL.md:28-34 (the block) + core.md:964-966 (the sourced half). addressed by D3.
- **F3** [VERIFIED — addressed] The framework SPEC is harness-clean — `TaskCreate`/`TaskUpdate` appear NOWHERE in `spec/`, `foundation.md`, or `instantiation-guide.md`. So placing the rule (with those tool names) in `core.md` would introduce Leakage (harness concretion in a harness-general file). — basis: `rg "TaskCreate|TaskUpdate" spec/ foundation.md instantiation-guide.md` → empty. addressed by D2.
- **F4** [VERIFIED — addressed] No existing harness / run-state / context-independence note in the instantiation-guide — the note is net-new. — basis: `rg -ni "harness|context-independence|ambient|task tool|run-state" instantiation-guide.md` → empty. addressed by D3.

## D-track (design decisions)

- **D1** [VERIFIED] SCOPE — this run edits `instantiation-guide.md` only (add the render-time note that sources the block). The per-instance re-render of the 4 SKILL.md blocks from the sourced note = downstream Phase B. CORPUS-EVOLUTION (instantiation-guide ∉ {spec/*, foundation.md, anneal-dev/spec/*} → not method-kernel → no operator-soundness gate; the commit-msg discharge hook still fires since instantiation-guide.md is rule-corpus). — basis: F1 (4-instance dependent set); development-process.md method-kernel definition (the render-source set).
- **D2** [VERIFIED] HOME = instantiation-guide (option b), NOT framework spec (option a). — basis: F3 (spec is harness-clean; naming TaskCreate/TaskUpdate in core.md = Leakage of a harness concretion into a harness-general file) + F2 (the METHOD invariant — run-state lives in the persistence mechanism — is ALREADY sourced at core.md §6; the harness-disambiguation is a render-TARGET concern, not a method invariant, so it belongs at the render/guide layer).
  - considered: framework spec §6 (option a) — rejected: introduces harness-tool Leakage into the harness-general spec (F3); the disambiguation is render-target-specific, not a method invariant (F2).
- **D3** [VERIFIED] THE NOTE — a harness-GENERAL render-time note in `instantiation-guide.md` (near the §2 run-artifact-persistence slot): when the target harness provides ambient task/run-state-tracking tools, the rendered protocol states that run-state lives in the instance's persistence mechanism (the source of truth — `core.md` §6 + the persistence slot), not those ambient tools (which may serve harness-level work outside the protocol). The note NAMES no specific tool — the concrete names (TaskCreate/TaskUpdate) are the instance-render concretion. This SOURCES the existing rendered blocks → resolves the contract-2 finding. Enforcement: the existing render-fidelity verify (the rendered block traces to this note); no new mechanism needed (the note sources legitimate content, it does not forbid a pattern). — basis: F2 (the two halves + the §6 source), F3 (harness-general → no tool names in the guide note).

---

## [READY] (cycle 2 convergence clean) — auto-battle, proceeding to implement

- **Convergence:** cycle-2 fresh convergence CLEAN (falsification `acdad54d44768d392`; D1-D3 all hold).
- **Fresh-session implementability — PASSED:** one step — add the harness-general render-time note
  to `instantiation-guide.md` §2 (near the run-artifact-persistence slot, :84-92). ext-evidence:
  located reads instantiation-guide.md:84-92 (persistence slot) + clippy SKILL.md:28-34 (the block) +
  core.md:964-966 (the §6 source). No step introduces a new design decision (target/placement/content
  all specified in D3). 
- **Commit handling (applying prior-run F9/D7):** instantiation-guide.md is rule-corpus → the commit-msg
  discharge hook fires; a pre-verify checkpoint commit is impossible. So impl produces the note STAGED-only
  (no commit); the orchestrator commits ONCE post-verify with the Step-4 discharge. CORPUS-EVOLUTION →
  no operator-soundness gate (skill-craft form-review in the discharge suffices).
- Impl plan: 1 unit, single container, sequential/in-place. Proceeding to implement.

---

## verify [PASSED] (isolated) — run complete; corpus-evolution, committed + merged

Isolated verify subagent `adcfc4c26936e445f`. All three checks accounted for; battery
dispatched-and-shown; finding ledger empty. Post-verify extension: none (render-and-open-diff disabled).

- Check 1 planned-vs-actual: D1/D2/D3 HOLD; design-completeness audit clean.
- Check 2 lenses: all 8 cited-clean — Leakage critically confirmed (no harness-tool name in the note).
- Check 3 battery: (a) fidelity — the note faithfully sources the block's two halves (SKILL.md:28-34 ↔ note ↔ core.md:962-967); the **not** negation preserved; (b) coherence — nests under §2 persistence bullet, core.md §6 resolves; (c) skill-craft form review — clean (Edit-as-Pareto: retires the Edit-without-spec-origin anti-pattern on 4 rendered blocks).

### Step-4 discharge artifact (corpus-evolution; no operator-soundness gate)
- Render fidelity: [N/A: git diff --name-only = 1 file (instantiation-guide.md), zero plugin/skills/ render files]
- Practice-4 dependent audit: [verify adcfc4c26936e445f, clean — additive, no rule changed/removed; the 4 rendered SKILL.md blocks are downstream Phase-B re-render targets, enumerated F1]
- Skill-craft full review on changed skill files: [N/A: zero skill files in change-set]
- Skill-craft self-review on framework-spec section: [verify adcfc4c26936e445f invoked skill-craft, clean — form review on the instantiation-guide.md render-time note]
- Skill-craft self-review on commits to skill-craft canonical files: [N/A: zero skill-craft canonical files in change-set]
- Practice-6 whole-document coherence: [verify adcfc4c26936e445f, clean]
- Cross-spec multi-file coherence: [verify adcfc4c26936e445f, clean — note coheres with §2; core.md §6 cross-ref resolves]
- Spec-origin trace: [N/A: zero instance plugin-render files in change-set]

### Run outcome
- anneal-dev run: PASSED (auto-battle throughout; cycles 1-2 → verify PASSED; no loopback — the staged-only commit handling was planned upfront from prior-run F9/D7).
- Rule-text: 1 file, +9/-0; committed post-verify with discharge, merged to main.
