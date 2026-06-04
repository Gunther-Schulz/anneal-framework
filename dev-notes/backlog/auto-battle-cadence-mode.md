# Auto-battle cadence: an "auto-advance-until-next-phase" cadence (+ default-mode question)

**Status:** OPEN — framework mode-mechanics idea, operator-raised 2026-06-04. **Not for now** (filed
per no-silent-deferral). Framework-spec (`foundations.md`/`core.md` Modes + `SKILL.md` Modes) →
anneal-dev + kernel-independent verify when pursued.

## The idea
Today there are **two modes** (`core.md`/`foundations.md` Modes): **interactive** (operator selects
`(a)nother-cycle` / `(n)ext-phase` at *every* cycle's closed artifact) and **auto-battle** (loop
self-advances all the way to [READY] with no operator). The operator wants a **middle cadence**:
auto-advance the *cycle loop* (no per-cycle `(a)/(n)` menu) but **stop at the phase-transition `(n)`** —
i.e. the operator is asked only at `[READY]` (and other genuine phase gates), not every cycle.

## The tension (the real design problem — don't just bolt on a 3rd mode)
A third *named* mode = **3 modes** (interactive + two auto-battle variants), which the operator judges
**too many**. The design work is a **unifying** solution, not a third mode. Candidates to weigh:
- **(a) one "auto-advance" axis with a `stop-at` parameter** (`per-cycle` / `per-phase` / `never`) —
  a single mode, parameterized; interactive = `stop-at: per-cycle`, full auto-battle = `stop-at: never`,
  the requested cadence = `stop-at: per-phase`.
- **(b) interactive gains a "run-until-(n)" affordance** at the menu (operator says "advance until
  ready"; cycles self-run meanwhile).
- **(c) auto-battle gains a `stop-at-[READY]` toggle.**
(a) looks cleanest — collapses 3 apparent modes into one parameterized axis. Resolve as part of the cycle.

## Parked sub-idea
**Full auto-battle as the default** (vs interactive-by-default today). Operator-flagged, explicitly
*"not to discuss now"* — parked here so it's not lost. Couples to the unifying solution above (if mode
becomes a `stop-at` parameter, "default" = the default parameter value).

## Relates to
- `core.md`/`foundations.md` Modes + `SKILL.md` Modes (the two-mode definition this revises) — method-kernel.
- Mode-mechanics were a flagged coherence-audit deep-sweep target (`clippy-run-findings-dispatch-coupling` tail).
