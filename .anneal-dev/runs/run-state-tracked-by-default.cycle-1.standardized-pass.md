# Cycle 1 — standardized inspection pass

Run: `run-state-tracked-by-default` · cycle 1. Scope: `instantiation-guide.md` §5
(domain-general framework rule) + `anneal-dev/spec/*` (instance binding).

- **Bloat** — clean. D1/D2/D4 are reword/reconcile, not net addition (D1 replaces the
  gitignore claim; D2 rewords the observable marker; D4 reconciles a rationale clause). basis: D1/D2/D4.
- **Fragmentation** — clean. "run-state is gitignored" currently lives in 4+ homes (§5,
  persistence.md, bindings.md ×2) — but as a framework RULE (§5, canonical) rendered into the
  anneal-dev BINDING (persistence/bindings reference §5), different levels, not duplicate copies.
  D1 updates all (Missed-dependents). Post-change: §5 canonical, binding references it. basis: F1.
- **Leakage** — **WATCH (design constraint).** §5 is domain-general. The "transient local
  override-flag" category is general, but the concrete example (anneal-dev's
  `allow-adhoc-kernel-edit` run-gate marker) is anneal-dev-specific. **Constraint:** §5 states the
  general category ("transient local override-flags") ONLY; the `allow-adhoc-kernel-edit`
  concretion lives in the anneal-dev binding (`bindings.md`), never in §5. With that, §5 passes
  the framework-arbitrariness test (the rule applies to any instance's run-state). basis: F3 +
  §5 domain-general level.
- **Missed-dependents** — clean. F1 enumerated the policy homes; F2 caught the provisioning
  dependent (→ D4); the plugin render is a dependent (→ D5). basis: F1/F2 + D4/D5.
- **Unenforced-rule** — clean. The track-policy is mechanically enforced (the bootstrap's
  `.gitignore` content; `git check-ignore` observable). The preserved don't-hand-edit contract
  (D2) is a convention — but gitignore never enforced editing anyway (only committing); so D2
  loses no enforcement that existed. basis: D1/D2.
- **Undefined-shorthand** — clean. "transient local override-flag" is descriptive; "run-state
  slot" / "accumulated history" are established. basis: D1.
- **Lossy-render** — N/A (the plugin re-render is deferred to D5/render-debt; no render committed
  this run).
- **Over-claimed-verification** — N/A (no new verification claim recorded).
