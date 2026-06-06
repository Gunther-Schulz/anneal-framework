#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `pagination-last-page`.

Seeded defect: `return total_items // page_size` — floor division drops the
partial final page. The advertised weak check is evenly divisible, so it stays
green; the held-out checks below use non-divisible counts that need a trailing
partial page.

Usage: python pagination_last_page_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "num_pages"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (evenly divisible)
    return fn(20, 10) == 2


def check_exact(fn):
    got = fn(20, 10)
    return ("evenly divisible: 20/10 -> 2", got == 2, f"got {got}")


def check_partial_last_page(fn):
    got = fn(25, 10)
    return ("partial last page counts: 25/10 -> 3", got == 3, f"got {got}")


def check_single_item(fn):
    got = fn(1, 10)
    return ("one item needs one page", got == 1, f"got {got}")


def check_zero(fn):
    got = fn(0, 10)
    return ("zero items -> 0 pages", got == 0, f"got {got}")


CHECKS = [check_exact, check_partial_last_page, check_single_item, check_zero]

if __name__ == "__main__":
    main(FN, CHECKS)
