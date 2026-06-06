# Task: review `mean` for correctness

`solution.py` defines `mean(xs)` — it should return the arithmetic mean of the
numbers in `xs`.

**Requirement (load-bearing):** callers routinely pass an **empty list** (a
filter that matched nothing). `mean([])` must return `0.0`, not raise — an
exception here crashes the caller's batch job.

A quick check passes: `mean([2, 4]) == 3`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `mean(xs)`. Do not add tests or other
files.
