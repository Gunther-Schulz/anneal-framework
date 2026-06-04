#!/usr/bin/env python3
"""
PreToolUse hook — gates Edit/Write/NotebookEdit on the anneal method-kernel /
dev-process SOURCE files behind an ACTIVE anneal-dev run.

Trigger: Edit/Write/NotebookEdit on the kernel/corpus-evolution source files:
  - spec/*.md (anneal-framework/spec/* AND anneal-dev/spec/*)
  - foundation.md, development-process.md, post-run-review.md,
    instantiation-guide.md

Why this and not the skill-craft pre-edit hook: skill-craft-pre-edit gates the
SAME files behind a skill-craft *invocation* (the authoring discipline). This
hook is the second, complementary gate — it enforces the *process* discipline
(CLAUDE.md "Development process grounding": method-kernel / corpus-evolution
edits run through anneal-dev: investigate-design -> implement -> verify). The
commit-msg discharge hook enforces this at COMMIT; this enforces it at EDIT
(fail-fast — block the ad-hoc kernel edit before effort is sunk).

Action:
  - Walk up from the edited file to the nearest `.anneal-dev/` directory.
  - If a bypass sentinel `.anneal-dev/allow-adhoc-kernel-edit` exists -> allow
    (the deliberate-ad-hoc escape, like `git commit --no-verify`).
  - Else if any tracker in `.anneal-dev/runs/*.md` has Status: IN-PROGRESS
    (an anneal-dev run is active — the implement phase edits the kernel under
    exactly this state) -> allow.
  - Else -> block (exit 2, permissionDecision deny) with how-to-proceed.

This is a fail-fast REMINDER, not a guarantee: it cannot stop a determined
fabrication, and the operator + the commit-msg discharge gate remain the real
backstops. It exists so an ad-hoc "just fix one line" in the kernel is caught
at the edit, not discovered at commit.

Carve-outs (allow without gating): dev-notes/ (the repo's working-notes area,
"not the spec") and .anneal-dev/ (gitignored run state — the tracker the AI
edits throughout a run is not the spec).

Fail-open: any error, or no `.anneal-dev/` found up-tree, returns 0 (don't
block) — defensive; the gate must never wedge legitimate work on an unexpected
state. The realistic state (this repo, after any run) always has `.anneal-dev/`.

Bypass (deliberate ad-hoc edit) — TIME-BOUNDED so it can't linger:
  touch <repo>/.anneal-dev/allow-adhoc-kernel-edit
It is valid 15 min, then auto-expires AND is removed (self-heal), so a forgotten
sentinel re-enables the gate on its own. Every edit it allows surfaces a
reminder (additionalContext), so the bypass is never silent.
"""

import json
import os
import re
import sys
import time

# Kernel / dev-process SOURCE files (canonical rule-text the spec work edits).
# Mirrors skill-craft-pre-edit's SPEC_SOURCE_PATTERNS; /spec/.+\.md$ also
# covers anneal-dev/spec/*.
KERNEL_PATTERNS = [
    re.compile(r"/spec/.+\.md$"),
    re.compile(r"/foundation\.md$"),
    re.compile(r"/development-process\.md$"),
    re.compile(r"/post-run-review\.md$"),
    re.compile(r"/instantiation-guide\.md$"),
]

# Non-corpus working areas — allowed without gating even if the path contains a
# spec-shaped segment (e.g. a draft spec under dev-notes/) or is run state.
NON_CORPUS_PATTERNS = [
    re.compile(r"/dev-notes/"),
    re.compile(r"/\.anneal-dev/"),
]

BYPASS_SENTINEL = "allow-adhoc-kernel-edit"
# The bypass is TIME-BOUNDED: valid only this many seconds after the sentinel's
# mtime. Past that it's treated as absent AND removed (self-heal) — a forgotten
# sentinel cannot silently disable the gate forever (the very failure structural
# enforcement exists to prevent). `touch` again to renew.
BYPASS_TTL_SECONDS = 900  # 15 minutes

