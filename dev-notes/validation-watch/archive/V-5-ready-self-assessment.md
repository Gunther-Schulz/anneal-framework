## V-5. [READY] self-assessment vs external check

**Status: RESOLVED (2026-05-28).** Load-bearing instance: unit-8
arb-strategy run (beat-the-books project), cycle 3 — the
convergence cycle's falsification pass caught 3 [VERIFIED]
D-entries with unsurfaced gaps (F21 — D1 missing 2 test files;
F22 — D5 missing SQL projection; F23 — D9 wrong file name +
wrong handling). All three would have escaped under the
pre-fix self-test-only protocol and surfaced as
implement-loopback or verify [ISSUES FOUND]; the convergence
cycle caught them at investigate-design.

**Origin: FIX-SHIPPED (2026-05-25, commit e18bca1).** The recurrence
the production-signal watched for was observed in the unit-14 run
(beat-the-books project): cycle 3 declared [READY], operator chose
Continue, cycle 4 surfaced material design corrections (F31-F36 +
D9/D10 amendments). The diagnosis (AI in the working context
answered the fresh-session test from the same recall pool that
wrote the design) confirmed self-assessment alone is insufficient.

**Resolution.** Two layered mitigations now in spec:

1. **§4.1.2 sharpened — per-implementer-step external evidence.**
   The fresh-session-implementability test artifact requires
   file:line citations from re-reading source per implementer
   step, not paraphrases of the tracker. Structural enforcement at
   the AI's self-test moment — forces re-reading (or fabrication,
   which is harder) to satisfy the PASSED artifact.

2. **§4.1.4 added — convergence cycle.** [READY] requires one more
   cycle after the AI's self-test passes, producing zero D-track
   deltas. A full cycle (investigation + standardized inspection
   passes) with enumerated new surfaces, not lens-clean re-attest.
   Catches what the self-test misses by switching the working
   context from self-assessment mode to fresh investigation mode.

**Alternative considered: V-5's original prescribed candidate —
operator-invoked subagent-at-[READY] external check.** Not chosen
because (a) the unit-14 failure shape was recall, not frame, and
the convergence cycle directly addresses recall via fresh
investigation; (b) the convergence cycle reuses existing cycle
machinery rather than adding a new mechanism; (c) operator's
empirical workflow already includes an extra cycle on every run —
the convergence cycle codifies this. The external subagent remains
the defined escalation candidate if **frame-lock failures** emerge
(cycles produce material findings but all reinforce a wrong frame
— a different failure shape that fresh investigation alone might
not catch). Frame-lock has not been observed yet; per practice 8,
the external subagent earns its place at n=1 if observed.

**Closing criterion (FIX-SHIPPED → RESOLVED).** A post-run review
identifies a run where the convergence cycle was load-bearing — it
surfaced a D-track delta that would have escaped under the
pre-fix self-test-only protocol. One observed instance is
sufficient.

**Original observation preserved below for audit trail.**

---

**Decision (`core.md` §4.1, v0.8.7 + v0.8.9).** The [READY] judgment
is sharpened — a presence-based fresh-session-implementability test
plus the named silent-substitution failure shape — but it remains
self-assessment. The producing AI judges whether a fresh session
could implement from the tracker alone. No external check (no
subagent) at [READY]; the operator's review at the closed-artifact
presentation is the only external catcher.

**Why uncertain.** The v0.8.0 lean rework removed the 0.7.0 isolated
[READY] evaluation (a per-cycle automatic subagent that
false-confirmed once and missed cross-decision contradictions). The
replacement is operator-review-at-presentation plus, in v0.8.7/0.8.9,
sharper self-assessment criteria. Whether the named self-assessment
reduces false-[READY]s enough — or whether an external check is
needed — is empirical. Cycle 3 of the Unit-5 run was a false-[READY]
the sharpening targets; the next runs under v0.8.9 are the first
real test. Adding a subagent-at-[READY] check before that evidence
would be the over-mechanization reflex this session repeatedly
reversed.

**Production signal to watch.** Whether false-[READY]s recur under
v0.8.9 — cycles declaring [READY] that subsequent cycles still
surface material design gaps for. If they recur, the candidate fix
is an *operator-invoked* subagent-at-[READY] external check —
structurally different from the 0.7.0 isolated eval: operator-invoked
(not automatic), whole-design (not per-decision), "what would
surface during implementation" simulation (not cached verdict),
output to the operator (not cached in the tracker). If false-[READY]s
do not recur, the named self-assessment is sufficient and no new
mechanism is warranted.

---

