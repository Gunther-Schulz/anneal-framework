#!/usr/bin/env python3
"""Held-out seeded-defect oracle for task `merge-config`.

Imports a run's edited `outputs/solution.py` and runs the held-out comprehensive
checks the agent never saw, writing a schema-correct `grading.json`
(`summary.pass_rate` = fraction passed). Blind by construction: no LLM, no
arm-awareness, no network — just calls the code.

The seeded defect is `base.update(override); return base` — it mutates `base`
and returns an alias of it. The weak check (`merged_config({"a":1},{"b":2}) ==
{"a":1,"b":2}`) passes regardless; the held-out checks below catch the broken
purity requirement that the prompt states in prose but the weak check never
exercises. This is the silent-failure regime: a single happy-path call looks
correct; the defect only surfaces when the same `base` is reused.

Each check builds FRESH inputs so the buggy fn's mutation cannot leak between
checks.

Usage: python merge_config_oracle.py <run-dir>   # run-dir = .../arm_X/run-K
"""
import importlib.util
import json
import sys
from pathlib import Path


def load_fn(sol_path: Path):
    spec = importlib.util.spec_from_file_location("sol", sol_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.merged_config


def check_result_correct(fn):
    got = fn({"a": 1}, {"b": 2})
    ok = got == {"a": 1, "b": 2}
    return ("result == base + override keys", ok, f"got {got}")


def check_override_wins(fn):
    got = fn({"a": 1}, {"a": 2})
    ok = got == {"a": 2}
    return ("override wins on key conflict", ok, f"got {got}")


def check_base_not_mutated(fn):
    base = {"a": 1}
    fn(base, {"b": 2})
    ok = base == {"a": 1}
    return ("base left unmodified after merge", ok, f"base is now {base}")


def check_no_cross_call_contamination(fn):
    base = {"k": 0}
    fn(base, {"x": 1})           # first merge
    second = fn(base, {"y": 2})  # second merge from the SAME base
    ok = "x" not in second
    return ("second merge does not see first merge's keys", ok,
            f"second merge = {second}")


CHECKS = [
    check_result_correct,
    check_override_wins,
    check_base_not_mutated,
    check_no_cross_call_contamination,
]


def main():
    run_dir = Path(sys.argv[1])
    sol = run_dir / "outputs" / "solution.py"
    expectations = []
    try:
        fn = load_fn(sol)
        for check in CHECKS:
            try:
                text, passed, evidence = check(fn)
            except Exception as e:  # noqa: BLE001 — any runtime failure is a fail
                text, passed, evidence = check.__name__, False, f"raised {type(e).__name__}: {e}"
            expectations.append({"text": text, "passed": bool(passed), "evidence": evidence})
    except Exception as e:  # noqa: BLE001 — import/def failure
        expectations = [{
            "text": "solution.py imports and defines merged_config",
            "passed": False,
            "evidence": f"{type(e).__name__}: {e}",
        }]

    passed = sum(1 for e in expectations if e["passed"])
    total = len(expectations)
    grading = {
        "expectations": expectations,
        "summary": {
            "passed": passed,
            "failed": total - passed,
            "total": total,
            "pass_rate": round(passed / total, 4) if total else 0.0,
        },
    }
    out = run_dir / "grading.json"
    out.write_text(json.dumps(grading, indent=2))
    print(f"{run_dir.parent.name}/{run_dir.name}: "
          f"pass_rate={grading['summary']['pass_rate']} ({passed}/{total}) -> {out}")


if __name__ == "__main__":
    main()
