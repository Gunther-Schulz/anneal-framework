# Backlog — anneal-framework

Work items in two grades: parked (carries its named missing evidence
or trigger) and ready (decision-complete). Items leave by commit ref
or are dropped with a one-line reason. Consumer: the session that
picks the item up — method-kernel items additionally run the full
development process (soundness verdict included), never a ride-along.

- READY — **anneal-dev machinery cost redesign: buy fresh context
  retail, not wholesale.** Principle: mechanical verifiers gain no
  verdict value from a fresh context; freshness pays only at
  self-blindness surfaces. Design sketch (cut-list):
  (a) mechanical falsification pass → orchestrator-run, no dispatch —
  the protocol already distrusts subagent judgment there (closed
  predicates, orchestrator-computed verdicts); candidate derivation
  from a basis's declared coupling shapes is mechanical;
  (b) isolated verify → narrow L4-shaped review: fresh context ONLY
  for the judgment residue (design-completeness audit, requirements
  coverage incl. the verbatim-request leg, cold-read restatement of
  the produced text); every mechanical check (gates, greps, render
  batteries) runs orchestrator-side with outputs pasted into the
  tracker; anything precipitable leaves the protocol into standing
  tools;
  (c) intent-falsification KEEPS its fresh dispatch — criteria-first
  derivation before seeing the design is the parentage breaker inline
  categorically cannot replicate — sized narrow;
  (d) tracker, requirements record, basis rule, loopbacks untouched.
  Net target: 4-5 spawns (one at ≈1.1M processed) → 2 narrow spawns
  (each L4-sized: ≈500k processed / ≈220k cost-weighted).
  GROUNDING (measured 2026-07-30, dedup-CORRECTED same day —
  transcript usage entries are per-stream snapshots, several per API
  call; dedupe by call id, one instrument both sides): anneal
  isolated verify = 12 calls, ≈1.10M processed (108.8k creation /
  962k reads / 28.0k out), unique catch one cosmetic line-wrap
  (which then became a free standing mechanism — diff-scoped wrap
  check); skill-craft L4 self-review = 8 calls, ≈502k processed
  (78.9k creation / 400k reads / 16.7k out), three substantive
  findings, two in the cross-file class inline authoring is
  documentedly blind to. ≈2.2x raw / ≈1.7x cost-weighted — the
  YIELD asymmetry carries the argument, not an order-of-magnitude
  cost gap; the variable is check design, not model tier.
  NAMED CONSTRAINTS: (1) the distillation-boundary's founding
  evidence ("a falsification round killed a decision the prior round
  had confirmed") predates the current top tier — cheapen the
  falsification machinery, never delete the concept; the fire-rate
  lens decides retirement, not this redesign. (2) This is a
  method-kernel edit (spec + renders): full development process,
  operator soundness verdict included. (3) Evidence caveat: the
  grounding runs were operator-truncated (the 3.1M verify was
  retroactive on an already-shipped edit; the falsification
  dispatches were vetoed) — n is small; the redesign session
  re-checks against the framework's own recorded run history before
  cutting.
  DONE-CRITERION: revised spec through the dev process; anneal-dev
  re-rendered; one live corpus-evolution run at the new shape with
  per-dispatch usage recorded and compared against the 2026-07-30
  baseline numbers above.
  EVIDENCE POINTERS (for the re-check): the 3.1M cost record lives in
  claude-code-cache-fix `.anneal-dev/runs/widen-definition-parentage.md`
  (its closing "Cost record" section; per-dispatch usage extractable
  from that session's subagent transcripts under
  `~/.claude/projects/<cwd-hash>/<session>/subagents/`). The 79k
  exemplar: skill-craft commit f2a97a5 (findings + dispositions in its
  message), the pattern itself in skill-craft
  `references/self-review.md`. The truncated-run caveat's detail: the
  same tracker's "Operator override" and "Retroactive isolated verify"
  sections. Framework-side run history for the re-check:
  `.anneal-dev/runs/` in any repo anneal-dev has run in.
