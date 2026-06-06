# Standardized inspection pass — cycle 1

Run: anneal-dev-model-tier-policy. Lens set = core (8) ∪ project supplement
(`anneal-dev.config/lenses.md` — empty, no supplements). All 8 core lenses in
scope: the cycle designs a new rule (bindings.md section) + config artifacts.

- **Bloat** — CLEAN. The bindings.md section carries only load-bearing prose:
  the policy (D3), the tier-source + default (D4/D6), and the floor framing
  (R4, which is load-bearing — it bounds the claim against over-reading as a
  safety guarantee). The INV-3-diversity rationale is held OUT of rule-text
  (D7) precisely to avoid narrating reasoning the rule does not act on. —
  basis: D3, D7 (this cycle); Load-bearing test applied per-passage.
- **Fragmentation** — CLEAN. The principle is not stated anywhere in the corpus
  today (no second copy to drift). — basis: F1 (this cycle) corpus-wide search
  empty.
- **Leakage** — CLEAN (the change's whole point). The rule lands in the
  instance spec (bindings.md) + config; the domain-general framework spec is
  untouched and carries zero model tokens, so no domain/harness concretion leaks
  into a domain-general file. — basis: D2, F3 (this cycle).
- **Missed-dependents** — CLEAN. New contract → no pre-existing dependents
  (F1). The one dependent the change creates — the rendered anneal-dev plugin —
  is enumerated and queued as render-debt (D8); the bootstrap-list dependents
  are NOT incurred because D5 adds no bootstrapped placeholder. — basis: F1, D1,
  D5, D8 (this cycle).
- **Unenforced-rule** — CLEAN. The rule produces an observable artifact: the
  model param on each dispatch (a downgraded dispatch is visible) — mechanical
  criteria per practice 8. — basis: D3 (this cycle).
- **Undefined-shorthand** — CLEAN. "model tier" / "top tier" is defined inline
  where introduced (bindings.md), not left to pattern-completion; no
  multiply-defined use (the term is new — F1). — basis: D9, F1 (this cycle).
- **Lossy-render** — NOTED (design-time clean; render deferred). The rule is a
  "forbidden"/"must"-class prescription; the design commits to preserving that
  enforcement strength at render. The render itself is checked by the
  render-fidelity battery at the batch re-render (D8), not this run. — basis:
  D3, D8 (this cycle).
- **Over-claimed-verification** — CLEAN. The floor framing (R4/D7) explicitly
  states top-tier is NOT a safety guarantee and does not substitute for the
  structural checks — the design avoids the over-claim by construction. — basis:
  D7, R4 (this cycle).
