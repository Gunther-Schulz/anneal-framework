# skill-craft pre-edit hook blocks subagent-dispatched spec edits

**Status:** **DONE 2026-06-02** — fixed in `hooks/skill-craft-pre-edit.py`
(+ regression test `hooks/test_skill_craft_pre_edit.py`); end-to-end verified (a
diagnostic subagent that got 5/5 denials now lands a gated edit). Surfaced as
F10 during the `framework-spec-cleanup-pipeline` run (the §4 re-derivation); that
run continued via spawn-fallback. **The originally-recorded root cause (the
isMeta boundary-detection hypothesis) was WRONG — empirically corrected below.**
Machinery fix (NOT rule-corpus → not skill-craft-gated).

## The actual root cause (empirically captured — corrects the first guess)

The hook gates `Edit`/`Write` to `spec/*` by scanning a transcript for an
in-turn skill-craft `Skill` `tool_use`. For a **subagent** edit it denied 5/5
(subagent `af60f2dc239967b6b`).

The first diagnosis — the Unit-1 subagent's, echoed in `pre-edit-hook-findings`
Finding 3 — blamed the `isMeta` boundary detection (a Skill-*result* `user` event
without `isMeta=True` being mis-read as a prompt boundary). **That was a
plausible-but-wrong inference from reading the hook code without the runtime
payload.** Empirical capture (temporary in-hook logging of the actual PreToolUse
payload + a controlled diagnostic subagent) showed the truth:

- The PreToolUse payload hands the hook the **PARENT session `transcript_path`**
  (`.../<session>.jsonl`), **not** the subagent's own transcript — plus the
  subagent's **`agent_id`** (the payload carries `agent_id` + `agent_type`).
- The subagent's skill-craft invocation lives in its **sidechain** transcript
  (`.../<session>/subagents/agent-<agent_id>.jsonl`), which the hook never read.
  So the scan of the parent (whose last boundary is the operator prompt, with no
  skill-craft after it) returns False → deny. **The gate could never discharge
  from a subagent**, regardless of isMeta.
- The boundary/isMeta logic is FINE: running the real function against the
  subagent's *own* transcript returns True (boundary = the dispatch brief at idx
  0; Skill result is a `tool_result` block, skipped; skill content is `isMeta=True`,
  skipped). No flush-lag either — the subagent's invocation is on disk at
  hook-time (the Skill tool-result round-trip flushes it).

## The fix (shipped)

`resolve_scan_transcript(transcript_path, agent_id)`: when `agent_id` is present
(a subagent edit), scan `.../<session>/subagents/agent-<agent_id>.jsonl` (the
subagent's drafting context) instead of the parent; main-session edits (no
`agent_id`) keep scanning the parent; fall back to the parent if the sidechain
file is absent (never fail-open). Precise (targets the exact active subagent via
`agent_id` — no over-broad "scan all subagents"). Regression test covers:
subagent-with/without skill-craft, main-with/without, fallback, and
skill-craft-before-boundary (9 cases, all pass).

## Impact

anneal-dev's **subagent-dispatch impl model is blocked for every `spec/*`
(method-kernel) edit** — not just one unit. Until fixed, method-kernel impl must
use the **spawn-fallback** (orchestrator implements in-context), which waives the
impl-isolation guarantee (backstopped by the isolated verify + the kernel-
independent review). Corpus-evolution edits to `plugin/skills/*/` from a subagent
hit the same gate and the same block.

## Contradiction with the archived item — RESOLVED

The archived `archive/anneal-dev-impl-skillcraft-gate.md` concluded **"the gate
IS satisfiable from a subagent."** Now resolved: that conclusion was **wrong, on a
flawed test**. The prior "RE-GROUNDED → MOOT" check (`pre-edit-hook-findings`
Finding 3) ran the `has_skill_craft_invocation_this_turn` *function* against a
subagent transcript **by hand** and got True — but the **hook is never handed the
subagent transcript**; the PreToolUse payload passes the *parent* transcript. So
the function-in-isolation worked while the live hook always denied. Lesson: test
the hook via its actual payload (what `transcript_path` it receives), not the
inner function against a hand-picked file. No harness regression — the gate was
never subagent-satisfiable until this fix. (`ee9e2e6`'s method-kernel edits
landed via the main-session/spawn path, where the gate works.)

## Relates to
- `skill-craft-pre-edit-hook-findings.md` — same hook (Findings 1 done / 2 Bash-bypass / 4 spec-origin over-match open); this is a distinct failure mode (subagent-path false-block, not gating-scope).
- `archive/anneal-dev-impl-skillcraft-gate.md` — the contradicted "gate IS satisfiable from a subagent" conclusion.
- `framework-spec-cleanup.md` — the run that surfaced this (its impl is proceeding via spawn-fallback).
