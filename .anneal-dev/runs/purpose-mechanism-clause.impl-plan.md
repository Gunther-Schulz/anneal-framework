# purpose-mechanism-clause — impl plan

**1 dispatch unit, sequential (no parallelism).** Disjointness basis: a single unit touching a single
file/region; nothing to parallelize.

## Unit 1 — add the Mechanism clause to `spec/core.md` Purpose
- **Scope:** `spec/core.md`, Purpose section — insert one paragraph between goal #2 (ends line 20)
  and the "Human inspectability" paragraph (line 22).
- **Dispatch:** subagent, **in place** (single unit, not parallel-eligible) under the Integrity check
  (`phases/implement.md`). The subagent **invokes skill-craft via the Skill tool before the edit**
  (project `CLAUDE.md` rule-corpus gate + anneal-dev dispatch-brief requirement) — this is a
  rule-corpus edit to a domain-general spec file.
- **Realization (locked design D1, amended):**
  > **The mechanism: structural, not willed.** These goals are secured by shifting rigor from the
  > AI's discipline to **structural enforcement** — because a rule that depends on the AI *choosing*
  > rigor leaks: it loads but does not fire. Each load-bearing step is bound to an evidence-bearing
  > artifact that a separate, non-producing context re-derives (§3.1), so adherence is read off the
  > artifact rather than trusted. The one irreducible exception is the **operator's verdict** at the
  > genuinely-irreducible judgment (§3.1): a deliberately-willed terminus, not a gap to close.
- **Write-time self-check lenses** (`lenses.md`): Lossy-render (no softening), Bloat (each sentence
  carries one of the 4 claims), Over-claimed-verification (both §3.1 cites accurate), Undefined-
  shorthand ("structural, not willed" defined inline). F9 ("secured by" echo of "exists to secure" at
  `core.md:12`) is a surfaced impl-wording call — keep "secured by" (it ties to "secure two things")
  unless the self-check finds it confusing.
- **Acceptance:** clause present at the insertion point; both §3.1 cites verifiable against
  `core.md:139-154` / `:156-157`; no asymptote framing; ≤4 sentences.

## Deferred (not impl units this run)
- **D2:** render to instances queued to `instance-reinstantiation` render-debt (spec-only this run).
- **D3/D4:** WS2 (anneal-dev run-state render-sync) excluded — in the render-debt batch.

## Verify (method-kernel)
Isolated subagent: render/coherence is N/A (spec-only, no render this run); the kernel-independent
review = **skill-craft self-review (form)** + **operator soundness** (already originated at the
[READY] gate via `next phase`). Planned-vs-actual: the clause matches D1's locked realization; both
§3.1 cites accurate; asymptote excluded.
