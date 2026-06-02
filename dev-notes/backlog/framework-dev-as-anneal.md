# Framework-dev as an anneal instance — locked decision + derivation reasoning

**Status:** **DECISION LOCKED 2026-06-01 (reframed-A).** Via
`pbs:decision-design-sharpening` (2 rounds: full-monty + 1 user-triggered),
adapted with anneal's own anchors (foundation contracts / practice 9 /
validation-watch) substituting the skill's PBS-internal apparatus.
**Steps 1–4 DONE.** Pass-1 forward-derivation (2026-06-01) → core de-pollution
(`contract1-depollution-cluster`, COMPLETE) → **Pass-2 finalization DONE
2026-06-02** (isolated derivation subagent `ab6a459e` + separate-context verify
`ad3e3e3c`, PASS-with-fixes-applied; finalized draft `dev-notes/derivation-pass2/`).
Surfaced four framework-core flow-back questions → [[anneal-dev-framework-flowback]].
**Next: step 5 — dogfood** the finalized instance on an instance-corpus cleanup.
Not spec — this is the durable design handoff.

## High-level description

**The problem.** Every time we work on the framework, the corpus decays the
same three ways: files bloat, one principle gets restated in many places and the
copies drift apart, and domain-specific details leak into the domain-general
core. We have disciplines meant to prevent this — but they're advisory, so they
don't reliably fire.

**The root cause.** The document governing how we develop the framework
(`development-process.md`) is secretly a hand-written *copy* of the framework's
own method. Its practices are anneal's concepts restated ad-hoc — "ground before
asserting" is the basis rule, "design → implement → verify" is anneal's core
split, the pre-commit review is anneal's verify. So our development process is
the single worst case of the very fragmentation we keep fighting: anneal's
method, duplicated at the highest level, quietly drifting from the real thing.

**The decision.** Stop maintaining a shadow copy. Make framework development a
real **anneal instance** — just as Clippy is "anneal applied to coding" and
Daneel is "anneal applied to debugging," build a sibling that is "anneal applied
to evolving the rule-corpus itself." The development process then becomes
"anneal + a small set of corpus-specific bindings," and the duplication
disappears. The rigor we wanted comes built in: anneal's machinery (grounding,
coherence checks, verification, lens inspection) *is* a set of per-cycle forcing
functions — we inherit them instead of bolting them on.

**The honest cost.** This is foundational and maximally self-referential —
skill-craft improving skill-craft, the process rewriting the process — so it
carries the highest self-validation risk we have; separate-context review is
non-negotiable. It also adds some real per-cycle ceremony (the development
process now gets re-rendered and fidelity-checked like any other instance). The
bet: that ceremony replaces a worse, invisible cost we're already paying as
drift.

## The locked shape (what the sharpening settled)

- **Surgical, not wholesale.** The duplication is interleaved clause-by-clause
  inside the practices, not separable practice-by-practice — so this is careful
  extraction (pull the anneal kernel out of each practice, leave the
  corpus-specific mechanics as bindings), not a rewrite.
- **The instance never governs its own foundation.** It governs editing the
  *corpora* (skill-craft, the framework spec, instance specs, the rendered
  plugins) — but editing anneal's *kernel*, the thing the instance is built
  from, stays one layer up with independent review. That's the answer to "won't
  you saw off the branch you're sitting on?": you never use the instance to edit
  its own foundation. (Already how framework-spec edits work; we preserve it,
  not invent it.)
