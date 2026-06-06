# Falsification-pass artifact — cycle 2 (convergence cycle) — D1 FALSIFIED

Dispatched fresh-context subagent `a35fcd294e34c42d0` (isolated), instructed to re-derive
independently (NOT trust the prior audit, a secondary source). Orchestrator computed
holds-or-falsified and adjudicated the D1 falsifier by direct read (two subagents
contradicted on the [READY] claim).

D1 {target-dependents (firewall completeness), candidate: `rg -Un '(core|modules)\.md[^\n]{0,4}§' anneal-dev/plugin/...` + alternate-form hunt (space/`section N`/bare file-ref) + flatten, predicate: any-match for a 6th, result: EXACTLY 5 (the named); no 6th under any form, **holds**}; {target-dependents (content-divergence completeness), candidate: read current core.md §4/§5.3 + the bf32f9c cleanup delta vs the render phase/reference files; de-dup mirror sub-check, predicate: any-match for an un-enumerated content divergence beyond the 3 breadcrumbs, result: **FALSIFYING** — bf32f9c collapsed core.md §5.3 "Relationship to [READY]" from a full supporting-facts restatement to a THIN status→[READY] bridge; the render's foundations.md:391-404 STILL carries the OLD full restatement verbatim. (de-dup mirror itself: CONFIRMED faithful — tracker.md owns the closed-set, investigate-design only cites it.), **FALSIFIED**} → **aggregate: FALSIFIED**

D2 {target-existence, candidate: glossary/bindings lookup of the 5 re-point targets, predicate: expected-match:each-target-defined, result: ALL present — Coupling shape (glossary:87), Post-run review (glossary:435), Integrity check (glossary:217), Isolation slot (bindings:124), Name/Question/Scope lens-entry shape (modules:132 + glossary:40), **holds**} → **aggregate: holds**
  - soft note: SKILL.md:297's target is a shape-description-within-entry / section-heading, not a dedicated glossary headword — present (non-falsifying), flagged for awareness.

D3 {target-existence, candidate: `rg -Un 'V-[0-9]' spec/core.md`, predicate: expected-match:zero-V-N-in-source, result: exit 1 (zero); bf32f9c removed the 3 source breadcrumbs — stripping is faithful, **holds**}; {target-dependents, candidate: `rg -Un 'V-[0-9]' anneal-dev/plugin/...`, predicate: any-match for a 4th, result: EXACTLY 3 (implement.md:35, investigate-design.md:151, :256); no 4th, **holds**} → **aggregate: holds**

## Orchestrator computation + adjudication
- D2 holds, D3 holds. **D1 FALSIFIED** — flips [INVALIDATED]→[PENDING].
- The D1 falsifier was independently adjudicated by orchestrator DIRECT READ (the audit and the
  falsification contradicted): render `foundations.md:393-404` carries the full restatement ("no
  finding is [INVALIDATED], no load-bearing finding below [VERIFIED], every design decision
  [VERIFIED]/[AUTO-ACCEPTED]…"); current `core.md §5.3` (915-922) is the thin bridge ("The status
  tags gate [READY] (§4.1.1)… not a gate a separate evaluation re-derives"). Divergence confirmed.
- Orchestrator extended the check to the OTHER [READY] restatement the audit waved off:
  render `tracker.md:213-226` carries the SAME full restatement → same divergence. Both reference
  files missed the §5.3 collapse. The full [READY] list legitimately lives once, in
  `investigate-design.md` (← §4.1.1); foundations.md + tracker.md should be thin bridges.
- The firewall (5) + de-dup mirror, which the falsification independently re-confirmed, stand.
