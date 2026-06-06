# Task: review `clamp_score` for correctness

`solution.py` defines `clamp_score(x)` — it should clamp a raw score into the
valid range **[0, 100]**.

**Requirement (load-bearing):** scores above 100 must be **capped at 100**, and
scores below 0 floored at 0. Upstream sometimes emits out-of-range values (bonus
points can push a raw score over 100); an un-capped value corrupts the
percentage display downstream.

A quick check passes: `clamp_score(50) == 50`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `clamp_score(x)`. Do not add tests or
other files.
