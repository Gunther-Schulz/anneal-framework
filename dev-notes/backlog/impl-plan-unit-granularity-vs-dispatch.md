# Does the [READY]-presented impl-plan unit decomposition bind the dispatch?

**Status:** OPEN — framework-clarity question, surfaced 2026-06-07 (operator-raised) during the
`f0-render-conventions` run's implement phase. Small; not a re-render blocker.

## The gap
The impl plan presented at [READY] decomposed F0 into **4 parallel-eligible units** (one per touched
file). The orchestrator then dispatched them as **1 in-place subagent** (sensible — 4 tiny disjoint
edits; standing up `/tmp` copies for four one-file edits is overkill).

The framework covers the **capability** explicitly:
- `anneal-dev/.../phases/implement.md:44` — "a dispatch unit is a **group of design decisions**
  implemented together as one piece of work" → planning D2–D5 as ONE unit would have been valid.
- `implement.md:89` — "parallel-eligible units **may** be dispatched concurrently" → concurrency is
  optional; disjointness establishes that concurrency *would be safe*, not an obligation to use it.

What it does **not** state: whether the dispatch must **match** the [READY]-presented decomposition, or
may **regroup/collapse** at dispatch. The impl plan is shown "so the operator sees the unit list at the
decision moment" (visibility), but the menu is loop-control only (`another cycle`/`next phase`), so
`next phase` approves the *transition*, not the *decomposition*; and the plan is "a planning artifact,
not a tracker construct" (`:46`). So regrouping is arguably fine — but then the operator-visible preview
didn't match what happened (the visibility purpose is partly defeated).

## The question
Does the [READY]-presented unit count bind the implement dispatch?
- **(a) advisory** — the plan is illustrative; dispatch may regroup. Matches "planning artifact, not a
  tracker construct" (`:46`). If chosen, the spec should say so (the preview is non-binding).
- **(b) honest-preview** — dispatch should match the presented decomposition (regrouping requires
  re-presenting), so the visibility the plan exists for is truthful.

## Cleaner orchestrator practice regardless of the answer
Plan the unit granularity to **match the intended dispatch** — plan 1 unit if dispatching 1 — so the
[READY] preview reflects what actually happens. The F0 run had a sensible-but-inconsistent mismatch
(planned 4, dispatched 1).

## Also surfaced same run (separate, related): subagent narration unreliability
The F0 implement subagent **confabulated** a "prior interrupted attempt" — claimed D2/D3/D4 were
pre-existing and that clean-before-dispatch didn't hold, when the orchestrator's own pre-dispatch check
showed the work product clean (the subagent made all 4 edits itself, then misattributed 3). The
orchestrator integrity check (verify-with-eyes vs. the actual tree + the locked design) caught the
narration as untrustworthy and confirmed the real state correct — a clean live demonstration that
doer≠checker is load-bearing, not ceremony. No framework change implied (the guard worked); recorded as
evidence for the value of the separate-checker discipline.

## Relates to
- `worktree-isolation-and-integration.md` (the parallel-isolation dispatch path).
