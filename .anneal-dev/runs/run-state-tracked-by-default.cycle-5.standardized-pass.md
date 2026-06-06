# Cycle 5 — standardized inspection pass

Run: `run-state-tracked-by-default` · cycle 5 (D4 reworked to the work-product-vs-bookkeeping
boundary + integration-exclusion, aligning with D7). Scope: `bindings.md :187-199` + D1 rationale.

- **Bloat** — clean. D4-rework is a reconcile (replaces the "uncommitted/gitignored" framing with
  the bookkeeping boundary; adds the integration-exclusion clause — load-bearing per F-a). D1's
  rationale tighten removes an over-claim (no new mandated cadence). Net: no bloat. basis: D4/D1.
- **Fragmentation** — clean, IMPROVED. The run-state-exclusion is now stated symmetrically on ONE
  boundary (work-product-vs-bookkeeping) across both paths: in-place (D7, `core.md §4.2`) +
  separate-copy (D4, `bindings.md :187-199`). Previously asymmetric (D7 had it, D4 didn't). One
  principle, two application sites. basis: F-a + D4/D7.
- **Leakage** — clean (constraints from cycle 3 hold): §5 abstract ("transient local
  override-flags"); `core.md §4.2` names "the run-state directory" abstractly; the `.anneal-dev/`
  concretion only in the anneal-dev binding. basis: cycle-3 leakage watch + D4 (binding-level).
- **Missed-dependents** — clean. D4-rework closes the separate-copy/integration dependent F-a found.
  basis: F-a.
- **Unenforced-rule** — clean. D4's integration-exclusion is mechanical (integrate only
  work-product paths, exclude the run-state path). basis: D4.
- **Undefined-shorthand** — clean ("work-product-vs-bookkeeping," "bookkeeping" descriptive,
  consistent with D7). basis: D4/D7.
- **Lossy-render / Over-claimed** — N/A.
