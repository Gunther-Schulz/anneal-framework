#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `csv-escape`.

Seeded defect: `",".join(fields)` — concatenates with commas and never quotes,
so a field that itself contains a comma splits into extra columns when parsed.
The advertised weak check has no embedded commas, so it stays green; the held-out
checks below round-trip each row through the stdlib csv reader and require it to
reproduce the original fields exactly.

Usage: python csv_escape_oracle.py <run-dir>
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "to_csv_row"


def _roundtrip(fn, fields):
    row = fn(fields)
    parsed = next(csv.reader([row]))
    return parsed == fields, f"row={row!r} parsed={parsed}"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (no embedded commas)
    return fn(["a", "b", "c"]) == "a,b,c"


def check_plain(fn):
    ok, ev = _roundtrip(fn, ["a", "b", "c"])
    return ("plain fields round-trip", ok, ev)


def check_embedded_comma(fn):
    ok, ev = _roundtrip(fn, ["Smith, John", "42"])
    return ("field containing a comma round-trips", ok, ev)


def check_comma_in_middle(fn):
    ok, ev = _roundtrip(fn, ["a", "b,c", "d"])
    return ("comma-bearing middle field does not split", ok, ev)


CHECKS = [check_plain, check_embedded_comma, check_comma_in_middle]

if __name__ == "__main__":
    main(FN, CHECKS)
