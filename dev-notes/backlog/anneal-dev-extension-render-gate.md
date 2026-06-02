# anneal-dev render-and-open-diff extension — gated rule-corpus write path

**Status:** OPEN — filed 2026-06-02 by the `impl-skillcraft-gate` anneal-dev run (cycle-3 convergence, F7 [VERIFIED — deferred]). Same family as [[anneal-dev-impl-skillcraft-gate]] but a SEPARATE lifecycle path (post-verify, not impl).

The `render-and-open-diff` lifecycle extension (`anneal-dev/spec/extensions.md`; fires on-verify-PASSED) re-renders affected plugin skill files (`plugin/skills/*/*.md`) into the working tree for the operator's diff review. Writing plugin skill files is a rule-corpus edit → it hits the framework pre-edit gate (`skill-craft-pre-edit.py`) the same way the impl dispatch does. But it is a post-verify **bookend**, outside the impl phase, so the impl-dispatch fix ([[anneal-dev-impl-skillcraft-gate]]) does not cover it.

**Open question (decide before enabling render-and-open-diff in any project):** does a *render* write — a mechanical re-render of already-`[PASSED]`-verified spec — even warrant the skill-craft gate? The relevant discipline for a render is **render-fidelity** (already verified at `[PASSED]`), not skill-craft's *authoring* disciplines. So either (a) the extension's render context invokes skill-craft before its writes (gate satisfied), or (b) the render path is a legitimate gate exemption (mechanical re-render, not authoring) — which would be a `skill-craft-pre-edit.py` carve-out, relating to [[skill-craft-pre-edit-hook-findings]].

Relates to [[anneal-dev-impl-skillcraft-gate]], [[skill-craft-pre-edit-hook-findings]], [[dev-process-adoption]].
