# Anneal framework — repo-local instructions

## Development process grounding

Before any rule-corpus edit cycle on the triad (anneal-framework
spec, skill-craft canonical, or instance renders), re-ground in the
governing process — per edit cycle, not per session, and never from
summary or earlier-turn invocations (practice 5; memory pointers are
insufficient):

- **Corpus-evolution work** (instance / skill-craft / dev-process
  machinery edits — anneal-dev renders from none of these) runs through
  **anneal-dev**: invoke it; it loads its own foundations and lenses.
- **Method-kernel edits** (the edited file is in anneal-dev's
  render/foundation source: `anneal-framework/spec/*`, `foundation.md`,
  `anneal-dev/spec/*`) — these run through anneal-dev too; the one rule
  they add is the verify, which **must** include a review grounded
  outside the anneal kernel — the skill-craft self-review (form) + the
  operator (soundness; skill-craft checks skill-quality, not
  methodology-correctness) — because anneal-dev never self-certifies its
  own foundation. Read `development-process.md` for that discipline +
  the shared release machinery.

Doubt-voicing about whether re-grounding applies IS the evidence
it applies.

**New instantiation** (a brand-new instance, e.g. anneal-marketing) is
not one of the above edit cycles: it starts with the **pre-channel
derivation** — author the instance spec *with the operator*
(`instantiation-guide.md`; `README.md` "Building a new instance"),
*then* anneal-dev builds it. anneal-dev evolves an existing corpus; it
does not author a spec from a blank domain — do not start by invoking
it.

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
  - **No silent deferral — file, don't defer.** When work won't be done
    now (a follow-up, a "future cycle", a parked idea, a "we should also…"),
    file it as a backlog item in `dev-notes/backlog/`, never a vague
    "defer"/"later". The backlog folder is the index; a deferral that isn't
    an item is invisible. Prefer over-capturing a small item to dropping it.
    (Distinct from the framework's practice-8 anti-deferral, which is about
    shipping *classifiable fixes* now; this is about making *any* not-now
    work an explicit tracked item.)
  - Verify subagent IDs / SHAs from a compaction summary against the
    transcript before citing them in evidence-bearing artifacts.
