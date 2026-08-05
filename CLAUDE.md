# Anneal framework — repo-local instructions

## Development process grounding

Before any rule-corpus edit cycle on the triad (anneal-framework
spec, skill-craft canonical, or instance renders), re-ground in the
governing process — per edit cycle, not per session, and never from
summary or earlier-turn invocations (practice 5; memory pointers are
insufficient):

- **Corpus-evolution work** (instance / skill-craft / dev-process
  machinery edits) runs the **direct path** — the release loop in
  `development-process.md` ("One channel": spec-first inline, one
  consolidated vet per release commit). The **anneal-dev run** is the
  explicit-routing exception (below-grade orchestrator, or the
  operator routes a full adversarial run).
- **Method-kernel edits** (the edited file is in anneal-dev's
  render/foundation source: `anneal-framework/spec/*`, `foundation.md`,
  `anneal-dev/spec/*`) — in EITHER path the one rule
  they add is the verify, which **must** include a review grounded
  outside the anneal kernel — the skill-craft self-review (form) + the
  operator (soundness; skill-craft checks skill-quality, not
  methodology-correctness) — because anneal-dev never self-certifies its
  own foundation. The foundation-invariant register check
  (`dev-notes/foundation-invariants/`) produces the focusing artifact that
  aims the operator's soundness pass (which invariants touched, which
  anchors to satisfy) — it focuses, never replaces it. Read
  `development-process.md` for that discipline + the shared release
  machinery.

Doubt-voicing about whether re-grounding applies IS the evidence
it applies.

**Self-hosting: the live spec governs, the loaded plugin is a build
artifact.** This repo is the one place anneal-dev operates on its *own*
source — and that source (`spec/*`, `anneal-dev/spec/*`, `foundation.md`)
is **co-located** with the work. The installed anneal-dev plugin is a
**build artifact** of that source and may lag it (renders batch as
hygiene, not per-edit).
So when anneal-dev runs *here*, ground the method in the **live
co-located spec**, not the loaded plugin's rendered `foundations`/`phases`;
where they diverge, the live spec governs. (Asymmetry: a *downstream*
project using anneal-dev has only the rendered plugin — the spec isn't
shipped with it — so there the plugin **is** the source of truth and
normal instance-staleness applies. The rule is self-hosting-only, which
is why it lives in this always-fresh, never-rendered `CLAUDE.md` rather
than in the plugin or the kernel.)

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

- **Open work / where things stand** → root `BACKLOG.md` — the ONE
  live queue (two grades, parked/ready, per the global file-role
  convention). The former homes `dev-notes/backlog/` and
  `dev-notes/validation-watch/` were ARCHIVED WHOLESALE 2026-08-05
  (operator backlog-clear GO; superseded by the direct-path release
  loop) — their `archive/` dirs are historical record; nothing new
  lands there, and re-mints come from fresh incident evidence only,
  never by resurrecting an archived file.
- **Working disciplines:**
  - **No silent deferral — file, don't defer.** Work not done now (a
    follow-up, a parked idea, a "we should also…") becomes an entry
    in root `BACKLOG.md` — ready (decision-complete) or parked (with
    its named missing evidence or trigger) — never a vague
    "defer"/"later" in chat. Post-ship effect-watches (the former
    V-entry role) are parked entries carrying their closing rule.
    Prefer over-capturing a small entry to dropping it.
  - Verify subagent IDs / SHAs from a compaction summary against the
    transcript before citing them in evidence-bearing artifacts.
