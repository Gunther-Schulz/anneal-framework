#!/usr/bin/env python3
"""Held-out oracle for the design-surface task `config-resolver`.

This is NOT a single-function silent-failure task (it is not in the frozen pack).
It is the design-surface probe: a from-stub build whose 8 held-out checks cover
inheritance, deep merge, chains, interpolation, and the error cases. The score is
the fraction of behaviours the built solution holds — the "design held" analog of
catch-rate.

The load-bearing checks are the interactions a naive incremental build tends to
corner on:
  C5 — a child override must retroactively change a parent's ${...} result
       (eager interpolation, the natural first cut, fails this);
  C7/C8 — cycles must raise ValueError, not hang or RecursionError (a build with
       no cycle bookkeeping fails these).

Usage: python config_resolver_oracle.py <run-dir>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _harness import main  # noqa: E402

FN = "resolve_config"


def WEAK_CHECK(fn):  # the prompt's advertised quick check
    return fn({"app": {"port": 8080}}, "app") == {"port": 8080}


def _expect_value_error(fn, configs, name, text):
    try:
        got = fn(configs, name)
        return (text, False, f"no raise; got {got!r}")
    except ValueError:
        return (text, True, "raised ValueError")
    except Exception as e:  # noqa: BLE001 — wrong exception type is a fail
        return (text, False, f"raised {type(e).__name__}, not ValueError")


def check_c1_trivial(fn):
    got = fn({"app": {"port": 8080}}, "app")
    return ("C1 trivial config (no extends/interp)", got == {"port": 8080}, f"got {got!r}")


def check_c2_extends_override(fn):
    configs = {"base": {"timeout": 30, "retries": 3},
               "svc": {"_extends": "base", "timeout": 99}}
    got = fn(configs, "svc")
    return ("C2 single extends + key override", got == {"timeout": 99, "retries": 3}, f"got {got!r}")


def check_c3_deep_merge(fn):
    configs = {"base": {"db": {"host": "h", "port": 5432}},
               "svc": {"_extends": "base", "db": {"port": 6000}}}
    got = fn(configs, "svc")
    return ("C3 nested dict deep-merge", got == {"db": {"host": "h", "port": 6000}}, f"got {got!r}")


def check_c4_chain_nearest_wins(fn):
    configs = {"a": {"x": 1},
               "b": {"_extends": "a", "x": 2, "y": 20},
               "c": {"_extends": "b", "y": 30}}
    got = fn(configs, "c")
    return ("C4 3-level chain, nearest wins", got == {"x": 2, "y": 30}, f"got {got!r}")


def check_c5_override_changes_interpolation(fn):
    configs = {"base": {"host": "default.com", "url": "https://${host}/api"},
               "prod": {"_extends": "base", "host": "prod.com"}}
    got = fn(configs, "prod")
    want = {"host": "prod.com", "url": "https://prod.com/api"}
    return ("C5 child override changes parent ${host} (merge-then-interpolate)",
            got == want, f"got {got!r}")


def check_c6_transitive_interpolation(fn):
    configs = {"c": {"a": "${b}", "b": "deep"}}
    got = fn(configs, "c")
    return ("C6 transitive interpolation ${a}->${b}", got == {"a": "deep", "b": "deep"}, f"got {got!r}")


def check_c7_extends_cycle(fn):
    return _expect_value_error(fn, {"a": {"_extends": "b"}, "b": {"_extends": "a"}}, "a",
                               "C7 _extends cycle raises ValueError")


def check_c8_interpolation_cycle(fn):
    return _expect_value_error(fn, {"c": {"a": "${b}", "b": "${a}"}}, "c",
                               "C8 interpolation cycle raises ValueError")


CHECKS = [
    check_c1_trivial,
    check_c2_extends_override,
    check_c3_deep_merge,
    check_c4_chain_nearest_wins,
    check_c5_override_changes_interpolation,
    check_c6_transitive_interpolation,
    check_c7_extends_cycle,
    check_c8_interpolation_cycle,
]

if __name__ == "__main__":
    main(FN, CHECKS)
