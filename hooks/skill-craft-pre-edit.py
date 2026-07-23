#!/usr/bin/env python3
"""
PreToolUse hook — gates Edit/Write/NotebookEdit on rule-corpus files
behind a per-turn transcript-verified skill-craft invocation.

Trigger: Edit, Write, NotebookEdit tool calls on rule-corpus files:
  - Plugin render paths (plugin/skills/<skill>/{SKILL,PROCEDURE}.md,
    references/*.md, phases/*.md)
  - Framework-spec paths (spec/*.md, development-process.md,
    post-run-review.md, instantiation-guide.md, foundation.md)

Action:
  - Scans the JSONL transcript from the last operator prompt (a
    user message with text content, NOT a tool_result message)
    forward, looking for a Skill tool_use invoking skill-craft.
  - If found in the current turn → allow (exit 0). For plugin
    renders (excluding skill-craft canonical), additionally inject
    spec-origin reminder via additionalContext.
  - If not found in the current turn → block (exit 2 with
    permissionDecision: deny). Forces AI to invoke skill-craft via
    Skill tool in this turn before proceeding.
  - Operator-CLAUDE.md paths additionally require a same-turn Read
    of CLAUDE-maintenance.md (composition rules live there, stack
    layer 3 — skill-craft is layer 2 and does not carry them).

Per anneal-framework development-process.md practice 5: skill-craft
invocation gates Edits to rule-corpus files. Per-turn enforcement
aligns the gate with operator-request boundaries — a new operator
message starts a new turn requiring fresh invocation. Mid-turn
cycle boundaries remain an AI-discipline goal (multiple scopes of
change within one operator response are not mechanically separated).

Housekeeping carve-out: files outside the rule-corpus patterns
(README.md, .gitignore, plugin.json version bumps) pass without
gating. Working-area carve-out: paths under non-corpus working
areas (dev-notes/) pass without gating even if they contain a
spec-shaped segment (e.g. a draft instance spec under
dev-notes/derivation-pass1/spec/) — dev-notes is "not the spec".
"""

import json
import os
import re
import sys

# Plugin render paths (instance plugin files — rendered from spec).
PLUGIN_RENDER_PATTERNS = [
    re.compile(r"/plugin/skills/[^/]+/(SKILL|PROCEDURE)\.md$"),
    re.compile(r"/plugin/skills/[^/]+/references/[^/]+\.md$"),
    re.compile(r"/plugin/skills/[^/]+/phases/[^/]+\.md$"),
]

# Framework-spec / dev-process paths (source files — canonical content).
SPEC_SOURCE_PATTERNS = [
    re.compile(r"/spec/.+\.md$"),
    re.compile(r"/development-process\.md$"),
    re.compile(r"/post-run-review\.md$"),
    re.compile(r"/instantiation-guide\.md$"),
    re.compile(r"/foundation\.md$"),
    # Operator's global instruction frame (dotfiles source + deployed
    # symlink) — rule-corpus by operator decision 2026-07-10; edits
    # follow claude/CLAUDE-maintenance.md via a skill-craft-vetted
    # process. CLAUDE-maintenance.md itself is maintenance doctrine
    # (ungated), matching the dev-notes carve-out rationale.
    re.compile(r"/dotfiles/claude/CLAUDE\.md$"),
    re.compile(r"/\.claude/CLAUDE\.md$"),
]

# Operator-CLAUDE.md paths additionally gate on a same-turn Read of
# CLAUDE-maintenance.md (operator decision 2026-07-23): its composition
# rules (provenance, density, render test) live in stack layer 3, which
# the skill-craft check (layer 2) does not carry. Only these two paths —
# the anneal spec paths carry their composition rules in the specs
# themselves.
CLAUDEMD_PATTERNS = [
    re.compile(r"/dotfiles/claude/CLAUDE\.md$"),
    re.compile(r"/\.claude/CLAUDE\.md$"),
]

