# Mechanical falsification-pass artifact — provenance-basis-naming, convergence cycle 3

Fresh-context subagent (opus `a084481a447c038bb`). Attacked [VERIFIED] D1, D2, D3, D4.
Orchestrator-computed verdict: **D2, D3, D4 hold; D1 FALSIFIED** (scope incomplete — see below).

- **{D1, [{target-dependents, candidate: corpus-wide flattened search for §3.2.1 basis-naming
  dependents (`embedded claim`/`claims embedded`/`target-naming`/`basis-naming`), predicate:
  any-outside-scope:{core.md §3.2.1 + §4.1.1 + glossary Basis + clippy-render-debt}, result: hits
  = core.md:219-224 (edit) + :410-411 (§4.1.1 no-edit) + **anneal-dev/plugin/.../foundations.md:199-204
  (renders §3.2.1) + investigate-design.md:143-145 (renders §4.1.1)**, orchestrator-verdict:
  **FALSIFIED** — the two anneal-dev/plugin self-renders of the edited kernel text are OUTSIDE D1's
  as-written render-debt scope (which named only the clippy fire-point)}, {target-existence,
  expected-match: edit-site + no-edit dependents exist, result: core.md:219/:410 + glossary:49-59 all
  present, holds}], aggregate: FALSIFIED}**
- **{D2, [{target-existence, expected-match:"located read of the source", result: core.md:186 present,
  holds}, {target-existence(no-collision), grep `provenance|distrust|use-site` → zero hits, holds}],
  aggregate: holds}**
- **{D3, [{target-existence, expected-match: §3.2.1 bullet enumerates target-naming/cited-rules/counts,
  result: core.md:219-221 = exactly the 3 forms (4th absent → distinct), holds}, {target-dependents,
  any-outside-scope:{core.md §3.2.1}, result: "cited rules or prior" in core.md only (+ the same plugin
  render, ref'd to D1's scope fix), holds}], aggregate: holds}**
- **{D4, [{target-existence, expected-match:"embedded target-naming and count premises", result:
  core.md:410-411 = 2 forms (omits "cited rules" → curated subset, non-exhaustive pre-edit → not made
  stale), holds}], aggregate: holds}**

## Orchestrator determination on D1
The anneal-dev/plugin renders ARE render-debt (build artifacts of the spec, batched per the
render-cadence policy + CLAUDE.md self-hosting). D1's error was OMITTING them from the named
render-debt set (the prior §3.2.2 run's D1 named `anneal-dev/plugin/*` explicitly). Fix = amend D1's
render-debt scope to include the anneal-dev/plugin self-render of §3.2.1/§4.1.1. **Behavior-preserving**
(no edit changes; completes the deferred-render-debt enumeration) → intent-clean carries forward.
