# anneal-dev packaging — register + install so "run anneal-dev" is invocable

**Status:** OPEN — filed 2026-06-02 by [[dev-process-adoption]]. Mechanical Layer-1
plugin work (skill-craft `references/plugin-engineering.md`), not a corpus edit.

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
