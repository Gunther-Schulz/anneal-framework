## V-8. Dispatch self-check at the impl-phase subagent boundary

**Status: WATCHING.**

**Kind: correctness-watch.** The catcher under watch is the dispatch-boundary self-check (`core.md` §4.2.5) — closes on an instance where it caught a post-design reference or behavior slipping the locked enumeration that would otherwise have reached verify.

**Decision (`core.md` §4.2 "Self-check at dispatch boundary").**
Each dispatched subagent applies the instance's standardized lenses
against its own diff before returning state. The check compounds with
the design-time forcing function (§3.2) as the implement-time catcher
for references introduced post-design and behaviors slipping the
locked enumeration.

**Why uncertain.** Lever B selected from the impl-phase
lens-application discussion (alongside lever A: catch at orchestrator
post-merge; lever C: defer to verify). Rests on judgment that
per-unit self-check produces a useful signal that compounds with
design-time and verify-time checks rather than duplicating them.
Originally appended as a stowaway addendum inside V-6
(decomposition + topology) — split out at audit time per practice 8
entry hygiene.

**Production signal to watch.** (a) whether the self-check catches
what would otherwise have reached verify in subsequent runs;
(b) per-dispatch overhead remaining acceptable; (c) subagent findings
well-shaped as ledger lines (no free-text drift); (d) **superseded
by V-24** — the loopback-vs-in-scope-concern classification this
signal monitored no longer exists; the always-loopback rule
eliminates the classification surface (see V-24).

---

