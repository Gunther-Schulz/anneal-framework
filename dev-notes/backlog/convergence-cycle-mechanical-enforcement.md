# Convergence cycle is unenforced (behavioral rule, no gate) → silently skippable in auto-battle

**Status:** OPEN — surfaced 2026-06-06 by a clippy Unit-18 auto-battle run (other session, carried
in by the operator; re-grounded against the live spec here, not taken on the session's word).
**High-stakes** — the convergence cycle is *the* un-fakeable-bind soundness mechanism (`core.md
§3.1`/§4.1.4), and it can be silently skipped. **Method-kernel** (`core.md §4.1.4` convergence
requirement + §4.3 verify + the tracker [READY] gate) → anneal-dev + irreducible operator soundness;
rendered to all instances.

## The failure (clippy Unit-18)
An auto-battle run (7 mechanical design decisions) went: cycle 1 (investigation) → cycle 2
(concretize + verify decisions) → **[READY]** → implement → verify [PASSED] — **the convergence
cycle (new-surface investigation + falsification pass + zero-D-delta confirmation) never ran.**
Worse: a D7-shape amendment *during* cycle 2 is itself a D-track delta that should have held the
phase until a clean convergence ran *after* it. Verify [PASSED] (the design was correct) — but
**outcome-correctness ≠ process-correctness** (the convergence exists to check the working
context's certainty with a fresh context that doesn't share its anchoring; "I'm sure it'd pass"
defeats its purpose).

**Contrast (same session, same model, same auto-battle, same protocol files):** the earlier
Units 26-28 run ran convergence correctly — cycle 3 caught a real D-delta, cycle 4 was the clean
convergence. So it's **not** a stale render or unloaded rule — it's **adherence degrading with
accumulated session length** (Unit 18 came after a full prior run + deploy + 2 hotfixes + the
Coupled-change discussion).

## Why the rule is present-but-unenforced (re-grounded)
`core.md §4.1.4` is unconditional ("[READY] requires a convergence cycle … zero D-track deltas").
The [READY] closed-artifact form *requires* citing the convergence-cycle status (intent + mechanical
artifacts, or recorded skip, + zero-D-delta) — **malformed if absent**. But: (a) no **mechanical
gate** confirms the artifacts exist before [READY]→implement; (b) **auto-battle has no operator
checkpoint** at the closed-artifact presentation, so the malformed [READY] is invisible; (c) verify's
planned-vs-actual checks the *decisions*, not "did the convergence cycle run." → the skip is
uncaught until (optional) post-run review. V-5 (false-[READY]) documents the role; the rule exists;
adherence + enforcement both failed.

## Candidate fix (clippy's, re-grounded + sharpened)
Convert the behavioral rule → **artifact-checkable gate**:
- **Primary — [READY]-transition self-check (earlier than clippy's proposal).** The orchestrator,
  at [READY]→implement, mechanically confirms a **clean convergence cycle's falsification artifact
  exists with a cycle number post-dating the last D-track-modifying cycle** (+ zero-D-delta). Absent
  → not [READY]. The **post-dating** clause is the key insight — it also catches the
  amendment-then-[READY] sub-case (a D-delta in cycle 2 ⇒ convergence must post-date cycle 2).
- **Backstop — verify planned-vs-actual** confirms the same artifact presence (clippy's proposal;
  fires after implement, so it's the net, not the gate).
- Instance binding: clippy's `.clippy/runs/<run>.passes.md` is its rendering of the framework
  artifact-check.

## Composition with `proportional-cycle-weight` (load-bearing — state it)
A "skip convergence if the design is simple" clause is **rejected** (clippy's call, correct — any
"simple enough" boundary reintroduces the judgment convergence exists to remove). This is exactly
`proportional-cycle-weight`'s **circular-self-certification hazard**: a light-skip is licit **only
via a non-circular external/operator certifier**, recorded as an artifact the gate accepts — never
the pass's own "I'm sure." **And in auto-battle there is no operator certifier → convergence is
unconditionally mandatory there.** The Unit-18 skip was doubly-wrong (self-judged + no certifier).
So the gate = *clean convergence post-dating the last D-delta* **OR** *a recorded external-certified
light-skip*; **in auto-battle, no skip**. This run is **evidence for `proportional-cycle-weight`'s
hazard** (the self-certified skip is the failure it warns about).

## The meta-pattern + V-watch note
Fresh, high-stakes instance of `skill-craft-antipatterns-loaded-but-inert` (a behavioral rule,
loaded, that doesn't fire) — here at the *convergence-cycle* level. The fix is the **structural-
enforcement** mitigation (skill-craft Judgment-mitigation #2), not "adhere harder." Per the
post-ship-only rule (shipped this session), this is a **backlog item, not a V-watch** (a V-watch
fits later, to watch whether the gate reduces skip recurrence — catcher: an auto-battle run whose
[READY] gate blocks on a missing post-last-D-delta convergence artifact).

## Relates to
- `skill-craft-antipatterns-loaded-but-inert` — same shape (behavioral rule doesn't fire); this is
  the highest-stakes instance (the soundness mechanism itself).
- `proportional-cycle-weight` — composes (the light-skip certifier) + this is evidence for its
  circular-self-cert hazard.
- `auto-battle-cadence-mode` — the auto-battle context (no operator checkpoint is what makes the
  skip invisible); a gate is what lets auto-cycle stay sound.
- `convergence-surfaced-finding-action-brake` — sibling convergence-process enforcement item.
- V-5 (false-[READY]) — the watch this gate would make mechanically enforceable.
- Origin: clippy Unit-18 runner-execution-model run (other session, operator 2026-06-06).
