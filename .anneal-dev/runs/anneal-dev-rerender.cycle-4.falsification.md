# Falsification-pass artifact — cycle 4 (fresh convergence) — re-formed D1 FALSIFIED AGAIN

Dispatched fresh-context subagent `a8568c6e7efe41151` (isolated, re-derive independently).
Orchestrator computed + adjudicated by direct read.

D1 (re-formed) {target-dependents, candidate: `git show bf32f9c` §4 diff vs render, predicate: any-match for a bf32f9c/e453678 content change with render impact NOT in the change-set, result: **FALSIFYING** — bf32f9c §4.1 reconciled the cycle pass-count: OLD "A cycle has two passes, in order" + "standardized pass runs every cycle" → NEW core.md:257 "two passes BY DEFAULT" + :271-272 "the convergence cycle (§4.1.4) ADDS A THIRD PASS — falsification" (commit msg: "two-vs-three-passes contradiction reconciled"). Render investigate-design.md:9-10 carries the OLD absolute "Each cycle has two passes, in order:"; `rg -i 'by default|adds a third|three.{0,8}pass' <render>` → EMPTY. ORCHESTRATOR-CONFIRMED by direct read (render :9-10 vs core.md:257/271-272), **FALSIFIED**} → **aggregate: FALSIFIED**
  - secondary (not rested on): bf32f9c added a §Purpose three-contracts paragraph absent from foundations.md Purpose — flagged instance-droppable, not asserted.

D2 {target-existence, exactly-5-firewall-leaks, result: confirmed 5 (matches the named), **holds**} → holds
D3 {target-existence + target-dependents, V-N strips, result: exactly 3 in render, zero in source, **holds**} → holds

## Orchestrator computation + the pattern
- D2, D3 hold. **re-formed D1 FALSIFIED** (3rd content divergence found: the two-vs-three-passes reconciliation).
- **PATTERN (the load-bearing observation):** the investigation-pass AUDIT (`a8dfe52f70ab7d08f`) declared the re-render "light-touch — 5 cites + 3 strips, no clause rewrites." TWO independent convergence falsifications have now each found a real §4-content divergence the audit MISSED (cycle 2: §5.3 [READY] collapse; cycle 4: the two-vs-three-passes reconciliation). The audit's completeness CONCLUSION ("no clause rewrites") was unreliable — it eyeballed the renders rather than diffing them against the §4-re-derivation commit (`bf32f9c`).
- **RE-SCOPE (re-formed D1, section-level):** the §4-derived render content (investigate-design.md's cycle/passes/[READY]/convergence/falsification; the [READY] sections of foundations.md/tracker.md; and a check of implement.md/verify.md §4.2/§4.3 content) needs a FAITHFUL re-render against the CURRENT core.md §4/§5.3 — section-level, NOT the audit's line-level "light-touch." Enumerate by DIFFING bf32f9c's §4 changes (the source delta), not by eyeballing. The render-fidelity verify (clause-by-clause vs current §4) is the completeness guarantee.
- Run PAUSED here for operator (the audit-vs-falsification retrospective the operator queued is now directly load-bearing; the scope materially changed).
