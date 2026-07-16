# Intent-falsification artifact — cycle 7 (fresh dispatch adeed464515fcf2a3, model fable-5 = actor; no declared ordering → equal-ceiling-under-assumed-ordering, F11-class, header-stamped)

Criteria-first: C1-C7 derived from verbatim + R1-R6 before design read. Faithfulness leg: clean.
Per-R# lines: R1 finding · R2 served · R3 finding · R4 finding · R5 served · R6 finding.

Per-finding lines (full verbatim in subagent return):
1. D2 mirrors only 2 of 3 legs of the structural-bind pattern it cites: §3.3 dispatch-brief
   carriage (the leg that lets the SUBAGENT stamp the header producer-independently) is outside
   D2's target set; no D-entry targets §3.3 — R1/R6 — mechanical-falsification-candidate on D2:
   {shape: target-dependents, candidate: rg -n 'dispatch-brief' spec/core.md spec/modules.md,
   predicate: any-outside-scope:core.md §4.1.4 + modules.md §3.4.1 + glossary.md,
   result: modules.md:351 (§3.4→§3.3 (c)), core.md:500, core.md:534}
   ORCHESTRATOR-COMPUTED: modules.md:351/§3.3 outside D2's enumerated targets → FALSIFIED →
   D2 [INVALIDATED]→[PENDING]. INTENT-DELTA THIS CYCLE.
2. D3's boundary value "equal-ceiling-under-assumed-ordering" is not a member of D2's closed
   enum — within-field-qualifier-on-bare-enum shape (modules.md:207-210); where the
   assumed-ordering marker lives is an open design decision — R3 — [VERIFIED — surfaced] → F21.
3. D5's boundary-example obligation has no tasked checker (§4.1.1 facts don't cover body-shape
   (c); in-run demonstration: D2/D3 are boundary-bearing, carry no worked example, and the
   finding-4 boundary cell survived six cycles) — R4 — [VERIFIED — surfaced] → F22.
4. Floor × elevation composition undefined in the absent-ordering + pinned-floor-≠-actor cell —
   this repo's LIVE config (floor opus, actor fable-5, no order line); the absent-ordering
   branch presupposes the comparability it lacks — R3/R1 — [VERIFIED — surfaced] → F23.
5. D6's trigger classification lacks a named backstop (asymmetric with D5's F15 correction);
   generic §4.1.4 re-spawn backstop exists but uncited — R4 — [VERIFIED — surfaced] → F24.

mechanical skipped: intent-delta this cycle.