DENY_REASON = """anneal-dev run required before editing the method-kernel.

Edit/Write to a kernel / dev-process source file ({file}) with no active
anneal-dev run. Per CLAUDE.md (Development process grounding), method-kernel and
corpus-evolution edits run through anneal-dev: investigate-design -> implement ->
verify. No tracker in .anneal-dev/runs/ has Status: IN-PROGRESS.

To proceed:
  1. Invoke the anneal-dev skill and reach the IMPLEMENT phase (the run's
     tracker carries Status: IN-PROGRESS), then retry — the gate will allow the
     dispatched edit. This is the intended path; it also gives you verify + the
     kernel-independent review before anything ships.
  OR
  2. Deliberate ad-hoc edit — create the bypass sentinel and retry:
       touch {anneal_dev}/allow-adhoc-kernel-edit
     Time-bounded (15 min) and auto-removed on expiry, so it cannot silently
     disable the gate; each edit it allows surfaces a reminder."""


def find_anneal_dev_dir(file_path):
    """Walk up from the edited file's directory to the nearest ancestor holding
    a `.anneal-dev/` directory. Returns its path, or None if none found.

    Robust to where run-state lives vs. where the file lives: an edit to
    anneal-dev/spec/* still resolves to the OUTER repo's .anneal-dev/ (the repo
    the run was invoked from), because the walk continues past anneal-dev/."""
    d = os.path.dirname(os.path.abspath(file_path))
    while True:
        candidate = os.path.join(d, ".anneal-dev")
        if os.path.isdir(candidate):
            return candidate
        parent = os.path.dirname(d)
        if parent == d:  # filesystem root
            return None
        d = parent


def has_in_progress_run(anneal_dev_dir):
    """True if any tracker in `<anneal_dev_dir>/runs/*.md` carries an
    `IN-PROGRESS` Status header. Only the main trackers have a Status header;
    the per-cycle / impl-plan artifacts do not, so scanning all *.md is safe."""
    runs = os.path.join(anneal_dev_dir, "runs")
    if not os.path.isdir(runs):
        return False
    status_re = re.compile(r"Status:?\*{0,2}\s*IN-PROGRESS")
    for name in os.listdir(runs):
        if not name.endswith(".md"):
            continue
        try:
            with open(os.path.join(runs, name), "r", encoding="utf-8") as fh:
                head = "".join(fh.readline() for _ in range(8))
        except OSError:
            continue
        if status_re.search(head):
            return True
    return False


def deny(reason):
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
        },
        "systemMessage": f"Blocked: {reason}",
    }
    sys.stderr.write(json.dumps(payload))
    sys.exit(2)


def check_bypass(anneal_dev_dir):
    """Time-bounded bypass. Returns 0 (allow — and prints a visible reminder) if
    a FRESH sentinel exists; None (fall through to the run-check) otherwise. An
    EXPIRED sentinel is removed (self-heal) so it can't linger and silently
    disable the gate."""
    sentinel = os.path.join(anneal_dev_dir, BYPASS_SENTINEL)
    try:
        age = time.time() - os.path.getmtime(sentinel)
    except OSError:
        return None  # absent / unreadable — not bypassed
    if age > BYPASS_TTL_SECONDS:
        try:
            os.remove(sentinel)  # expired — self-heal, then gate normally
        except OSError:
            pass
        return None
    remaining = max(1, int((BYPASS_TTL_SECONDS - age) // 60))
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": (
                f"anneal-dev-run gate BYPASSED via {sentinel} (~{remaining} min "
                f"left). This kernel edit is AD-HOC — NOT under an anneal-dev "
                f"run. Remove the sentinel when done."
            ),
        }
    }))
    return 0


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # invalid input — don't block

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not file_path:
        return 0

    if any(p.search(file_path) for p in NON_CORPUS_PATTERNS):
        return 0  # dev-notes / run state — not the kernel
    if not any(p.search(file_path) for p in KERNEL_PATTERNS):
        return 0  # not a kernel source file — out of scope

    anneal_dev = find_anneal_dev_dir(file_path)
    if anneal_dev is None:
        return 0  # no .anneal-dev/ up-tree — fail-open (defensive)

    bypass = check_bypass(anneal_dev)
    if bypass is not None:
        return bypass  # fresh sentinel — allowed (with a surfaced reminder)

    if has_in_progress_run(anneal_dev):
        return 0  # an anneal-dev run is active

    deny(DENY_REASON.format(file=file_path, anneal_dev=anneal_dev))
    return 0  # unreachable; deny() exits


if __name__ == "__main__":
    sys.exit(main())
