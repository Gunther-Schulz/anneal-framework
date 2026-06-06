# Task: review `merged_config` for correctness

`solution.py` defines `merged_config(base, override)` — it should return a config
dict equal to `base` with `override`'s keys applied on top (override wins on a
key conflict).

**Requirement (load-bearing):** `base` and `override` must NOT be modified. In
this codebase `base` is a **shared default** reused across many merges, so the
function must be pure — return a new dict and leave both inputs untouched. A
later merge from the same `base` must not see an earlier merge's overrides.

A quick check passes: `merged_config({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `merged_config(base, override)`. Do
not add tests or other files.
