# Framework-dev as an anneal instance (vs bolt-on anti-decay) — effort design capture

Durable design artifact for the most **foundational + reflexive** framework
effort: how to make working on the framework rigorous and non-decaying.
The deep proposal — **make framework-dev itself an anneal instance** —
with the shallower "bolt anti-decay forcing-functions onto the ad-hoc
process" as the fallback. Written in-context 2026-06-01; **start fresh**
(foundational, reflexive, decision-heavy — the wrong thing to rush).
Not spec.

## The symptom: corpus structural decay

Working on the framework keeps producing the same mess:
- **Bloat** — files accrete walls of text (clippy `SKILL.md`).
- **Fragmentation** — one principle restated across N homes (FB-5 the
  `[VERIFIED]`-family; the slot-collapse).
- **Leakage** — domain concretions in domain-general homes (the
  contract-1 de-pollution).

## The deeper diagnosis: `development-process.md` is a shadow-anneal

The dev-process's practices are **anneal concepts re-stated ad-hoc**:
- practice 5 (ground before asserting) = **the basis rule**
- practice 9 (design → decide → implement) = **the design↔impl split**
- release-loop step 4 (separate-context render/coherence/skill-craft review) = **verify**
- practice 6 (integrate, don't insert) = **lens-based coherence**
- practice 12 (periodic coherence-audit) = **inspection at set scale**

So the current setup is **FB-5 fragmentation at the highest possible
level** — anneal's own method, duplicated and drifting. And the
anti-decay disciplines (skill-craft's Amendment/Edit-as-Pareto/
domain-independence) are **advisory, so they don't fire** (practice-8
violation). Both are symptoms of *not using the methodology that has the
rigor built in.*

## Option A (foundational, recommended): make framework-dev an anneal instance

Re-derive the dev-process **as anneal bound to the corpus-evolution
domain** (a sibling of clippy / daneel / campaign-craft).

- **Domain fit is clean:** investigate-design = ground claims about the
  corpus (where does X live, what's the contract) + lock the rule change;
  implement = edit the rule-corpus; verify = skill-craft self-review +
  render-fidelity + coherence (= what step-4 already does). "The domain's
  executable verification" binds to those separate-context checks.
- **Corpus-specific bits → instance bindings** (like clippy's git):
  release/version-bump/plugin-update mechanics, the coherence-audit
  cadence, the `Coherence-audit-handoff` marker, the skill-craft gate.
- **Inherits the rigor for free:** the basis rule, convergence cycle,
  evidence-bearing artifacts, and lens inspection **are** the per-cycle
  forcing functions we wanted from anti-decay. You don't bolt them on —
  they come with the methodology.
- **Ultimate dogfooding + arbitrariness test** (foundation contract 1):
  if anneal can develop anneal, that's the strongest domain-generality
  evidence there is; if it *can't*, that's a smell worth finding.

**Caveats:**
1. **Self-hosting / bootstrap.** You'd edit the methodology *using* the
   methodology. Manageable — the process runs the **last-committed**
   framework version while you edit the spec; the edit takes effect the
   *next* cycle (exactly how clippy runs a pinned version while you change
   its spec). But it needs an explicit "**the process uses the stable
   version, not the in-flight edit**" rule, or you saw off the branch
   you're sitting on.
2. **Big, foundational re-derivation** — highest leverage *and* highest
   risk.
3. **Even A needs an internal escape hatch** — a light / manual path for
   trivial edits and bootstrap-blocked moments (mirroring clippy's
   spawn-fallback + anneal's single-unit lightness). The fallback is
   **fractal**: B backs up A, and A backs up itself.

## Option B (fallback, shallow): bolt anti-decay forcing-functions on

If A proves too big, the cheaper partial: convert skill-craft's advisory
anti-decay disciplines into **artifact-producing forcing functions**
(Amendment's all-homes scan → required artifact; Edit-as-Pareto's
"name what was removed" → required line; domain-independence → a
domain-term grep artifact; word-count → a budget gate), then **wire a
cheap per-cycle structural-hygiene check into dev-process step-4** (three
diff-computed checks: bloat = size/structure delta; leakage = domain-term
grep; fragmentation = the forced all-homes scan). Keep it **cheap** or it
becomes the ceremony it fights.

**A subsumes B's process-mechanism** — anneal's apparatus *is* those
forcing functions. B is the shallow version of the same goal — but
**keep B genuinely buildable, not a discarded alternative.** A's
self-hosting bootstrap is a real failure mode; if A stalls, the bolt-on
is the parachute. Commit to A, keep B in reach.

## What neither subsumes: the cleanup (do it regardless)

`SKILL.md` de-bloat, FB-5 consolidation, the de-pollution cluster are
**dirty corpus, not process** — they need fixing either way. Nicely,
they become the **first dogfooding tasks** of the anneal-ified process:
use the new instance to clean the corpus, and you've validated it on
real work.

## Reflexivity caveat — non-negotiable

This is skill-craft improving skill-craft + dev-process improving (or
replacing) dev-process — **maximal self-validation risk** (`CLAUDE.md`:
"rule-edit subagent PASS may self-validate — pause + re-read before
push"). Separate-context review is the whole ballgame.

## Sequencing

1. **Decide A vs B** — a real decision-design question; give it a proper
   design surface (it's exactly the kind of thing the
   `decision-design-sharpening` skill is for).
2. **If A:** derive the corpus-evolution anneal instance (its bindings +
   the self-hosting rule); the old `development-process.md` collapses into
   "anneal + these bindings," shedding its shadow-anneal duplication.
   **If B:** sharpen skill-craft + wire the step-4 hygiene check.
3. **Coherence-audit + the cleanups** (SKILL.md, FB-5) as the first real
   work — and, under A, the first dogfooding.

## Why start fresh
Foundational (governs how *all* future framework work goes), maximally
reflexive (self-validation), multi-corpus, and decision-heavy. This doc
is the durable handoff.
