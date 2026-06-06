#!/usr/bin/env python3
"""Pre-freeze well-formedness gate for the silent-failure task pack.

For every task in the frozen pack, verify the rubric's 3-way check
(`dev-notes/backlog/measurement-harness-mve.md`):

  (a) the advertised WEAK check passes on the seeded-defect starter
      (`tasks/<slug>/solution.py` — the file shipped to the agent);
  (b) the held-out oracle scores < 1.0 on that defect (the defect is catchable);
  (c) a reference correct fix (`oracle/fixtures/<slug>_fixed.py` — gate-only,
      never shown to an arm) passes the WEAK check AND scores exactly 1.0 on the
      held-out oracle (the oracle is neither blind nor over-strict).

No agent, no arms, no network — pure mechanical conformance. Run before freezing
the pack; a non-PASS row means the task is not in-regime and must not ship.

(`discount-floor` is intentionally excluded: it is the Step-0 null that failed
rubric criterion 4 — requirement-trivia, not requirement-space-gated.)

Usage: python eval/wellformedness.py
"""
import contextlib
import importlib
import io
import sys
import tempfile
from pathlib import Path

EVAL = Path(__file__).resolve().parent
ORACLE = EVAL / "oracle"
FIXTURES = ORACLE / "fixtures"
TASKS_DIR = EVAL / "tasks"
sys.path.insert(0, str(ORACLE))

import _harness  # noqa: E402

# The frozen pack: (task slug, oracle module, fixture filename).
TASKS = [
    ("merge-config", "merge_config_oracle", "merge_config_fixed.py"),
    ("dedup-order", "dedup_order_oracle", "dedup_order_fixed.py"),
    ("sort-tiebreak", "sort_tiebreak_oracle", "sort_tiebreak_fixed.py"),
    ("csv-escape", "csv_escape_oracle", "csv_escape_fixed.py"),
    ("migrate-idempotent", "migrate_idempotent_oracle", "migrate_idempotent_fixed.py"),
    ("word-count-ci", "word_count_ci_oracle", "word_count_ci_fixed.py"),
    ("average-empty", "average_empty_oracle", "average_empty_fixed.py"),
    ("clamp-range", "clamp_range_oracle", "clamp_range_fixed.py"),
    ("round-half-up", "round_half_up_oracle", "round_half_up_fixed.py"),
    ("pagination-last-page", "pagination_last_page_oracle", "pagination_last_page_fixed.py"),
]


def _stage(solution_path: Path) -> Path:
    """Copy a solution into a temp run-dir laid out as the oracle expects."""
    d = Path(tempfile.mkdtemp(prefix="wf_"))
    (d / "outputs").mkdir()
    (d / "outputs" / "solution.py").write_text(solution_path.read_text())
    return d


def _pass_rate(run_dir: Path, fn_name: str, checks) -> float:
    with contextlib.redirect_stdout(io.StringIO()):  # silence per-run grade() line
        grading = _harness.grade(run_dir, fn_name, checks)
    return grading["summary"]["pass_rate"]


def gate_one(slug, oracle_mod, fixture):
    mod = importlib.import_module(oracle_mod)
    fn_name, weak, checks = mod.FN, mod.WEAK_CHECK, mod.CHECKS

    defect_dir = _stage(TASKS_DIR / slug / "solution.py")
    fix_dir = _stage(FIXTURES / fixture)
    defect_fn = _harness.load_fn(defect_dir / "outputs" / "solution.py", fn_name)
    fix_fn = _harness.load_fn(fix_dir / "outputs" / "solution.py", fn_name)

    a_weak_green = bool(weak(defect_fn))
    b_defect_rate = _pass_rate(defect_dir, fn_name, checks)
    c_fix_weak = bool(weak(fix_fn))
    c_fix_rate = _pass_rate(fix_dir, fn_name, checks)

    ok = a_weak_green and (b_defect_rate < 1.0) and c_fix_weak and (c_fix_rate == 1.0)
    return ok, a_weak_green, b_defect_rate, c_fix_weak, c_fix_rate


def main():
    rows = [(slug,) + gate_one(slug, mod, fix) for slug, mod, fix in TASKS]
    all_ok = all(r[1] for r in rows)

    print()
    print(f"{'task':22} {'GATE':5} {'(a)weak✓':9} {'(b)defect<1':12} {'(c)fix✓':8} {'(c)fix==1':9}")
    print("-" * 70)
    for slug, ok, a, b, cw, c in rows:
        print(f"{slug:22} {'PASS' if ok else 'FAIL':5} {str(a):9} {b:<12} {str(cw):8} {c:<9}")
    print("-" * 70)
    print("ALL TASKS WELL-FORMED" if all_ok else "*** SOME TASKS FAILED THE GATE ***")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
