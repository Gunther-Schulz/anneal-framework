#!/usr/bin/env python3
"""Shared grading harness for the held-out seeded-defect oracles.

Every task oracle is the same shape: import a run's edited
`<run-dir>/outputs/solution.py`, call a list of deterministic held-out checks,
and write a schema-correct `grading.json` (`summary.pass_rate` = fraction
passed). This module holds that shared machinery so each `<task>_oracle.py` is
just three module-level names:

  FN          — the function name the task defines (e.g. "merged_config").
  WEAK_CHECK  — fn(callable) -> bool : the quick check the PROMPT advertises.
                Exposed (not just prose) so the pre-freeze well-formedness gate
                (`eval/wellformedness.py`) can run it mechanically.
  CHECKS      — list[ fn(callable) -> (text, passed, evidence) ] : the held-out
                comprehensive checks the agent never sees.

Blind by construction: no LLM, no arm-awareness, no network — just calls the
code. Each check must build FRESH inputs so a buggy fn's mutation can't leak
between checks.

Run as a script (the scoring path):  python <task>_oracle.py <run-dir>
"""
import importlib.util
import json
import sys
from pathlib import Path


def load_fn(sol_path: Path, fn_name: str):
    spec = importlib.util.spec_from_file_location("sol", sol_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, fn_name)


def grade(run_dir, fn_name: str, checks) -> dict:
    """Score `<run-dir>/outputs/solution.py`, write grading.json, return it."""
    run_dir = Path(run_dir)
    sol = run_dir / "outputs" / "solution.py"
    expectations = []
    try:
        fn = load_fn(sol, fn_name)
        for check in checks:
            try:
                text, passed, evidence = check(fn)
            except Exception as e:  # noqa: BLE001 — any runtime failure is a fail
                text, passed, evidence = check.__name__, False, f"raised {type(e).__name__}: {e}"
            expectations.append({"text": text, "passed": bool(passed), "evidence": evidence})
    except Exception as e:  # noqa: BLE001 — import/def failure
        expectations = [{
            "text": f"solution.py imports and defines {fn_name}",
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
    (run_dir / "grading.json").write_text(json.dumps(grading, indent=2))
    print(f"{run_dir.parent.name}/{run_dir.name}: "
          f"pass_rate={grading['summary']['pass_rate']} ({passed}/{total})")
    return grading


def main(fn_name: str, checks):
    grade(sys.argv[1], fn_name, checks)
