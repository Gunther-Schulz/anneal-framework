# Platform-native vs anneal-genuine — what Anthropic's official docs already solve

**Status:** OPEN — surfaced 2026-06-06 (operator: "look at Anthropic's official skill-building docs;
a lot of what anneal is trying to do may already be solved"). **Strategic/audit finding**, grounded
via `claude-code-guide` against the live official docs + a direct read of the local `anthropics/skills`
clone (`~/dev/reference/skills/`). Complementary to the **session-4 kill-switch research** (which
checked *academic methodology* literature) — this checks Anthropic's **own platform** docs, the more
relevant baseline. Feeds the **intent/V1** thread: anneal's genuine value = the delta from
platform-native.

## The three-layer verdict
- **Layer 1 — skill authoring: largely SOLVED by the platform + an official tool.** Official docs
  (Agent Skills overview + **best-practices** + Claude Code skills guide) cover SKILL.md structure,
  description-based triggering, 3-tier progressive disclosure, bundling, and "build evaluations first /
  iterate with a tester-Claude." There **is** an official **skill-creator** (confirmed in
  `~/dev/reference/skills/skills/skill-creator/`: draft→eval→benchmark→rewrite loop + `eval-viewer` +
  variance analysis + a **description-improver** for triggering). skill-craft's Tier-1/Tier-2 eval is
  the *same shape*; `measurement-harness-mve` already vendored skill-creator's `aggregate_benchmark.py`.
  **skill-craft's genuine delta = the anti-pattern corpus + the load-bearing form discipline** (NOT
  canonicalized officially).
- **Layer 2 — hooks: mechanism is platform-NATIVE.** PreToolUse can block a tool call; Stop/
  SubagentStop can block turn-end. The convergence-gate hook (`convergence-cycle-mechanical-enforcement`)
  is *applying documented primitives*, not inventing a mechanism. anneal's delta = the **discipline**
  (which gates / the cost-gradient enumeration), never the mechanism.
- **Layer 3 — the method: NOT solved. anneal's genuine core.** Platform ships building blocks
  (extended thinking, subagents/multi-agent, mid-conversation system messages, the "demystifying evals"
  post) but **no unified verified-multi-step methodology** — no canonical evaluator/critic pattern, no
  phase-gating, no evidence-grounding/citation discipline, no design→verify cycle. Deliberately left to
  the developer. The "demystifying evals" post (20–50 real-failure tasks, code-graders > LLM-judges,
  trajectory-vs-outcome) **independently validates the proof-thread eval design**.

