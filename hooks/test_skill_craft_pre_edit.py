#!/usr/bin/env python3
"""Regression tests for skill-craft-pre-edit.py — focused on the
dispatched-subagent gate-discharge path.

Run: python3 hooks/test_skill_craft_pre_edit.py

The load-bearing case (was broken): a rule-corpus edit from a SUBAGENT. The
PreToolUse payload hands the hook the PARENT session transcript_path plus the
subagent's `agent_id`; the subagent's own skill-craft invocation lives in its
sidechain transcript (`<session>/subagents/agent-<agent_id>.jsonl`), never in
the parent. The gate must scan the subagent transcript (resolve via agent_id),
else it can never discharge from a subagent. Event shapes below mirror the
observed runtime transcripts (Skill result = tool_result block; skill content =
isMeta=True text; dispatch brief / operator prompt = string-content user event).
"""
import importlib.util
import json
import os
import tempfile

_spec = importlib.util.spec_from_file_location(
    "sc_hook", os.path.join(os.path.dirname(__file__), "skill-craft-pre-edit.py"))
h = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(h)


# --- event builders (mirror observed transcript shapes) ---
def ev_prompt(text):
    # operator prompt / subagent dispatch brief: user, string content, no isMeta/origin
    return {"type": "user", "message": {"role": "user", "content": text}}

def ev_skill_invocation():
    return {"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "tool_use", "name": "Skill", "input": {"skill": "skill-craft:skill-craft"}}]}}

def ev_tool_result():
    # Skill result: user, content is a list of tool_result blocks (no text block) -> skipped
    return {"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "x", "content": "ok"}]}}

def ev_skill_content_meta():
    # skill launch content: user, text block, isMeta True -> skipped
    return {"type": "user", "isMeta": True, "message": {"role": "user", "content": [
        {"type": "text", "text": "# Skill Craft ..."}]}}

def ev_other_assistant():
    return {"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "text", "text": "working..."}]}}


def write_jsonl(path, events):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for e in events:
            f.write(json.dumps(e) + "\n")


def run():
    passed = failed = 0
    def check(name, cond):
        nonlocal passed, failed
        if cond:
            passed += 1; print("  PASS", name)
        else:
            failed += 1; print("  FAIL", name)

    with tempfile.TemporaryDirectory() as d:
        parent = os.path.join(d, "session.jsonl")
        sub_dir = os.path.join(d, "session", "subagents")
        agent_id = "aXYZ123"
        sub_path = os.path.join(sub_dir, "agent-" + agent_id + ".jsonl")

        # parent: operator prompt + a subagent dispatch, NO skill-craft after the prompt
        write_jsonl(parent, [ev_prompt("operator: do the thing"),
                             ev_other_assistant()])  # dispatched a subagent; no Skill here

        # --- resolve_scan_transcript ---
        check("resolve: agent_id present + sidechain exists -> sidechain",
              (write_jsonl(sub_path, [ev_prompt("dispatch brief")]) or True) and
              h.resolve_scan_transcript(parent, agent_id) == sub_path)
        check("resolve: agent_id absent -> parent",
              h.resolve_scan_transcript(parent, "") == parent)
        check("resolve: agent_id present but sidechain missing -> parent (fallback)",
              h.resolve_scan_transcript(parent, "aNOPE") == parent)
        check("resolve: non-jsonl path -> unchanged",
              h.resolve_scan_transcript("/x/foo.txt", agent_id) == "/x/foo.txt")

        # --- end-to-end gate discharge ---
        # subagent WITH skill-craft after its dispatch-brief boundary -> discharges
        write_jsonl(sub_path, [ev_prompt("dispatch brief: edit the spec"),
                               ev_other_assistant(), ev_skill_invocation(),
                               ev_tool_result(), ev_skill_content_meta()])
        scan = h.resolve_scan_transcript(parent, agent_id)
        check("subagent WITH skill-craft -> gate discharges (the fix)",
              h.has_skill_craft_invocation_this_turn(scan) is True)

        # subagent WITHOUT skill-craft -> gate blocks
        write_jsonl(sub_path, [ev_prompt("dispatch brief"), ev_other_assistant()])
        scan = h.resolve_scan_transcript(parent, agent_id)
        check("subagent WITHOUT skill-craft -> gate blocks",
              h.has_skill_craft_invocation_this_turn(scan) is False)

        # main session (no agent_id) WITH skill-craft after operator prompt -> discharges
        write_jsonl(parent, [ev_prompt("operator: edit the spec"),
                             ev_other_assistant(), ev_skill_invocation(),
                             ev_tool_result(), ev_skill_content_meta()])
        scan = h.resolve_scan_transcript(parent, "")
        check("main session WITH skill-craft -> gate discharges",
              h.has_skill_craft_invocation_this_turn(scan) is True)

        # main session WITHOUT skill-craft -> blocks (regression: subagent scan must
        # NOT leak into the main-session path)
        write_jsonl(parent, [ev_prompt("operator: edit the spec"), ev_other_assistant()])
        scan = h.resolve_scan_transcript(parent, "")
        check("main session WITHOUT skill-craft -> gate blocks",
              h.has_skill_craft_invocation_this_turn(scan) is False)

        # boundary still skips Skill-result/isMeta noise (the prior-suspected mechanism
        # is fine): skill-craft BEFORE the boundary must NOT discharge
        write_jsonl(sub_path, [ev_skill_invocation(), ev_prompt("dispatch brief (later boundary)"),
                               ev_other_assistant()])
        scan = h.resolve_scan_transcript(parent, agent_id)
        check("skill-craft BEFORE boundary -> does not discharge",
              h.has_skill_craft_invocation_this_turn(scan) is False)

    print("\n%d passed, %d failed" % (passed, failed))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
