# purpose-mechanism-clause — cycle 3 mechanical falsification pass

Fresh-context subagent (opus) declared candidates + predicates + ran them; orchestrator computes
holds-or-falsified by applying each predicate to the result.

```
{D1, [
  {shape: target-existence, candidate: read spec/core.md:111-169 for the separate-checker mechanism,
   predicate: expected-match:"context that did not produce the artifact re-derives it",
   result: PRESENT — core.md:139-154 ("enforced by a separate checker: a context that did not produce
     the artifact re-derives it … producer-independent re-derivability"),
   holds-or-falsified: HOLDS},
  {shape: target-existence, candidate: read spec/core.md:111-169 for the operator terminus,
   predicate: expected-match:"genuinely-irreducible judgment",
   result: PRESENT — core.md:156-157 ("operator's verdict is a binding terminus only at the
     genuinely-irreducible judgment"),
   holds-or-falsified: HOLDS},
  {shape: target-dependents, candidate: corpus wrap-tolerant search for an "exactly two
     (goals|elements)" closure on Purpose + cross-refs,
   predicate: any-match (a dependent asserting closed two-element Purpose),
   result: NO such closure — core.md:12 + anneal-dev/.../foundations.md:9 state two goals but already
     carry a 3rd non-goal paragraph; cross-refs (README:107/148/152, instantiation-guide:77 "two
     values") refer to the goals, not a closed count. Flag: INV-2-complete-state.md:6 anchors
     core.md:18 (goal #2) — orchestrator-verified PRESERVED (clause inserts after line 20; line 18
     does not shift),
   holds-or-falsified: HOLDS},
 ], aggregate: HOLDS}

{D2, [
  {shape: target-existence, candidate: grep render-cadence policy at the basis-cited location
     dev-notes/README.md,
   predicate: expected-match:"framework runs ship spec-only / renders batch",
   result: ZERO matches at dev-notes/README.md (an 18-line index). The policy EXISTS verbatim but at
     instance-reinstantiation.md:24-36 ("Render-cadence policy (operator-decided 2026-06-04) … ships
     spec-only … does NOT render into the instances per-run"),
   holds-or-falsified: FALSIFIED (basis citation points at the wrong file; substance holds elsewhere)},
 ], aggregate: FALSIFIED → D2 [INVALIDATED]→[PENDING], basis citation corrected (F10)}

{D3/D4, [
  {shape: target-existence, candidate: read dev-notes/backlog/instance-reinstantiation.md:140-153,
   predicate: expected-match:"run-state render-debt enumerated (all 6 stale-render spots)",
   result: PRESENT — lines 147-152 enumerate SKILL.md:315, :347, foundations.md:462/469, tracker.md:402,
     implement.md:160 = 5 files / 6 line-anchors, matching D4's "all 6 spots",
   holds-or-falsified: HOLDS},
 ], aggregate: HOLDS}
```

**Outcome:** D1, D3/D4 hold; **D2 falsified on its basis citation** (a real defect in the
orchestrator's tracker — the render-cadence policy was cited to `dev-notes/README.md` but lives at
`instance-reinstantiation.md:24-36`). D-track delta → cycle 3 not clean → correct D2's basis, run
cycle 4. (Notable: the mechanical pass caught an error in the orchestrator's own artifact — the
separate-checker requirement working as designed.)
