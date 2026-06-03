# Could clippy's impl-dispatch run on a deterministic Workflow substrate?

**Status:** OPEN — architecture consideration, operator-raised 2026-06-03.
Assessed this session; **no change recommended now** — captured so it isn't
re-derived. Verdict turns on scale (see below).

## The question
Clippy's impl phase already runs multiple subagents in parallel via a *live
orchestrator* (the clippy context spawns Agent calls, recomputes the
dispatchable set, manages worktrees + loopback). Could that machinery instead
run on the Claude Code **Workflow** tool (deterministic JS orchestration:
pipeline/parallel, concurrency cap, first-class worktrees, schema-validated
agent returns)?

## Verdict (this session)
- **Whole run: no.** Two headless-incompatible blockers — operator decision
  moments (`[READY]`, loopback-vs-defer) and **loopback as a phase transition**
  back into investigate-design. Workflows are fire-and-return.
- **Impl phase alone: a defensible hybrid.** Both blockers sit at impl's
  *boundaries* (entry `[READY]`, exit loopback), not in its body. Happy path =
  pure fan-out-and-collect = workflow sweet spot. A workflow could run
  dispatch-and-integrate **up to completion-or-first-finding**, then hand the
  loopback result (+ completed-unit set to audit) back to the live orchestrator.

## The legitimizing frame
Not "methodology → code." The rule-corpus stays the spec (disjointness-as-basis,
integrity checks, append-only tracker, loopback semantics); a workflow is a
*conforming binding of the dispatch mechanism-slot* — same move clippy already
makes calling the worktree "its binding of the framework isolation slot."
Disjointness is *judged* at `[READY]` (pre-impl); impl only *executes* the
schedule, so it's mechanism, not judgment — the cheap place to bind to code.

## Gains
- Auto concurrency cap + queueing (today the orchestrator hand-manages
  parallel-call count).
- **Schema-enforced return-state** — the four-field loopback result + ledger
  lines valid-by-construction, not rule-enforced. Biggest robustness win.
- Context economy — orchestrator gets a structured batch result, not N
  subagent transcripts.

## Reconciliation costs (real, not fatal)
1. **Can't hard-halt in-flight units on first loopback.** Clippy *wants* to halt
   siblings (save compute + preserve uncommitted work for redo-inheritance). A
   workflow lets them finish, then audits by set-intersection. **Soundness
   preserved**; diverges on compute + redo-material shape.
2. **Clippy's worktree defenses aren't the built-in worktree's behavior**
   (remote-strip, cherry-pick integration, pre/post HEAD-integrity) — must be
   scripted in-agent.
3. Per-run operator opt-in to a workflow.

## Decision factor
**Scale.** A 2–3-unit plan doesn't justify re-scripting the defenses + accepting
the halt divergence. A routinely-15+-disjoint-unit plan does (concurrency +
context-economy + schema gains pay for setup). Re-evaluate if impl plans grow.

## Relates to
- `clippy-run-findings-dispatch-coupling` (Cycle G — orchestrator-out-of-impl).
- `worktree-isolation-and-integration` (the defenses a workflow would re-script).
- `dispatch-brief-one-source-of-truth` (schema-return-state touches brief shape).
- Framework isolation slot (`anneal-framework/spec/core.md` §4.2).
