# Mechanical falsification-pass artifact — enumeration-target-blindness, convergence cycle 4

Fresh-context subagent (opus). Attacked [VERIFIED] D-entries D1, D2, D3, D4, D5, D7
(D6 [CONDITIONAL], excluded). Subagent declared candidate+predicate; orchestrator
computed holds-or-falsified. Coverage-check on return: each line carries ≥1 candidate
per claimed shape; predicates from the closed set, shape-coherent. **All aggregate = holds.**

- **{D1, [{target-dependents, candidate: corpus-wide wrap-tolerant grep for §3.2.2
  completeness-claim dependents (`preserved or dropped` / `non-reference structural
  dependent` / `producer of an artifact the target consumes` / `§3.2.2` cross-refs) +
  newline-flattened sweep, predicate: any-outside-scope:{core §3.2.2 + §5.2 :1123-1124 +
  glossary :112-122 + lens-set :106-119 + modules §3.4 + render-debt}, result: extra
  hits (modules:408-410/:337, core:352/:495, glossary:58) are §3.2.2 SECTION-POINTERS
  (cite the rule, don't restate the enumeration → not dependents of the content change);
  no clause-restating dependent outside scope, holds}, {target-existence,
  expected-match:"§3.2.2"/"behaviors preserved or dropped"/"Coupling shape"/"Missed-dependents",
  result: all edit-sites present as cited, holds}], aggregate: holds}**
- **{D2, [{target-existence, expected-match:"Closed set of three"/"no fourth shape",
  result: glossary:99,113 + lens-set:119 all assert the invariant, holds},
  {target-existence, expected-match:"target-existence`, `target-dependents" (modules keys
  on shapes), result: modules:358-359/:337 key §3.4 on the three shapes; ZERO
  dependent-form-token hits in modules → untouched, holds}, {target-dependents(fourth-shape
  probe), any-match on `fourth/4th shape` assertion, result: only hit is lens-set:119
  "(no fourth shape)" — a negation, not a contradicting assertion, holds}], aggregate: holds}**
- **{D3, [{target-existence, expected-match:"an explicit enumeration of behaviors
  preserved or dropped", result: core:255-257 bare clause present (no form, no method),
  holds}, {target-dependents, any-outside-scope:{core §3.2.2 :256-257 + §5.2 :1124},
  result: exactly two copies (core:257 + :1124), both in the D3+D7 scope, holds}],
  aggregate: holds}**
- **{D4, [{target-existence, expected-match:"producer of an artifact the target consumes"
  + path-hardcoder + precedent, result: core:248 (form 1) + :250 (form 2) + :253
  (producer↔consumer precedent) all present, holds}, {target-dependents,
  any-outside-scope:{core §3.2.2 :246-254 + glossary :112-122 + lens-set :106-119},
  result: dependents-form statements all in scope; "co-producer"/"equality-compared sink"
  pre-exists nowhere (genuinely new), holds}], aggregate: holds}**
- **{D5, [{target-dependents, any-outside-scope:{glossary :112-122 + lens-set :106-119 +
  core §3.2.2}, result: glossary cross-refs §3.2.2 at :105/:106/:109/:125, lens-set at
  :125/:134/:136; sweep for a THIRD form-restatement outside the two scoped renderings =
  EMPTY (no un-reconciled Fragmentation co-home), holds}, {target-existence,
  expected-match:"Coupling shape"/"Missed-dependents", result: both rendering targets
  present (glossary:98, lens-set:99), holds}], aggregate: holds}**
- **{D7, [{target-existence, expected-match:"references + behaviors preserved/dropped"
  (present) + the dependents-omission (range LACKS "dependent"), result: core:1123-1124
  carries the leg-list paraphrase; grep "dependent" over :1115-1130 = EMPTY → stale, as
  claimed, holds}], aggregate: holds}**

## Orchestrator verdict
All six entries **hold**; no entry falsified; no flip. Combined with the clean
intent-falsification pass (cycle 4, zero new D-delta), the convergence cycle produced
**zero D-track deltas → CONVERGED**.

**Subagent note (basis clarification, NOT a falsification):** D5's summary phrase
"renderings are pointers, not restated rules" understates them — glossary:112-122 and
lens-set:106-119 inline-restate the dependent FORM-LIST; the co-producer must be added to
those restating lists (D5's action already commits to this — "gains the co-producer as a
… rendering" / "form-list gains the co-producer (eighth form)"). Recorded as a D5
basis sub-annotation; resolution unchanged → not a D-delta.