# Non-corpus working areas — scratch/notes/draft copies that may contain
# spec-shaped paths but are NOT canonical rule-corpus (e.g. a draft instance
# spec under dev-notes/derivation-pass1/spec/). dev-notes is the repo's
# designated working-notes area (dev-notes/README.md: "not the spec").
# Checked before corpus classification so an excluded path never gates.
NON_CORPUS_PATTERNS = [
    re.compile(r"/dev-notes/"),
]

# Skill-craft canonical exemption — skill-craft is a meta-plugin where
# canonical files ARE the source (no upstream render). Spec-origin
# discipline doesn't apply.
SKILL_CRAFT_CANONICAL = re.compile(r"/skill-craft/plugin/skills/skill-craft/")

# Skill-craft invocation pattern — matches any Skill tool_use whose
# `skill` input includes "skill-craft" (covers "skill-craft:skill-craft",
# "plugin:skill-craft:skill-craft", and similar fully-qualified forms).
SKILL_CRAFT_INVOCATION = re.compile(r"skill-craft")

DENY_REASON = """skill-craft invocation required in the current turn
before Edit/Write to rule-corpus files. No Skill tool_use with
skill-craft was found in the transcript since the last operator
message.

To proceed:
  1. Invoke skill-craft via the Skill tool:
     Skill(skill="skill-craft:skill-craft")
  2. Retry this Edit/Write — the hook will scan again and allow.

Per anneal-framework development-process.md practice 5
(skill-craft invocation gates Edits to rule-corpus files;
per-turn enforcement at the transcript-scan layer). Invocations
in prior turns do NOT discharge the current turn's gate; each
operator message starts a fresh enforcement window."""

MAINTENANCE_DENY_REASON = """CLAUDE-maintenance.md Read required in the
current turn before editing the operator CLAUDE.md. The composition
rules (provenance, density, render test) live in the maintenance
doctrine — a read earlier in the session has gone inert at the edit
moment before (incident 2026-07-23).

To proceed:
  1. Read ~/.claude/CLAUDE-maintenance.md (the Read tool, this turn).
  2. Retry this Edit/Write — the hook will scan again and allow.

Each operator message starts a fresh enforcement window."""

SPEC_ORIGIN_REMINDER = """Spec-origin trace required for this plugin
render edit (per anneal-framework development-process.md practice 5
"Spec-origin grounding for plugin edits" + contract 2). Surface which
spec clause this edit originates from:
  → framework spec section (anneal-framework/spec/*.md), OR
  → instance spec slot (e.g., coding-clippy/spec/*.md), OR
  → `cosmetic-no-spec-origin` exemption with sources considered.

The citation IS the artifact; a plugin edit without a cited spec
origin is drift (Edit-without-spec-origin anti-pattern,
skill-craft references/anti-patterns.md)."""


def is_anneal_instance_render(file_path: str) -> bool:
    """A plugin render that belongs to an anneal INSTANCE — it renders from an
    instance spec living at its repo root (e.g. coding-clippy/spec/ ↔
    coding-clippy/plugin/skills/clippy/; anneal-dev/spec/ ↔ anneal-dev/plugin/).
    A standalone skill (a sibling-repo plugin like bildhauer) has plugin/ but
    NO sibling spec/, so the spec-origin reminder does not apply to it.

    Scopes the (informational) spec-origin reminder only — NOT the
    skill-craft-invocation gate, which stays broad (any skill edit should
    route through skill-craft). Finding 4: the reminder previously fired on
    every /plugin/skills/ path on disk, including non-anneal sibling skills.
    """
    if not any(p.search(file_path) for p in PLUGIN_RENDER_PATTERNS):
        return False
    repo_root = file_path.split("/plugin/skills/")[0]
    return os.path.isdir(os.path.join(repo_root, "spec"))


