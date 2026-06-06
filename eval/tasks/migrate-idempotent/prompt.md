# Task: review `ensure_prefix` for correctness

`solution.py` defines `ensure_prefix(path)` — it should return `path` guaranteed
to start with the prefix `"/api/"`.

**Requirement (load-bearing):** the function must be **idempotent**. It runs as a
data migration that is re-applied on every deploy, including on paths a previous
run already prefixed. Calling it on an already-prefixed path must return that
path unchanged — never `"/api//api/..."`.

A quick check passes: `ensure_prefix("users") == "/api/users"`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `ensure_prefix(path)`. Do not add
tests or other files.
