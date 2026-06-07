# f0-render-conventions — cycle 5 (re-convergence) mechanical falsification-pass

Fresh-context dispatch (subagent `ac95111a7deddda9f`, opus) over [VERIFIED] D1–D5. Orchestrator-computed
verdicts (predicate applied to result). **ALL HOLD → zero falsification.**

- **{D1, [{target-existence, candidate: read README:53-59, predicate: expected-match:consolidate,
  result: README:53-59 carries the full file-per-slot + may-consolidate statement}], aggregate: holds}**
- **{D2, [{target-existence, candidate: read persistence.md + guide:102-108, predicate:
  expected-match:isolation, result: persistence.md exists; guide:102-108 states the 6 elements;
  worked examples anneal-dev:124-168 + clippy:169}, {target-dependents, candidate: read guide §2
  supply-list :80-108/:135-140, predicate: any-outside-scope:guide-§2-supply-list, result: isolation is
  one of the "four required" in §2 — inside scope, no outside evidence}], aggregate: holds}**
- **{D3, [{target-existence, candidate: read README:22-32, predicate: expected-match:"Required slots",
  result: bucket exists, lists persistence.md}, {target-dependents, candidate: `grep -rn 'spec/
  persistence.md' instance-template/`, predicate: any-outside-scope:README:25-48, result: only
  README:27 — sole file-enumeration; guide:18 is a prose claim (D5's), not a file-list}], aggregate:
  holds}**
- **{D4, [{target-existence, candidate: grep headwords + read glossary:49-54,:77-79, predicate:
  expected-match, result: Basis LISTS located-read/executable-verification; Completeness lists
  mechanical-search — the terms D4 will define}, {target-dependents, candidate: `grep -rn 'glossary.md
  (Basis|Completeness)'`, predicate: any-outside-scope:spec/glossary.md, result: 0 live external
  citations (only a prior run artifact)}], aggregate: holds}**
- **{D5, [{target-existence, candidate: read README:53-59, predicate: expected-match:consolidate,
  result: canonical statement exists}, {target-dependents, candidate: read guide :92/:108/:120 + grep
  existing cross-ref, predicate: any-match, result: the 3 surfaces cohere with README:53-59 (no
  contradiction); no existing reconciliation clause (not duplicative)}], aggregate: holds}**

## Convergence outcome
Intent-falsification CLEAN (cycle-5.intent-falsification.md, no D-delta) + mechanical ALL-HOLD →
**convergence cycle CLEAN, zero D-track deltas.** Surfaced notes (guide-4-vs-template-3 = the gap the
design fixes; term-bodies-exist-but-no-competing-headword = consistent with D4 as an add) confirm,
not falsify. New surfaces this cycle (convergence-cycle requirement): guide:80-108/135-140 (slot-set
supply-list, not cited prior), `grep 'spec/persistence.md' instance-template/`, the headword-existence
greps — all verbatim-new this run.
