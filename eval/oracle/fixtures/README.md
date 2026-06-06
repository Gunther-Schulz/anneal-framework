# oracle/fixtures — reference correct solutions (gate-only)

One `<task>_fixed.py` per task: a reference *correct* implementation used solely
by `eval/wellformedness.py` to verify gate criterion (c) — a correct fix scores
1.0 on the held-out oracle (the oracle is not over-strict).

**These are never shown to an arm.** Arms receive only `tasks/<task>/prompt.md`
and the seeded-defect `tasks/<task>/solution.py`. Keeping the fixtures out of the
task dirs is what keeps the experiment blind.
