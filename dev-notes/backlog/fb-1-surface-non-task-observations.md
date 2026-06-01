# FB-1. Surface non-task observations — no channel for what the agent notices outside the task

**Status:** open finding — needs a practice-9 design surface. Operator-raised 2026-06-01 (Notes 2 + 5, merged).

**Gap.** Homes exist for *task-scoped* findings (always-loopback /
defer) and *protocol* critique (post-run review). Things the agent
encounters **outside the task's locked design** have no structured home
— they get dropped or silently resolved. The framework's own ethos is
"surface, don't silently decide"; this extends it to non-task
observations. One gap, two sub-shapes (different subject + consumer):

## (a) Work / codebase observations
Bugs, inconsistencies, architecture shortcomings, notables noticed
*during investigation + implementation*, unrelated to the task's design.
Consumer: the **operator** (awareness / future work). Design Q: where it
surfaces (a closed-artifact side-channel? post-run review?) and how to
keep it from becoming noise (a signal threshold — not every passing
thought).

## (b) Protocol tensions / conflicts
Two protocol rules pulling different ways, encountered at runtime.
**Seed:** single-unit impl in the working context vs a configured
`impl: sonnet` — the agent silently picked working-context instead of
surfacing the clash; the operator had to poke it. Consumer: the
**framework maintainer** (feeds dev-time resolution — sharpening /
coherence-audit).

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
the right consumer.
