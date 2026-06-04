# Re-instantiate the instances from the cleaned spec (via anneal-dev)

**Status:** OPEN — **the effort that closes the framework-spec-cleanup render-tail**,
expanded into its own home (operator-scoped 2026-06-03). Multi-run; downstream of
merging the spec cleanup. Coordinates the per-instance render work under one sequence
+ one governing principle. **(2026-06-04: the 3 bundled sub-efforts — render-resync,
SKILL.md de-bloat, CLAUDE.md seed re-point — folded in below; their standalone files
removed.)**

## The situation

The anneal-framework **spec** was cleaned (§4 re-derivation + S3; runs 1–2,
branch `spec-cleanup-core-phase-pipeline`). The **instances** (clippy, daneel,
anneal-dev, campaign-craft, bauleitplan) are **rendered artifacts** of that spec —
and they are now **stale**: rendered from the *old* messy spec. Confirmed
2026-06-03: anneal-dev's `phases/implement.md` has **zero** `§4.2.x` sub-sections
and `phases/investigate-design.md` **still carries the old duplicated falsification
spelling** the spec de-dup removed.

Separately, some instances are **structurally bloated** (clippy's `SKILL.md` is
372 ln, over budget — `clippy-skill-de-bloat.md`; plus at least one other long
file). This is a *different* problem from staleness.

## Render-debt queue — spec-only framework runs feed this batch (policy 2026-06-04)