## The three actions
1. **Slim skill-craft to its delta over the official baseline.** Position skill-craft explicitly as
   "delta over official skill-creator + best-practices": cite the official docs as the baseline, carry
   only the anti-pattern corpus + form/eval discipline. Pareto (cut redundant authoring mechanics) AND
   anti-drift (skill-craft won't diverge from official guidance as the platform evolves). A
   skill-craft-canonical edit → anneal-dev + skill-craft's own self-review.
2. **Build the hook program on documented primitives** (don't hand-roll the mechanism). Confirm the
   exact hook-event set at build time (see caveat).
3. **Invest L3 as the genuine core.** anneal = the verified-multi-step methodology + L1's
   anti-pattern/form delta, *built on* platform primitives (hooks, skill-creator). NOT a skill-authoring
   tool (skill-creator is) nor a hook framework (Claude Code is). Combined with the mechanism clause
   (`purpose-mechanism-clause`): **anneal is the discipline of *which* rigor to enforce structurally, on
   platform primitives.**

## L1 concrete cut/keep map (action 1 detail, 2026-06-06)
Grounded in a direct read of skill-craft (`~/dev/Gunther-Schulz/skill-craft/plugin/skills/skill-craft/`).
**Key fact: skill-craft already admits the redundancy** — its `SKILL.md` "Companion: official plugin-dev"
section says `references/plugin-engineering.md` "covers only partially" what the official plugin-dev
covers authoritatively. The slim *finishes a delegation skill-craft already started.*

**Cut / thin to a cited pointer (redundant with official baseline):**
- `references/plugin-engineering.md` (**382 lines** — marketplace/layout/install/distribution) →
  ~40-line pointer to official plugin-dev + Agent Skills docs. Biggest single win.
- PROCEDURE Layer 1 (plugin-structure plumbing) → pointer (SKILL.md: "most authors get layer 1 right").
- PROCEDURE Layer 3's progressive-disclosure teaching → cite the official 3-tier model.
- `evaluation.md` Tier-1 triggering *mechanics* + the `/eval-skill` runner → lean on skill-creator's
  runner + description-improver (already vendored); keep the framing, drop the re-built plumbing.

**Keep — the genuine delta (why skill-craft exists):**
- `references/anti-patterns.md` (325 lines) — the failure-mode corpus; nothing official canonicalizes it.
- PROCEDURE Layer 2 "Enforcement mechanics" (closed enums / must-verbs / evidence-bearing artifacts) —
  the structural-enforcement form discipline; the **bridge to the method layer**.
- Layers 4-5 + `self-review.md` (evolution, reflexivity, self-review mandate).
- `evaluation.md` Tier-2 behaviour-delta *signature* framing (un-fakeable-artifact applied to eval).

**Slim principle:** skill-craft carries only the delta over {Agent Skills docs + plugin-dev +
skill-creator}. ~20-25% smaller, concentrated in plumbing; value-density up. **Discipline (basis rule):**
every cut cites the official doc that now covers it → an anneal-dev + skill-craft-self-review cycle, not
a blind delete.

## L3 prior-art investigation (action 3 detail — scope, not yet run)
**Warranted, and distinct from the session-4 research.** Session-4 framed it as design-first-vs-act-first
+ placement + academic process-literature, and found **APF** (arXiv 2602.19065) as the peer (same
unmeasured-reliability gap, no testbed). This investigation is narrower + more current: *"who has assembled
plan→evidence→verify→loop into a reusable **methodology** (not a single technique, not an eval suite), and
what did they get that anneal doesn't?"* — aimed at the kill-switch (is one superior?), the adoptables, and
anneal's defensible L3 delta. Clusters to sweep (starting points, to verify — NOT asserted): reflection/critic
loops (Reflexion, Self-Refine, CRITIC); plan-then-execute / plan-verify (arXiv 2509.08646, LATS);
process-discipline agent frameworks (LangGraph, DSPy, AutoGen/CrewAI); coding-agent scaffolds with verify
loops (SWE-agent, OpenHands, the Anthropic three-agent harness); spec-driven/designation-grounded
(Zave-Jackson, per session-4). **Method:** grounded (deep-research/web), **one run at a time** (session-4's
concurrency lesson). Can graduate to its own item when greenlit. Feeds the intent/V1 delta.

## Caveat (secondary-source discipline)
`claude-code-guide` is a secondary source. Its doc URLs + the load-bearing facts (official skill-creator
exists — *confirmed directly in the clone*; PreToolUse/Stop blocking — established) are relayable; its
coverage-% figures and *exhaustive* hook-event list are its synthesis — **verify the exact event set at
build time**, don't bank the full list. Per `core.md` §3.2 secondary-sources rule.

## Relates to
- `framework-intent-vision-statement` — the platform delta IS half the intent ("what does anneal add
  beyond platform-native"); the candidate articulation should incorporate "on platform primitives;
  delta = L3-method + L1-anti-patterns."
- `convergence-cycle-mechanical-enforcement` — build the gate on documented PreToolUse/Stop hooks.
- `measurement-harness-mve` — already vendored skill-creator; the "demystifying evals" post validates
  the seeded-defect / real-failure-task / code-grader design.
- skill-craft items (`skill-craft-antipatterns-loaded-but-inert`, `anneal-dev-evaluation-discipline`)
  — the slim-to-delta action lands here.
- session-4 kill-switch research (archived) — complementary (platform docs, not academic lit).
- Origin: operator strategic check, 2026-06-06.
