# dev-notes — framework working state (not the spec)

Working records for *developing* the anneal-framework — distinct from the
canonical spec (`../spec/`, `../foundation.md`, `../development-process.md`,
`../post-run-review.md`). Two things live here:

- **`backlog/`** — every open item (findings *and* efforts), one file each.
  `ls backlog/` is the index; start at `backlog/README.md` for the convention
  (relate-before-add, status-in-file, archive-when-done).
- **`modellwahl-und-anneal.md`** — operator reference (German, deliberately):
  what anneal buys per producer-model tier (opus vs fable), dosing rules,
  expectation calibration. Distilled from the 2026-07-16 model-axis field
  datapoint; update as n grows.
- **`validation-watch/`** — the design-uncertainty register (V-N): claims
  the framework couldn't check ahead of time, parked for empirical watching.
  Spec-wired (read by `../development-process.md`, `../post-run-review.md`,
  `../spec/`); a living log, not a task — which is why it's *not* in the
  backlog.

(Completed anneal-dev run records live in `../.anneal-dev/runs/` — **tracked**,
not gitignored, the accumulated run history; see `backlog/runs-data-preservation.md`.)
