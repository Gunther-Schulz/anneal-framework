#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `merge-config`.

Seeded defect: `base.update(override); return base` — mutates `base` and returns
an alias of it. The advertised weak check (`merged_config({"a":1},{"b":2}) ==
{"a":1,"b":2}`) passes regardless; the held-out checks below catch the broken
purity requirement the prompt states in prose but the weak check never exercises.
Silent-failure regime: one happy-path call looks correct; the defect only
surfaces when the shared `base` is reused.

Usage: python merge_config_oracle.py <run-dir>   # run-dir = .../arm_X/run-K
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "merged_config"


def WEAK_CHECK(fn):  # the prompt's advertised quick check
    return fn({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def check_result_correct(fn):
    got = fn({"a": 1}, {"b": 2})
    return ("result == base + override keys", got == {"a": 1, "b": 2}, f"got {got}")


def check_override_wins(fn):
    got = fn({"a": 1}, {"a": 2})
    return ("override wins on key conflict", got == {"a": 2}, f"got {got}")


def check_base_not_mutated(fn):
    base = {"a": 1}
    fn(base, {"b": 2})
    return ("base left unmodified after merge", base == {"a": 1}, f"base is now {base}")


def check_no_cross_call_contamination(fn):
    base = {"k": 0}
    fn(base, {"x": 1})           # first merge
    second = fn(base, {"y": 2})  # second merge from the SAME base
    return ("second merge does not see first merge's keys", "x" not in second,
            f"second merge = {second}")


CHECKS = [
    check_result_correct,
    check_override_wins,
    check_base_not_mutated,
    check_no_cross_call_contamination,
]

if __name__ == "__main__":
    main(FN, CHECKS)
