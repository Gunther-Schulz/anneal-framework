# clippy-reinstantiation — cycle 7 mechanical falsification-pass artifact (CONVERGED)

**Per-artifact header — cited this-cycle intent-clean verdict:** `cycle-7.intent-falsification.md` = CLEAN. Pass runs.

Fresh-context subagent (opus) declared candidate+predicate+result; orchestrator-computed holds-or-falsified. Coverage: all 14 [VERIFIED] entries + D2/D15 [CONDITIONAL] technical shapes.

## Changed entries (deep-focus)
- **D1''** — `{target-dependents, candidate: re-run full whole-repo sweep rg 'validation-watch\.md|target-shape|target-uses|(core|modules)\.md[^\n]{0,4}§|V-[0-9]+' coding-clippy/, predicate any-outside-scope:<11 targets + exempt archived/docs/dev-notes>, result: every live-corpus hit maps to one of the 11 targets; 5 hits in docs/archived/ (exempt, not rendered/active-spec); zero escapee, holds}` → **holds**
- **D17** — `{target-existence, ls dev-notes/validation-watch/ (exists, 32 entries+README+archive) vs dev-notes/validation-watch.md (No such file), expected-match, holds}` · `{target-dependents, rg 'validation-watch' coding-clippy/spec/README.md → exactly :27, any-outside-scope:<:27>, holds}` → **holds**

## Held set re-confirmed (unchanged since cycle 6 all-hold)
- D4 (core.md:813 run-state excl + foundation contract 3) holds · D5 (core.md:22/222/275/320 all 4 clauses) holds · D6' (core.md:392/489 + V-5 sites in target) holds · D7 (core.md:903/922/813) holds · D8 (core.md:981/1006) holds · D9 (core.md:1078 + modules:51/187) holds · D10' (core.md:261 + glossary:122 co-producer) holds · D11 (CLAUDE.md:20 lens-set→plugin) holds · D12' (bindings.md 6 §-cites all in target) holds · D13 (framework post-run-review.md vw-folder + Q7) holds · D14' (modules:49 convergence status + SKILL:209 V-9 strip site) holds · D16 (instantiation-guide.md:190 firewall coherence check) holds.
- D2 [COND tech] (wc -w SKILL.md=2579 + SKILL∈scope) holds · D15 [COND tech] (tracker 3015/investigate-design 2364/implement 1988) holds.

## AGGREGATE VERDICT: ALL-HOLD — CONVERGENCE (zero D-track deltas).
Both passes clean this cycle (intent CLEAN + mechanical ALL-HOLD). The cycle-6 fix (spec/README.md as target #11) closed the only gap; no entry falsified; held set unaffected by the scope expansion. The convergence cycle is satisfied.
