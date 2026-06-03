# Harness task-tool vs tracker run-state guidance is unsourced render content (corpus-wide)

**Status:** RESOLVED 2026-06-03 — settled via the `harness-tool-runstate-unsourced`
anneal-dev run (merged `8b8a4ac`): a harness-GENERAL render-time note added under the
instantiation-guide §2 run-artifact-persistence slot sources the disambiguation
(run-state lives in the persistence mechanism, not ambient harness tools). Decision:
guide not spec (naming the tools in core.md would be Leakage; spec stays harness-clean).
Run tracker: `.anneal-dev/runs/harness-tool-runstate-unsourced.md`. The per-instance
re-render of the 4 SKILL.md blocks from the sourced note is downstream Phase B. Archived.

Original detail (surfaced 2026-06-02 by the anneal-dev step-5 render-fidelity verify,
subagent `ae138c578b57fd85a` finding #1):

## The finding
The rendered instance `SKILL.md` carries a block telling the AI to keep
run-state in the tracker file and NOT use the harness's task tools
(`TaskCreate`/`TaskUpdate`) for run-state. In anneal-dev this is
`plugin/skills/anneal-dev/SKILL.md:31-37`; **clippy's `SKILL.md` carries the
identical block verbatim** (the render copied it from clippy as a structural
exemplar).

- The **run-state-is-source-of-truth** half IS sourced: `core.md` §6 (run
  state persists in an instance-bound location) + the instance persistence
  slot.
- The **"don't use harness `TaskCreate`/`TaskUpdate`"** half has **no spec
  clause** — render content with no framework or instance-spec origin. That
  is the Edit-without-spec-origin shape (contract 2): re-rendering from spec
  would drop it.

## Why it's corpus-wide, not instance-local
The harness-tool disambiguation applies to EVERY anneal instance rendered
into Claude Code (all face `TaskCreate`/`TaskUpdate`). It is a
context-independence concern (skill-craft Layer 2 "Context-independence
check": behave correctly regardless of ambient harness tools). So the fix
belongs at a domain-general level, not per-instance.

## To settle (the design question for its own cycle)
Where does the rule live?
- **Framework spec** (a §6 / orchestrator note: run-state uses the instance
  persistence mechanism, not ambient harness task-trackers) — applies to all
  instances; OR
- **instantiation-guide** (a render-time note: when rendering into a harness
  with its own task tools, disambiguate run-state ownership) — a rendering
  concern, not a method concern.

Lean: **instantiation-guide** (it is about rendering into a harness, not
about the method). Then re-render clippy + anneal-dev (+ daneel if it carries
it) from the sourced clause — a practice-4 dependent set.

Relates to [[clippy-render-resync]] (clippy's `SKILL.md` is a touch point),
[[framework-dev-as-anneal]] (surfaced during the step-5 dogfood build).