- **The "bolt-on hygiene checks" fallback isn't a competing plan — it splits.**
  The actual disciplines (name what you removed, keep the core domain-agnostic,
  don't let files bloat) are general skill-quality rules that belong in
  skill-craft — and some of that hardening is worth doing now regardless. The
  per-cycle enforcement mechanics become bindings in the new instance. What's
  left of the fallback is a genuine parachute if the big effort stalls.
- **Start small.** First build the instance skeleton and run *one small real
  cleanup* through it as a bootstrap test. Works → continue; stalls → fall back.
  Keeps the effort from silently swallowing weeks.
- **The cleanups become the proof.** The corpus messes we already need to fix
  (the bloated `SKILL.md`, the scattered `[VERIFIED]` principle, the domain
  leaks in the core) are needed either way — and they become the first real work
  the new instance does. Cleaning the corpus *with* the anneal-ified process is
  how we validate it on real work.

## Reflexivity caveat — non-negotiable

This is skill-craft improving skill-craft + dev-process improving (or replacing)
dev-process — **maximal self-validation risk** (`CLAUDE.md`: "rule-edit subagent
PASS may self-validate — pause + re-read before push"). Separate-context review
is the whole ballgame. This is why the first derivation pass is a strong
candidate for isolation (an uncontaminated subagent), per the planner precedent.

## Sequencing

1. **Decide A vs B** — **DONE** (reframed-A locked, 2026-06-01).
2. **Pass-1 forward-derivation (anneal-dev)** — **DONE** (2026-06-01, isolated
   subagent; draft `dev-notes/derivation-pass1/`). Result: **arbitrariness test
   passes** — the clean-room derivation independently regenerated dev-process
   practices 2/4/8/10 + the FB-5 principle as lenses/bindings WITHOUT seeing
   `development-process.md`, empirically confirming the shadow-anneal diagnosis.
   It found one gap dev-process lacks (a **Bloat** lens — the anti-decay check)
   and corroborated the `contract1-depollution-cluster` leaks (see that file's
   Pass-1 corroboration).
3. **De-pollute the core FIRST** (`contract1-depollution-cluster`, Cycles
   a→b→c; **Cycles a + b DONE; Cycle c next**) — **before** finalizing
   the instance. Two locked principles force this order: (i) *clean foundation* — the instance renders FROM the core; pass-1's
   draft already carries scar-tissue workarounds for the core's leaks
   (single-tree, code-shaped coupling enum), so finalizing on the un-de-polluted
   core bakes them in + forces re-derivation; (ii) the *bootstrap rule* —
   de-pollution edits the anneal kernel = the instance's own foundation, which
   the instance never governs → framework-layer work, current stable process,
   separate-context review.
4. **Finalize the anneal-dev derivation** on the cleaned core — bindings derived
   once, no scar tissue. The clean derivation is itself a second non-code
   validation that the de-pollution abstractions worked. **DONE 2026-06-02**
   (`dev-notes/derivation-pass2/`): pass-2 re-derived against the de-polluted
   core; the three pass-1 scar-tissue workarounds (single-tree, code-shaped
   coupling, code vocab) dissolved — the validation held. Separate-context verify
   confirmed faithful (the C1 multi-repo simplification cleared as safe) and
   caught one buried over-claim, now flow-back R4 ([[anneal-dev-framework-flowback]]).
5. **Dogfood** the finalized instance on an *instance-corpus* cleanup (clippy
   `SKILL.md` de-bloat / open clippy cycles) — corpus-evolution work that is NOT
   the instance's own foundation, so fully instance-governable (genuine
   self-hosting validation, no bootstrap conflict). Kernel/foundation cleanups
   (FB-5, the de-pollution itself) stay framework-layer, not dogfooded.
   **Entry (NOT started — next move on this effort):** step 5 is a *build* —
   render pass-2 (`dev-notes/derivation-pass2/`) into a minimal runnable skeleton
   (per "Start small" above), then drive one small cleanup through it. Two
   sub-decisions at start: **skeleton scope** (how minimal is "enough to run one
   cleanup") + **target**. **Caveat:** dogfooding *on clippy* re-activates clippy →
   un-parks its batched render-debt ([[clippy-render-resync]], whose re-entry
   trigger this is). Prefer a **contained** first target, or accept that the clippy
   dogfood bundles the render-debt clearing.

## Open / deferred to the derivation cycle

- **Instance name + domain framing** — **RESOLVED:** ratified `anneal-dev` /
  `corpus-evolution` (pass-2 derivation-rationale Naming verdict). The cleaned
  core did not touch the domain boundary.
- **Contract-2 render-ceremony cost** — **DONE 2026-06-02:** filed as
  `validation-watch` **V-27** (WATCHING) — watch whether the per-cycle re-render +
  fidelity check on the dev-process-as-instance justifies itself once anneal-dev
  is operational. Settles empirically at step 5.
- **B's skill-craft-hardening ship-order** — whether to harden skill-craft's
  advisory anti-decay disciplines into forcing functions *before* A (low-rework,
  early value) is a Phase-2 (pre-implementation) sequencing call. Still open.
- **Design-decision body-shape vs non-build committed positions** (surfaced
  Cycle b) — **RESOLVED 2026-06-02 as flow-back R1** (kernel fix `287901d`):
  §5.2(b)'s "what to build" shape strained for prose (the contract/realization
  split blurred); the discriminator was abstracted to coupling-based. The verdict
  generalization (D-track verdicts) was the same §5.2(b) surface, closed with it.
  ([[anneal-dev-framework-flowback]], archived.)
