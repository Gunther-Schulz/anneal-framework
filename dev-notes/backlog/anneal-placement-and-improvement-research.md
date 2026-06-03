# Place anneal in the agent-reliability landscape + learn / find-superior (research)

**Status:** OPEN — research, operator-raised 2026-06-03. Goal: situate anneal properly, extract
improvements, and honestly check whether something *superior* exists. This holds a **preliminary
4-search placement** + leads + a sharpened question **for a rigorous `deep-research` run (best
post-`/clear`, clean window)**. Preliminary ≠ verdict.

## anneal characterization (for the research to place it)
Domain-agnostic, **instantiable methodology** that makes open-ended AI work *sound*: (1) every
load-bearing claim grounded in re-checkable evidence (basis rule — search/located-read), (2) a
coherent, complete state held (tracker; nothing silently dropped), (3) investigate-design → implement
→ verify with **INDEPENDENT (separate-context) verification** + a convergence requirement.
Instances: clippy/daneel/campaign-craft/bauleitplan/anneal-dev. Tentative identity: *controlled
settling of work toward a sound, low-stress state* (the "annealing" essence — not yet confirmed).

## Preliminary placement (4 searches — hedge accordingly)
anneal sits at the **process-discipline layer**, which is *less crowded* than the layers it gets
confused with:
- **Above tool/pattern level.** Anthropic's "Building Effective Agents" (5 patterns: prompt-chaining,
  routing, parallelization, orchestrator-workers, evaluator-optimizer + reflection) are *building
  blocks*. anneal USES them (orchestrator-workers = its dispatch; evaluator-optimizer + reflection =
  its verify/loopback) but is a *methodology composing them toward an epistemic standard*. Not a pattern.
- **Orthogonal to formal verification.** AgentVerify (LTL model-checking the agent's control-flow FSM),
  VeriGuard (verified policy + runtime monitor), SMT/Z3 work give **provable SAFETY/behavioral bounds**
  — a *different* guarantee-type. anneal gives **evidence-discipline for open-ended CORRECTNESS** where
  there is *no formal spec* ("is this design/rule sound?"). Complementary, not competing.
- **Distinct from RL / agentic-RL** (training-level reliability) and from **guardrail/envoy tooling**
  (tool-level). anneal is none of these.

## Superior-check (PRELIMINARY — the part that most needs the rigorous run)
- Nothing found is straightforwardly *superior at anneal's own problem* (open-ended work → sound
  outcome, domain-agnostic, instantiable). The self-correction literature **validates** anneal's bets:
  *self-audit fails; reliability needs external grounding + independent verification; combine
  techniques.* anneal is on the right side of that.
- The closest "superior" — **formal verification** — is superior for a *different* problem (provable
  safety bounds) and is **complementary** (it could bound an anneal-driven agent's actions while anneal
  makes the *work* sound).
- **CAVEAT:** 4 searches only. A rigorous adversarial survey could surface a real methodology-peer or a
  stronger approach — don't conclude "anneal is unique" from this.

## Leads to ADOPT (candidate improvements)
1. **Self-grounded verification** — elicit success criteria *in isolation* BEFORE verifying (beats
   "agreement bias"; ~+20pt failure-detection). → sharpen anneal's verify (establish criteria first).
2. **Offline-verify-policy + lightweight-online-monitor** split (VeriGuard) — parallels anneal's
   design-time-vs-runtime; possible model for a safety-bound complement on high-stakes instances.
3. **Reliability measurement** — anneal has *no* way to *measure* its reliability gains; the biggest
   gap. **ELEVATED to its own item → `anneal-reliability-measurement.md` (operator's next exploration).**

## Sharpened deep-research question (for the rigorous run)
> Place the Anneal framework (above) in the landscape of approaches to reliable/dependable AI-agent
> work. (a) Where does it sit vs agent design patterns, self-correction/self-verification, formal
> verification of agents, agentic-RL, eval/benchmarks, guardrail/envoy tooling? (b) Is there a
> methodology doing anneal's specific thing (force-evidence + independent-verify + coherent-state +
> structured-convergence, domain-agnostic) that is equal or SUPERIOR? (c) What evidence-backed ideas
> should anneal adopt? Adversarially verify; cite.

## Sources (preliminary)
anthropic.com/research/building-effective-agents; arxiv 2503.16416 (agent-eval survey); ResearchGate
"When Can LLMs Correct Their Own Mistakes?" (self-correction survey); arxiv 2603.02798 (Self-Grounded
Verification); preprints.org 202604.1029 (AgentVerify); arxiv 2510.05156 (VeriGuard).
