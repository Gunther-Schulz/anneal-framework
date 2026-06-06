#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `migrate-idempotent`.

Seeded defect: `return "/api/" + path` — prepends unconditionally, so re-running
the migration on an already-prefixed path yields "/api//api/...". The advertised
weak check only passes an unprefixed path, so it stays green; the held-out checks
below apply the function to already-prefixed input and twice in a row.

Usage: python migrate_idempotent_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "ensure_prefix"


def WEAK_CHECK(fn):  # the prompt's advertised quick check (unprefixed input)
    return fn("users") == "/api/users"


def check_adds_when_missing(fn):
    got = fn("users")
    return ("adds prefix when missing", got == "/api/users", f"got {got!r}")


def check_idempotent_on_prefixed(fn):
    got = fn("/api/users")
    return ("leaves an already-prefixed path unchanged", got == "/api/users", f"got {got!r}")


def check_idempotent_under_reapply(fn):
    got = fn(fn("x"))
    return ("re-applying does not double-prefix", got == "/api/x", f"got {got!r}")


CHECKS = [check_adds_when_missing, check_idempotent_on_prefixed, check_idempotent_under_reapply]

if __name__ == "__main__":
    main(FN, CHECKS)
