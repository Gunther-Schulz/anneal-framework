#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `sort-tiebreak`.

Seeded defect: `sorted(players, key=lambda p: -p[1])` — orders by score only.
Python's sort is stable, so tied scores keep input order instead of the required
name-ascending tiebreak. The advertised weak check has no ties, so it stays
green; the held-out checks below feed tied scores whose input order differs from
alphabetical order.

Usage: python sort_tiebreak_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "rank"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (no ties)
    return fn([("a", 3), ("b", 1)]) == ["a", "b"]


def check_score_order(fn):
    got = fn([("a", 3), ("b", 1)])
    return ("orders by score, highest first", got == ["a", "b"], f"got {got}")


def check_tiebreak_by_name(fn):
    got = fn([("bob", 5), ("alice", 5), ("carol", 9)])
    return ("ties break by name ascending", got == ["carol", "alice", "bob"], f"got {got}")


def check_tiebreak_against_input_order(fn):
    got = fn([("y", 1), ("x", 1)])
    return ("tiebreak independent of input order", got == ["x", "y"], f"got {got}")


CHECKS = [check_score_order, check_tiebreak_by_name, check_tiebreak_against_input_order]

if __name__ == "__main__":
    main(FN, CHECKS)