def _events_after_last_prompt(transcript_path: str):
    """Events after the last operator-prompt boundary, or None on the
    fail-open failure modes (callers treat None as "couldn't verify,
    so don't block"):

      1. Transcript file unreadable (OSError/IOError).
      2. No operator-prompt boundary found in events (empty
         events list, malformed JSONL with all lines unparseable,
         or all user events filtered as non-prompts — should not
         happen in normal operation)."""
    try:
        events = []
        with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except (OSError, IOError):
        # Transcript unreadable — fail-open. Defensive: should not
        # happen in normal operation.
        return None

    # Find index of last operator-prompt user message. Discriminators
    # observed in Claude Code transcripts:
    #   - isMeta=True user-role events carry Skill outputs and system
    #     notifications as text content under role=user. Skip them.
    #   - The `origin` field has changed meaning across transcript
    #     formats. Old format: real prompts carry NO origin; a non-empty
    #     origin (e.g. {'kind': 'task-notification'}) marks a non-prompt.
    #     Current format (observed 2026-07-23): real operator prompts
    #     carry origin={'kind': 'human'}. Blanket-skipping every truthy
    #     origin therefore found NO boundary in current transcripts and
    #     silently fail-opened the gate on every corpus edit. Rule:
    #     accept origin absent (old prompts) or kind=='human' (current
    #     prompts); skip any other origin kind.
    #   - Tool-result user events have content as a list with
    #     tool_result blocks (no text block). Skip them via the
    #     content-shape check below.
    last_prompt_idx = -1
    for i, event in enumerate(events):
        msg = event.get("message")
        if not isinstance(msg, dict):
            continue
        if msg.get("role") != "user":
            continue
        if event.get("isMeta") is True:
            continue
        origin = event.get("origin")
        if origin and not (isinstance(origin, dict) and origin.get("kind") == "human"):
            continue
        content = msg.get("content")
        if isinstance(content, str):
            last_prompt_idx = i
            continue
        if not isinstance(content, list):
            continue
        if any(
            isinstance(b, dict) and b.get("type") == "text"
            for b in content
        ):
            last_prompt_idx = i

    if last_prompt_idx == -1:
        # No user prompt found yet — degenerate case (very early in
        # session, before any prompt). Fail-open.
        return None

    return events[last_prompt_idx + 1:]


def _tool_uses_after_last_prompt(transcript_path: str):
    """(name, input) of every assistant tool_use after the boundary,
    or None on the fail-open modes of _events_after_last_prompt."""
    tail = _events_after_last_prompt(transcript_path)
    if tail is None:
        return None
    uses = []
    for event in tail:
        msg = event.get("message")
        if not isinstance(msg, dict):
            continue
        if msg.get("role") != "assistant":
            continue
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") != "tool_use":
                continue
            tool_input = block.get("input", {})
            uses.append((block.get("name"),
                         tool_input if isinstance(tool_input, dict) else {}))
    return uses


def has_skill_craft_invocation_this_turn(transcript_path: str) -> bool:
    """True if skill-craft was invoked via the Skill tool since the
    last operator prompt — or on the fail-open modes (couldn't
    verify, so don't block)."""
    uses = _tool_uses_after_last_prompt(transcript_path)
    if uses is None:
        return True
    return any(
        name == "Skill" and SKILL_CRAFT_INVOCATION.search(str(inp.get("skill", "")))
        for name, inp in uses
    )


def has_maintenance_read_this_turn(transcript_path: str) -> bool:
    """True if CLAUDE-maintenance.md was Read since the last operator
    prompt — or on the fail-open modes (couldn't verify, so don't
    block). Same per-turn window as the skill-craft check: the
    composition rules (provenance, density, render test) live in the
    maintenance doctrine, not in skill-craft, and a read 100K tokens
    ago has demonstrably gone inert at the edit moment — the re-anchor
    must sit at the decision, not somewhere in the session."""
    uses = _tool_uses_after_last_prompt(transcript_path)
    if uses is None:
        return True
    return any(
        name == "Read"
        and str(inp.get("file_path", "")).endswith("/CLAUDE-maintenance.md")
        for name, inp in uses
    )


