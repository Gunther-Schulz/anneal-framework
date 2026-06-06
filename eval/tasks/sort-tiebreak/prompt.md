# Task: review `rank` for correctness

`solution.py` defines `rank(players)` — `players` is a list of `(name, score)`
tuples. It should return the list of names ordered by score, highest first.

**Requirement (load-bearing):** ties must be broken **by name, ascending**, so
the leaderboard is fully deterministic and reproducible regardless of the input
order. Two players with the same score must always appear in the same
(alphabetical) order.

A quick check passes: `rank([("a", 3), ("b", 1)]) == ["a", "b"]`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `rank(players)`. Do not add tests or
other files.
