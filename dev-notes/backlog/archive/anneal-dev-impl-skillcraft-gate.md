# anneal-dev impl dispatch must invoke skill-craft for gated edits

**Status:** **DONE 2026-06-02** — shipped via the **first method-kernel
self-hosting anneal-dev run** (anneal-dev `ee9e2e6`, verify [PASSED] isolated; 4
investigate-design cycles — the convergence falsification caught the author's
cycle-1 under-scoping: a missed 3rd render + the spawn-fallback edit path, both
fixed). The run's own implement phase exercised the gap (spawn-fallback), and its
output is the fix that ends it. Filed 2026-06-02 by the re-grounding of
[[skill-craft-pre-edit-hook-findings]] Finding 3. A **method-kernel edit** (touches
`anneal-dev/spec/*` — the impl-phase dispatch brief), so it runs through anneal-dev
(drive) + a kernel-independent verify (skill-craft + operator), per
[[dev-process-adoption]]'s refined bootstrap rule.

The pre-edit gate (`hooks/skill-craft-pre-edit.py`) fires on rule-corpus Edits inside
subagent contexts and is satisfied by a Skill `tool_use` invoking skill-craft *in that
subagent's turn* (empirically confirmed working this session — Finding 3 re-grounding).
anneal-dev's impl phase dispatches each unit's edit to a subagent briefed to load
`references/{foundations,tracker}.md` + `phases/implement.md` — but **not** to invoke
the skill-craft Skill tool. So a dispatched rule-corpus edit carries no Skill `tool_use`
→ the gate blocks it (correctly), forcing the spawn-fallback (main-context edit).

**Fix shape:** anneal-dev's impl dispatch brief (`anneal-dev/spec` → the
`phases/implement.md` render) instructs the dispatched subagent to **invoke skill-craft
via the Skill tool before any rule-corpus edit**. This both satisfies the gate AND
activates the skill-craft disciplines at the edit moment (complementary to the
verify-time skill-quality battery check, not redundant with it). Open sub-question:
gate-invoke unconditionally, or only when the unit's scope includes rule-corpus paths.

Relates to [[skill-craft-pre-edit-hook-findings]] (Findings 2 Bash-bypass + 4 over-match
still open), [[framework-dev-as-anneal]], [[dev-process-adoption]].