**Render-cadence policy (operator-decided 2026-06-04).** A framework-change
anneal-dev run ships **spec-only**: it edits the kernel (`spec/` + `foundation.md` +
dev-process) and does **NOT** render into the instances per-run. Each such run
appends its **source-delta** to the queue below; the batch re-render (Sequence
section) carries the *accumulated* delta into every instance **once**. Rationale: N
spec changes rendered per-run drive N×(#instances) render passes; batched, it is one
pass per instance over the union delta. Cost of the policy: instances stay
transiently **stale** between a spec ship and the batch — tracked here, low-urgency
per the parked-while-idle convention (drift ~0 while an instance is unused); the debt
is *bounded* because the batch is gated to run before instances are relied on for
real work / before release.

This is the run-level operationalization of the tier rationale already in
`README.md` ("framework before clippy … *or you render twice*") and aligns with the
framework's own model — `render-and-open-diff` fires **on-verify-PASSED**, a
decoupled bookend, so renders were never part of a spec-change run's verify. The
batch enumerates its change-set by **source-delta diff** per
`anneal-dev-rerender-changeset-by-source-delta` (never an eyeball audit).

**Queue (accumulating; clear an entry when the batch renders it into all instances):**
- **verify-vs-original-requirements** — run `.anneal-dev/runs/verify-vs-original-requirements.md`;
  spec change on branch `anneal-dev/verify-vs-original-requirements`. Source-delta:
  `spec/core.md` §4.1 (requirements-record capture + verbatim-request, D3/D8) + §4.3
  (requirements-coverage check incl. the soft record-vs-request leg, D4/D8) +
  `spec/glossary.md` (entries: "requirements record", "requirements-coverage check",
  D6). **Render obligation** (the run's deferred U2/U3/U4): each instance's
  `phases/investigate-design.md` (capture rule) + `phases/verify.md` (coverage check —
  render the soft leg honestly, NOT as a mechanical gate) + the 2 term homes. Commit
  ref: _<filled at run ship>_.

## Two kinds of work — do NOT conflate

1. **Faithful re-render (propagation).** Carry the §4 cleanup into an instance's
   rendered files, clause-by-clause. Preserves existing structure → **does NOT
   de-bloat.** Mechanism: anneal-dev's `render-and-open-diff` extension (fires on a
   spec-change verify-PASSED) or a light anneal-dev pass. Right for an
   already-clean instance that just needs syncing.
2. **Disciplined fresh-rewrite (de-bloat).** Re-derive an instance's file(s) from
   the clean spec + re-author the instance-specific parts **from scratch**, with
   anneal-dev's **Bloat / Fragmentation lenses** and the **skill-craft review**
   firing. This is what fixes a structurally-messy SKILL.md — a *full* anneal-dev
   run on the instance, not a propagation. The **render-fidelity verify**
   (clause-by-clause vs spec, separate context) is the safety net that makes an
   aggressive rewrite safe (it catches drift).

## Governing principle — all rendering runs THROUGH anneal-dev

The spec README already mandates this ("re-rendering runs as corpus-evolution
through the anneal-dev instance"). The current bloat is **legacy** — instances
authored/rendered before that discipline was consistently applied. Making
anneal-dev the standing render mechanism means **bloat is caught at render-time**
(Bloat lens + skill-craft review) and can't re-accumulate. So: one-time
disciplined rewrite of the legacy bloat, then every future render through
anneal-dev keeps them clean.

## Settle render CONVENTIONS first (prerequisites — or you re-render twice)

These fix the *instantiation-guide / rendering rules themselves*. Re-rendering
before they're settled bakes the old conventions back in. Settle first:
- **[[harness-tool-runstate-unsourced]]** — every rendered `SKILL.md` carries an
  unsourced "don't use harness `TaskCreate`/`TaskUpdate`" block (contract-2 drift);
  fix = an instantiation-guide render-time note, *then* re-render from the sourced clause.
- **[[cite-glossary-not-section-numbers]]** — instance specs should cite glossary
  terms, not framework §-numbers (the glossary is the instance-facing interface);
  a render convention (needs the glossary-as-interface scoping — partial today).
- **[[instance-template-slot-scaffolding]]** — the template doesn't scaffold the
  mechanism-slot placeholders; settle slot-as-file vs slot-as-section, then fix the
  guide/template so derivations are correct.

(These are method/guide-level; a couple may ride a small spec follow-up. The big
per-instance re-render below should run *after* they land.)

## Sequence

1. **Merge the cleaned spec to `main`.** Instances render *from* the spec; it must
   be the settled source of truth first. (Don't hold the spec branch *for* the
   re-render — merge enables it.)
2. ✅ **Re-render `anneal-dev` FIRST** — **DONE** 2026-06-03 (anneal-dev repo `cf71ec7`,
   merged to its `main` local). Run: `.anneal-dev/runs/anneal-dev-rerender.md` (auto-battle).
   6 files, +45/-54: §4 pass-count reconciliation + §5.3 [READY] thin-bridges + 3 V-N
   breadcrumb strips + 5 cite-glossary firewall re-points; render-fidelity verify
   exhaustive-clean. NOTE: the audit under-scoped it as "light-touch"; 2 convergence
   falsifications caught real §4 divergences (→ method finding
   `anneal-dev-rerender-changeset-by-source-delta`). **CACHE NOT YET UPDATED:** the
   re-render is in the repo source; the running installed cache (`0.1.1`) updates only
   on a version bump + re-install — a separate packaging step before the *next* anneal-dev
   session runs the clean render. (Filed implicitly here; do at next convenient point.)
3. **Then the domain instances**, each a pass + render-fidelity verify. Idle
   instances may stay parked to next-active per the render-settlement convention
   (drift cost ~0 while idle) — do them now only if a fully-clean baseline is
   wanted:
   - **clippy** — the heaviest: bundle clippy's **whole** render-debt into ONE full
     anneal-dev run (the flagged "2nd anneal-dev dogfood"): (i) the parked
     **de-pollution** vocab debt (`clippy-render-resync` — c-safe/T1/T2/R1/R4,
     pre-dates the §4 work); (ii) the **new §4-cleanup** debt (sub-numbering/de-dup/
     consolidation — NOT in clippy-render-resync); (iii) the **SKILL.md de-bloat**
     fresh-rewrite (`clippy-skill-de-bloat`); (iv) the **CLAUDE.md seed re-point**
     (`adoption-instance-settlement`).
   - **daneel** — faithful re-render of §4.
   - **campaign-craft** — faithful re-render; also **locate its source repo first**
     (stale `diligence-framework` name; only the marketplace clone exists — see
     `adoption-instance-settlement`).
   - **bauleitplan** — lighter (no phase files, only `references/`); minimal
     re-render.

Each instance pass also closes its share of `adoption-instance-settlement` (the
"rendered, not authored" CLAUDE.md seed re-point) when touched.

## Bundled sub-efforts (folded in 2026-06-04 — were separate files)

### A. clippy render-resync — parked vocab render-debt (re-enter when clippy active)
Clippy lags framework core by these cycles (behavior-unchanged vocab alignment; batches freely while
clippy idle — drift ~0). A **semantic** change instead pulls a render-validation forward, not into
this batch.
- **c-safe (§4.1.4 falsification)** — fw `5f4ed74`: coupling shapes `target-shape`/`target-uses` →
  `target-existence`/`target-dependents`; predicate evidence abstracted in core (clippy binds the
  concrete grep forms in §3); F3 [CONDITIONAL]/[AUTO-ACCEPTED]→verify handoff; sites:
  `investigate-design.md`, `tracker.md`, check `lens-set.md`/`lenses.md`.
- **T1** (`file:line` → "located read") fw `f9fd5b4` — clippy's `file:line` is its legit binding.
- **T2/T3** fw `c634ebf` (`code`/`fixtures`→"work product"; `grep`→"search") — clippy binds; minimal.
- **Coherence-audit** fw `8bfa20b` — unified **spawn-fallback** name across §4.2/§4.1.4/§4.3.
- **R1** contract-surface discriminator + **R4** coupling-shape glossary bridge — fold into the same
  §5.2 / falsification render-sync.
- **Re-entry:** diff clippy render vs then-current core → isolate the delicate falsification
  re-render → skill-craft gate → re-render → separate-context render-fidelity → release. Check daneel.

### B. clippy SKILL.md de-bloat (the "2nd anneal-dev dogfood" candidate)
`plugin/skills/clippy/SKILL.md` ~372 ln / ~2400 words — over skill-craft's 1500–2000 ideal. Compress
the dispatch-mechanics overlap that restates the phase files; keep the closed-artifact form. Driving
it as a 2nd anneal-dev dogfood (larger change = better V-27 datapoint) un-parks A above — bundle them.

### C. CLAUDE.md seed re-point (all instances)
The adoption re-pointed the instance-CLAUDE.md "rendered, not authored" SEED (`instantiation-guide.md`
§6 + template); already-rendered instances still carry the old seed:
- clippy (`coding-clippy/CLAUDE.md:15`) + daneel (`daneel/CLAUDE.md:15`) — straightforward re-point.
- campaign-craft — stale + **no local source repo** (`CLAUDE.md:16-17` cites obsolete
  `diligence-framework` + single-spec model; only the marketplace clone exists). Locate/clone source
  first, then a larger re-point. Each instance pass closes its share when touched.

## Done when

Every actively-used instance is current with the cleaned spec and de-bloated;
idle instances are either done or explicitly parked-to-next-active. Then archive
`framework-spec-cleanup.md` (its render-tail residual is this effort).

## Relates to
- `framework-spec-cleanup.md` — the spec cleanup whose render-tail this is.
- `anneal-dev-extension-render-gate.md` — the render extension's gating (relevant to the faithful-render path).
- (folded in 2026-06-04: clippy-render-resync, clippy-skill-de-bloat, adoption-instance-settlement — now the Bundled sub-efforts above.)
