# Task: review `dedupe` for correctness

`solution.py` defines `dedupe(items)` — it should return a list with duplicate
values removed.

**Requirement (load-bearing):** the result must preserve **first-occurrence
order** — the order in which each value first appears in the input. Downstream
code walks this list positionally, so reordering it corrupts the output even
though the set of values is unchanged.

A quick check passes: `set(dedupe([1, 2, 2, 3])) == {1, 2, 3}`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `dedupe(items)`. Do not add tests or
other files.
