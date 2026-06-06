# Cycle 6 — convergence cycle: mechanical falsification pass

Run: `run-state-tracked-by-default` · cycle 6. Intent-falsification came up clean (no D-delta,
one surfaced residual F-prov-framing not actioned), so the mechanical pass ran. Fresh-context
subagent `af9b1c3c3afb6c3d3` (opus); orchestrator computed holds/falsified.

Per-decision artifact (candidate + predicate + result → orchestrator-computed verdict):

- **D0** {target-dependents · `rg "gitignor|check-ignore"` across the corpus · `any-outside-scope:{§5 :359-387, persistence :102-105/:55-77, bindings :282/:295-296/:187-199/:175-180, core §4.2 :763-772}`} → result: 10 matches; 8 in-scope policy sites; 2 outside-scope BUT non-policy (`instantiation-guide.md:341` extension-enable-state; `lens-set.md:113` generic lens-example). → **HOLDS** (no run-state-gitignore-policy site outside D0's scope).
- **D1** {target-existence · read the 6 cited spots · `expected-match:gitignore`} → all 6 present + state run-state gitignored. → **HOLDS**.
- **D2** {target-existence · read `instantiation-guide.md:359-367` · `expected-match:check-ignore`} → the git-observable marker (`git check-ignore`) + the blur-contract rationale present. → **HOLDS**.
- **D3** {target-dependents · `rg "must track|always track|all instances.*track|default.*track"` §5 · `any-match`} → EMPTY (no leaked universal/downstream-track mandate). → **HOLDS**.
- **D4** {target-existence · read `bindings.md:187-199` · `expected-match:Provisioning`} → Provisioning + Integration text present as cited. → **HOLDS**.
- **D7** {target-existence · read `core.md §4.2 :763-772` · `expected-match:clean`} → clean-before-dispatch + exactly-the-unit's-change + restore text present. → **HOLDS**.
- **D6** {target-dependents · read INV-1..5 · `any-match` (invariant depending on run-state gitignore)} → NONE; no invariant's home/behavior keys on run-state gitignore. → **HOLDS** (no invariant breached).
- **D5** {target-dependents · `rg "gitignore"` rendered plugin · `expected-match:gitignore`} → rendered SKILL.md:315 + foundations.md:469 carry "adds `.anneal-dev/` to `.gitignore`" (the render-debt dependent). → **HOLDS** (render-follow obligation confirmed).

## Convergence verdict
**Intent-falsification clean** (no D-delta; F-prov-framing [VERIFIED — surfaced], not actioned per the brake) + **mechanical falsification clean** (all 8 [VERIFIED] D-entries hold). **ZERO D-track delta → convergence cycle observed clean → [READY].**

New surfaces this convergence cycle: `core.md §4.2` in-place integrity, the separate-copy Integration step, the rendered plugin cache, the 5 INV files, the scope re-search — none re-attestations of prior cycles.

## Surfaced residuals for the operator's soundness pass (all [VERIFIED — surfaced], terminal)
- **D3 (the soundness crux):** per-instance default-on for anneal-dev; framework does NOT mandate downstream tracking. (cycle-2/4 F-D3.)
- **F-prov-framing:** 4 framework sites carry "non-tracked run-inputs" — now mildly misleading (run-state IS tracked) but the rule stays TRUE (run-state isn't *work-product*); a Pareto-consistency terminology cleanup, not a requirement-failure.
- **F-b/F-c/F-d/F-e** (cycle 4): resume-precedence (resolved by append-only latest-line), commit-cadence (operational, not mandated), extensions.md ref (stays true), D7 detection-gap (parity-preserved).
- **D7 integrity-exclusion correctness** + **D6 no-invariant-breach** — the kernel-edit focusing artifact (D6) aims the operator's soundness here.
