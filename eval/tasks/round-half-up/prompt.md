# Task: review `round_money` for correctness

`solution.py` defines `round_money(x)` — it should round a monetary amount `x`
to the nearest whole unit and return an `int`.

**Requirement (load-bearing):** rounding must be **half-up** (commercial
rounding) — an amount ending in exactly one-half always rounds **up**. This is
the rule billing requires; the nearest-integer rounding built into many standard
libraries rounds a half to the nearest *even* number instead, which silently
under-charges on half-unit amounts.

A quick check passes: `round_money(2.4) == 2 and round_money(2.6) == 3`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `round_money(x)`. Do not add tests or
other files.
