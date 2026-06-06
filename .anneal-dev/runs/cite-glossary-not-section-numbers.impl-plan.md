# Impl plan — cite-glossary-not-section-numbers

**1 dispatch unit**, single container (the `anneal-framework` repo), **sequential/single**
→ runs in-place under the in-place Integrity check (no parallelism, no disjointness search
needed; nothing in flight). The unit touches rule-corpus files → the dispatched subagent
invokes skill-craft (Skill tool) before editing, per the method-kernel gate.

State marker (HEAD before dispatch): `2f96c43bdb9df86b6a258ea97d82fe8f4ff85c20` on branch
`cite-glossary-not-section-numbers`.

## Unit U1 — the citation convention (implements D2, D3, D4, D5 within D1's scope)

- **Implements:** D2 (firewall rule), D3 (3 glossary headwords), D4 (enforcement check),
  D5 (README interface naming). D1 = scope (the boundaries); D6 = orchestrator-filed backlog
  item (not rule-corpus, filed post-unit).
- **Container:** `anneal-framework` (1 touched container).
- **Element scope:**
  - `spec/glossary.md` — add 3 definitions-only headwords (D3): "evidence-bearing-artifact
    rule" (Basis-and-evidence section, ~:47-113), "standardized-pass findings artifact"
    (near "Pass" :232, parallel to "Falsification pass" :152 / "Impl plan" :343), "post-run
    review" (Triage-and-review-classifications section, ~:423).
  - `instantiation-guide.md` — add the firewall citation rule + its grep-check (D2+D4), in/after
    §3 (Binding, :139-158), WITHOUT renumbering §4-§6.
  - `spec/README.md` — name the glossary the instance-facing interface, reconciling
    "definitions-only" (~:77-81) (D5).
- **Contract scope (locked contracts the unit honors):**
  - D2 forces: instance specs reference the framework only via glossary terms, never a
    framework §-number; glossary = instance-facing interface (owns term→section mapping);
    §-coupling legal intra-framework, forbidden across the instance boundary.
  - D3: exactly 3 new headwords; definitions-only (state meaning + point to §; never specify
    shape/behavior — those live in core.md/modules.md), per spec/README:77-81.
  - D4 evidence-bearing artifact: `rg '(core|modules)\.md[^\n]{0,4}§' <instance>` returns empty;
    run as a coherence check at render-verify.
  - D5: additive to definitions-only (no contradiction — the glossary defines the term AND
    points to its section, already done 71×).
- **Parallel-eligibility:** none (single unit). Sequential, in-place.
- **Out of unit scope (NOT edited):** any instance repo's §-citations (= Phase B re-render);
  the binding-table completeness (= D6, separate item).
