# campaign3-enforcement-fidelity — cycle 3 mechanical falsification-pass artifact

**Header — cited this-cycle intent-clean verdict:** `.cycle-3.intent-falsification.md` shows NO `mechanical-falsification-candidate` finding (sole finding F11 → `[VERIFIED — surfaced]`) → intent-clean THIS cycle. Mechanical pass runs (per `core.md` §4.1.4). Dispatched: fresh-context subagent `a75d68f4fdf34a922` (opus). Orchestrator computes holds-or-falsified.

## Per-decision lines (subagent candidates+results; orchestrator-computed holds)
`{D0, [`
- `{target-dependents, candidate: rg "deferred" across whole corpus (wrap-tolerant single-token), predicate any-outside-scope:core.md §5.1, result: 11 matches — only core.md:1018-1029 enumerates sub-cases; all others cite generically (core.md:653/797 impl-routing, glossary:254/345/456/458, modules:119) or unrelated verb-sense (dev-process:735, instantiation-guide:427), holds-or-falsified: HOLDS}`
- `{target-dependents, candidate: rg "Finding disposition" (newline-flattened), predicate any-outside-scope:glossary "Finding disposition" index, result: 2 matches both glossary (342 entry indexes 4 names→§5.1; 456 generic cite); no sub-case restatement, holds-or-falsified: HOLDS}`
- `aggregate: HOLDS]}`

`{D3.1, [`
- `{target-existence, candidate: read core.md §5.1 (1009-1047), predicate expected-match:"deferred — one of: (a)…or (b)…" with no (c), result: §5.1:1018-1029 has exactly (a)/(b), (c) absent — amendment target exists as claimed, holds-or-falsified: HOLDS}`
- `{target-dependents, candidate: re-run §3.2.2 reference enumeration (rg "deferred" + "Finding disposition"), predicate any-outside-scope:{core.md §5.1; glossary index (no edit); render→⑥}, result: all non-§5.1 generic; glossary indexes 4 names (adding sub-case under deferred doesn't change the enum); no unaccounted restating dependent, holds-or-falsified: HOLDS}`
- `{target-behavior, candidate: read core.md §3.2 (187-190) + §4.3 (920-948), predicate expected-match:"Verifiers (§4.3) and convergence cycles re-open each citation", result: §3.2:187-190 carries it verbatim (pattern present); §4.3's 4 enumerated legs don't restate it = the inherited-surface residual F11 (already [VERIFIED — surfaced]); expected pattern present, holds-or-falsified: HOLDS}`
- `aggregate: HOLDS]}`

`{D1 (technical-basis shapes only; operator-resolvable residual-acceptance EXEMPT per core.md §4.1.4), [`
- `{target-existence, candidate: rg "wrap-tolerant" bindings.md + rg "wrap-tolerant|incomplete audit|dispatched audit subagents" dev-process practice 4, predicate expected-match:"wrap-tolerant" present in both, result: bindings.md:41 (wrap-tolerant search-binding row) + dev-process:163/166/167 (practice 4 audits + dispatched subagents) — both present, holds-or-falsified: HOLDS}`
- `aggregate: HOLDS]}`

`{D2 (technical-basis shapes only; V-entry-vs-build EXEMPT per core.md §4.1.4), [`
- `{target-existence, candidate: read core.md §4.1.4 (494-499 + 513-518) + ls dev-notes/validation-watch/, predicate expected-match:"subagent names a search…runs it" (independent re-derivation) + dir present, result: §4.1.4:494-499 ("the subagent names a search or read whose positive result would invalidate the entry's basis, runs it") — separate-checker re-derives from its OWN search; validation-watch/ dir EXISTS, holds-or-falsified: HOLDS}`
- `aggregate: HOLDS]}`

## Orchestrator coverage check (core.md §4.1.4)
- (i) candidate sets non-empty per entry ✓ (D0:2, D3.1:3, D1:1, D2:1).
- (ii) each candidate: shape tag ∈ closed set ✓; candidate field (query/read) ✓; predicate ∈ closed set (any-outside-scope / expected-match) ✓; result field ✓; shape-coherence ✓ (target-dependents→any-outside-scope; target-existence/target-behavior→expected-match).
- (iii) orchestrator-computed holds-or-falsified matches per candidate ✓ (all HOLD).
- (iv) aggregate = conjunction of per-candidate holds ✓ (all entries HOLD).
- (v) intent-clean re-derived from this cycle's §3.4.1 artifact (no mechanical-falsification-candidate) + the header's cited intent-clean verdict MATCHES ✓.
- Coverage: every [VERIFIED] entry (D0, D3.1) lined; [CONDITIONAL] entries (D1, D2) lined for technical-basis shapes only (operator-resolvable exempt) ✓. Shape coverage matches each basis's claimed shapes ✓.

**RESULT: COVERAGE CHECK PASS. All entries HOLD. Zero D-track delta this cycle → CONVERGED.**
