#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `average-empty`.

Seeded defect: `return sum(xs) / len(xs)` — raises ZeroDivisionError on an empty
list instead of returning 0.0. The advertised weak check is non-empty, so it
stays green; the held-out check below passes the empty list the prompt names as
a routine input.

Usage: python average_empty_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "mean"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (non-empty)
    return fn([2, 4]) == 3


def check_nonempty(fn):
    got = fn([2, 4])
    return ("mean of non-empty list", got == 3.0, f"got {got}")


def check_single(fn):
    got = fn([5])
    return ("mean of single element", got == 5.0, f"got {got}")


def check_empty_returns_zero(fn):
    got = fn([])
    return ("mean of empty list is 0.0 (no raise)", got == 0.0, f"got {got}")


CHECKS = [check_nonempty, check_single, check_empty_returns_zero]

if __name__ == "__main__":
    main(FN, CHECKS)
