# anneal-dev evaluation discipline — render skill-craft v1.0.61's Tier 1/2 into anneal-dev-the-plugin

**Status:** [READY] — filed 2026-06-05. Renders skill-craft v1.0.61's new evaluation
discipline (Tier 1 triggering + Tier 2 behaviour-delta signature) into anneal-dev-the-plugin
specifically. **Scoped to anneal-dev only** — the broader question of method-level
meta-evaluation (promoting `anneal-empirical-validation-experiment` / `anneal-reliability-measurement`
/ `canonical-scenario-regression-suite` from tier-6 to first-class) is flagged for separate
operator decision, not folded here.

## The gap

skill-craft v1.0.61 added a new Layer-2 discipline: **inspection ≠ measurement**. A skill
can read clean (inspection passes) and still under-trigger (the description doesn't fire on
should-trigger queries) or sit inert (the skill loads but doesn't produce its signature
artifact). The discipline mandates building the eval **before** the procedure text:

- **Tier 1 — Triggering** (mechanical; the description is the oracle): assemble ≥5
  should-trigger queries + ≥3 should-NOT-trigger near-misses; run each ≥3×; record fire
  rates; fix the description, not the body.
- **Tier 2 — Behaviour-delta signature** (un-fakeable artifact applied to evaluation): name
  the skill's signature — the artifacts it forces that the bare model omits; run a
  representative task with and without the skill; signature-present-with + absent-without =
  the skill is doing its work. Present-in-both = inert; absent-in-both = the skill failed
  to fire its own discipline.

**anneal-dev IS a Claude Code skill** — `plugin/skills/anneal-dev/SKILL.md` with a
description that triggers on "anneal-dev", "use anneal-dev", or natural-language
"corpus-evolution task" phrasing. It has never had its triggering measured (Tier 1 N/A
claim is false — anneal-dev is description-triggered, not slash-command-only). It has a
clear signature set (the tracker + falsification artifacts + closed-artifact form), but the
with-vs-without measurement has not been run.

This is a render gap: skill-craft v1.0.61 is shipped at the meta-skill level; anneal-dev
hasn't adopted the discipline its own authoring meta-skill now mandates.

## Empirical resonance

The parallel-dispatch bug this session is exactly the failure shape skill-craft v1.0.61
names: **inspection passed, measurement would have caught it**. I had read the sequencing
rule in `core.md §4.1.4`, then parallel-dispatched the convergence passes; the operator
caught it. L1's fix made the violation **measurable on the artifact** (the cited
intent-clean verdict is now an un-fakeable signature). That IS the Tier-2 shape — we
solved the right problem; we just hadn't named the discipline.

V-30 (filed today) is already structurally Tier-2-shaped (measures whether the
form-not-binding class recurs in shapes the fixes don't cover). The discipline rendered
here composes with V-30: V-30 is the watch; this is the per-skill mechanism that produces
the watch's input.

## Fix direction (design seed, not the locked design)

**Tier 1 — anneal-dev triggering harness:**
- Assemble a should-trigger query set: "anneal-dev", "use anneal-dev", "evolve this rule",
  "sharpen the lens", "consolidate this principle", "re-render this clause", etc. ≥5.
- Assemble should-NOT-trigger near-misses: "edit this file", "rename this variable",
  "improve this code" (which should trigger clippy, not anneal-dev), "review the
  glossary" (which might be coherence-audit), etc. ≥3.
- Per skill-craft: the mechanical harness is plugin-dev / skill-creator tooling — author
  the set, delegate the run.

**Tier 2 — anneal-dev behaviour-delta signature:**
- Name the signature: an anneal-dev run produces (i) a tracker file under
  `.anneal-dev/runs/`, (ii) at the convergence cycle: an intent-falsification artifact +
  mechanical-falsification artifact (or recorded skip), (iii) a closed-artifact form at
  each phase boundary with the 5 named sections, (iv) a verify result with a finding ledger.
  An ad-hoc rule-corpus edit produces none of these. **The signature is the artifact set.**
- Run a representative task with anneal-dev loaded vs not loaded. Signature present with +
  absent without → working.

**Tier 3 — isolated grade (likely deferred):**
- skill-craft v1.0.61 reserves Tier 3 for "high-stakes or widely-used skills." anneal-dev
  is widely-used in this corpus (every method-kernel edit goes through it). Tier 3 may
  apply — but the per-run grader already exists at step-4 (the operator's soundness
  verdict + the skill-craft form-review subagent). Whether Tier 3 needs a separate
  meta-level grader is an open question.

## Open questions for the cycle

- **Where does the Tier-1 harness live?** skill-craft delegates to plugin-dev's
  skill-creator harness. anneal-dev would need integration with that — or a project-local
  harness if plugin-dev's isn't yet available for this skill.
- **What's the control task for Tier 2?** A representative corpus-evolution task that has
  a known-good outcome — something like "sharpen `core.md` §X to remove a softened
  must"; the with-anneal-dev run produces the falsification artifacts that catch a
  candidate softening; the without-anneal-dev run just edits and leaves no audit trail.
- **Composition with the foundation-invariants register:** the register's "register-clean
  ≠ sound" residual is structurally similar to skill-craft's "inspection ≠ measurement"
  distinction. Both name a residual the operator's soundness verdict carries. The
  evaluation discipline may strengthen the register's framing.
- **Build-eval-before-procedure ordering for anneal-dev:** skill-craft v1.0.61 says
  build the eval first. anneal-dev was authored long before this discipline existed, so
  the eval is being retrofit. Is that OK, or does retrofitting bias the eval toward
  what anneal-dev already does? (Likely fine — the signature set is genuine; the test
  is whether the AI fires it, not whether the eval was authored first.)

## Relates to

- **skill-craft v1.0.61** — the source discipline being rendered. `references/evaluation.md`,
  the new review-checklist 13th item "Evaluation", PROCEDURE.md "Build the evaluation
  before the procedure text."
- **`instance-reinstantiation` capability matrix** (filed today) — add an "evaluation
  discipline" row tracking each instance's adoption. anneal-dev is the first to receive it.
- **V-30 `form-not-binding-class-recurrence`** — composes: the watch is Tier-2-shaped; this
  discipline produces the watch's input at the per-skill level.
- **`anneal-empirical-validation-experiment` / `anneal-reliability-measurement` /
  `canonical-scenario-regression-suite`** (tier 6) — siblings at the *method* level
  (broader scope). The promotion question is flagged separately, not folded here. Once
  decided, sequence: per-skill discipline (this item) lands first; method-level
  meta-evaluation second.
- **`cross-instance-precedent-discipline`** — once this lands, other skills (clippy,
  daneel, etc.) inherit the same discipline as part of their re-render. Precedent is set.

## Surfacing context

skill-craft v1.0.61's framing is direct: *"Evaluation measures whether a skill changes
behaviour as intended. It complements review (which inspects the text) with measurement
(which observes the skill in use): a skill can read clean and still under-trigger or sit
inert. Run the minimum tier the skill's type and stakes require."* anneal-dev fits the
"Domain-general framework" row of skill-craft's tier-applicability table — *yes/yes/yes*
across all three tiers.

The operator's prompt that surfaced this filing 2026-06-05: "skill-craft now has some
sort of evaluation layer ... check if something similar is a good fit for anneal/anneal-dev."
