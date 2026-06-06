#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `round-half-up`.

Seeded defect: `return round(x)` — Python's built-in round is half-to-even
(banker's rounding), so round(2.5)==2 and round(0.5)==0, violating the required
half-up rule. The advertised weak check uses non-.5 values, so it stays green;
the held-out checks below hit the exact-.5 boundary where the rules diverge.

Usage: python round_half_up_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "round_money"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (non-.5 values)
    return fn(2.4) == 2 and fn(2.6) == 3


def check_rounds_down(fn):
    got = fn(2.4)
    return ("2.4 rounds to 2", got == 2, f"got {got}")


def check_rounds_up(fn):
    got = fn(2.6)
    return ("2.6 rounds to 3", got == 3, f"got {got}")


def check_half_up_2_5(fn):
    got = fn(2.5)
    return ("2.5 rounds up to 3 (half-up, not banker's)", got == 3, f"got {got}")


def check_half_up_0_5(fn):
    got = fn(0.5)
    return ("0.5 rounds up to 1 (half-up, not banker's)", got == 1, f"got {got}")


CHECKS = [check_rounds_down, check_rounds_up, check_half_up_2_5, check_half_up_0_5]

if __name__ == "__main__":
    main(FN, CHECKS)
