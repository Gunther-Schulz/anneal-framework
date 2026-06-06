# dev-notes — framework working state (not the spec)

Working records for *developing* the anneal-framework — distinct from the
canonical spec (`../spec/`, `../foundation.md`, `../development-process.md`,
`../post-run-review.md`). These live here:

- **`backlog/`** — every open item (findings *and* efforts), one file each.
  `ls backlog/` is the index; start at `backlog/README.md` for the convention
  (relate-before-add, status-in-file, archive-when-done).
- **`validation-watch/`** — the design-uncertainty register (V-N): claims
  the framework couldn't check ahead of time, parked for empirical watching.
  Spec-wired (read by `../development-process.md`, `../post-run-review.md`,
  `../spec/`); a living log, not a task — which is why it's *not* in the
  backlog.
- **`run-history/`** — completed anneal-dev runs, archived on close (the
  committed durable record of *how* a run unfolded — tracker + per-cycle
  pass artifacts). Live run state stays in gitignored `.anneal-dev/runs/`;
  on verify-[PASSED] close the run is copied here. Provisional first instance
  pending the `runs-data-preservation` formalization (backlog).
