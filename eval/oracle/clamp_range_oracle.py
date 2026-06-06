#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `clamp-range`.

Seeded defect: `return max(x, 0)` — floors at 0 but never caps at 100. The
advertised weak check is an in-range value, so it stays green; the held-out
checks below probe both bounds, including the upper cap the defect omits.

Usage: python clamp_range_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "clamp_score"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (in range)
    return fn(50) == 50


def check_in_range(fn):
    got = fn(50)
    return ("in-range value unchanged", got == 50, f"got {got}")


def check_floor(fn):
    got = fn(-5)
    return ("below 0 floored to 0", got == 0, f"got {got}")


def check_cap(fn):
    got = fn(150)
    return ("above 100 capped to 100", got == 100, f"got {got}")


CHECKS = [check_in_range, check_floor, check_cap]

if __name__ == "__main__":
    main(FN, CHECKS)
