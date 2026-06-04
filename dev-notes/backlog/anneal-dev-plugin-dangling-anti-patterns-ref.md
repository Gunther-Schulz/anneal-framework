# anneal-dev plugin tracker.md cites a dangling `references/anti-patterns.md`

**Status:** OPEN — pre-existing render defect, surfaced 2026-06-04 by the
`anneal-dev-reinstantiation` verify pass (F16). Low-severity; not introduced by
that run (present at `d9033ee`, outside its source-delta).

## The issue

`anneal-dev/plugin/skills/anneal-dev/references/tracker.md` (currently L345)
cites `references/anti-patterns.md` ("Naked-judgment") — but the plugin's own
`references/` dir has no `anti-patterns.md` (only `foundations.md`, `lenses.md`,
`post-run-review.md`, `tracker.md`). The intended referent is **skill-craft's**
`references/anti-patterns.md`, so the bare `references/…` form is dangling: it
resolves against the plugin's references, not skill-craft's.

The malformed-annotation rule it renders (`modules.md` §3.1 — naked-judgment /
common-word-qualifier) is faithful; only the **citation path** is wrong.

## Fix (when next touched)

Qualify the citation as skill-craft's (e.g. `skill-craft`'s
`references/anti-patterns.md`, matching how the plugin cites other cross-plugin
sources), OR drop the cross-plugin pointer and state the rule self-contained.
Confirm the framework source (`spec/modules.md` §3.1 Persistence) cites it
correctly first, then re-point the render.

## Relates to
- The `anneal-dev-reinstantiation` run (verify F16; archived run tracker).
- A render-convention point (cite-glossary / cross-plugin citation discipline) —
  candidate to fold into a coherence-audit sweep rather than its own run.
