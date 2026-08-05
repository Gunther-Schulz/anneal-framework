# verify battery is render-instance-shaped — a non-render (rule-corpus-only) instance must define its own executable-verification battery

**Status:** [DESIGN] — surfaced 2026-07-16 from a separate deployed instance (Planungsbüro-Schulz pbs
rule-corpus, anneal-dev in-context), operator-flagged. An **instance-binding** gap, not a kernel gap.

## What
verify's executable battery (`bindings.md` Verification battery; `phases/verify.md` §4) has three checks:
(a) render-fidelity, (b) coherence, (c) skill-quality. Two of the three — **(a) and (c) presuppose a
rendered-plugin instance** (a clause rendered from a source spec; a skill file). For a **rule-corpus-only**
instance that renders no plugin and changes no skill file — where the work product *is* the governance/
process rule-text (pbs) — (a) and (c) are N/A, leaving only (b) coherence. So verify's "executable" leg
collapses to static coherence: exactly the "domain with no executable verification → verify is weaker"
strain `instantiation-guide.md` §1 already names, but the battery is **not parameterized** for it — the
three checks read as universal in `bindings.md`, so a non-render instance has no battery to run, only a
leg to mark N/A.

## The fix direction
The instance should **define its executable-verification battery** in its bindings, not inherit the
render-centric three. For a rule-corpus instance the runnable substrate **exists — it is just different**:
the corpus's own mechanical checks — commit-msg / governance hooks, CI/lint, doc compile, and, where a rule
precipitates into a guard, the actual guard/test. The battery's binding row should read "**the instance's
executable verification**" as a slot the instance fills, with render-fidelity + skill-quality as the
*rendered-plugin instance's* filling, not the universal one. So: every instance names its substrate; a
non-render instance's substrate is not render-fidelity.

## Evidence
The pbs `reviewer-regel-kanal` run's verify ran checks 1–3 (planned-vs-actual, requirements, lenses) fully
+ (b) coherence with real substrate greps, and correctly recorded (a)/(c) as cited-N/A. It reached
[PASSED] **substantively** — but only because a substrate check was folded in *ad hoc* (from
`clippy-category-b-recalibration` #1) + checks 1–3 carried the weight (a)/(c) would carry in a render
instance. A **standing** battery binding (not ad-hoc folding) would make this substantive-by-construction,
and would stop a future non-render run from passing on coherence-alone.

## Relates to
- `clippy-category-b-recalibration` #1 (verify-must-execute-against-the-real-substrate) — the same instinct
  at clippy-instance level; this is the **framework-level generalization** (parameterize the battery slot,
  don't hardcode render-fidelity as universal).
- `instantiation-guide.md` §1 — the strain it names ("no executable verification → verify weaker"); this
  **parameterizes the battery** for it rather than only recording the strain.
- `planner-instance-exploration.md` — another prospective non-coding instance that would hit the same
  render-centric-battery assumption.
