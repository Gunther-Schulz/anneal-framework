# firewall-regex-wrap-tolerance — cycle 1 standardized inspection pass

Scope: a regex swap + a wrap-tolerance clause in instantiation-guide.md (D1) + a render-debt
queue row (D2). Each line cites this-cycle basis.

- **Bloat** — clean-with-commitment. D1's wrap-tolerance note is ~1 sentence and load-bearing (states the
  multiline + non-alnum-gap rationale + the false-positive guard); it cross-references the glossary idiom
  rather than restating it. basis: D1 (this cycle).
- **Fragmentation** — clean. D1 cross-references the wrap-tolerant idiom (`glossary.md` §Completeness claim /
  `core.md` §3.2), not a second copy. basis: F3 + D1.
- **Leakage** — clean. The regex tokens `(core|modules)\.md` are framework spec file-names (framework-general),
  not an instance-domain concretion; instantiation-guide.md is the (non-rendered) instantiation guide. basis: D1.
- **Missed-dependents** — clean. The only in-repo home is instantiation-guide.md:189 (F2); instance renders are
  render-debt (D2). basis: F2 search.
- **Unenforced-rule** — clean. The firewall check is a mechanical rg command run by the render-verify (an
  acceptance gate); D1 strengthens it (catches wraps). Enforcement = the render-verify running the (now
  wrap-tolerant) command; a non-empty result is a finding. basis: located read instantiation-guide.md:190-191.
- **Undefined-shorthand** — clean. No new coined term ("wrap-tolerant" is established in glossary.md). basis: F3.
- **Lossy-render** — clean (note for D2). The firewall check renders into instances (clippy/daneel render-verify);
  D1's fix is a LITERAL regex command (no paraphrase) → it renders verbatim, so no softening risk. The render-debt
  (D2) ensures the literal regex propagates. basis: D1 (literal artifact) + D2 (render-debt).
- **Over-claimed-verification** — clean. F1/F4's "empirically tested" claims cite the actual `rg` test output
  (wrap:1, normal:2, prose:0, neither:0), not an assertion. basis: F1, F4 Bash tests.
