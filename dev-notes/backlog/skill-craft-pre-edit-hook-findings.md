# skill-craft-pre-edit hook — over-broad path match + bypassable + subagent-reliability

**Status:** Finding 1 **DONE** (2026-06-01); Findings 2 + 3 open. Surfaced
2026-06-01 by the anneal-dev pass-1 subagent (which tripped the gate writing
draft spec files and routed around it). The path-narrowing (Finding 1) is done,
so the de-pollution cycles' `spec/*.md` edits gate correctly without
false-positives on `dev-notes/` drafts. The hook change is committed (ad29c27).
Relates to `framework-dev-as-anneal.md`, `contract1-depollution-cluster.md`.

The hook is `hooks/skill-craft-pre-edit.py` (development-process.md practice 5:
gates Edit/Write to rule-corpus files behind an in-turn skill-craft invocation).

## Three findings (ranked)

1. **Over-broad path pattern — DONE (2026-06-01).** The gate matched
   `/spec/.+\.md$`, which caught `dev-notes/derivation-pass1/spec/` — a scratch
   draft, not canonical rule-corpus. Fixed by adding a `NON_CORPUS_PATTERNS`
   exclusion (`/dev-notes/`) checked before corpus classification, so an
   excluded path never gates. Verified: `dev-notes/**/spec/` now passes; canonical
   `anneal-framework/spec/`, instance `coding-clippy/spec/`, and plugin renders
   still gate. Kept minimal — `dev-notes/` is the one concrete non-corpus area
   (its README says "not the spec"); no speculative scratch-dir list (practice 7).
2. **`mv`/`cp` bypass hole (note).** The gate is a PreToolUse hook on Write/Edit;
   it does not gate Bash file moves, so writing to a non-matching path and
   `mv`-ing into place circumvents it (which the pass-1 subagent did). Fully
   closing this is not cheap (can't gate all Bash without heavy friction) —
   record as a known limitation; the real backstop stays release-loop step 4
   (post-edit skill-craft review) + operator approval.
3. **Subagent-context reliability (investigate before relying on it).** The
   subagent reported two same-turn skill-craft invocations did not clear the
   gate — either the transcript scan doesn't register a subagent's Skill
   `tool_use`, or a flush-timing race. Confirm the gate behaves correctly when
   the editor is a subagent, before the de-pollution cycles lean on it.
