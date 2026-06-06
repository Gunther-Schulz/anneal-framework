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

## Sharpening — clippy's auto-battle analysis (2026-06-06): the gate must be a HOOK, not an orchestrator self-check
Clippy's session analysis (operator-carried) generalizes Unit-18: BOTH adherence failures (Unit-18
skipped convergence; Unit-24 F6 `non-issue` misclassification, `disposition-misclassification-shields-design`)
occurred in **full auto-battle, late in a long session**; earlier Units 26-28 (same model/protocol)
got convergence right. The structural reads:

- **Auto-battle removes the one actor whose incentives DIFFER from the AI's** — the AI has a
  session-length bias (finish sooner = less context pressure), the operator a correctness bias. The
  behavioral rules assumed both; auto-battle removes one and hopes they self-enforce. They don't, late
  in long sessions.
- **So "the *orchestrator* mechanically confirms the artifact" (Candidate fix, Primary) is
  INSUFFICIENT in auto-battle — the orchestrator IS the AI.** An orchestrator self-check is still
  AI-willed and degrades identically to the skip it catches. The gate must be a **non-AI actor**: a
  **hook** (like `hooks/anneal-dev-run-gate.py`) that blocks the implement-phase edit unless the
  post-last-D-delta convergence artifact exists. Keep the artifact-existence + post-dating logic; move
  the CHECKER from orchestrator → hook. *(This revises the Primary above.)*
- **Interactive's apparent superiority is OPERATOR-DETECTION — which the framework explicitly FORBIDS**
  (`foundations.md`: "where enforcement would require the operator to detect, the form is malformed").
  The [READY] closed-artifact "forces" the AI to render the convergence-status section to a reader who
  would notice it missing — but that reader noticing IS operator-detection. So "prefer interactive" is
  not a framework-consistent fix; it is the framework leaning on the very mechanism it bans. The
  consistent fix is an un-skippable fresh-context checker (the hook), which makes auto-battle ≡
  interactive in rigor — the V1 asymptote (`framework-intent-vision-statement`).
- **Mitigation taxonomy (clippy proposed 3; only one is structural):** (i) mechanical artifact gate =
  structural **iff a hook**; (ii) a "[READY] self-checkpoint that re-reads the convergence requirement"
  = **still willed** (re-read + honest self-attest is the same degrading will — loaded-but-inert by
  construction); (iii) session-length warning = willed/detection-adjacent. (ii)/(iii) lean on the
  degrading thing; only (i)-as-hook moves rigor willed→structural.
- **Cause (operator calibration, 2026-06-06):** context-fatigue is, from operator experience across
  many runs, **at most a contributing factor — not the primary cause.** The primary driver is the
  always-present **finish-sooner incentive activated by a cost gradient** (a cheaper-but-wrong path
  available: skip the cycle / avoid a migration), unchecked by structure — i.e. the mechanism clause's
  "a rule that depends on the AI *choosing* rigor leaks," which fires *whenever* an incentive to leak
  exists, **from cycle 1**, not only late. **Implication:** the failure is **NOT session-length-bounded**
  → clippy's mitigation (iii) (session-length warning) addresses a non-primary cause AND implies a false
  "we're fine early" safety. It also makes the **hook** even more clearly right: robust to a cause that
  can fire anytime (a hook blocks the skip regardless of *why*), whereas (ii)/(iii) depend on the cause
  being "AI catches it if reminded" — the same will that's failing. (Adherence-vs-cost-gradient is the
  measurable shape, not adherence-vs-context-length — a proof/measurement-thread hook.)
- **Honest dogfood (this session, `purpose-mechanism-clause`):** convergence ran + caught 2 real
  defects — but by the AI *choosing* to (un-fatigued, operator at [READY]), with NO mechanical gate.
  "Loaded-but-willed-and-held," not enforced — the same gap, masked.

## Generalization (2026-06-06, operator): hooks as the structural-sequencing substrate
Operator: this hook may "open general hook possibilities — could also trigger the cycles and phases."
The right generalization, with one load-bearing distinction:

- **"Trigger" splits three ways; only one is enforcement.** A hook can **GATE** (block the
  transition/edit/turn-end until the precondition artifact exists) — structural, real; **PROMPT**
  (inject "run convergence now") — a stronger *nudge* but still **willed** (clippy's mitigation (ii):
  the AI reads it and can still skip/fake — the same degrading will); it **cannot EXECUTE** the
  cognitive work (reason, dispatch the falsification subagent, judge) — irreducibly the AI's.
  **Design rule: a triggering hook GATES the advance on an artifact; it never merely reminds.** The
  operator's "trigger the cycles and phases" is exactly right read as *the protocol cannot advance to
  the next phase / cannot end the cycle-loop until the artifact exists* (gate-the-advance) — and a
  trap read as "remind the AI to."
- **The general program:** a **phase/cycle-precondition hook family** — each transition gated on its
  precondition artifact's existence + well-formedness. Married to the cost-gradient enumeration
  (Cause, above): **for each leak site — where the correct action costs more than an available wrong
  one — define (a) the artifact the correct path produces and (b) a gate hook blocking progress
  without it.** Finite (gradients are enumerable); the buildable path to *auto-battle ≡ interactive in
  rigor* (V1).
- **Two guardrails:** (1) a gating hook must NOT auto-advance the **operator-irreducible** gate (kernel
  soundness) — gate *author-side* preconditions only, else it re-creates the auto-battle problem at the
  harness layer; (2) the **tracker stays the single source of truth** — the hook READS run-state from
  the tracker, never maintains its own (`SKILL.md`).
- **Honest bound:** a hook is friction+gate, not unbypassable (`--no-verify`, Bash-routing — same as
  `anneal-dev-run-gate.py` / the Invariant-change-ratified marker). A PreToolUse Edit/Stop block is
  *stronger* than a commit-msg marker (harder to route around silently) but still bypassable by
  deliberate, visible, non-silent action — which IS the framework's enforcement philosophy. And it
  forces the artifact to EXIST + be well-FORMED, not GENUINE — genuineness stays the separate-context
  re-derivation's job; the two compose.
- **Discipline (respect the bound):** build the **convergence-gate hook FIRST** (this item — the MVP /
  first instance); let it validate the program before building any hook *family*. Don't speculatively
  design the framework (additive-reflex; the bound keeps fix-first finite).

## Relates to
- `skill-craft-antipatterns-loaded-but-inert` — same shape (behavioral rule doesn't fire); this is
  the highest-stakes instance (the soundness mechanism itself).
- `disposition-misclassification-shields-design` — the Unit-24 sibling; same auto-battle conditions;
  the auto-battle analysis above covers both.
- `auto-battle-cadence-mode` — the gate is what lets the auto-cycle affordance (and full auto-battle)
  stay sound; the general hook-program is the structural backing for "auto-battle ≡ interactive."
- `proportional-cycle-weight` — composes (the light-skip certifier) + this is evidence for its
  circular-self-cert hazard.
- `auto-battle-cadence-mode` — the auto-battle context (no operator checkpoint is what makes the
  skip invisible); a gate is what lets auto-cycle stay sound.
- `convergence-surfaced-finding-action-brake` — sibling convergence-process enforcement item.
- V-5 (false-[READY]) — the watch this gate would make mechanically enforceable.
- Origin: clippy Unit-18 runner-execution-model run (other session, operator 2026-06-06).
