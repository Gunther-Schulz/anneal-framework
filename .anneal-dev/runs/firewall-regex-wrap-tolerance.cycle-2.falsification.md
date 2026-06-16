# firewall-regex-wrap-tolerance — cycle 2 (convergence) mechanical falsification pass

**Per-artifact header — intent-clean verdict:** cycle-2 intent-falsification CLEAN
(`.cycle-2.intent-falsification.md`), no `mechanical-falsification-candidate`. Fresh-context subagent (opus)
declared candidates+predicates; **orchestrator computed holds-or-falsified**. Subagent agent-id: af1696b81e5e0d5eb.
Result: **every D-entry HOLDS — no falsification.**

- **D1** {target-existence `expected-match` OLD regex → instantiation-guide.md:189 present verbatim → **holds**}
  {target-existence `expected-match:"wrap-tolerant"` → glossary.md:84-87 idiom present → **holds**}
  {target-behavior — re-ran F1/F4 tests: OLD `rg -c` wrap:0 normal:1 prose:0 neither:0 (misses wrap); NEW `rg -Uc`
  wrap:1 normal:2 prose:0 neither:0 (catches wrap, no prose FP); matched wrap span = `modules.md`+backtick+newline+indent+§
  → behavior matches basis claim → **holds**}. aggregate: **holds**.
- **D2** {target-dependents `any-outside-scope:instantiation-guide.md` — corpus-wide regex + paraphrase hunt
  (excluding gitignored `.anneal-dev/runs/` runtime + `dev-notes/backlog/` tracking, neither a check-home) → the
  firewall check has exactly ONE active-corpus home (instantiation-guide.md:189); no second spot specifies/runs it
  → no outside-scope home → **holds**} {target-existence `expected-match:"instance-reinstantiation.md"` →
  `dev-notes/backlog/instance-reinstantiation.md` exists (28470 bytes) → **holds**}. aggregate: **holds**.

Coverage check (orchestrator): 2 lines for 2 [VERIFIED] entries; every claimed coupling shape covered; predicates
from the closed set, shape-coherent. The subagent's scoping of `any-outside-scope` to the active corpus (excluding
gitignored runtime + backlog tracking) is correct — those are not render-verify check-homes. **No falsified
aggregate. Zero cycle-2 D-track deltas → convergence CLEAN → [READY].** New-surface requirement met (cycle 2 ran
new corpus-indent measurement, FP probes, home search, instance-reinstantiation ls, glossary read).
