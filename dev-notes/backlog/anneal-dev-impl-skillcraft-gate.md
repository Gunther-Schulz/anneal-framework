# anneal-dev impl dispatch doesn't INVOKE skill-craft → pre-edit gate blocks dispatched rule-corpus edits

**Status:** OPEN — anneal-dev / gate-interaction finding. Filed 2026-06-04 as the real residual of
`skill-craft-pre-edit-hook-findings` Finding 3 (which was MOOT *as a hook bug* — the hook side is
correct; this is the dispatch side). Editing anneal-dev = corpus-evolution → routes through
anneal-dev + kernel-independent verify.

## The finding
The skill-craft pre-edit hook (`hooks/skill-craft-pre-edit.py`, development-process.md practice 5)
gates Edit/Write to rule-corpus files behind a skill-craft **invocation** (a `Skill` tool_use) in the
current turn. anneal-dev's impl dispatch briefs a subagent to **load** skill-craft references
(foundations / lenses) but does NOT **invoke** skill-craft via the Skill tool. So a dispatched
rule-corpus edit has no `Skill` tool_use in its (sidechain) transcript → the gate correctly denies
it. The subagent cannot discharge the gate.

Hook side is **correct** and not the bug: it now scans the subagent's own sidechain transcript via
`agent_id` (`skill-craft-hook-subagent-dispatch-block`, archived/DONE). The gap is purely on the
**anneal-dev dispatch side** — it loads but doesn't invoke.

## Consequence / current workarounds
Subagent-dispatched rule-corpus edits — including the framework's own impl-phase dispatch
(`core.md` §4.2) — can't satisfy the gate. Today, two workarounds, neither the intended discipline:
- **spawn-fallback** — orchestrator edits in main context, where a turn-level skill-craft invocation
  discharges the gate; or
- accept the **Bash-bypass** (`skill-craft-pre-edit-hook-findings` F2, accepted-known-limitation)
  under the release-loop-step-4 backstop (separate-context verify). The step-5 render did this.

## Fix shape (own anneal-dev cycle)
Reconcile anneal-dev's impl dispatch with the gate: the dispatched subagent should **invoke**
skill-craft via the Skill tool before its rule-corpus edits (not merely load the references), so the
gate discharges in-subagent — or a sanctioned, explicit dispatch path. Decide within anneal-dev
(corpus-evolution machinery) + kernel-independent verify.

## Relates to
- `skill-craft-pre-edit-hook-findings` (archived — this is its reframed Finding-3 residual).
- anneal-dev impl phase (`core.md` §4.2 dispatch) — the mechanism this interacts with.
