# Cycle 2 — convergence cycle: intent-falsification pass

Run: `run-state-tracked-by-default` · cycle 2 (convergence). Fresh-context subagent
`a2640839dba9ff35c` (opus), criteria-first vs R1–R5. New surfaces: `core.md` §4.2 in-place
integrity (`:763-772`), `bindings.md :151-180` (separate-copy + HEAD marker), the 5 INV files,
independent scope re-search. Orchestrator re-ground each finding.

## Per-R# attack lines
- **R1 served** (no missed policy-bearing "run-state gitignored" site; `:341` near-miss correctly excluded).
- **R2 served** (binding sites covered).
- **R3 finding** (F-contract-marker — observable marker downgraded).
- **R4 finding** (F-integrity-interaction — the reconcile is INCOMPLETE: in-place path unaddressed).
- **R5 served** (render-follow recorded; F-render-debt-shape is a capture-shape nudge).

## Findings
- **F-integrity-interaction [VERIFIED — surfaced → ACTIONED: reopens D4 + D0]** *(the load-bearing finding)*. Tracked run-state collides with the in-place Integrity check (`core.md :763-772`): "clean before dispatch" (`git status --porcelain` empty) + "advanced by exactly the unit's intended change and no other modification" + restore (`reset --hard` + remove untracked). The run-state dir lives in the invoke repo (`persistence.md :60-61`), which in self-hosting IS a work-product container. When gitignored, the orchestrator's mid-run tracker writes (`core.md :800-802`) were invisible to these checks; tracked, they (a) fail clean-before-dispatch and (b) a restore `reset --hard`/remove-untracked would **discard the live tracker**. D4 reconciled only the separate-copy provisioning rationale; the in-place path is what tracking newly perturbs. **Fix direction → new D7:** the in-place integrity check + restore EXPLICITLY exclude the run-state dir (`.anneal-dev/runs/`) — clean-before excludes it, no-other-modification excludes it, restore preserves it — making explicit what gitignore did implicitly. basis: read `core.md :763-772` + `:800-802` + `persistence.md :60-61` + `bindings.md :175-180`.
- **F-persistence-58 [VERIFIED — surfaced → ACTIONED: reopens D0]** same root, scope angle: D0 must grow to include the in-place integrity sites (`core.md §4.2` / `bindings.md :175-180` / `persistence.md :55-77`), which it currently no-edits. basis: read `persistence.md :55-77` vs D0 no-edit list.
- **F-contract-marker [VERIFIED — surfaced]** D2's replacement marker (namespace/path + convention) is WEAKER than §5 rule 1's git-observable marker (`git check-ignore`, a strong artifact → a naming convention, a weak one). Implement MUST rewrite the `:362-364` "runtime-state paths are gitignored" sentence + the `:365-367` rationale, or §5 self-contradicts (says tracked, marker-sentence says gitignored). Operator-soundness residual: is "namespace + don't-hand-edit convention" a sufficient marker? basis: read `instantiation-guide.md :359-367` + `:371-376`.
- **F-D3-downstream-courtesy [VERIFIED — surfaced]** *(the operator-soundness crux, sharpened)*. Universal default-on imposes committed instance run-trackers on a downstream PRODUCT repo by default; the asymmetry (preserve-because-unrecoverable) is strong for a **corpus/methodology repo** (run history = valued provenance), **weak for a downstream consumer repo** (run history = the tool's operational log, not the repo's product). **D3 conflates "no new slot needed" with "default must be on"** — gitignore-as-toggle works regardless of default *direction*. → rework D3 (below). basis: read D3 + `bindings.md :154`.
- **F-leakage [VERIFIED — surfaced]** implement must keep the anneal-dev `allow-adhoc-kernel-edit` concretion OUT of domain-general §5 (state "transient local override-flags" abstractly; the flag name lives only in the anneal-dev binding). basis: D1 body + `instantiation-guide.md :350-376`.
- **F-render-debt-shape [VERIFIED — surfaced]** confirm the render-follow lands as an actual `instance-reinstantiation` render-debt row, not a tracker-only note. basis: CLAUDE.md filing-shape.
- **F-D6-invariants-confirmed [VERIFIED — surfaced]** D6 independently CONFIRMED: touches none of INV-1..5 (filesystem/gitignore policy orthogonal to the kernel-soundness invariants; INV-3 verify-isolation reads the tracker regardless of gitignore). The integrity-check interaction touches `core.md §4.2` (contamination guard), which is INV-3-*adjacent* but not INV-3 — a binding-completeness gap, not an invariant breach. basis: read INV-1..5.

## Outcome
**D-track delta** (F-integrity-interaction + F-persistence-58 reopen D0 + D4; D3 reworked). Per the skip carve-out, the **mechanical falsification pass is SKIPPED this cycle** (intent-delta). The design is **NOT [READY]** — cycle 3 reworks D0 (scope+), D4/D7 (integrity reconcile), D3 (per-instance default). **Operator confirmation sought on the result before continuing** (operator request).
