# anneal-dev packaging — register + install so "run anneal-dev" is invocable

**Status:** **DONE 2026-06-02 — installed; pending operator `/reload-plugins` to
activate** in the running session. Filed by [[dev-process-adoption]]; mechanical
Layer-1 work (skill-craft `references/plugin-engineering.md`).

**Shipped:** added `anneal-dev/.claude-plugin/marketplace.json` (marketplace
`anneal-dev`) + filled `plugin/.claude-plugin/plugin.json` (was a name-only stub);
committed + pushed (`f90ddb8`); `claude plugin marketplace add Gunther-Schulz/anneal-dev`
+ `claude plugin install anneal-dev@anneal-dev` → pinned `anneal-dev@anneal-dev` 0.1.0
in `installed_plugins.json`. Operator runs `/reload-plugins` to make the skill
invocable by name this session.

The adoption re-points dev work to "run anneal-dev," but anneal-dev is
**followed-in-context, not installed** — it isn't in a marketplace, so the Skill
tool can't invoke it by name. Until packaged, "run anneal-dev" means reading its
`SKILL.md` in-context (what the step-5 dogfood and this adoption cycle did).

**To do:** add anneal-dev to a marketplace (marketplace.json) + register + install
(`claude plugin install … && /reload-plugins`), so a session can invoke the skill by
name. Sequence with the next time dev work actually runs through anneal-dev.

Relates to [[framework-dev-as-anneal]], [[dev-process-adoption]],
[[skill-craft-pre-edit-hook-findings]] (the hook ↔ subagent-dispatch seam surfaces
for real once anneal-dev's dispatch runs installed).
