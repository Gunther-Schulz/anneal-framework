# clippy reference/phase-file de-bloat

**Status:** [PARKED] — follow-up spawned by the `clippy-reinstantiation` run (2026-06-07, D15 [AUTO-ACCEPTED]). Low-priority; not staleness, structural budget.

## What

The clippy re-render (run `clippy-reinstantiation`, `.anneal-dev/runs/`) de-bloated the always-loaded **SKILL.md** (2579→2182 words, no rule dropped) but **deferred** de-bloat of the large reference/phase files, which the faithful render grew further:

- `references/tracker.md` — **3880** words (largest)
- `phases/investigate-design.md` — **3545**
- `phases/implement.md` — **2319**
- `references/foundations.md` — **2216**

## Why deferred (the D15 rationale)

skill-craft's tight 1500–2000 ideal targets the **always-loaded activation file** (SKILL.md), which the run did de-bloat. Reference/phase files are loaded on-demand and carry more latitude. De-bloating them is **work-kind 2** (fresh-rewrite needing skill-craft per file) — mixing it into the faithful-propagation re-render would have inflated that run for a non-staleness reason. So: flagged (R5 satisfied), de-bloat split here.

## Next action

A focused skill-craft-gated de-bloat pass on the 4 files (compress restatement/narration, keep every rule/closed-enum) — its own anneal-dev cycle when clippy structural-budget is worth a pass. Not urgent (drift ≈ 0; the files are faithful + correct, just verbose).

## Relates to
- `instance-reinstantiation.md` — the umbrella; clippy's staleness render is DISCHARGED, this is the residual budget tail.
