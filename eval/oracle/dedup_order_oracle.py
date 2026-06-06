#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `dedup-order`.

Seeded defect: `return list(set(items))` — dedupes correctly but drops the
first-occurrence ordering the prompt requires. The advertised weak check is a
set comparison (order-blind), so it stays green; the held-out checks below
assert insertion order on inputs whose set-iteration order provably differs from
insertion order (ints chosen so CPython's value-ordered small-int set layout —
which is stable across runs; int hashing is not randomized — disagrees with the
input order).

Usage: python dedup_order_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "dedupe"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (order-blind)
    return set(fn([1, 2, 2, 3])) == {1, 2, 3}


def check_keeps_distinct(fn):
    got = fn([1, 2, 3])
    return ("keeps every distinct value", set(got) == {1, 2, 3} and len(got) == 3, f"got {got}")


def check_first_occurrence_order(fn):
    got = fn([3, 1, 2, 1, 3])
    return ("preserves first-occurrence order", got == [3, 1, 2], f"got {got}")


def check_order_two(fn):
    got = fn([5, 5, 4])
    return ("preserves order for [5, 5, 4] -> [5, 4]", got == [5, 4], f"got {got}")


CHECKS = [check_keeps_distinct, check_first_occurrence_order, check_order_two]

if __name__ == "__main__":
    main(FN, CHECKS)
