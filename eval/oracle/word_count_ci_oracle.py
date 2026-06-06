#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `word-count-ci`.

Seeded defect: `Counter(text.split()).most_common(1)[0][0]` — counts
case-sensitively and returns the original casing, so "The"/"the"/"THE" are
counted as distinct words. The advertised weak check is all-lowercase, so it
stays green; the held-out checks below mix casing so that the case-insensitive
winner differs from any case-sensitive count.

Usage: python word_count_ci_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "most_common_word"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (single case)
    return fn("a a b") == "a"


def check_single_case(fn):
    got = fn("a a b")
    return ("plain single-case input", got == "a", f"got {got!r}")


def check_combines_casings(fn):
    got = fn("The the THE cat")
    return ("combines casings: the=3 beats cat=1", got == "the", f"got {got!r}")


def check_lowercase_winner(fn):
    got = fn("Dog dog cat")
    return ("returns lowercase winner (dog=2)", got == "dog", f"got {got!r}")


CHECKS = [check_single_case, check_combines_casings, check_lowercase_winner]

if __name__ == "__main__":
    main(FN, CHECKS)
