# f0-render-conventions — cycle 4 standardized-pass

In scope (the re-form touched): the guide §2 reconciliation (D5), the README bucket (D3), the
glossary define (D4), the template-firewall-clean finding (F-E).

- **Fragmentation** — CLEAN (resolves the cycle-3 finding): D5 **cross-references** the canonical
  consolidation statement (`instance-template/README.md` "After instantiation", `:53-59`) rather than
  restating it in the guide — one canonical home + a pointer, not two drifting copies. basis: D5 body,
  `README:53-59`.
- **Missed-dependents** — CLEAN (grounded): the "every slot" claim's dependents are now all assigned —
  README slot-list `:25-48` → D3; guide `:18` prose claim → D5; guide worked-examples `:92/108/120` →
  D5; the instance left-column cites → F-E (render-debt, deferred with a trigger). No dependent left
  stale. basis: F-C/F-E, D3/D5 bodies.
- **Bloat** — CLEAN: D4 holds define-in-place (no new headwords); D5 is a clause + cross-ref (no
  duplication); D2's isolation.md is the load-bearing capability-signal file. basis: D4/D5 considered
  lines, `guide:404-408`.
- **Leakage** — CLEAN (re-attest at drafting): D2's isolation.md modeled on the domain-general
  persistence.md placeholder; D5/D4 edits are domain-general (guide/glossary are framework-level).
  basis: `instance-template/spec/persistence.md`.
- **Unenforced-rule** — CLEAN: "file for every slot" enforced by file-presence (`:404-408`), satisfied
  by D2; the firewall rule (`:182-186`) is mechanically checked (`rg` → empty), satisfied for the
  template (F-E: 0 cites). basis: located reads `:404-408`, `:182-186`.
- **Lossy-render / Over-claimed-verification** — CLEAN: D4/D5 additive (define / clause-add), no
  enforcement softened; the re-formed [VERIFIED] bases carry run searches (F-E grep counts, sole-home
  searches). basis: D2-D5 bases.

No load-bearing finding open; D1–D5 [VERIFIED]; F-E [VERIFIED — deferred]. Design CHANGED this cycle →
a fresh convergence cycle (intent + mechanical falsification) is required before [READY] (cycle 3's is
stale).
