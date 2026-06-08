# FB-1. Surface non-task observations (work/codebase) — no channel for what the agent notices outside the task

**Status:** open finding — needs a practice-9 design surface. Operator-raised 2026-06-01 (Notes 2 + 5, merged).

**▶ Consolidation (session 14):** originally two sub-shapes; **(b) protocol-tensions moved to
`self-review-missed-side`** (it's a Q3 framework-gap feeder — see `self-improvement-signal-architecture`).
**This item now holds (a) — work/codebase observations only.**

**Gap.** Homes exist for *task-scoped* findings (always-loopback / defer) and *protocol* critique (the
missed-side self-review). But **work/codebase** things the agent notices *outside the task's locked design* —
bugs, inconsistencies, architecture shortcomings, notables seen during investigation + implementation,
unrelated to the task — have no structured home; they get dropped or silently resolved. The framework's ethos
is "surface, don't silently decide"; this extends it to non-task work-observations.

- **Consumer:** the **operator** (awareness / future work) — *not* the framework maintainer (that's the
  protocol-tension half (b), now in the self-review cluster). The split is by consumer: work-observation →
  operator; protocol-tension → maintainer/dev-time.
- **Design Q:** where it surfaces (a closed-artifact side-channel? the post-run review? a separate
  observations log?) and how to keep it from becoming noise — a **signal threshold** (not every passing
  thought). The threshold is the hard part: too low → noise; too high → the point (catching real notables) is
  lost.

## Relates to
- `self-improvement-signal-architecture` / `self-review-missed-side` — absorbed this item's **(b)**
  protocol-tension half (a Q3 feeder); **(a)** (this) stays separate: different subject (work-product vs
  protocol) and consumer (operator vs maintainer).
- the always-loopback / defer task-finding homes — the existing channels this complements.
- Origin: operator, 2026-06-01 (Notes 2 + 5).
