# Place anneal in the agent-reliability landscape + learn / find-superior (research)

**Status:** RESEARCH RUN DONE (deep-research `wf_7dbc2c5e`, 2026-06-03) — verdict
below; preliminary hypotheses largely **CONFIRMED**, one **refuted** (anneal is
*not* unique — a peer exists). Raw run (23 sources, 107 claims, top-25
adversarially 3-vote-verified, 19 confirmed / 6 killed) preserved at
`dev-notes/research/anneal-placement-deep-research-2026-06-03.raw.json`. Residual
open work spun out: (1) the measurement design → `anneal-reliability-measurement.md`
(the live thread); (2) positioning-corrections to apply if/when anneal is described
externally (below — not yet checked against the actual spec).

## anneal characterization (CONFIRMED as well-placed)
Domain-agnostic, **instantiable methodology** that makes open-ended AI work *sound*:
(1) every load-bearing claim grounded in re-checkable evidence (basis rule), (2) a
coherent, complete state held (tracker; nothing silently dropped), (3) investigate-
design → implement → verify with **INDEPENDENT (separate-context) verification** + a
convergence requirement. Instances: clippy/daneel/campaign-craft/bauleitplan/anneal-dev.

## Placement — CONFIRMED (3 hypotheses, each verified 3-0)
anneal sits at the **process-discipline layer**, genuinely less crowded than the layers
it's confused with:
- **Above the agent-pattern level.** It composes Anthropic's building-block patterns
  toward an epistemic standard; **evaluator-optimizer** is the closest single-pattern
  analog to its independent-verify+convergence loop, but that's one workflow, not a
  methodology.
- **Orthogonal/complementary to formal verification.** Formal verification certifies
  well-specified *safety* under explicit assumptions + needs a formal spec; **end-to-end
  formal verification of LLM agents is infeasible** (probabilistic generation). anneal
  targets open-ended *correctness* where no spec exists. Distinct layers.
- **Distinct from eval/monitoring tooling** (e.g. AgentCompass = *post-deployment*
  retrospective trace analysis — different lifecycle position than anneal's in-process
  pre-output discipline).
- **Self-correction literature strongly VALIDATES the core bets** (TACL survey; Huang
  et al. ICLR 2024): intrinsic same-model self-audit is unreliable and *degrades*
  performance (GPT-4 GSM8K 95.5→91.5→89.0 across rounds); the "closed loop of correlated
  errors when the verifier shares the actor's base model" is the **mechanistic case for
  separate-context verification.** Calibration: "separate-context" is a reasonable
  operationalization of "outside the generating model" but isn't directly tested as
  isolation → honest verb is **"supports," not "proves."**

## Superior-check — VERDICT: NOT unique, but no superior found
- **A genuine methodology-PEER exists: APF — Agentic Problem Frames** (arXiv 2602.19065,
  Chanjin Park, Seoul National Univ., Feb 2026). Independently exhibits all four
  disciplines: evidence-grounding, **independent verification** ("the executor does not
  approve their own work"), coherent state, structured convergence (Act-Verify-Refine
  loop). So **"anneal is unique" is refuted** — do not claim it.
- **But APF is not superior**, and differs in anneal's favor: APF **leads with Act
  (execute-first)** — no explicit up-front investigate/design; anneal designs *before*
  implementing. APF's coherent-state is **looser** (no "nothing silently dropped"
  mandate). And APF is validated only by **two qualitative case studies it calls a
  "conceptual proof,"** zero metrics, ending in a *"Call for Collaboration: Empirical
  Validation"* — it shares anneal's exact measurement gap. (Single-authored v1, unpeer-
  reviewed.) The tight "one-to-one peer" framing was *refuted 1-2*: peer-status holds,
  the over-tight match doesn't.
- **CARE (arXiv 2604.28043)** was hypothesized as a peer + measurement source —
  **refuted 0-3 on all claims.** Do NOT cite it as either.

## APF deep-read (2026-06-03) — further lessons + a recorded rejection
A full read of APF (arXiv 2602.19065) beyond the peer-status finding:
- **ADOPT → Callback/Confirm split.** APF makes verify two mandatory channels — *Callback*
  (fact: world changed as specified) + *Confirm* (value: aligns with intent, approved by a
  separate actor). Corroborates + reframes `verify-vs-original-requirements` (folded there).
- **ADOPT-CANDIDATE → multi-voter adversarial verify** for no-mechanical-predicate claims (from
  APF's separate-critic + deep-research's 3-vote). Own item:
  `multivoter-verify-no-predicate-claims.md` (validate-before-adopt).
- **CONSIDER → negative-authority spec field.** APF's *Scope* = explicit *negative* constraints
  / jurisdictional boundaries. anneal binds what work *is*, less what the agent must *not* do —
  low-urgency check whether that's a binding-slot gap.
- **CONSIDER → S,K⊢R completion shape.** "Done = accumulated evidence + spec entails the
  requirement" — a framing for convergence/[READY]. Borrow the shape, not the math (APF gives no
  stopping criterion).
- **REJECTED by design → the "data flywheel."** APF auto-feeds verified trajectories back as
  future-run context — exactly the auto-accumulating memory anneal distrusts (CLAUDE.md: opaque,
  stale; repo + post-run-review instead). Recorded as a *decision*, not a gap.
- **Differentiators confirmed in anneal's favor:** design-before-act (APF acts-first, late-binds)
  + complete-state/nothing-dropped (APF assetizes selectively). Cross-link: APF's act-first
  late-binding may fit *operational/recurring* ad-hoc domains → relevant to
  `anneal-adhoc-use-and-graduation.md`.

## Positioning-corrections (apply when anneal is described externally; not yet grepped vs spec)
- Anthropic's five patterns are **"representative workflow patterns," NOT a "canonical
  taxonomy"** — the source says they're "common patterns, not prescriptive," one tier
  (workflows) of three. Don't over-cite them.
- Self-correction lit **"supports"** separate-context verify; it does not **"prove"** it.
- APF expands to **"Agentic Problem Frames"** (not "…Process Framework").

## Leads — status after the run
1. **Reliability measurement** — confirmed the biggest real gap. **The live thread →
   `anneal-reliability-measurement.md`** (borrowable templates + the A/B-via-instances
   path landed there).
2. **Offline-verify-policy + lightweight-online-monitor split** (VeriGuard, verified
   3-0) — real, borrowable as an **architectural pattern** (amortize verification of a
   stable standard once; cheap per-step conformance checks), but its formal-guarantee
   teeth need a formal spec anneal lacks → adopt the SHAPE, not the proof machinery.
   Open question: is there a *spec-free* analog (compile the basis rule + verify criteria
   once into cheap per-step checks)? → candidate for the measurement/verify thread.
3. **Self-grounded verification** (elicit success criteria in isolation before verifying,
   the "~+20pt" lead) — **did NOT survive into the verified set** (fell below the top-25
   budget cut; neither confirmed nor refuted). Treat as **still-unverified**, not
   established. Re-probe if pursued.

## Sources (primary, adversarially verified — full evidence in the preserved raw json)
Anthropic "Building Effective Agents"; APF arXiv 2602.19065; trustworthy-agentic survey
2605.23989; VeriGuard 2510.05156; AgentCompass 2509.14647; TACL self-correction survey
(tacl_a_00713); Huang et al. 2310.01798. Unverified-but-surfaced measurement sources:
ReliabilityBench 2601.06112 (pass^k, Reliability Surface), Tau²-Bench, 2603.14987.
