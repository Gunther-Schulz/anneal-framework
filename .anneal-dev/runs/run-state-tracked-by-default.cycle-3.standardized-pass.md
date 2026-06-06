# Cycle 3 — standardized inspection pass

Run: `run-state-tracked-by-default` · cycle 3 (reworked: scope+, D7 integrity-exclusion, D3
per-instance default, D1 rationale strengthened). Scope: `instantiation-guide.md` §5
(domain-general) + `anneal-dev/spec/*` + now `core.md §4.2` (in-place integrity, domain-general).

- **Bloat** — clean. D7 adds the run-state-exclusion clause to the in-place integrity check
  (load-bearing: prevents the F-integrity collision + the restore-wipes-tracker hazard); D1's
  rationale strengthening is load-bearing (the resume-durability WHY + the decisive argument vs
  commit-on-completion). No restatement. basis: D7/D1.
- **Fragmentation** — clean. D7's run-state-exclusion is stated at `core.md §4.2` (canonical
  in-place integrity, domain-general) and referenced by the anneal-dev binding (`bindings.md`),
  not duplicated. The track-policy: §5 canonical (framework), binding references it. basis: D0/D7.
- **Leakage** — **WATCH (two constraints).** (1) §5 states "transient local override-flags"
  abstractly; the `allow-adhoc-kernel-edit` concretion lives only in `bindings.md` (F-leakage).
  (2) **D7's exclusion at `core.md §4.2` must name "the run-state directory" ABSTRACTLY** (the
  instance's run-state path per its persistence binding), NOT the anneal-dev concretion
  `.anneal-dev/runs/` — that concretion belongs in the anneal-dev binding. With both, §5 + core.md
  stay domain-general. basis: §5/core.md domain-general level + D7.
- **Missed-dependents** — clean. D0 now enumerates the in-place integrity sites (the F-integrity
  dependent); the plugin render is a dependent (D5/render-debt row). basis: D0 + F-integrity/F-persistence.
- **Unenforced-rule** — clean. D7's exclusion is mechanical (`git status --porcelain` scoped to
  exclude the run-state path; observable). D3's per-instance default is enforced by the instance's
  bootstrap (anneal-dev binds default-on). The preserved don't-hand-edit contract (D2) stays a
  convention (gitignore never enforced editing). basis: D7/D3/D2.
- **Undefined-shorthand** — clean. "transient local override-flag", "resumable checkpoint",
  "run-state slot" — descriptive / established. basis: D1/D7.
- **Lossy-render / Over-claimed-verification** — N/A (plugin re-render deferred to D5/render-debt;
  no new verification claim).
