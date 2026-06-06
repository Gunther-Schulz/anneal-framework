# Mechanical falsification-pass artifact — anneal-dev-reinstantiation, cycle 3

Fresh-context subagent (agentId aed9b95cbec713212). Iterates the [VERIFIED]
D-entries D1–D6 (D7/D8 [CONDITIONAL] → skipped; discharged by verify/operator).
Orchestrator-confirmed: each line's aggregate computed from per-candidate
predicate-applied-to-result.

- `{D1, [
    {target-existence, `git diff --stat d9033ee HEAD -- <6 source files>`,
     expected-match:`5 files changed`, result="417 ins; each contract clause
     located (core §4.1.4/§5.1/§4.1/§4.3, modules §3.4/§3.4.1/§3.1, bindings
     model-tier, persistence)", holds},
    {target-dependents, `grep -rniE '<contract tokens>' implement.md lenses.md
     post-run-review.md`, any-outside-scope:{5 in-scope files}, result=empty for
     all 3 out-of-scope files, holds}
  ], aggregate=holds}`
- `{D2, [
    {target-existence, grep core.md §4.1.4 + modules §3.4/§3.4.1,
     expected-match:`mechanical falsification-pass artifact`/`intent-
     falsification-pass artifact`/intent-first, result=core L393-399 + L529;
     modules L322/L412, holds},
    {target-dependents, `grep -rniE 'falsif' .`, any-outside-scope:{invdesign,
     tracker, SKILL}, result=invdesign(35)+tracker(22)+SKILL(1@L186, in D6
     range), holds}
  ], aggregate=holds}`
- `{D3, [
    {target-existence, grep core.md disposition/surfaced/four/five,
     expected-match:`four cases`/`surfaced`/`five paths`, result=core L901/L922/
     L954/L1051/L325, holds},
    {target-dependents, `grep -rniE 'VERIFIED —|disposition|surfaced' .`,
     any-outside-scope:{foundations, tracker, verify, +SKILL per D6},
     result=out-of-scope hits all `[VERIFIED — deferred]` (existing enum member
     use, not changed-contract); `VERIFIED — surfaced` grep empty (net-new),
     holds}
  ], aggregate=holds}`
- `{D4, [
    {target-existence, grep core.md requirements-record/coverage/four-checks,
     expected-match present, result=core L299-300 + L800 + §4.3 "Requirements
     coverage" soft leg, holds},
    {target-dependents, `grep -rniE 'requirement' .`, any-outside-scope:{4 named
     files}, result=only common-word uses (basis-rule requirement / convergence
     cycle requirement); requirements-record contract has zero current sites,
     holds}
  ], aggregate=holds}`
- `{D5, [
    {target-existence, grep bindings.md Dispatch-model-tier/blanket/forbidden/
     four-placeholder, expected-match present, result=bindings L249-260 +
     L297 + L278-291, holds},
    {target-dependents, `grep -rniE 'model-tier|top-tier|opus' .`,
     any-outside-scope:{SKILL, foundations}, result=empty everywhere (net-new),
     vacuously holds}
  ], aggregate=holds}`
- `{D6, [
    {target-existence, read modules §3.1 + grep core mode-keyed/surfaced,
     expected-match:State-summary dual-citation + recorded-skip + §5.2 mode-keyed,
     result=modules L51-53 + core L929-930 + L1051, holds},
    {target-dependents, `grep -niE 'falsif|surfaced|disposition' SKILL.md`,
     any-outside-scope:{SKILL.md}, result=L186 + L248-249, both within D6 cited
     ranges (184-187, 243-249), single-file target, holds}
  ], aggregate=holds}`

target-behavior shape not statically attacked (render decisions → behavior-
preservation = verify's render-fidelity battery, R2; holds-deferred-to-verify).

## Bottom line
All D1–D6 aggregate=holds; **no falsification → zero D-track delta**. Coverage
note (not a falsification): SKILL.md's rename site (L186) + surfaced/mode-keyed
text (L248-249) are held in scope via D6's SKILL.md coverage, not D2/D3's named
targets → the impl plan assigns SKILL.md as ONE per-file unit rendering all its
deltas (D5+D6 + the L186 rename + L248-249 surfaced text), removing the
cross-decision ambiguity.
