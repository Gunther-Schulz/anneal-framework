# Standardized-pass — cycle 1

This cycle produced F1–F5 (current-state observations) + D1 (scope), D2 (the
rule) [OUTLINED], D3 (interface completeness), D4 (enforcement) [PENDING]. No
realization rule-text committed yet (decisions OUTLINED/PENDING; realization
deferred to impl). In-scope lenses:

- **Fragmentation** — CLEAN. The rule (D2) is not stated elsewhere: no
  instance→framework citation discipline exists in the corpus. — basis: F1 (`rg`
  over instantiation-guide.md empty of any citation rule). The glossary-as-interface
  framing is additive to spec/README's existing "operational vs analytic terms" +
  "definitions-only" (README:71-81), not a second copy of an existing rule.
- **Leakage** — CLEAN (N/A by content). D1's edits land in domain-general files
  (instantiation-guide.md, spec/glossary.md, spec/README.md); the rule (D2) is
  domain-general — it applies to any instance, names no domain concretion. — basis:
  Leakage Scope (fires on domain-general files); D2 carries no language/tool/path.
- **Missed-dependents** — FINDING (folded into D1). D2 reframes the glossary's
  role, so spec/README.md:77-81 ("Glossary is definitions-only ... those live in
  core.md") is a dependent that must be reconciled (the interface role must be
  shown compatible with definitions-only — it is: the glossary DEFINES the term and
  POINTS to the section, already done 71×, F3). Reconciliation is additive, in D1(c)
  scope. The other dependents — every instance §-citation (F2) — are the convention's
  downstream re-point targets (Phase B), not this run's edits. — basis: located read
  spec/README.md:77-81; F3.
- **Unenforced-rule** — FINDING (→ D4). D2 is a load-bearing rule; as stated it
  would be prose-only. Per the prescription discipline (README:97-119) a load-bearing
  rule earns structural enforcement. D4 holds the open enforcement-form decision. —
  basis: README:97-119; D2.
- **Undefined-shorthand** — NOTE. The cycle uses "instance-facing interface" /
  "term→section mapping" / "firewall" as load-bearing phrasing; these must be defined
  at the rule's home (D2/D1(c)) when realization is written, not left as coined
  shorthand. Carried to impl. — basis: D2 wording.

Out of scope this cycle (no committed render / verification claim): **Bloat**
(no realization rule-text added yet), **Lossy-render**, **Over-claimed-verification**.
