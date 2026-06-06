# Cycle 4 — falsification pass (convergence cycle)

Dispatched fresh-context subagent `a3ce2e1c8a1d14f59`. Candidate+predicate declared by the subagent;
**holds-or-falsified computed by the orchestrator** (predicate applied to result). One line per
[VERIFIED] D-entry at convergence-cycle start (D1, D2, D3, D4, D6). D5/D8 are [CONDITIONAL] — not
falsified textually (discharged by verify per foundations.md).

- **{D1, [{target-existence, `grep -n '^### 4.1|^### 4.3' core.md`, expected-match:§4.1/§4.3 headings, result: `252:### 4.1 investigate-design` + `684:### 4.3 verify` present → HOLDS}, {target-dependents, `grep -rln '<requirements/coverage tokens>'` corpus-wide, any-outside-scope:{core,glossary,modules,*/investigate-design.md,*/verify.md,*/foundations.md}, result: ZERO outside-scope matches → HOLDS}], aggregate: HOLDS}** (basis strengthened via D1 sub-annotation: the multi-repo searches are the accurate basis.)
- **{D2, [{target-behavior, read core.md:693-697, expected-match:"need nothing from the run's conversation", result: present verbatim → HOLDS}, {target-existence, read core.md:708-720, expected-match:"design-completeness audit", result: present verbatim → HOLDS}], aggregate: HOLDS}**
- **{D3, [{target-existence, read core.md:763 §5, expected-match:"There are two tracks" (no "three tracks"), result: `:763` present, §5 subsections exactly 5.1/5.2/5.3 (no third track) → HOLDS}, {target-existence, read modules.md:197-202, expected-match:"one-line task summary" + "mutable run-state", result: present verbatim → HOLDS}, {target-existence, read core.md:80, expected-match:"request sets the task", result: present verbatim → HOLDS}], aggregate: HOLDS}**
- **{D4, [{target-existence, read core.md:708-720, expected-match:"a material element surfaces as a finding classifying", result: present verbatim (material-element→classify, closed 5-member enum) → HOLDS}], aggregate: HOLDS}**
- **{D6, [{target-existence, read development-process.md:357-362, expected-match:"New terminology needs a glossary entry", result: present verbatim → HOLDS}], aggregate: HOLDS}**

**Coverage check (orchestrator):** 5 lines for 5 [VERIFIED] entries; each candidate carries a shape from the closed set, a predicate from the closed set (shape-coherent), a result, a per-candidate holds; aggregates = conjunction. All HOLD. No entry falsified. **Zero D-track deltas** (only a basis-only sub-annotation on D1 — not an amendment). Convergence cycle CLEAN → [READY].
