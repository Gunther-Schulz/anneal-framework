#!/usr/bin/env python3
"""Step-0 deterministic seeded-defect oracle for task `discount-floor`.

Imports a run's edited `outputs/solution.py`, runs the held-out comprehensive
cases the agent never saw, and writes a schema-correct `grading.json`
(`summary.pass_rate` = fraction of held-out cases passed). Blind by
construction: no LLM, no arm-awareness, no network — just runs the code.

The seeded defect in the starter is floor division (`//`), which silently
truncates the fractional part. The weak check (discount_price(100, 10) == 90)
passes regardless; the held-out cases below catch the truncation.

Usage: python score.py <run-dir>   # run-dir = .../arm_X/run-K
"""
import importlib.util
import json
import sys
from pathlib import Path

# Held-out comprehensive oracle (hidden from the agent): exact percentage.
HELDOUT = [(99, 10, 89.1), (50, 15, 42.5), (100, 10, 90.0)]
TOL = 1e-6


def load_fn(sol_path: Path):
    spec = importlib.util.spec_from_file_location("sol", sol_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.discount_price


def main():
    run_dir = Path(sys.argv[1])
    sol = run_dir / "outputs" / "solution.py"
    expectations = []
    try:
        fn = load_fn(sol)
        for price, pct, want in HELDOUT:
            try:
                got = fn(price, pct)
                passed = abs(got - want) < TOL
                evidence = f"got {got}, want {want}"
            except Exception as e:  # noqa: BLE001 — any runtime failure is a fail
                got, passed, evidence = None, False, f"raised {type(e).__name__}: {e}"
            expectations.append({
                "text": f"discount_price({price}, {pct}) == {want}",
                "passed": bool(passed),
                "evidence": evidence,
            })
    except Exception as e:  # noqa: BLE001 — import/def failure
        expectations = [{
            "text": "solution.py imports and defines discount_price",
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