def resolve_scan_transcript(transcript_path: str, agent_id: str) -> str:
    """Resolve which transcript the gate scans for the skill-craft invocation.

    For a tool call made from a **subagent**, the PreToolUse payload carries
    the PARENT session transcript_path AND the subagent's `agent_id` — but the
    subagent's own skill-craft invocation lives in its sidechain transcript
    (`<session>/subagents/agent-<agent_id>.jsonl`), never in the parent. The
    subagent IS the drafting context for its rule-corpus edit, so the gate must
    scan that transcript, not the parent (otherwise the gate can never discharge
    from a subagent — the dispatched-subagent block). Main-session edits carry no
    `agent_id` and keep scanning the parent. Falls back to the parent transcript
    if the sidechain file is absent (preserve the gate; never fail-open here)."""
    if not agent_id or not transcript_path.endswith(".jsonl"):
        return transcript_path
    sub_path = transcript_path[: -len(".jsonl")] + "/subagents/agent-" + agent_id + ".jsonl"
    return sub_path if os.path.exists(sub_path) else transcript_path


def deny(reason: str) -> None:
    """Emit deny payload and exit with code 2 (hard block)."""
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
        },
        "systemMessage": f"Blocked: {reason}",
    }
    sys.stderr.write(json.dumps(payload))
    sys.exit(2)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Invalid hook input — don't block, just exit.
        return 0

    tool_input = payload.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    transcript_path = payload.get("transcript_path", "")

    if not file_path:
        return 0

    if any(p.search(file_path) for p in NON_CORPUS_PATTERNS):
        # Working/scratch area (e.g. dev-notes/) — not canonical
        # rule-corpus even if the path contains a spec-shaped segment.
        return 0

    is_plugin_render = any(p.search(file_path) for p in PLUGIN_RENDER_PATTERNS)
    is_spec_source = any(p.search(file_path) for p in SPEC_SOURCE_PATTERNS)
    is_sc_canonical = bool(SKILL_CRAFT_CANONICAL.search(file_path))

    if not (is_plugin_render or is_spec_source):
        # Not a rule-corpus file — out of scope, allow.
        return 0

    # Rule-corpus file — gate on per-turn-verified skill-craft invocation.
    if not transcript_path:
        # No transcript path provided — fail-open (don't block).
        # Defensive: should not happen in normal operation.
        return 0

    # A subagent's own skill-craft invocation lives in its sidechain
    # transcript, not the parent the payload hands us — resolve to it via
    # agent_id so the gate scans the actual drafting context.
    scan_path = resolve_scan_transcript(transcript_path, payload.get("agent_id", ""))

    if not has_skill_craft_invocation_this_turn(scan_path):
        deny(DENY_REASON)
        # Unreachable; deny() exits.

    # Operator-CLAUDE.md: second condition — same-turn maintenance-doctrine
    # read (see CLAUDEMD_PATTERNS comment).
    if any(p.search(file_path) for p in CLAUDEMD_PATTERNS):
        if not has_maintenance_read_this_turn(scan_path):
            deny(MAINTENANCE_DENY_REASON)
            # Unreachable; deny() exits.

    # Skill-craft was invoked in the current turn. Allow, with an
    # informational spec-origin reminder for anneal-INSTANCE plugin renders
    # (sibling spec/ at the repo root). NOT for skill-craft canonical (IS
    # source, not render) and NOT for standalone non-anneal skills, which have
    # no anneal spec-origin to cite (Finding 4: the reminder over-matched
    # sibling-repo skills like bildhauer).
    if is_anneal_instance_render(file_path) and not is_sc_canonical:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": SPEC_ORIGIN_REMINDER,
            }
        }
        print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
