# Framework backlog — open findings & deferred efforts

Single index so the backlog isn't scattered across dev-notes. Open
**findings** (surfaced, not yet a cycle) carry their full text here;
**efforts** (already designed / in-flight) are one-line pointers to the
doc that holds the detail. Add when a framework finding is surfaced;
mark done / remove when it ships. Memory-indexed
([[project-framework-backlog]]) so it auto-loads.

---

## Open findings (need a practice-9 design surface)

### FB-1. Surface non-task observations — no channel for what the agent notices outside the task

**Gap.** Homes exist for *task-scoped* findings (always-loopback /
defer) and *protocol* critique (post-run review). Things the agent
encounters **outside the task's locked design** have no structured home
— they get dropped or silently resolved. The framework's own ethos is
"surface, don't silently decide"; this extends it to non-task
observations. One gap, two sub-shapes (different subject + consumer):

- **(a) Work / codebase observations** — bugs, inconsistencies,
  architecture shortcomings, notables noticed *during investigation +
  implementation*, unrelated to the task's design. Consumer: the
  **operator** (awareness / future work). Design Q: where it surfaces
  (a closed-artifact side-channel? post-run review?) and how to keep it
  from becoming noise (a signal threshold — not every passing thought).

- **(b) Protocol tensions / conflicts** — two protocol rules pulling
  different ways, encountered at runtime. **Seed:** single-unit impl in
  the working context vs a configured `impl: sonnet` — the agent
  silently picked working-context instead of surfacing the clash; the
  operator had to poke it. Consumer: the **framework maintainer** (feeds
  dev-time resolution — sharpening / coherence-audit).
  - **Key insight:** an *interaction* conflict (two rules that don't
    textually contradict — they only clash in a specific runtime
    situation) is **structurally invisible to a dev-time text review** —
    the protocol-level twin of Cycle 3's static-blind-to-behavioral-
    coupling. Runtime is the only place it reliably surfaces (the
    situation is *real*, not simulated). So **runtime-surface →
    dev-time-resolve**, not either/or; the dev-time-only version is
    largely the coherence-audit we already have.
  - **Hard part:** runtime *detection* is judgment-heavy — no clean
    mechanical trigger for "this is a conflict," so it risks being a
    naked-judgment discipline. Tractable hardening: flag *known*
    interaction-points with a runtime surface (e.g. the model-selector
    binding says "if I won't apply here, surface why") — but those tend
    to get *resolved* instead of flagged.

**Unifying design:** likely a single "surfaced-observations" output
channel with a type tag (work-observation / protocol-tension) routing to
the right consumer. Operator-raised 2026-06-01 (Notes 2 + 5, merged).

### FB-2. Verify checks the locked design, not the original task requirements

A requirement dropped at investigate-design escapes — verify checks
work-vs-locked-design + lenses + executable verification, none of which
re-derive against the *original ask* (e.g. "data integrity" for the btb
instance). Design fork: a per-task **requirements artifact** verify
checks against, **and/or** recurring-requirement **lenses** (a
data-integrity lens). Detail + steelman: `planner-instance-exploration.md`
finding 5. Memory: [[project-verify-requirements-coverage-gap]].

### FB-3. Instance specs cite framework section-numbers, not glossary terms

Brittle coupling to framework layout; the glossary should be the
instance-facing interface (term = the trace). Detail:
`planner-instance-exploration.md` finding 4. (Sibling of the slot-collapse
fork; both informed by the planner derivation.)

---

## Deferred / in-flight efforts (detail elsewhere)

- **Contract-1 de-pollution cluster** (3 cycles: §4.2 → §5.2b → §4.1.4)
  → `contract1-depollution-cluster.md` ([[project-contract1-depollution-cluster]]).
- **Cycle 2.5 — bindings.md slot-collapse** → deferred to the planner
  derivation (over-split-vs-drift fork) → `clippy-run-findings-dispatch-coupling.md`
  + `planner-instance-exploration.md` finding 3.
- **Coherence-audit deep-sweep** (§4.4 / §5.1 / mode mechanics not yet
  swept) → `clippy-run-findings-dispatch-coupling.md` (coherence-audit section).
- **Planner instance build** (pre-build; validates whether the
  de-pollution abstractions actually render into a non-code instance)
  → `planner-instance-exploration.md` ([[project-planner-instance-effort]]).
