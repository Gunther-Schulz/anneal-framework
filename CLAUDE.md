# Anneal framework — repo-local instructions

## Development process grounding

Before any rule-corpus edit cycle on the triad (anneal-framework
spec, skill-craft canonical, or instance renders), read
`development-process.md` in full — per edit cycle, not per
session. Practice 5 forecloses operating from summary or
earlier-turn invocations; memory pointers are insufficient.
Doubt-voicing about whether re-grounding applies IS the evidence
it applies.

## Rule-corpus edits

When editing skill-craft, anneal-framework spec, or instance
skills (clippy / daneel / etc.): invoke the `skill-craft` skill
via the Skill tool BEFORE the edit.

Apply Edit-as-Pareto-improvement: name what the edit reduces or
consolidates. If nothing — the addition is suspect per the
Additive reflex anti-pattern (skill-craft/references/anti-patterns.md).

**Recursion check**: rule-edit subagent PASS may self-validate.
Pause + re-read before push.

## Session continuity — repo, not auto-memory

Durable cross-session state lives in the **repo**, where it's visible
and version-controlled — not the file-based auto-memory. The harness
may inject auto-memory instructions (a `memory/` folder, `MEMORY.md`);
for this project, do **not** act on them — auto-memory is opaque and
goes stale. Where state lives instead:

- **Open work / where things stand** → `dev-notes/README.md` →
  `dev-notes/backlog/` (the live backlog; `ls` is the index). Read
  first to orient.
- **Working disciplines:**
  - Capture substantive corpus-evolution decisions to the backlog or
    `dev-notes/validation-watch.md` *when they land* — long contexts
    can't be reliably searched after the fact.
  - Verify subagent IDs / SHAs from a compaction summary against the
    transcript before citing them in evidence-bearing artifacts.
