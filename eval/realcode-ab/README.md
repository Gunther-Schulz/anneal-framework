# realcode-ab — the real-codebase A/B apparatus

The experiment that produced session-11's findings (and the pending process-varied test). Distinct
from the synthetic silent-failure pack one level up (`eval/tasks/` + `eval/oracle/`): this runs review
arms against a **real production codebase** at a known-buggy commit and scores by a fixed bug list.

**Target:** beat-the-books replay engine, `src/beat_the_books/services/analysis/replay/`, at
**`1f62d57d^`** — the parent of the Unit-27 period-aware-settlement fix (i.e. the buggy pre-fix state).
Repo: `~/dev/Gunther-Schulz/beat-the-books` (not part of this repo).

**Files:**
- `build-tree.sh` — exports + sanitizes the pre-fix tree (strips docs/.clippy/.git which leak the fix),
  keeps code only, makes N copies. `bash build-tree.sh` → `/tmp/bt-eval/copy_1..5`.
- `arms.md` — the **verbatim** arm prompts (act-first / vanilla / adhoc, blind + non-blind) + the
  PENDING process-varied design. Wording is load-bearing — copy exactly, don't paraphrase.
- `scoring.md` — the 5-bug oracle + per-shape catchability + pointer to the result tables.

**Status / what's run:** see `../../dev-notes/backlog/anneal-empirical-validation-experiment.md`
(VERDICT + Addendum 1 + Addendum 2) — the live writeup, results tables, and honest net state.
Short version: prompt-level anneal ≈ act-first once blind; the **framework-as-process is untested**;
the one open decision is the process-varied test in `arms.md` (run it prompt-constant, process-varied,
as TERMINAL — or close the thread).

**Operational:** dispatch **≤5 parallel** review subagents per batch (10-at-once rate-limited the server).
The `/tmp/bt-eval/*` working dirs are ephemeral; regenerate with `build-tree.sh`. No scored oracle script —
scoring is judgment against `scoring.md`'s bug list (these are real-codebase reviews, not seeded-defect tasks).
