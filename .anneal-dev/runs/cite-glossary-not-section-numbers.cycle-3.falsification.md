# Falsification-pass artifact — cycle 3 (convergence cycle)

Dispatched to fresh-context subagent `abdae88a728929cd7` (isolated). Iterated each
[VERIFIED] D-entry at convergence-cycle start (D1, D2, D3, D4, D5; D6 [CONDITIONAL]
excluded). Subagent declared candidate+predicate; orchestrator computed
holds-or-falsified and spot-verified the falsifying result.

D1 {target-existence, candidate: `ls instantiation-guide.md spec/glossary.md spec/README.md`, predicate: expected-match:all-present, result: all 3 exist, **holds**}; {target-dependents, candidate: `rg -Ul '(core|modules)\.md[^\n]{0,4}§|anneal-framework/spec/(core|modules)' <instance>` minus spec/+plugin/, predicate: any-outside-scope:{<instance>/spec/**, <instance>/plugin/**}, result: only out-of-population cites are in `coding-clippy/docs/archived/**` + `anneal-dev/derivation-rationale.md` — both brief-excluded; zero in-scope uncounted, **holds**} → **aggregate: holds**

D2 {target-existence, candidate: flattened `tr '\n' ' ' < instantiation-guide.md | rg -io "instance[^.]{0,60}(cite|citation|section.number|glossary term)"` + `rg -niU "citation|cite|section.number" instantiation-guide.md`, predicate: expected-match:no-preexisting-citation-rule, result: no match (the one "citation" hit at :257 is an events-table cell "basis citations", not a rule); guide §-cites are framework-internal self-refs, **holds**}; {target-dependents, candidate: `rg -c "§[0-9]" spec/glossary.md`, predicate: any-match (glossary carries term→section pointers), result: 71 matches (e.g. glossary:53-54), **holds**} → **aggregate: holds**

D3 {target-existence, candidate: `rg -ni "^\*\*evidence-bearing" + "^\*\*post-run" spec/glossary.md`, predicate: expected-match:neither-is-current-headword, result: both exit 1 (not current headwords), **holds**}; {target-dependents, candidate: `rg -U "standardized-pass findings artifact" <instance-specs>` + `rg -ni "^\*\*[^*]*(standardized-pass|findings artifact)" spec/glossary.md` + read glossary:232-244, predicate: any-match for a THIRD §-cited method-concept lacking a glossary headword, result: **POSITIVE** — `modules.md §3.2` "standardized-pass findings artifact" is cited live by in-scope instance specs (clippy/spec/bindings.md:48, anneal-dev/spec/persistence.md:6, daneel/spec/bindings.md) but has NO dedicated glossary headword; its siblings §3.3→"Impl plan"(:343) and §3.4→"Falsification pass"(:152) each have one; the "Pass" headword (:232) defers the artifact to `modules.md §3.2` (glossary:240-241), **FALSIFIED**} → **aggregate: falsified**

D4 {target-behavior, candidate: `rg -U '(core|modules)\.md[^\n]{0,4}§' <instance>` on all 4 instances, predicate: expected-match:regex:. (non-empty on repos known to contain §-cites; empty falsifies), result: non-empty on every instance (clippy 19, daneel 11, anneal-dev 56 in-scope, bauleitplan 8), **holds**} → **aggregate: holds**

D5 {target-existence, candidate: located read spec/README.md:77-81 + `rg -ni "instance-facing|interface" spec/README.md`, predicate: expected-match:{"definitions-only" present AND no "interface" naming}, result: README:77 literally "**Glossary is definitions-only.**"; `rg interface` → exit 1 (README never names glossary an interface), both halves hold, **holds**} → **aggregate: holds**

## Orchestrator computation + disposition

- D1 holds, D2 holds, **D3 FALSIFIED**, D4 holds, D5 holds.
- Orchestrator spot-verified the D3 falsifier directly: `rg "^\*\*[^*]*(standardized-pass|findings artifact)" spec/glossary.md` → no headword; siblings present (glossary:152, 343); "Pass" defers at glossary:240-241; instance citation confirmed by orchestrator's own cycle-1 located read (clippy/spec/bindings.md:48).
- **D3 flips [INVALIDATED]→[PENDING]** (per tracker.md Design-decision states). Convergence cycle 3 is NOT clean (one D-delta). Re-formation runs in cycle 4; a fresh convergence cycle (5) follows.
- Remedy surface (orchestrator's): D3 count 2→3 — add headword "standardized-pass findings artifact" alongside "evidence-bearing-artifact rule" and "post-run review". The §3.3 concept clippy names "implementation decomposition" is NOT a new gap — it re-points to the existing "Impl plan" headword (variant naming = render-drift, Phase B).
