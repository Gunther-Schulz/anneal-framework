# f0-render-conventions — impl plan

4 dispatch units, **all parallel-eligible** (pairwise file-disjoint, contract-disjoint). D1 produces no
edit (it confirms the existing slot-model; the corpus-consistency work is D2–D5). F-E is render-debt
(not an F0 unit). Disjointness basis: the four units touch four distinct files —
`grep`-established each unit's scope is a single file with no shared contract surface:
`instance-template/spec/isolation.md` (new) · `instance-template/README.md` · `spec/glossary.md` ·
`instantiation-guide.md` — no two units name the same file or term.

- **U1 (D2)** — CREATE `instance-template/spec/isolation.md` (persistence.md-style placeholder; 6-element
  declaration shape; required; domain-general). first; parallel with U2/U3/U4.
- **U2 (D3)** — AMEND `instance-template/README.md`: add `spec/isolation.md` under "Required slots" (with
  persistence), `core.md §4.2.3` pointer. first; parallel with U1/U3/U4. (References U1's filename only,
  not its content — disjoint.)
- **U3 (D4)** — AMEND `spec/glossary.md`: Basis (:49-54) defines located-read / construct-taken-whole /
  executable-verification; Completeness-claim (:77-79) defines wrap-tolerant search; concise gloss +
  `core.md §3.2` pointer; no new headwords. first; parallel with all.
- **U4 (D5)** — AMEND `instantiation-guide.md`: reconciliation clause at/before the first §2 worked
  example (`:92`) cross-referencing `instance-template/README.md` "After instantiation" (:53-59). first;
  parallel with all.

Each unit dispatched to a subagent that invokes skill-craft before the rule-text edit (per the dispatch
brief); method-kernel edits (U3 glossary, U4 guide) carry the verify's skill-craft self-review +
operator soundness pass (CLAUDE.md development-process grounding).
