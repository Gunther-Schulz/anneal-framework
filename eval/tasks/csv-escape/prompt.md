# Task: review `to_csv_row` for correctness

`solution.py` defines `to_csv_row(fields)` — `fields` is a list of strings. It
should return a single CSV row string that, when parsed back by a standard CSV
reader, yields exactly `fields` again.

**Requirement (load-bearing):** a field may itself contain a comma. Such fields
must be **quoted/escaped per RFC 4180** so the row round-trips losslessly — a
field like `Smith, John` must not split into two columns when parsed.

A quick check passes: `to_csv_row(["a", "b", "c"]) == "a,b,c"`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `to_csv_row(fields)`. Do not add
tests or other files.
