# Re-instantiate the instances from the cleaned spec (via anneal-dev)

**Status:** OPEN — **the effort that closes the framework-spec-cleanup render-tail**,
expanded into its own home (operator-scoped 2026-06-03). Multi-run; downstream of
merging the spec cleanup. Coordinates the existing per-instance render items
(below) under one sequence + one governing principle.

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

## Done when

Every actively-used instance is current with the cleaned spec and de-bloated;
idle instances are either done or explicitly parked-to-next-active. Then archive
`framework-spec-cleanup.md` (its render-tail residual is this effort).

## Relates to
- `framework-spec-cleanup.md` — the spec cleanup whose render-tail this is.
- `clippy-render-resync.md` — clippy's faithful-propagation share.
- `clippy-skill-de-bloat.md` — clippy's structural fresh-rewrite share (bundle the two).
- `adoption-instance-settlement.md` — per-instance CLAUDE.md seed re-point + campaign-craft source-repo location.
- `anneal-dev-extension-render-gate.md` — the render extension's gating (relevant to the faithful-render path).
